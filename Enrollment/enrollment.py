#******************************************************
# Assignment 3 Task 1: Create a table and queue for students
# Author: Ayaan Jutt
# Collaborators/References: Assistance from Mansur Gulami (TA) and Kseniia Priakhina (TA) on how to better my code 
#******************************************************


from enrollStudent import StudentNode, EnrollTable, PriorityQueue

def askForInput():
    """input: N/A
    output: a userInput
    asks the user for the input and returns it  
    """
    #asks the userInput 
    userInput = input('Would you like to register or drop students [R/D]: ')
    #as long as it doesn't match R,D, or Q keep asking for an input, if it does, return the input 
    while userInput != 'R' and userInput != 'D' and userInput != 'Q':
        userInput = input('Incorrect input, please try again\nWould you like to register or drop students [R/D]: ')
    return userInput    
def registerFile(queue, capacity, enrollTable):
    """input: a boolean on whether or not we add to the queue, the capacity of the students and the EnrollyTable class 
    output: a list of the file lines, the list of students who can't get in, and a boolean if whether or not we need a queue 
    asks and looks at a register file, deciphers it and puts into a list and checks if we need a queue 
    """
    #create variables for an input and a list for a queue 
    testFile = ''
    waitingList = []
    #while the file doesn't end with .txt 
    while not testFile.endswith('.txt'):
        #ask the user for a file
        testFile = input('Please enter a filename for student records: ')
        try:
            #open the fule, read it, and split the lines
            file = open(testFile)
            content = file.read()
            lines = content.splitlines()
            #if the lines are bigger than 50,
            if capacity == enrollTable.size():
                queue = True
            elif len(lines) > capacity - 1:
                #set queue to True, the waitinglist goes from the 50th index to the end, and the lines start at 0 up till the 49th item 
                queue = True
                waitingList = lines[50:]
                lines = lines[0:50]
            #or if the capacity is full, set the queue to true 
        except FileNotFoundError:
            #if we dont find a file, print an error and ask again 
            print('Error, cannot read from '+testFile)
            testFile = ''
    #return the needed items 
    return lines, waitingList, queue
def dropFile():
    """input: N/A
    output: a list of file lines
    asks the user for a drop file
    """
    #ask for a file and keep asking until we can read it 
    testFile = ''
    while not testFile.endswith('.txt'):
        testFile = input('Please enter a filename for student records: ')
        try:
            file = open(testFile)
            content = file.read()
            lines = content.splitlines()
        except FileNotFoundError:
            print('Error, cannot read from '+testFile)
            testFile = '' 
    return lines
def enroll(lines, enrollTable,faculties):
    """input: a list version of a file 
    """
    #go through every line, 
    for line in lines:
        #assign the ID, faculty, first and alst name to a split.
        ID, faculty, first, last = line.split(' ')
        #if the ID isnt 6 chars, or not an int, raise an exception 
        if len(ID) != 6 or type(int(ID)) != int:
            raise Exception('ERROR! Invalid ID length or ID cannot be turned into an int')
        #double check if the faculty exists within the dictionary
        faculties[faculty]
        #assign a variable to the class and insert it 
        student = StudentNode(ID, faculty, first, last)
        enrollTable.insert(student)
def enqueue(waitingList, priorityQ,faculties):
    #go through every item
    for item in waitingList:
        #split the item and assign it to astudent 
        ID, faculty, first, last = item.split(' ')
        #if the ID isnt 6 chars, or not an int, raise an exception 
        if len(ID) != 6 or type(int(ID)) != int:
            raise Exception('ERROR! Invalid ID length or ID cannot be turned into an int')
        #double check if the faculty exists within the dictionary
        faculties[faculty]                        
        student = StudentNode(ID, faculty, first, last)
        #add it to the queue
        priorityQ.enqueue(student)    
def removeStudent(lines, faculties, enrollTable, priorityQ):
    #go through every line 
    for line in lines:
        #split the line into the respected variables 
        ID, faculty, first, last = line.split(' ')
        #check if the id and faculties are right 
        if len(ID) != 6 or type(int(ID)) != int:
            raise Exception('ERROR! Invalid ID length or ID cannot be turned into an int')                         
        faculties[faculty]
        #assign the variables to a student 
        student = StudentNode(ID, faculty, first, last)
        try:
            #try to add a student
            enrollTable.remove(student.getID())     
        except Exception as inst:
            #if a student doesn't exist, raise an exception 
            print('WARNING: '+student.getFirstName() + ' '+ student.getLastName() + ' (ID: '+student.getID()+') is not currently enrolled and cannot be dropped.')
        else:
            #if we can remove it, add someone to the table if there is someone waiting in the queue 
            if not priorityQ.isEmpty():
                enrollTable.insert(priorityQ.dequeue())    
def main():
    capacity = 51
    faculties = {'SCI': 4, 'ENG':3, 'BUS':2, 'ART': 1, 'EDU': 0}
    enrollTable = EnrollTable(capacity)
    priorityQ = PriorityQueue()
    queue = False
    userInput = askForInput()
    while userInput != 'Q':
        try:
            #if we are registering, 
            if userInput == 'R':
                #open two text files that will take what we input into a file 
                enrolled = open('enrolled.txt', 'w+')
                waitlist = open('waitlist.txt', 'w+')
                #get the variables from the method 
                lines, waitingList, queue = registerFile(queue, capacity, enrollTable)
                enroll(lines, enrollTable, faculties)
                #if there is a waiting list and the queue is true 
                if queue:
                    enqueue(waitingList, priorityQ,faculties)
                #print the table, the queue and add it to the files 
                print(enrollTable)
                print(priorityQ)
                #add the str to the text and close it 
                enrolled.write(str(enrollTable))
                waitlist.write(str(priorityQ))
                enrolled.close()
                waitlist.close()
            elif userInput == 'D':
                #open the text files 
                enrolled = open('enrolled.txt', 'w+')
                waitlist = open('waitlist.txt', 'w+')
                #ask the user for a file to drop 
                lines = dropFile()

                removeStudent(lines, faculties, enrollTable, priorityQ)
                
                #print the table, the queue, add it to the file and clsoe it 
                print(enrollTable)
                print(priorityQ)  
                enrolled.write(str(enrollTable))
                waitlist.write(str(priorityQ))
                enrolled.close()
                waitlist.close()
        #if any error happens, quit the program with an explanation 
        except Exception as inst:
            print(inst)
            userInput = 'Q'
        except KeyError:
            print('ERROR! Invalid faculty.')
            userInput = 'Q'
        except:
            print('WARNING! An unknown error has occurred while processing your input.')
            userInput = 'Q'
        #if there is no error, ask a user again 
        else:    
            userInput = askForInput()
    print('Closing program... Goodbye.')
main()