class Course:
    _id_counter = 1  # class attribute

    def __init__(self, name):
        self.course_id = Course._id_counter
        Course._id_counter += 1
        self.name = name
        self.enrolled_students = []

    def __str__(self):
         return f"Student ID :{self.student_Id} \nName : {self.name}\nGrades:{self.grades}\nCourses:{self.enrolled_courses}"
     
    def __repr__(self)->str:
         return f"Student ID :{self.student_Id} \nName : {self.name}\nGrades:{self.grades}\nCourses:{self.enrolled_courses}"
     
    