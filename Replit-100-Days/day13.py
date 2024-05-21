# Day 13 - Replit 100 Days of Code              #
# Author: Frederick Pellerin                    #
# --------------------------------------------- #

exam_name = input("What is the name of the exam? ")
exam_max_score = int(input("What is the maximum score? "))
exam_score = int(input("What is your score? "))
exam_percentage = int(round(exam_score / exam_max_score * 100, 2))

print()
print('-'*20)
print()
print(f"You got {exam_percentage}% on your {exam_name} exam.")
if exam_percentage >= 90:
  print("You got", exam_percentage,"% which is an A+")
elif exam_percentage >= 80:
  print("You got", exam_percentage,"% which is an A")
elif exam_percentage >= 70:
  print("You got", exam_percentage,"% which is a B")
elif exam_percentage >= 60:
  print("You got", exam_percentage,"% which is a C")
elif exam_percentage >= 50:
  print("You got", exam_percentage,"% which is a D")
else:
  print("You got", exam_percentage,"% which is a U")
