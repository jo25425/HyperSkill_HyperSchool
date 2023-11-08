import random
from time import sleep

from schedule.models import Teacher, Course, Student


def run():

    # Create instances of Teacher
    teacher1 = Teacher.objects.create(
        name="Professor John",
        surname="Smith",
        age=48,
        about="Professor John Smith is a distinguished scholar in computer science at Brown University..."
    )

    teacher2 = Teacher.objects.create(
        name="Dr. Alice",
        surname="Turner",
        age=36,
        about="Dr. Alice Turner is a dynamic educator and course creator at Online Courses Inc..."
    )

    teacher3 = Teacher.objects.create(
        name="Professor Maria",
        surname="Gonzalez",
        age=55,
        about="Professor Maria Gonzalez is a leading authority in robotics and automation at the University of Technology..."
    )

    teacher4 = Teacher.objects.create(
        name="Dr. Mark",
        surname="Anderson",
        age=42,
        about="Dr. Mark Anderson is a dedicated eLearning instructor with a specialization in psychology and human behavior..."
    )

    teacher5 = Teacher.objects.create(
        name="Professor Emily",
        surname="White",
        age=39,
        about="Professor Emily White is a data science expert at the Data Science Institute..."
    )

    sleep(1)

    # Create instances of Course and link them to the respective teachers
    course1 = Course.objects.create(
        title="Advanced AI and Machine Learning",
        info="Explore the depths of artificial intelligence and machine learning with Professor John Smith...",
        duration_months=6,
        price=249.99,
    )
    course1.teacher.add(teacher1)

    course2 = Course.objects.create(
        title="Digital Marketing Mastery",
        info="Master the art of digital marketing strategies with Dr. Alice Turner at Online Courses Inc...",
        duration_months=3,
        price=149.99,
    )
    course2.teacher.add(teacher2)

    course3 = Course.objects.create(
        title="Robotics and Automation Engineering",
        info="Join Professor Maria Gonzalez at the University of Technology and delve into the world of robotics and automation engineering...",
        duration_months=9,
        price=349.99,
    )
    course3.teacher.add(teacher3)

    course4 = Course.objects.create(
        title="Understanding Human Behavior",
        info="Discover the complexities of human behavior with Dr. Mark Anderson. This online course at eLearning University provides insights into psychology and behavioral analysis...",
        duration_months=4,
        price=99.99,
    )
    course4.teacher.add(teacher4)

    course5 = Course.objects.create(
        title="Data Science and Machine Learning Fundamentals",
        info="Professor Emily White's course at the Data Science Institute introduces you to the world of data science and machine learning...",
        duration_months=5,
        price=199.99,
    )
    course5.teacher.add(teacher5)

    # Create a new course and link it to multiple teachers
    course6 = Course.objects.create(
        title="Advanced Data Analysis",
        info="This comprehensive course covers advanced data analysis techniques in Python.",
        duration_months=5,
        price=179.99,
    )
    course6.teacher.add(teacher1, teacher5)  # This course is taught by both Professor John Smith and Professor Emily White

    # Create another new course and link it to a different set of teachers
    course7 = Course.objects.create(
        title="Digital Marketing Strategies for E-commerce",
        info="Learn the ins and outs of digital marketing strategies for e-commerce with Dr. Alice Turner and Dr. Mark Anderson.",
        duration_months=4,
        price=149.99,
    )
    course7.teacher.add(teacher2, teacher4)  # This course is co-taught by Dr. Alice Turner and Dr. Mark Anderson


    sleep(1)

    # Create a list of student instances
    students = [
        Student(name="John", surname="Doe", age=20),
        Student(name="Jane", surname="Smith", age=22),
        Student(name="Michael", surname="Johnson", age=21),
        Student(name="Emily", surname="Wilson", age=23),
        Student(name="David", surname="Brown", age=19),
        Student(name="Olivia", surname="Garcia", age=20),
        Student(name="William", surname="Martinez", age=24),
        Student(name="Sophia", surname="Perez", age=20),
        Student(name="James", surname="Miller", age=22),
        Student(name="Ava", surname="Anderson", age=21),
        Student(name="Benjamin", surname="Harris", age=19),
        Student(name="Mia", surname="Clark", age=20),
        Student(name="Samuel", surname="Hall", age=22),
        Student(name="Isabella", surname="Gonzalez", age=21),
        Student(name="Elijah", surname="Rodriguez", age=23),
        Student(name="Oliver", surname="Lopez", age=20),
        Student(name="Emma", surname="Young", age=21),
        Student(name="Henry", surname="Taylor", age=22),
        Student(name="Aria", surname="Walker", age=20),
        Student(name="Lucas", surname="Hernandez", age=23),
        # Add more students as needed
    ]

    # Bulk create the student instances
    Student.objects.bulk_create(students)

    sleep(1)

    # Convert the set of courses to a list
    all_courses = list(Course.objects.all())

    # Assign students to various courses
    for student in students:
        num_courses_to_enroll = random.randint(1, 4)  # Randomly select 1 to 4 courses
        courses_to_enroll = random.sample(all_courses, num_courses_to_enroll)
        student.course.add(*courses_to_enroll)
