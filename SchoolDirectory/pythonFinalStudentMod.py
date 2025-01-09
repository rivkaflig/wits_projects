# Project Name: Programming in Python - FINAL studentMod
# Purpose: WITS Student Courses and Grades Directory 3.0 - Student Module
# Developer: Rivka Chana Flig
# Date 12/12/2024

from pythonFinalCourseMod import Course

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

#######################################################################################################

class Student(object):
    
# Function: __init__
# Purpose: initialize Student object
# Parameters: self, studentName, studentDirectory
# Returns: None

    def __init__(self, studentName, ID):
        self.studentName = studentName
        self.courses = {}
        self.studentID = ID

#######################################################################################################
    # Function: __str__
    # Purpose: Provides a string of the Student object.
    # Parameters: self
    # Returns: A string of the student's name and ID

    def __str__(self):
        printStudent = (f"{self.studentName} (ID {self.studentID}): ")
        return printStudent

#######################################################################################################

# Function: addCourse
# Purpose: Adds course to a student's record (dictionary)
# Parameters: self
# Returns: None (changes the student's record directly)

# Interacts with addGrade() or changeGrade() to add a course and grade to student record

    def addCourse(self, studentName):
    
            course = simpledialog.askstring("Student Directory", "Enter the course name: ")
            
            if course == "" or course == None: # No input
                messagebox.showerror("Student Directory", "New course cannot be empty")
                self.addCourse(studentName)

            # If course is in student's record, ask if grade should change
            # Overriding grade
            elif course in self.courses:
                
                # Call changeGrade function to update the grade
                self.courses[course].changeGrade(studentName, course)

            else:
                semester = simpledialog.askstring("Student Directory", "Semester FALL or SPRING? ")
                
                if semester == "" or semester == None:
                    messagebox.showerror("Student Directory", "Semester cannot be empty")
                    self.addCourse(studentName)

                else:
                    semester=semester.upper() # Uppercase semester

                    if semester != 'FALL' and semester != 'SPRING': # Validate semester
                        messagebox.showerror("Student Directory", "Semester must be FALL or SPRING")
                        self.addCourse(studentName)

                    else:     
                        grade = simpledialog.askstring("Student Directory", "Enter the grade for the course: ")
                        
                        if grade == "" or grade == None: # Validate grade input
                            messagebox.showerror("Student Directory", "Grade cannot be empty")
                            self.addCourse(studentName)

                        else:
                            comments = simpledialog.askstring("Student Directory", "Enter comment for the course: ")
                            
                            if comments == "" or comments == None: # Vlaidate comments input
                                messagebox.showerror("Student Directory", "Comments cannot be empty")
                                self.addCourse(studentName)

                            else:
                                # Call addGrade function to add a new course and grade
                                self.courses[course] = Course(course, grade, semester, comments)
                                messagebox.showinfo("Student Directory", f"\nGrade for {course} has been added to {studentName}'s record.\nCurrent record for {studentName} in {course} (Semester {semester}): {grade}")


#######################################################################################################

# Function: studentRecord
# Purpose: prints grade of an input course for an input student
# Parameters: self
# Returns: None (performs function, doesn't return value)

    def studentRecord(self, studentName):

        course = simpledialog.askstring("Student Directory", f"Which course grade would you like to view for {studentName}? ")
                    
        # Check if student is in course
        if course in self.courses: # Check if student is in course
                
            # Student in course
            messagebox.showinfo("Student Directory", f"Current records for {studentName} in {course}: {self.courses[course].grade}")

        else: 
            # Student not in course
            messagebox.showinfo("Student Directory", f"{studentName} is not currently enrolled in {course}.")

#######################################################################################################

# Function: transcript
# Purpose: Generates a text file transcript for a specific student
# Parameters: self, studentName
# # Returns: None (writes transcript to a file and notifies the user)

    def transcript(self, studentName):
        
        # Create the filename for the transcript and open textfile for writing
        fileName = studentName + "_Transcript"
        transcriptFile = open(f"{fileName}.txt", "w")
        transcriptFile.write(f"Transcript: {studentName} ID: {self.studentID}\n----------------------------")

        # Write FALL semester courses to the transcript
        transcriptFile.write("\n\tFALL Courses:\n")
        for course in self.courses:    
            if self.courses[course].semester == "FALL":
                transcriptFile.writelines(f"\n\t\t{self.courses[course]}")
        
        # Write SPRING semester courses to the transcript
        transcriptFile.write("\n\n\tSPRING Courses:\n")
        for course in self.courses:  
            if self.courses[course].semester == "SPRING":
                transcriptFile.writelines(f"\n\t\t{self.courses[course]}")

        transcriptFile.close()

        # Tell user transcript has been made
        messagebox.showinfo("Student Directory", f"{studentName}'s Transcript has been uploaded.")

#######################################################################################################

# Function: reportCard
# Purpose: Generates a text file report card for a student for a specific semester
# Parameters: self, studentName, semester
# Returns: None (writes report card to a file and notifies the user) 

    def reportCard(self, studentName, semester):

        # Create filename and open file to write to
        fileName = studentName + "_Report Card_" + semester
        reportCardFile = open(f"{fileName}.txt", "w")
        reportCardFile.write(f"Report Card\n{studentName} ID: {self.studentID}\t{semester} Semester\n--------------------------------")
    
        # Write courses for the specified semester to the report card
        for course in self.courses:  
            if self.courses[course].semester == semester: # Only get courses that equal the semester specified
                reportCardFile.writelines(f"\n\t{self.courses[course].course}: {self.courses[course].grade}\n\t\tComments: {self.courses[course].comment}\n")

        reportCardFile.close()

        # Tell user report card has been made
        messagebox.showinfo("Student Directory", f"{studentName}'s {semester} Report Card has been uploaded.")

#######################################################################################################

if __name__=="__main__":
	messagebox.showerror("Oopsies", "This is a module and is meant to be imported.")
    