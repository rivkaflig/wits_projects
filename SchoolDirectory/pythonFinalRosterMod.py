# Project Name: Programming in Python - FINAL rosterMod
# Purpose: WITS Student Courses and Grades Directory 3.0 - Roster Module
# Developer: Rivka Chana Flig
# Date 12/12/2024

import os
import pickle
from pythonFinalStudentMod import Student

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

#######################################################################################################

# Create StudentDirectory class
class StudentDirectory(object):

    ID = 3269

# Function: __init__
# Purpose: initialize StudentDirectory object as a dictionary
# Parameters: self
# Returns: None

    def __init__(self):
        
        # Initialize the directory dictionary to store Student objects
        self.studentDirectory = {}

#######################################################################################################

# Function: loadData
# Purpose: Loads the student directory from a saved file ("datafile.dat") if it exists
# Parameters: self
# Returns: None (modifies the object studentDirectory with the data from the file)

    def loadData(self):

        # Import existing file
        if os.path.exists("datafile.dat"): 
            loadFile = open("datafile.dat", "rb")
            self.studentDirectory = pickle.load(loadFile) # Load the student directory
            StudentDirectory.ID = pickle.load(loadFile)   # Load the current ID 'count'
            loadFile.close()

        # Create an empty dictionary if no existing file
        else:
            self.studentDirectory = {}  

#######################################################################################################

# Function: saveData
# Purpose: Saves the current student directory to a file ("datafile.dat")
# Parameters: self
# Returns: None 

    def saveData(self):

        # Save current dictionary to "datafile.dat"
        saveData = open("datafile.dat", "wb")
        pickle.dump(self.studentDirectory, saveData) # Save the student directory
        pickle.dump(StudentDirectory.ID, saveData)   # Save the ID for the next student
        saveData.close()

#######################################################################################################

# Function: addStudent
# Purpose: Adds student to directory
# Parameters: self
# Returns: None (performs function, doesn't return value)

    def addStudent(self):

        studentName = simpledialog.askstring("Student Directory", "Enter student's name: ")
                    
        if studentName in self.studentDirectory: # Student exists
            messagebox.showinfo("Student Directory", f"{studentName} is already in the Student directory.")
            
        elif studentName != "" and studentName != None:

            # Key is [studentName] (a string Value) which equals = Student Object
            self.studentDirectory[studentName] = Student(studentName, StudentDirectory.ID)
            StudentDirectory.ID += 1 # Increment the ID for the next student

            messagebox.showinfo("Student Directory", f"{studentName} was successfully added to the Student Directory.\nID: {self.studentDirectory[studentName].studentID}")
            self.saveData()
        
        elif studentName == "" or studentName == None:
            messagebox.showerror("Student Directory", "New student cannot be empty")

#######################################################################################################

# Function: textFile
# Purpose: Reads a list of students from an input file and adds them to the student directory
# Parameters: self
# Returns: None (modifies the studentDirectory object by adding new students)

    def textFile(self):

        message = "Imported Students:\n\n"
        fileName = simpledialog.askstring("Student Directory", "Input a .txt extension file name to enter the list of Students: ")

        if fileName == None: # User didn't input
            return
        
        # Check if file exists
        elif not os.path.exists(fileName):
            messagebox.showerror("Student Directory", f"The file {fileName} does not exist.")

        # Open existing file
        else:
            fileName = open(fileName, "r") 
            names = fileName.readlines()
            print ()

            for line in names:      # Iterate over every line in txt file
                line = line.strip() # Remove '\n'

                if line in self.studentDirectory: # Student exists in directory
                    message += (f"{line} is already in the Student directory.\n\n")
                            
                else: # Add student
                    self.studentDirectory[line] = Student(line, StudentDirectory.ID) # Student added to directory
                    message += (f"{line} was successfully added to the Student Directory.\nID: {StudentDirectory.ID}\n\n")
                    StudentDirectory.ID += 1

                    self.saveData()
            
            messagebox.showinfo ("Student Directory", message)

            fileName.close()
            self.saveData() 

#######################################################################################################

# Function: listDirectory
# Purpose: Lists all students in directory along with their courses and grades
# Parameters: self
# Returns: None (performs function, doesn't return value)

    def listDirectory(self):

        if not self.studentDirectory: # Empty directory
            messagebox.showinfo("Student Directory", "No Students in the directory.")

        else:
            message = ("Students and their courses and grades:\n")

            for studentName in self.studentDirectory: # Iterate through every student in directory
                message += (f"\n\n{self.studentDirectory[studentName]}") #(ID: {self.studentDirectory[studentName].studentID})              
          
                if not self.studentDirectory[studentName].courses:
                    message += ("\n\n\tNo courses recorded.")

                for course in self.studentDirectory[studentName].courses:  
                    message += (f"\n\n\t{self.studentDirectory[studentName].courses[course]}")
                    #print (f"\n\tSemester {self.studentDirectory[studentName].courses[course].semester} Course: {self.studentDirectory[studentName].courses[course].course}: {self.studentDirectory[studentName].courses[course].grade}"

            messagebox.showinfo("Student Directory", message)

        self.saveData()

#######################################################################################################

if __name__=="__main__":
	messagebox.showerror("Oopsies", "This is a module and is meant to be imported.")
