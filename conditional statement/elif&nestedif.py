age=int(input("Enter your age:" ))
if age>=18 and age<=25:
    print("you are eligible for admission")

    marks=int(input("Enter your marks:"))
    if marks>=90:
        print("Admission is success")
    elif marks<90 and marks>75:
        print("you need to pay 2 lakh rs for admission")
    elif marks<75 and marks>50:
        print("you need to pay 4 lakh Rs for admission")
    elif marks<50 and marks>35:
        print("you need to pay 8 lakh Rs for admission")
    else:
        print("you are not eligible for addmission ")
else:
    print("you are not eligible for addmission due to age")