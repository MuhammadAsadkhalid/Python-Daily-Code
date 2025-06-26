# Checking if else statements a user can drive based on their age

age = int(input("Enter your age"))
if (age>18):
 print("You can drive")
else:
 print("You can not drive")

# Checking the grade based on the score input by the user using the if lese statements
score = int(input("Enter your score"))
if(score > 90 and score < 100):
  print("Garde is A+")
elif(score > 80 and score < 89):
    print("Grade is A")
elif(score > 70 and score < 79):
  print("Grade is B")
elif(score > 60 and score < 69):
  print("Grade is C")
elif(score > 50 and score < 59 ):
  print("Grade is D")
elif(score > 33 and score < 49):
  print("Grade is E")
else:
    print("Grade is F")

# Importing the time module to work with timestamps

import time
timetamp =time.strftime('%H:%M:%S')
print(timetamp)
timetamp = time.strftime("%H")
print(timetamp)
timetamp = time.strftime("%M")
print(timetamp)
timetamp = time.strftime("%S")
print(timetamp)


# Using "match case statements" to determine the grade based on the score input by the user

Name = input("Enter your name")
score = int(input("Enter your number"))
match score:
  case _ if score > 0 and score < 32:
    print("The ",Name," student is Fail ")
  case _ if score > 33 and score < 50:
    print("The ",Name," student is Pass ")
  case _ if score > 51 and score < 70:
    print("The ",Name," student is Good ")



    
