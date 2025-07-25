# Build a command-line Python application to store, view, search, and analyze student marks. The student data should be saved persistently in a CSV file so that it’s retained even after the program closes.

# Objective:
# Create a CLI-based system that allows users (e.g., a teacher or student) to:
# Add new student records
# View all student records
# Search for a specific student
# Analyze marks (average, highest, lowest)
# Delete a student record
# Exit the application safely
import csv

def add_student():
    with open("students.csv", "a", newline='') as f:
        writer = csv.writer(f)
        name = input("Enter your name: ")
        roll_no = int(input("Enter your Roll no: "))
        sub = input("Enter your sub: ")
        marks = int(input("Enter your marks(0-100): "))
        writer.writerow([name, roll_no, sub, marks])
        print("Student added successfully!")

def display_students():

    with open("students.csv","r") as f:
        reader = csv.reader(f)
        print(f"{'Name':^15}|{'Roll no':^10}|{'subject':^10}|{'marks'}") # <(left allgin) | >(right allign) | ^ center
        print("-"*50)
        for row in reader:
              print(f"{row[0]:^15}|{row[1]:^10}|{row[2]:^10}|{row[3]}")

def del_student():
      print(target := input("Enter the roll no of the student you want to delete record of : "))
      with open("students.csv","r") as f:
        reader = csv.reader(f)
        new_reader = list(reader)
        result = next((sublist for sublist in new_reader if target in sublist),None)
        # print(result)
        new_reader.remove(result)
        # print(new_reader)
        with open("students.csv", "w", newline='') as f:
             writer = csv.writer(f)
             for sub_reader in  new_reader:
                writer.writerow([sub_reader[0], sub_reader[1], sub_reader[2], sub_reader[3]])
        print("************* Updated List ***************** ")
        display_students()

                

def search_student():
      
      print(target := input("Enter the roll no of student you want info about: "))
      with open("students.csv","r") as f:
        reader = csv.reader(f)
        new_reader = list(reader)
        result = next((sublist for sublist in new_reader if target in sublist),None)
        print(f"# INFO ABOUT ROLL NO :- {target}")
        print(f"{'Name':^15}|{'Roll no':^10}|{'subject':^10}|{'marks'}")
        print("-"*50)
        print(f"{result[0]:^15}|{result[1]:^10}|{result[2]:^10}|{result[3]}")
        
        

def analyze_marks():
      print("1. Average Marks")
      print("2. Highest Marks")
      print("3. Lowest Marks")
#       print(task := int(input("Enter what you want to know (Ex 1 for avg ): ")))
#       print(task)
      task = int(input("Enter what you want to know (Ex 1 for avg ): "))

      match task:
           case 1:
                sum = 0
                count = 0
                with open("students.csv","r") as f:
                        reader = csv.reader(f)
                        students = list(reader)
                        for student in students:
                             sum += int(student[3])
                             count += 1
                print(f"The average of marks is: {sum/count}")
                
           case 2:
                with open("students.csv","r") as f:
                        reader = csv.reader(f)
                        students = list(reader)

                        max_list = max(students, key = lambda x : x[3])
                        max_ = max_list[3]
                        # i = 1
                        # for student in students:
                        #      max = students [0][3]
                        #      if students[i][3] > max: # 23>67   # My previous long take(I fkin forgot abt max min func of python)
                        #         max = students[i][3]
                        #      i+=1
                        #      if i == students.__len__():
                        #         break
                        print(f"Highest marks are : {max_}")
                        
           case 3:
                with open("students.csv","r") as f:
                        reader = csv.reader(f)
                        students = list(reader)
                        min_list = min(students, key = lambda x : x[3])
                        min_ = min_list[3]
                        # i = 1
                        # for student in students:
                        #      min = students [0][3] # 67
                        #      if students[i][3] < min: # 23 < 67
                        #         min = students[i][3]
                        #      i+=1
                        #      if i == students.__len__():
                        #         break
                        print(f"Lowest marks are : {min_}")

while True:
    print("-"*50)        
    print("1.Add Student")
    print("2.Show Student list")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Analyze marks")
    print("> Exit(0)")

    number = int(input("> Please select task number you wanna perform: "))

    match number:
        case 1:
                add_student()
        case 2:
                display_students()
        case 3:
                search_student()
        case 4:
                del_student()
        case 5:
                analyze_marks()
        case 0:
                print("Exiting..... Thank you!")
                break
        case _:
                print("Please enter a vaild task....")



    

