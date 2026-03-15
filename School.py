import mysql_

class School :
    pass

 
    
    
    # CALCULATE PERCENTAGE OF A ROLL NO 
    def get_percentage (self,rollno):
        if rollno not in self.marks:
            return "roll no not found"      
        else:
            return (sum(self.marks[rollno].values())  / (len(self.marks[rollno]) * 100))  *  100   # Calculate percentage  

    # ACCSESS GRADE 
    def grade(self,roll):
        percentage = self.get_percentage(roll)

        if roll in self.marks :
            for grade_index , cutoff in self.grade_system.items() :
                if percentage >= cutoff :
                    print(grade_index,"is the grade of ",self.students[roll]["Name"])
                    break
                
    # return subjects and marks through rollno
    def subject_marks (self,roll):
        if roll not in self.students:
            print("Roll no not found")
            return
        print(self.students[roll]["Name"],"'s All subjects marks : ")
        for subject , mark in self.marks[roll].items():
            print(subject,"-",mark)

    # GRADE WISE STUDENT ROLLNO         
    def grade_wise (self,Grade) :
        if Grade not in self.grade_system: 
            return "Grade is not found"
        
        previous_grade = 101

        for grade_index in self.grade_system:   #GRADE LOOP TO ASSIGH PREVIOUS GRADE 
            if grade_index == Grade : 
                break
            else:
                previous_grade = self.grade_system[grade_index] 

        for mark_index in self.marks:  # LOOPING THE MARK DICTIONARY
            prcntg = self.get_percentage(mark_index)   # CALL THE PERCENTAGE FUCNTION TO CALCULATE MARKS OF AGIVEN ROLL NO
            if prcntg >= self.grade_system[Grade] and prcntg < previous_grade :
                print(self.students[mark_index]["Name"])
        
    # STUDENTS PERFOMANCE SUBJECT WISE
    def sub_wise_performance (self,sub):
        for mark_index in self.marks:
                if self.marks[mark_index][sub] >= 90 :
                    print(self.students[mark_index]["Name"])
        print("These students are good in",sub)
    
    # FIND TOP 3 RANKED STUDENT OF A CLASS
    def top_rank (self):
        rank_list = []
        
        for roll in self.marks:
            percentage = (self.get_percentage(roll))
            name =(self.students[roll]["Name"])

            rank_list.append((percentage,name)) # store percentage and name with a tuple 

        rank_list.sort(reverse = True)
        a = 1
        for rank_percentage, ranker_name in rank_list:
            if a > 3 :
                break
            print(f"\n{ranker_name} scored {rank_percentage:.2f}% with top {a} rank🎉")
            a+=1