# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#using max or min function

# print(max(student_scores))

# by using for loops
# n=0
highest_score = 0 
for n in range(0, len(student_scores)):
  if student_scores[n] > highest_score:
    highest_score = student_scores[n]

# highest_score = 0 
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score 
print(f" The highest score in the class is : {highest_score}")