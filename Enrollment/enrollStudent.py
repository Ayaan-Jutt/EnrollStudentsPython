#******************************************************
# Assignment 3 Task 1: Create a table and queue for students
# Author: Ayaan Jutt
# Collaborators/References: Assistance from Mansur Gulami (TA) and Kseniia Priakhina (TA) on how to better my code 
#******************************************************

class StudentNode():
    def __init__(self, studentId, faculty, first, last):
        """Input: an ID, the Faculty, first and last name
        return: None
        initializes the Student Node with next and previous set to None
        """
        self.studId = studentId
        self.faculty = faculty
        self.first = first
        self.last = last 
        self.previous = None
        self.nextStudent = None
    def setID(self,studentId):
        """input: a new Id
        output: None
        a setter for ID
        """
        self.studId = studentId
    def setFac(self,faculty):
        """input: a new faculty
        output: None
        a setter for Fac
        """
        self.faculty = str(faculty[0:3])
    def setFirstName(self,first):
        """input: a new first name
        outpt: None
        a setter for the first name
        """
        self.first = first
    def setLastName(self,last):
        """input: a new Last name
        output: None
        a setter for the last name 
        """
        self.last = last
    def setNext(self,studNext):
        """input: a new next
        output: None
        a setter for next item
        """        
        self.nextStudent = studNext
    def setPrevious(self,previous):
        """input: a new previous
        output: None
        a setter for previous
        """        
        self.previous = previous
    def getID(self):
        """input: None
        output: the ID
        a getter for an ID
        """
        return str(self.studId)
    def getFac(self):
        """input: None
        output: the Fac
        a getter for a fac
        """        
        return self.faculty
    def getFirstName(self):
        """input: None
        output: the firstname
        a getter for a First name
        """        
        return self.first
    def getLastName(self):
        """input: None
        output: the lastName
        a getter for a lastname
        """        
        return self.last
    def getNext(self):
        """input: None
        output: the next item
        a getter for a next item
        """        
        return self.nextStudent
    def getPrevious(self):
        """input: None
        output: the previous item
        a getter for a previous item
        """        
        return self.previous
