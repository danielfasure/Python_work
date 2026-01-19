
firstname=input("what is your first name \n ")
surname=input(" and what is your last name \n ")
#you can concat your strings together using plus
print("thank for the answer your name is "+ firstname+" "+surname)

#if you want to add variable to your statement add f "" and for the variable your refering to use {} this will tell them to search and turn thoses variable into string

print(f"thank for the answer your name is {firstname} {surname}")

#to variable is not a string and you try to add them together you will get an error
#to avoided that make to use type casting str()
age = input("what is your age \n")
print("thank you "+firstname +" "+ surname + " age: "+str(age))
