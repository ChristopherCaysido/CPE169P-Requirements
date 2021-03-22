"""
File: student.py
Resources to manage a student's name and test scores.

Task : Add three methods to the Student class that compare two Student objects. 
One method should test for equality. A second method should test for less than. 
The third method should test for greater than or equal to. 
In each case, the method returns the result of the comparison of the two students’ names. 
Include a main function that tests all of the comparison operators.

Name: Christopher Nilo A. Caysido
"""
import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    #Make a method that compares two objects
    @classmethod
    def isEqual(cls,score1,score2):
        if score1 == score2:
            print("The scores are for both students are equal")
        else:
            print("The scores are not equal")
    @classmethod
    def isLessThan(cls,score1,score2):
        if score1 < score2:
            print(str(score1) + " is less than " + str(score2))
        else:
            print(str(score1) + " is not less than " + str(score2))
    @classmethod
    def greaterOrEqual(cls,score1,score2):
        if score1 >= score2:
            print(str(score1) + " is greater than or equal than " + str(score2))
        else:
            print(str(score1) + " is not greater " + str(score2))

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    """A simple test."""
    student1 = Student("Ken", 4)
    student2 = Student("Barbie",4)
    for i in range(1,4):
        student1.setScore(i,random.randint(60,100))
        student2.setScore(i,random.randint(60,100))
    student1HighScore = student1.getHighScore()
    student2HighScore = student2.getHighScore()
    print( student1.name+": "+str(student1HighScore) +"\n",student2.name+": "+str(student2HighScore))
    Student.isEqual(student1HighScore,student2HighScore)
    Student.isLessThan(student1HighScore,student2HighScore)
    Student.greaterOrEqual(student1HighScore,student2HighScore)


if __name__ == "__main__":
    main()
