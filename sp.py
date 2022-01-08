'''
Q1. Remove repeating chacaters form following string x = "Python is the best programming language"1. A three digit number is said to be an “Armstrong number” if the sum of the third power of its individual digits is equal to the number itself. Example: 371 is an Armstrong number as 371 = 3 3 + 7 3 + 1 3 407 is an Armstrong number as 407 = 4 3 + 0 3 + 7 3 Write a pseudo-code to check whether a given three digit number is an Armstrong number.
''' 

x = "Python is the best programming language"
x = x.lower()
y = list(x)
z = []
for i in y:
    if y.count(i) > 1:
        y.remove(i)
for i in y:
    if y.count(i) > 1:
        y.remove(i)
print(y)