from School import School

class std_8TH(School) :
    def __init__(self):
        # ALL STUDENT DETAILS     
        self.students = {
            1: {
                  "Name": "Nigam",
            },

            2: {
                  "Name": "Bishal",
            },

            3: {
                  "Name": "Biswajeet",
            },

            4: {
                  "Name": "Deepak"
            },

            5: {
                  "Name": "Maheswar",
            },
        }

        # All student marks in roll number of dictionary
        self.marks = {
            1: {
                "MIL": 56,
                "Chemistry" : 45,
                "IT" : 77,
                "life science" : 67,
                "English" : 86
            },
            2: {
                "MIL": 56,
                "Chemistry" : 45,
                "IT" : 77,
                "life science" : 67,
                "English" : 99
            },
            3: {
                "MIL": 56,
                "Chemistry" : 45,
                "IT" : 77,
                "life science" : 67,
                "English" : 86
            },
            4: {
                "MIL": 56,
                "Chemistry" : 45,
                "IT" : 77,
                "life science" : 88,
                "English" : 86
            },
            5: {
                "MIL": 96,
                "History" : 89,
                "IT" : 95,
                "life science" : 97,
                "English" : 88
            },     
        }
        
        # GRADE DICTIONARY
        self.grade_system = {
            "A" : 85,
            "B" : 70,
            "C" : 50
        }

    

