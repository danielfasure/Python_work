#if statement run with a condition
age=int(input(" what is your age "))



if age<13:
    print("you an kid")
elif age>= 13 and age <21:
    print("you are an teenager")
else:
    print("you are an adult")

#grade checker
grade =input("what is your grade ")

if grade >=0 or grade <=59:
    print("F")
elif grade>=60 or grade<=69:
    print("D")
elif grade>=70 or grade <80:
    print("C")
elif grade>=80 or grade <90:
    print("B")
elif grade>=90 or grade <100:
    print("A")