class EnrollTable():
    def __init__(self, capacity):
        """input, a capacity for how many students can go into a table
        output: None
        intializes the table with a given capacity 
        """
        #create an empty table, its size and using a for loop, create a given amount of items 
        self.table = []
        self.tableSize = 0
        self.capacity = capacity
        for number in range(self.capacity):
            self.table.append(None)
    def cmputIndex(self, studentId):
        """input: a student ID
        output: an index of where to put the student
        gets a student ID, and returns it with their given index
        """
        #turn the str of the ID into a list 
        studentIdList = list(studentId)
        #create a studentIndex int  
        studentIndex = 0
        #go through the list by an increment of 2
        for number in range(0,len(studentIdList), 2):
            #if the number matches the second last item in the list
            if number == len(studentIdList) - 2:
                #add to the index the second last and the last index together squared 
                studentIndex += (int(studentIdList[number]+ studentIdList[number + 1]))**2
    
            else:
                #else add the two items just together
                studentIndex += int(studentIdList[number] + studentIdList[number + 1])
        #modulus the index by the capacity and return the index
        studentIndex = studentIndex % self.capacity
        return studentIndex
    def insert(self, item):
        """input: an item
        output: None
        inserts a student into the list
        """
        if item != None:
            #as long as the size is less than the capacity
            if self.size() < self.capacity:
                #set the previous to None, and create the index 
                item.setPrevious(None)
                item.setNext(None)
                indexToAdd = self.cmputIndex(item.getID())
                #if nothing is at the index, just add the item
                if self.table[indexToAdd] == None:
                    self.table[indexToAdd] = item
                else: 
                    #else, go through every item until the ID is less than the current one, set the item after that 
                    current = self.table[indexToAdd]
                    
                    while current.getNext() != None and item.getID() > current.getID():
                        
                        current = current.getNext()
                        #print(current
                    item.setNext(current.getNext())
                    current.setNext(item)
                #increase the tableSize 
                self.tableSize += 1
    def remove(self, studentID):
        """input: a studentID
        output: None
        removes a student from the list 
        """
        #find the index of the student, and start the current from there
        indexToRemove = self.cmputIndex(studentID)
        current = self.table[indexToRemove]
        #create 2 variables, one to check the previous item, the other a boolean to if the student was removed
        previous = None
        studentRemoved = False
        #if the person doesn't exist raise an exception
        if current == None:
            raise Exception()            
            #keep going through the linked list till we find the item
        while current.getNext() != None and not studentRemoved:
            if current.getID() == studentID:
                studentRemoved = True 
            else:
                #keep in check the previous item and set the next item to be the current 
                previous = current
                current = current.getNext()
        if previous == None:
            #if we are removing the first item, decrease the index and the new head of the list is the next item
            self.tableSize -= 1
            self.table[indexToRemove] = current.getNext()
        else:
            #if it's somewhere else, take out the item to remove by setting the previous items next to the one after the current 
            previous.setNext(current.getNext())
            self.tableSize -= 1

    def isEnrolled(self, studentID):
        """input: a studentID 
        output: a boolean on whether or not the student is within the table
        gets a student ID and finds out whether or not it exists within the table 
        """
        #get the index
        studentIndex = self.cmputIndex(studentID)
        #get the head at the index 
        current = self.table[studentIndex]
        #if there is nothing there, return false 
        if current == None: 
            return False
        else:
            #go through the entire list within the index 
            while current.getNext() != None:
                #if the ID matches, return true, else keep going 
                if current.getID() == studentID:
                    return True
                else:
                    current = current.getNext()
            #if we have reached the end, return False 
            return False 
    def size(self):
        """input: N/A
        output: the size 
        a getter for the size
        """
        return self.tableSize
    def isEmpty(self):
        """input: N/A
        output: a boolean for if the table is empty
        checks if the table is empty
        """
        return self.tableSize == 0
    def __str__(self):
        """input: N/A
        output: a str version of our table 
        creates a string version of our table to display
        """
        #start off with a str
        enrollStr = '['
        #go through every item inthe table as long as it isn't None
        for studentIndex in range(len(self.table)):
            if self.table[studentIndex] != None:
                #get the first student, their index, id, fac, first and last name add it to the string and get the next student 
                student = self.table[studentIndex]
                enrollStr += str(studentIndex) + ': ' + student.getID() + ' ' + student.getFac() + ' ' + student.getFirstName() + ' ' + student.getLastName() + ', '
                student = student.getNext()
                #while there are still students, do the same thing 
                while student != None:
                    enrollStr += student.getID() + ' ' + student.getFac() + ' ' + student.getFirstName() + ' ' + student.getLastName() + ', '
                    student = student.getNext()
                #after that start a new line 
                enrollStr += '\n'
        #if there are students in a list, add a closing bracket after taking out some spaces and new lines, else just add the closing bracket as is and return 
        if len(enrollStr) > 2:
            enrollStr = enrollStr[:-3] + ']'
        else:
            enrollStr += ']'
        return enrollStr
