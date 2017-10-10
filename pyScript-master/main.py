import os
#printing the available options
print("Enter the file Number you want to run")
print("Enter 1 for Students to Teacher, 2 for Battleship, 3 for Exam Statistics")
value=int(input("Option:  "))

#sending user to selected script
if option_selected_by_user==1:
    os.system('python students_to_teacher.py')
elif option_selected_by_user==2:
    os.system('python battleship.py')
elif option_selected_by_user==3:
    os.system('python exam_stats.py')
