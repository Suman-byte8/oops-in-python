# 🎓 EduPulse - Student & Teacher Management System

Welcome to **EduPulse**, an Object-Oriented Programming (OOP) practice project built in Python. EduPulse models a school administration portal for enrolling students, registering teachers, assigning subject grades, and storing persistent data.

---

## 📌 Project Overview

This project showcases real-world applications of Object-Oriented Programming (OOP) concepts:
- **Abstraction**: Base class `Persons` using `@abstractmethod` from `abc` module.
- **Inheritance**: Subclasses `Student` and `Teacher` inheriting common properties from `Persons`.
- **Static Methods**: Email format validation using `@staticmethod`.
- **Polymorphism & Data Persistence**: Managing JSON database files (`school_data.json`) across CLI and Web UI layers.

---

## 📁 File Structure & Responsibilities

| File Name | Description |
| :--- | :--- |
| **`main.py`** | Terminal / CLI-based interactive menu interface. |
| **`app.py`** | Modern **Streamlit** light-themed web GUI interface. |
| **`school_data.json`** | Local JSON database storing registered students, teachers, and grades. |
| **`README.md`** | Detailed documentation for the `project/` subfolder. |

---

## 🚀 How to Run the Project

### Option 1: Run the Interactive Streamlit Web UI (Recommended)
Launch the professional light-themed web portal using Streamlit:

```bash
streamlit run app.py
```
Open your browser at: `http://localhost:8501`

### Option 2: Run the Command-Line Interface (CLI)
Run the Python script in your terminal:

```bash
python main.py
```

---

## 💡 Key Features Implemented

1. **Student Registration**:
   - Stores Full Name, Age, Email, Roll Number.
   - Validates email format (`@` and `.`).
   - Prevents duplicate Roll Numbers.

2. **Teacher Registration**:
   - Stores Full Name, Age, Email, Teacher ID.
   - Validates email format.
   - Prevents duplicate Teacher IDs.

3. **Grade Management**:
   - Select student by Roll Number or dropdown selection.
   - Add/update subject scores (e.g. Mathematics, Science).

4. **Search & Data Views**:
   - Real-time search across student & teacher directories.
   - Dynamic report cards and summary cards.

---

## 🔗 Project Link with Workspace Root

This project is part of the parent repository **OOPS in Python**. 
- Refer to the root [readme.md](file:///c:/Users/87591/Desktop/OOPS/readme.md) for conceptual explanations of OOP fundamentals (Classes, Objects, Inheritance, Abstraction, Encapsulation, Polymorphism, and Decorators).
