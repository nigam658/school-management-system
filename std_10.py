from School import School

class std_10TH(School) :
    def __init__(self):
        super().__init__()
        # ALL STUDENT DETAILS
        self.students = {
            1: {
                  "Name": "jogania",
            },

            2: {
                  "Name": "jyoti",
            },

            3: {
                  "Name": "priyansh",
            },

            4: {
                  "Name": "pawan"
            },

            5: {
                  "Name": "sai",
            },
        }
        # All student marks in roll number of dictionary
        self.marks = {
            1 : {
                "Geometric" : 75,
                "Social Science" : 45,
                "Geography" : 89,
                "Hindi" : 47,
                "English" : 59
            },
            2 : {
                "Geometric" : 67,
                "Social Science" : 86,
                "Geography" : 57,
                "Hindi" : 71,
                "English" : 87
            },
            3 : {
                "Geometric" : 75,
                "Social Science" : 45,
                "Geography" : 89,
                "Hindi" : 47,
                "English" : 59
            },
            4 : {
                "Geometric" : 96,
                "Social Science" : 56,
                "Geography" : 87,
                "Hindi" : 90,
                "English" : 67
            },
            5 : {
                "Geometric" : 76,
                "Social Science" : 80,
                "Geography" : 83,
                "Hindi" : 97,
                "English" : 58
            }
        }
            # GRADE DICTIONARY
        self.grade_system = {
                    "A" : 90,
                    "A1" : 75,
                    "B" : 60,
                    "B1" : 55,
                    "C" : 35
                }
        
    def add_new_student_details(self):
        roll = int(input("Enter roll no : "))
        student = input("Enter student name : ")
        if roll in self.students:
            return "roll no is already exist."
        else:
            self.students.update({roll : {"Name" : student}})
            print(self.students)
            return "student added successfully"
        
    
    def get_cgpa (self,rollno):
        if rollno not in self.marks:
            return "roll no not found"
            
        else:
            cgpa = (sum(self.marks[rollno].values()) / (len(self.marks[rollno]) * 100))  *  10   # Calculate percentage
            cgpa = round(cgpa,2)
            
            return f"{self.students[rollno]["Name"]} cgpa is : {cgpa}"
    
    def next_college_details (self,roll,new_college):
        if roll not in self.students:
            return "roll no not found"
        else:
            self.students[roll].update({"College" : new_college})
            return "update college sucessfully"



        