labs_completed = int(input("Enter the number of labs completed: "))

quiz_completed = int(input("Enter the number of quizzes completed: "))

assignment_1 = int(input("Enter grade for Assignment 1: "))
assignment_2 = int(input("Enter grade for Assignment 2: "))
assignment_3 = int(input("Enter grade for Assignment 3: "))
assignment_4 = int(input("Enter grade for Assignemnt 4: "))

midterm_1 = int(input("Enter grade for Midterm 1: "))
midterm_2 = int(input("Enter grade for Midterm 2: "))

final_exam = int(input("Enter grade for Final Exam: "))
mid_and_fin_prep = int(input("Enter grade for Midterm and Final Preparation: "))

labs_weight = labs_completed/6 * 20 if labs_completed <= 6 else 20
quiz_weight = quiz_completed/6 * 15 if quiz_completed <= 6 else 15

assignment_weight = (assignment_1 * 0.04) + (assignment_2 * 0.04) + (assignment_3 * 0.04) + (assignment_4 * 0.04)
midterms_weight = (midterm_1 * 0.125) + (midterm_2 * 0.125)
final_weight = (final_exam * 0.18)
mid_and_fin_pr_wt = (mid_and_fin_prep * 0.06)

total_grade =  labs_weight + quiz_weight + assignment_weight + midterms_weight + final_weight + mid_and_fin_pr_wt
total_grade = round(total_grade)

print("Your grade is: " + str(total_grade))

