import streamlit as st
import json
from pathlib import Path
from abc import ABC, abstractmethod

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="EduPulse Management System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

DATABASE = 'school_data.json'

# ---------------------------------------------------------
# Data Persistence Functions
# ---------------------------------------------------------
def load_data():
    if Path(DATABASE).exists():
        with open(DATABASE, 'r') as f:
            content = f.read()
            if content:
                return json.loads(content)
    return {'students': [], 'teachers': []}

def save_data(data):
    with open(DATABASE, 'w') as f:
        json.dump(data, f, indent=4)

data = load_data()

# ---------------------------------------------------------
# OOP Base & Derived Classes
# ---------------------------------------------------------
class Persons(ABC):
    @abstractmethod
    def get_roles(self):
        pass

    @staticmethod
    def validate_email(email):
        return '@' in email and '.' in email

class Student(Persons):
    def get_roles(self):
        return "student"

    @staticmethod
    def register(name, age, email, roll_no):
        if not Persons.validate_email(email):
            return False, "Invalid email address! Email must contain '@' and '.'."
        
        for s in data["students"]:
            if s["roll_no"] == roll_no:
                return False, f"Student with Roll No '{roll_no}' already exists!"
        
        data['students'].append({
            'name': name,
            'age': int(age),
            'email': email,
            'roll_no': roll_no,
            'grades': {}
        })
        save_data(data)
        return True, f"Student '{name}' registered successfully!"

    @staticmethod
    def add_grade(roll_no, subject, grade):
        for s in data["students"]:
            if s['roll_no'] == roll_no:
                s['grades'][subject] = float(grade)
                save_data(data)
                return True, f"Grade {grade} for '{subject}' added to student '{s['name']}'!"
        return False, "Student not found!"

class Teacher(Persons):
    def get_roles(self):
        return "teacher"

    @staticmethod
    def register(name, age, email, teacher_id):
        if not Persons.validate_email(email):
            return False, "Invalid email address! Email must contain '@' and '.'."
        
        for t in data["teachers"]:
            if t["teacher_id"] == teacher_id:
                return False, f"Teacher with ID '{teacher_id}' already exists!"
        
        data['teachers'].append({
            'name': name,
            'age': int(age),
            'email': email,
            'teacher_id': teacher_id
        })
        save_data(data)
        return True, f"Teacher '{name}' registered successfully!"

# ---------------------------------------------------------
# Custom Light Theme CSS Styling
# ---------------------------------------------------------
st.markdown("""
    <style>
    /* Global Styles */
    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Header Styling */
    .main-header {
        background: linear-gradient(135deg, #ffffff 0%, #eff6ff 100%);
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        margin-bottom: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    .main-header h1 {
        color: #1e3a8a;
        font-weight: 800;
        font-size: 2.2rem;
        margin-bottom: 4px;
    }
    .main-header p {
        color: #475569;
        font-size: 1rem;
    }

    /* Metric Card Styling */
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 16px 20px;
        border-radius: 14px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
    }
    div[data-testid="stMetricLabel"] {
        color: #64748b;
        font-weight: 600;
        font-size: 0.85rem;
        text-transform: uppercase;
    }
    div[data-testid="stMetricValue"] {
        color: #1e293b;
        font-weight: 800;
    }

    /* Buttons */
    .stButton>button {
        background-color: #2563eb;
        color: white;
        font-weight: 600;
        border-radius: 10px;
        border: none;
        padding: 8px 18px;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: #ffffff;
        padding: 8px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
    }
    .stTabs [data-baseweb="tab"] {
        height: 44px;
        border-radius: 8px;
        font-weight: 600;
        color: #475569;
    }
    .stTabs [aria-selected="true"] {
        background-color: #eff6ff;
        color: #2563eb;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3429/3429149.png", width=70)
    st.title("EduPulse")
    st.caption("School Management System")
    st.markdown("---")
    
    st.subheader("💡 Quick Info")
    st.info(f"📁 Database: `{DATABASE}`\n\n🟢 Synced & Active")

# ---------------------------------------------------------
# Header Banner
# ---------------------------------------------------------
st.markdown("""
    <div class="main-header">
        <h1>🎓 EduPulse Academy Management</h1>
        <p>A professional light-themed interface to manage students, teachers, and academic performance.</p>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Top Metrics Overview
# ---------------------------------------------------------
m_col1, m_col2, m_col3 = st.columns(3)

total_students = len(data.get('students', []))
total_teachers = len(data.get('teachers', []))
total_grades = sum(len(s.get('grades', {})) for s in data.get('students', []))

m_col1.metric("Total Students", total_students, delta="Active Enrolled")
m_col2.metric("Total Teachers", total_teachers, delta="Faculty Members")
m_col3.metric("Grades Recorded", total_grades, delta="Evaluations")

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Main Tabs Navigation
# ---------------------------------------------------------
tab_overview, tab_students, tab_teachers, tab_grades = st.tabs([
    "📊 Overview", 
    "👨‍🎓 Students Directory", 
    "👩‍🏫 Teachers Directory", 
    "📝 Grade Management"
])

# ---------------------------------------------------------
# TAB 1: OVERVIEW
# ---------------------------------------------------------
with tab_overview:
    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("📋 Recent Student Registrations")
        if data['students']:
            st.dataframe(
                [{"Roll No": s['roll_no'], "Name": s['name'], "Email": s['email']} for s in data['students']],
                use_container_width=True
            )
        else:
            st.write("No students registered yet.")

    with col_b:
        st.subheader("👨‍🏫 Faculty Overview")
        if data['teachers']:
            st.dataframe(
                [{"ID": t['teacher_id'], "Name": t['name'], "Email": t['email']} for t in data['teachers']],
                use_container_width=True
            )
        else:
            st.write("No teachers registered yet.")

# ---------------------------------------------------------
# TAB 2: STUDENTS MANAGEMENT
# ---------------------------------------------------------
with tab_students:
    s_col1, s_col2 = st.columns([1, 1.5])

    with s_col1:
        st.subheader("➕ Register New Student")
        with st.form("register_student_form", clear_on_submit=True):
            st_name = st.text_input("Full Name", placeholder="e.g. Peter Parker")
            st_age = st.number_input("Age", min_value=1, max_value=100, value=18)
            st_email = st.text_input("Email Address", placeholder="peter@example.com")
            st_roll = st.text_input("Roll Number", placeholder="e.g. STU-101")
            
            submit_student = st.form_submit_button("Register Student")
            
            if submit_student:
                if not st_name or not st_email or not st_roll:
                    st.error("Please fill in all required fields!")
                else:
                    success, msg = Student.register(st_name, st_age, st_email, st_roll)
                    if success:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)

    with s_col2:
        st.subheader("📚 Enrolled Students List")
        search_stud = st.text_input("🔍 Search Student", placeholder="Search by name, roll no, or email...")
        
        filtered_students = data['students']
        if search_stud:
            q = search_stud.lower()
            filtered_students = [s for s in data['students'] if q in s['name'].lower() or q in s['roll_no'].lower() or q in s['email'].lower()]
        
        if filtered_students:
            display_list = []
            for s in filtered_students:
                grades_str = ", ".join([f"{sub}: {score}" for sub, score in s.get('grades', {}).items()]) or "No grades"
                display_list.append({
                    "Roll No": s['roll_no'],
                    "Name": s['name'],
                    "Age": s['age'],
                    "Email": s['email'],
                    "Grades": grades_str
                })
            st.dataframe(display_list, use_container_width=True)
        else:
            st.info("No matching students found.")

