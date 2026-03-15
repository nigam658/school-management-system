from std_8 import std_8TH
from std_9 import std_9TH
from std_10 import std_10TH

def func ():
    print("Enter 1 for details 8TH class . ")
    print("Enter 2 for details 9TH class . ")
    print("Enter 3 for details 10TH class . ")
    user = input("Enter your choice ")

    if user == "1" :
        std_8 = std_8TH()
        print("\n1. Indivuisal student percentage : ")
        print("2. Grade of student through roll no ")
        print("3. Subject and marks of a student through roll number ")
        print("4. All student names of a specific grade ")
        print("5. Subject-wise student perfomance")
        print("6. access top 3 raked student of the class")
        
        user2 = input("\nENTER YOUR CHOICE (1 2 3 4 5 6)::-  ")

        if user2 == "1" :
            roll = int(input("\nEnter rollno for access "))
            print(std_8.get_percentage(roll))

        elif user2 == "2":
            roll = int(input("\nEnter rollno for access "))
            std_8.grade(roll)

        elif user2 == "3":
            roll = int(input("\nEnter rollno for access "))
            std_8.subject_marks(roll)

        elif user2 == "4":
            Grade = input("\nEnter Grade (A-B-C) :  ").upper()
            std_8.grade_wise(Grade)

        elif user2 == "5":
            subject = input("\nEnter subject name :")
            std_8.sub_wise_performance(subject)

        elif user2 == "6":
            std_8.top_rank()   
            
        
    elif user == "2":
        std_9 = std_9TH()
        print("\n1. Indivuisal student percentage : ")
        print("2. Grade of student through roll no ")
        print("3. Subject and marks of a student through roll number ")
        print("4. All student name of a specific grade. ")
        print("5. subject wise student perfomance")
        print("6. access top 3 ranked student of the class")

        user2 = input("\nENTER YOUR CHOICE (1 2 3 4 5 6)::-  ")

        if user2 == "1" :
            roll = int(input("\nEnter rollno for access "))
            print(std_9.get_percentage(roll))

        elif user2 == "2":
            roll = int(input("\nEnter rollno for access "))
            std_9.grade(roll)

        elif user2 == "3":
            roll = int(input("\nEnter rollno for access "))
            std_9.subject_marks(roll)

        elif user2 == "4":
            Grade = input("\nEnter Grade (A-B-C) :  ").upper()
            std_9.grade_wise(Grade)

        elif user2 == "5":
            subject = input("\nEnter subject name :")
            std_9.sub_wise_performance(subject)

        elif user2 == "6":
            std_9.top_rank()


    elif user == "3":
        std_10 = std_10TH()
        print("\n1. create a table for database")
        print("2. add student details")
        print("3. Indivuisal student cgpa : ")
        print("4. Grade of student through roll no ")
        print("5. Subject and marks of a student through roll number ")
        print("6. Allstudent name of a specific grade ")
        print("7. Subject-wise student perfomance")
        print("8. access top 3 ranked student of the class")
        

        user2 = input("\nENTER YOUR CHOICE (1 2 3 4 5 6 7)::-  ")

        if user2 == "1" :
            table = input("Enter table name : ")
            print(std_10.create_table(table))
        
        elif user2 == "2":
            roll = int(input("Enter roll no : "))
            name = input("Enter name of the student ")
            print(std_10.add_student_details(roll,name))

        if user2 == "3" :
            roll = int(input("\nEnter rollno for access "))
            print(std_10.get_cgpa(roll))

        elif user2 == "4":
            roll = int(input("\nEnter rollno for access "))
            std_10.grade(roll)

        elif user2 == "5":
            roll = int(input("\nEnter rollno for access "))
            std_10.subject_marks(roll)

        elif user2 == "6":
            Grade = input("\nEnter Grade (A-A1-B-B1-C) : ").upper()
            std_10.grade_wise(Grade)

        elif user2 == "7":
            subject = input("\nEnter subject name : ")
            std_10.sub_wise_performance(subject)

        elif user2 == "8":
            std_10.top_rank()


func()



