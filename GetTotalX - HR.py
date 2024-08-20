def getTotalX(a, b):
   count = 0
    
   for i in range(1,101):
     if isMultiple(i, a) and isFactor(i,b):
       count+=1
   return count
  
def isMultiple(a, array):
   for i in array:
     if a % i != 0:
       return False
   return True

def isFactor(a, array):
   for i in array:
     if i % a != 0:
       return False
   return True
