import subprocess
import json
from abc import ABC, abstractmethod
from pathlib import Path

database = 'school_data.json'
data = {'students': [], 'teachers': []}

if Path(database).exists():
    with open(database, 'r') as f:
        content = f.read()
        if content:
            data = json.loads(content)

def save():
    with open(database,'w') as f:
        json.dump(data, f, indent=4)

class Persons(ABC):
    
    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def register(self):
        pass
    
    @abstractmethod
    def show_details(self):
        pass

    @staticmethod
    def validate_email(email):
        if '@' in email and '.' in email:
            return True
        else:
            return False
    
class Student(Persons):
    def get_roles(self):
        return "student"

    def register(self):
        name = input('tell your name:--> ')
        age = int(input('tell your age:--> '))
        email = input('tell your email:--> ')
        roll_no = input('tell your roll no:--> ')
        
        if not Persons.validate_email(email):
            print("invalid email id")
            return
        
        for i in data["students"]:
            if i["roll_no"] == roll_no:
                print("student already exists")
                return
        
        data['students'].append({
            'name': name,
            'age': age,
            'email': email,
            'roll_no': roll_no,
            'grades': {}
        })

        save()
        print(f'Student {name} registered successfully!')

    def show_details(self):
        pass

stud = Student()


        



print("press 1 to register a student")
print("press 2 to register a teacher")
print("press 3 to add grades")
print("press 4 to show student details")
print("press 5 to show teacher details")


choice = int(input("Please tell your choice: "))

if choice == 1:
    stud.register()