class PriorityQueue():
    def __init__(self):
        """input: N/A
        output: None
        initializes the variables needed to make a queue 
        """
        #create a head, tail, a queue size and a priority queue 
        self.priorityDict = {'SCI':4, 'ENG': 3, 'BUS': 2, 'ART': 1, 'EDU': 0}
        self.head = None
        self.tail = None 
        self.qSize = 0 
    
       
    def enqueue(self, item):
        """input: a student item
        output: None
        enqueues a student by prioirtiy 
        """
        
        #create a variable referencing the fac 
        studFac = self.priorityDict[item.getFac()]
        #if there is nothing within the list...
        if self.isEmpty():
            #assign the head and the tail to the same item 
            self.head = item
            self.tail = item 
        elif studFac > self.priorityDict[self.head.getFac()]:
            #if the priority is higher than the head, the item should be the new head 
            item.setNext(self.head)
            self.head.setPrevious(item)
            self.head = item
        elif studFac < self.priorityDict[self.tail.getFac()]:
            #if the prioirity is less than the tail, the item should be the new tail 
            self.tail.setNext(item)
            item.setPrevious(self.tail)
            self.tail = item
        else:
            current = previous = self.head
             
            currentFac = self.priorityDict[self.head.getFac()]
            while current.getNext() != None and currentFac >= studFac:
                previous = current
                current = current.getNext()
                currentFac = self.priorityDict[current.getFac()]
            previous.setNext(item)
            item.setNext(current)
        self.qSize += 1
            

    def dequeue(self):
        """input: N/A
        output: the student we want to dequeue or None
        gets the first student, takes it out and returns it 
        """
        #if self:
        try:
            #try to dequeue an Item, if it's empty raise an error 
            if self.head == None:
                raise Exception('Cannot dequeue from an empty list')
            #else get the head, re-assign the head to the next item and return it 
            current = self.head
            self.head = self.head.getNext()
            self.qSize -= 1
            return current
        except Exception as inst:
            print(inst)
    def isEmpty(self):
        """input: N/A
        output: a bool whether or not the queue is empty
        checks if the size is empty
        """
        return self.head == None 
    def __str__(self):
        """input: N/A
        output: a str of the queue 
        turns the queue into a string 
        """
        #start at the head, create a string starting with an opening bracket 
        current = self.head
        pQStr = '['
        #keep going through the queue, add the id, fac, first name and last name and add a new line 
        while current != None:
            
            pQStr += current.getID() + ' ' + current.getFac() + ' '+ current.getFirstName() + ' '+ current.getLastName() + ',\n'
            current = current.getNext()
        #if there is something in a queue, add the closing bracket to the end, skipping past a new line and a comma 
        if len(pQStr) > 2:
            pQStr = pQStr[:-2] + ']'
        else:
            #else add a closing bracket as is 
            pQStr += ']'
        #return it 
        return pQStr

if __name__ == '__main__':
    sN  = StudentNode('129051', 'SCI', 'a','b')
    sN2 = StudentNode('188451', 'ART', 'c','d')
    sN3  = StudentNode('129051', 'ENG', '1','b')
    sN4 = StudentNode('188451', 'ART', '1','d')
    sN5 = StudentNode('188453', 'ART', '2','f')
    
    sN6 = StudentNode('188450', 'EDU', '1','h')
    sN7 = StudentNode('124830', 'EDU', '2','j')
    sN8 =  StudentNode('129051', 'SCI', '1','b')
    sN9 = StudentNode('188459', 'EDU', '3','H')
    sN10 =  StudentNode('129049', 'SCI', '2','b')
    sN11  = StudentNode('129051', 'ENG', '2','b')
    sN12  = StudentNode('129051', 'BUS', '1','b')
    sN13 =  StudentNode('129049', 'SCI', '3','b')
    sN14=  StudentNode('129049', 'SCI', '4','b')
    sN15 =  StudentNode('129049', 'SCI', '5','b')
    sN16 =  StudentNode('129049', 'SCI', '6','b')
    eT = EnrollTable(51)
    print(eT.isEmpty())
    pQ = PriorityQueue()
    
    eT.insert(sN)
    eT.insert(sN2)
    eT.insert(sN7)
    eT.insert(sN5)
    eT.remove(sN5.getID())
    try:
        eT.remove(sN6.getID())
    except Exception:
        print('WARNING: '+sN6.getFirstName() + ' '+ sN6.getLastName() + ' (ID: '+sN6.getID()+') is not currently enrolled and cannot be dropped.') 
    print(eT.isEmpty())
    print(eT)
    pQ.enqueue(sN3)
    pQ.enqueue(sN8)
    pQ.enqueue(sN6)
    pQ.enqueue(sN4)
    pQ.enqueue(sN5)
    pQ.enqueue(sN9)
    pQ.enqueue(sN10)
    pQ.enqueue(sN11)
    pQ.enqueue(sN12)
    pQ.enqueue(sN13)
    pQ.enqueue(sN14)
    pQ.enqueue(sN15)
    pQ.enqueue(sN16)
    print(pQ)
    for item in range(14):
        eT.insert(pQ.dequeue())
    print(eT)