# ---------------------------------------------------------
# TAB 3: TEACHERS MANAGEMENT
# ---------------------------------------------------------
with tab_teachers:
    t_col1, t_col2 = st.columns([1, 1.5])

    with t_col1:
        st.subheader("➕ Register New Teacher")
        with st.form("register_teacher_form", clear_on_submit=True):
            tc_name = st.text_input("Full Name", placeholder="e.g. Thor Odinson")
            tc_age = st.number_input("Age", min_value=1, max_value=2000, value=30)
            tc_email = st.text_input("Email Address", placeholder="thor@asgard.com")
            tc_id = st.text_input("Teacher ID", placeholder="e.g. TCH-874596")
            
            submit_teacher = st.form_submit_button("Register Teacher")
            
            if submit_teacher:
                if not tc_name or not tc_email or not tc_id:
                    st.error("Please fill in all required fields!")
                else:
                    success, msg = Teacher.register(tc_name, tc_age, tc_email, tc_id)
                    if success:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)

    with t_col2:
        st.subheader("👩‍🏫 Faculty Members Directory")
        search_teach = st.text_input("🔍 Search Teacher", placeholder="Search by name, ID, or email...")
        
        filtered_teachers = data['teachers']
        if search_teach:
            q = search_teach.lower()
            filtered_teachers = [t for t in data['teachers'] if q in t['name'].lower() or q in t['teacher_id'].lower() or q in t['email'].lower()]
        
        if filtered_teachers:
            display_teachers = [{
                "Teacher ID": t['teacher_id'],
                "Name": t['name'],
                "Age": t['age'],
                "Email": t['email']
            } for t in filtered_teachers]
            st.dataframe(display_teachers, use_container_width=True)
        else:
            st.info("No matching teachers found.")

# ---------------------------------------------------------
# TAB 4: GRADE MANAGEMENT
# ---------------------------------------------------------
with tab_grades:
    g_col1, g_col2 = st.columns([1, 1.5])

    with g_col1:
        st.subheader("📝 Assign / Update Grade")
        if data['students']:
            student_options = {f"{s['name']} (Roll: {s['roll_no']})": s['roll_no'] for s in data['students']}
            selected_student_label = st.selectbox("Select Student", list(student_options.keys()))
            selected_roll_no = student_options[selected_student_label]
            
            with st.form("add_grade_form", clear_on_submit=True):
                subject = st.text_input("Subject Name", placeholder="e.g. Mathematics, Science")
                grade = st.number_input("Score / Grade (0 - 100)", min_value=0.0, max_value=100.0, value=85.0, step=0.5)
                
                submit_grade = st.form_submit_button("Submit Grade")
                
                if submit_grade:
                    if not subject:
                        st.error("Please enter a subject name!")
                    else:
                        success, msg = Student.add_grade(selected_roll_no, subject, grade)
                        if success:
                            st.success(msg)
                            st.rerun()
                        else:
                            st.error(msg)
        else:
            st.warning("Please register at least one student before adding grades.")

    with g_col2:
        st.subheader("🏆 Report Card Overview")
        all_grades = []
        for s in data['students']:
            for sub, score in s.get('grades', {}).items():
                all_grades.append({
                    "Student Name": s['name'],
                    "Roll No": s['roll_no'],
                    "Subject": sub,
                    "Grade / Score": score
                })
        
        if all_grades:
            st.dataframe(all_grades, use_container_width=True)
        else:
            st.info("No grades have been submitted yet.")
