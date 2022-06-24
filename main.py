student_scores = {
  "Pedro": 81,
  "Carmen": 78,
  "Ella": 99, 
  "Maria": 74,
  "Jose": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

for key in student_scores:
  score = student_scores[key]
  if score > 90:
    student_grades[key] = "Outstanding"
  elif score > 80: 
    student_grades[key] = "Exceeds Expectations"
  elif score < 70:
    student_grades[key] = "Acceptable"
  else:
    student_grades[key] = "Fail"

#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇
print(student_grades)





