"""
Docstring for dictionary
    - it contains a "key" and "value"
    -key and value seperated by:
    -key on the left side value on the right side 
    -represent in {}and , to start a new key and value 
    -string represented by '' 
    
"""
user_dictionary = {
    'username':'daniel',
    'age':32
}
#when you print the dictionary all value are shown 
print(user_dictionary)

#when you want to show a specific key value the method used get "keyname"
print(user_dictionary.get("username"))

#you can add a new key and value (dictonary variable)[key]=value
user_dictionary["married"]=False
print(user_dictionary)

#using len before dictonary variable will give how many key and values are stored inside it 
print(len(user_dictionary))

#can remove an key and value using (dictonary).pop(key_name)
user_dictionary.pop("married")

#can remove all key and value by running dictonary.clear

#and finally you can delete the dictonary by using del dictonary_you_want_to_delete

#looping through to get dictonary values and keys
for x,y in user_dictionary.items:
    print(x,y)

#looping to get all keys
for x in user_dictionary:
    print(x)    

#copy a directonary to chage it value 
user_dictionary2 =user_dictionary.copy #this stop the python interper from making changes to the orginal dictonary
user_dictionary["occupation"]="unemployed"