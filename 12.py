# https://www.hackerrank.com/challenges/30-inheritance/problem

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNum, scores):
        self.scores=scores
        Person.__init__(self,firstName, lastName, idNum)
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    # Write your function here
    def calculate(self):
        # addition = 0
        # for i in range(0,len(scores)):
        #     addition=addition+scores[i]
        a = sum(self.scores)/len(self.scores)
        if a>=90 and a<=100: return "O"
        elif a>=80: return "E"
        elif a>=70: return "A"
        elif a>=55: return "P"
        elif a>=40: return "D"
        else: return "T"                      
        
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())