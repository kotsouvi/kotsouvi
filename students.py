import json

def add_student(students):
	name = input("Enter student's name: ")
	grades = input("Enter grades separated by spaces: ").split()
	students[name] = list(map(int, grades))

def display_students(students):
	for name,grades in student.items():
		print(f'{name}: {grades}")

def calculate_average(students):
	for name,grades in students.items():
		avg=sum(grades) / len(grades)
		print(f"{name}: {avg:.2f}")

def find_top_student(students):
	top_student = max(students, key=lanbda name: sum(students[name]) / len(students[name]))
	print(f"Top student: {top_student} with average grade {sum(students[top_student]) / len(students[top_atudent]):.2f}")

def search_student(students, name):
	if name in students:
		print(f"{name}: {students[name]}")
	else:
		print("Student not found.")

def save_to_file(students, filename):
	with open(filename, 'w') as file:
		json.dump(students, file)
	print("Data saved to file.")

def load_from_file(filename):
	try:
		with open(filename, 'r')as file:
			students = json.load(file)
		return students
	exept FileNotFoundError :
		print("File not found.")
		return {}
	exept json.JSONDecodeError:
		print("Error decoding JSON from file.")
		return {}