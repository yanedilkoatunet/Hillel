import random

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


DATABASE_URL = "postgresql+psycopg://student:student123@localhost:5432/student_management"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


student_courses = Table(
    "student_courses",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True)
)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    courses = relationship(
        "Course",
        secondary=student_courses,
        back_populates="students"
    )


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    students = relationship(
        "Student",
        secondary=student_courses,
        back_populates="courses"
    )


Base.metadata.create_all(engine)


def create_courses(session):
    course_names = [
        "Python",
        "Java",
        "JavaScript",
        "SQL",
        "QA Automation"
    ]

    for name in course_names:
        if not session.query(Course).filter_by(name=name).first():
            session.add(Course(name=name))

    session.commit()


def create_students(session):
    if session.query(Student).count() > 0:
        return

    first_names = [
        "Anna", "John", "Kate", "Mark", "Olivia",
        "James", "Emma", "Daniel", "Sophia", "Lucas",
        "Mia", "David", "Liam", "Emily", "Noah",
        "Alice", "Jack", "Chloe", "Leo", "Ella"
    ]

    last_names = [
        "Smith", "Brown", "Wilson", "Taylor", "Clark",
        "Walker", "Hall", "Young", "Allen", "King"
    ]

    courses = session.query(Course).all()

    for i in range(20):
        student = Student(
            first_name=first_names[i],
            last_name=random.choice(last_names),
            email=f"student{i + 1}@example.com"
        )

        student.courses = random.sample(
            courses,
            random.randint(1, 3)
        )

        session.add(student)

    session.commit()


def add_student(session, first_name, last_name, email):
    student = Student(
        first_name=first_name,
        last_name=last_name,
        email=email
    )

    session.add(student)
    session.commit()

    return student


def enroll_student(session, student_id, course_id):
    student = session.get(Student, student_id)
    course = session.get(Course, course_id)

    if student and course and course not in student.courses:
        student.courses.append(course)
        session.commit()


def get_students_by_course(session, course_name):
    course = session.query(Course).filter_by(name=course_name).first()

    if course:
        for student in course.students:
            print(student.first_name, student.last_name, student.email)


def get_courses_by_student(session, student_id):
    student = session.get(Student, student_id)

    if student:
        for course in student.courses:
            print(course.name)


def update_student(session, student_id, new_email):
    student = session.get(Student, student_id)

    if student:
        student.email = new_email
        session.commit()


def delete_student(session, student_id):
    student = session.get(Student, student_id)

    if student:
        session.delete(student)
        session.commit()


session = Session()

try:
    create_courses(session)
    create_students(session)

    new_student = add_student(
        session,
        "Alex",
        "Johnson",
        "alex.johnson@example.com"
    )

    enroll_student(session, new_student.id, 1)

    print("Students enrolled in Python:")
    get_students_by_course(session, "Python")

    print("\nCourses of student:")
    get_courses_by_student(session, new_student.id)

    update_student(
        session,
        new_student.id,
        "alex.new@example.com"
    )

    delete_student(session, new_student.id)

finally:
    session.close()
