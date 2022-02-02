'''
Instance Methods
'''

class Student:
   def __init__(self,scores = []):
       self.scores = scores

   def avg(self):
       return round (sum(self.scores) / len(self.scores))

# Object / Intance
bizz = Student(scores = [2,20,30,14,25,9,14])
Tee = Student(scores = [1,21,3,1,25,6,17])
print(bizz.avg())
print(Tee.avg())

'''
Static Methods
'''   # Doesn't require access to instance, absent of any 'self'.

class Student:
   def __init__(self,scores = []):
       self.scores = scores

   def avg(self):
       return round (sum(self.scores) / len(self.scores))

   @staticmethod
   def notice():
       return 'Be wise and revise!'

Tj = Student(scores = [9,281,233,121,125,63,117])
print(Student.notice())
print(Tj.notice())