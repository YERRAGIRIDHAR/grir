print("Exam results")
print("YERRA GIRIDHAR")
marks = 77
if marks == 35:
    print("you are promoted!")
elif marks > 35:
    print("you passed the exam!")
    if marks > 45 and marks < 54:
        print("Grade C Marks:",marks)
    elif marks > 55 and marks < 64:
        print("Garde C+ Marks:",marks)
    elif marks > 65 and marks < 74:
        print("Grade B Marks",marks)
    elif marks > 75 and marks < 82:
        print("Grade B+ Marks:",marks)
    elif marks > 83 and marks < 90:
        print("Grade A Marks:",marks)
    elif marks > 91:
        print("Grade A+ Marks:",marks)
else:
    print("you failed the exam!","Grade F Marks:",marks)