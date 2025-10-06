print("Takshashila University")
print("Ongur,tindivanam")
print("-----------------")
print("Student mark list")
print("-----------------")
num1=int(input("Enter the python mark:"))
num2=int(input("Enter the DBMS mark:"))
num3=int(input("Enter the industry mark:"))
total=num1+num2+num3
print("Total mark:",total)
avg=total/3
print("Average mark:",avg)
if(num1>=40 and num2>=40 and num3>=40):
    print("Result:Pass")
else:
    print("Result:Fail")
if(total>=250):
    print("Grade:O grade")
elif(total>=200):
    print("Grade:A+ grade")
elif(total>=150):
    print("Grade:A grade")
else:
    print("Grade:B grade")
