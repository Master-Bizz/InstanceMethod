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

