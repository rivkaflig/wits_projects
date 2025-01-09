# Project Name: Programming in Python - FINAL Main
# Purpose: WITS Student Courses and Grades Directory 3.0 - Main Program
# Developer: Rivka Chana Flig
# Date 12/12/2024

import os
from pythonFinalRosterMod import StudentDirectory

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

#----------------------------------------------------------------------------------------------------
# Create an instance of StudentDirectory class to hold student data
directory = StudentDirectory()

# Initialize Application to hold main GUI window
class Application:

    def __init__(self, root):

        self.root = root
        self.root.title("WITS Program")

        # Change directory
        os.chdir(os.path.dirname(os.path.realpath(__file__))) 
        
        # Load existing data
        directory.loadData()

        self.widgets()

#----------------------------------------------------------------------------------------------------

    def widgets(self):
        directory.saveData()

        self.header = Label(self.root, text = "WITS Grade System").grid(column = 0, row = 0)
        self.button1 = Button(root, text = "Add Student", command = self.buttonOne).grid(column = 0, row = 1)
        self.button2 = Button(root, text = "Import Students from Text File", command = self.buttonTwo).grid(column = 0, row = 2)
        self.button3 = Button(root, text = "Add Course and Grade to Student Record", command = self.buttonThree).grid(column = 0, row = 3)
        self.button4 = Button(root, text = "List Students with Courses and Grades", command = self.buttonFour).grid(column = 0, row = 4)
        self.button5 = Button(root, text = "Look-up Student's Grade in Course", command = self.buttonFive).grid(column = 0, row = 5)
        self.button6 = Button(root, text = "Print Student Transcript", command = self.buttonSix).grid(column = 0, row = 6)
        self.button7 = Button(root, text = "Print Student Report Card", command = self.buttonSeven).grid(column = 0, row = 7)
        self.button8 = Button(root, text = "Exit", command = exit).grid(column = 0, row = 8)

    def buttonOne(self): # Add Student
        directory.addStudent()
        directory.saveData()

    def buttonTwo(self): # Import list of students from separate text file      
        directory.textFile()
        directory.saveData()

    def buttonThree(self): # Add course and grade to record      
        studentName = simpledialog.askstring("Student Directory", "Enter student's name: ")

        if studentName in directory.studentDirectory:
            directory.studentDirectory[studentName].addCourse(studentName)

        else:
            messagebox.showerror("Student Directory", f"{studentName} is not in the directory.")        
        
        directory.saveData()

    def buttonFour(self): # List students and records in dictionary
        directory.listDirectory()
        directory.saveData()

    def buttonFive(self): # Look up specific student record and course
        studentName = simpledialog.askstring("Student Directory", "Enter student's name: ")

        if studentName in directory.studentDirectory:
            directory.studentDirectory[studentName].studentRecord(studentName)

        else:
            messagebox.showerror("Student Directory", f"{studentName} is not in the directory.")        

        directory.saveData()

    def buttonSix(self): # Print Student Transcript
        studentName = simpledialog.askstring("Student Directory", "Enter student's name: ")

        if studentName in directory.studentDirectory:
            directory.studentDirectory[studentName].transcript(studentName)
        else:
            messagebox.showerror("Student Directory", f"{studentName} is not in the directory.")        

        directory.saveData()

    def buttonSeven(self): # Print Student Report Card
        studentName = simpledialog.askstring("Student Directory", "Enter student's name: ")

        if studentName in directory.studentDirectory:
            semester = simpledialog.askstring("Student Directory", "Enter semester for report card (FALL or SPRING): ")
            if semester == "" or semester == None:
                messagebox.showerror("Student Directory", "Semester cannot be empty")
            
            else:
                semester=semester.upper()
            
                if semester == "FALL" or semester == "SPRING":
                    directory.studentDirectory[studentName].reportCard(studentName, semester)

                else:
                    messagebox.showerror("Student Directory", f"Semester must be FALL OR SPRING.")      

        else:
            messagebox.showerror("Student Directory", f"{studentName} is not in the directory.")        

        directory.saveData()

    def exit(self): # Exit Program
        directory.saveData()
        return

#----------------------------------------------------------------------------------------------------
# Create the Tkinter root window
root = Tk()

# Create the application instance
app = Application(root)

# Start the GUI loop
root.mainloop()
