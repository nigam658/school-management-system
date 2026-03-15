from School import School

class std_9TH(School) :
    def __init__(self):
        super().__init__()
        # ALL STUDENT DETAILS     
        self.students = {
            1: {
                  "Name": "Amit",
            },

            2: {
                  "Name": "Pranjal",
            },

            3: {
                  "Name": "Manas",
            },

            4: {
                  "Name": "Rajesh"
            },

            5: {
                  "Name": "Tapan",
            },
        }
        # All student marks in roll number of dictionary
        self.marks = {
            1: {
                "Physics": 56,
                "History" : 45,
                "Math" : 77,
                "Biology" : 67,
                "English" : 86
            },
            2: {
                "Physics": 56,
                "History" : 45,
                "Math" : 79,
                "Biology" : 67,
                "English" : 99
            },
            3: {
                "Physics": 56,
                "History" : 45,
                "Math" : 77,
                "Biology" : 67,
                "English" : 86
            },
            4: {
                "Physics": 56,
                "History" : 45,
                "Math" : 77,
                "Biology" : 88,
                "English" : 86
            },
            5: {
                "Physics": 96,
                "History" : 89,
                "IT" : 95,
                "Biology" : 97,
                "English" : 88
            },
        }

        # GRADE DICTIONARY
        self.grade_system = {
            "A" : 90,
            "B" : 75,
            "C" : 60
        }

    