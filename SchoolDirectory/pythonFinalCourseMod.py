# Project Name: Programming in Python - FINAL courseMod
# Purpose: WITS Student Courses and Grades Directory 3.0 - Course Module
# Developer: Rivka Chana Flig
# Date 12/12/2024

from tkinter import messagebox
from tkinter import simpledialog

#######################################################################################################

class Course (object):

    def __init__(self, course, grade, semester, comment):
        self.course = course
        self.grade = grade
        self.semester = semester
        self.comment= comment

#######################################################################################################

# Function: __str__
# Purpose: Provides a string of the Course object to display course details
# Parameters: self
# Returns: A string of the course with its semester and grade

    def __str__(self):
        printCourse = (f"{self.semester} Semester: {self.course} {self.grade}")
        return printCourse

#######################################################################################################

# Function: changeGrade
# Purpose: Change current grade for student in course
# Parameters: self, studentName, course
# Returns: None (performs function, doesn't return value)

    def changeGrade(self, studentName, course):

        # Ask if user wants to chnage grade for pre-existing course
        yesNo = simpledialog.askstring("Student Directory", f"{course} is already in {studentName}'s record.\nChange the current grade for {studentName} in {course}? (yes/no): ").lower()
        
        # Change grade with addGrade() passing in student and course name
        if yesNo == "yes":
            grade = simpledialog.askstring("Student Directory", "Enter the grade for the course: ")
            if grade == "" or grade == None: # Validate grade input
                messagebox.showerror("Student Directory", "Grade cannot be empty")
                self.changeGrade(self, studentName, course)

            self.grade = grade # Enter new grade into system
            messagebox.showinfo("Student Directory", f"Current record for {studentName} in {course} (Semester {self.semester}): {grade}")

        
        # return to main without chnaging grade
        elif yesNo == "no" or yesNo == "" or yesNo == None:
            return

        # Invalid input (not a yes or no)
        else:
            messagebox.showerror("Student Directory", "Invalid input.\n")
            self.changeGrade(self, studentName, course)

#######################################################################################################

if __name__=="__main__":
	messagebox.showerror("Oopsies", "This is a module and is meant to be imported.")
    