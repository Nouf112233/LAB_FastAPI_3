from database import Base
from sqlalchemy import String, Float, Integer, Column, Text,ForeignKey, Table
from sqlalchemy.orm import relationship

# Students_Courses = Table('students_courses', Base.metadata,
#     Column('student_id', ForeignKey('students.id'), primary_key=True),
#     Column('courses_id', ForeignKey('courses.course_id'), primary_key=True)
# )
class Students_Courses(Base):
    __tablename__ = 'students_courses'
    student_id = Column(ForeignKey('students.id'), primary_key=True)
    courses_id  = Column(ForeignKey('courses.course_id'), primary_key=True)

class Students(Base): # inherets from Base class
    __tablename__ = 'students'
    f_name = Column(String(255), nullable=False, unique=True)
    l_name = Column(String(255), nullable=False, unique=False)
    id = Column(Integer, primary_key=True)
    GPA = Column(Float, nullable=False)
    courses = relationship("Courses", secondary="students_courses",back_populates='students')

    def __repr__(self):
        return f"<Student name={self.f_name} ID={self.id}>"

class Courses(Base): # inherets from Base class
    __tablename__ = 'courses'
    course_name = Column(String(255), nullable=False, unique=True)
    course_hours = Column(String(255), nullable=False, unique=False)
    course_id = Column(Integer, primary_key=True)
    course_description = Column(Text)
    students = relationship("Students", secondary="Students_Courses", back_populates='courses')

class Students_Courses(Base):
    __tablename__ = 'students_courses'
    student_id = Column(ForeignKey('students.id'), primary_key=True)
    courses_id  = Column(ForeignKey('courses.course_id'), primary_key=True)

    def __repr__(self):
        return f"<Courses course_name={self.course_name} ID={self.course_id}>"