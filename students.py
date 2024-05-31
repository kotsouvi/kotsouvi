import json

def add_student(students):
	name = input("Enter student's name: ")
	grades = input("Enter grades separated by spaces: ").split()
	students[name] = list(map(int, grades))

def display_students(students):
	for name, grades in students.items():
		print(f"{name}: {grades}")

def calculate_average(students):
	for name, grades in students.items():
		avg=sum(grades) / len(grades)
		print(f"{name}: {avg:.2f}")

def find_top_student(students):
	top_student = max(students, key=lambda name: sum(students[name]) / len(students[name]))
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
	except FileNotFoundError :
		print("File not found.")
		return {}
	except json.JSONDecodeError:
		print("Error decoding JSON from file.")
		return {}
		
def main():
    students = {} 
    while True: 
        print("\nMenu:") 
        print("1. Add student") 
        print("2. Display all students")
        print("3. Caculate average grades") 
        print("4. Find top student")
        print("5. Search student by name") 
        print("6. Save to file") 
        print("7. Load from file")
        print("8. Exit") 
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student(students) 
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            calculate_average(students)
        elif choice == '4':
            find_top_student(students)
        elif choice == '5':
            name = input("Enter student's name to search:")
            search_student(students, name)
        elif choice == '6':
            filename = input("Enter filename to save: ") 
            save_to_file(students, filename)
        elif choice == '7':
            filename = input("Enter filename to save: ")
            students = load_from_file(filename)
        elif choice == '8':
            break 
        else:
            print("Invalid choice. Pleace try again.")
           
if __name__ == "__main__":
    main() 