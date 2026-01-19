"""
sets are similar to list but are unorder and cannot contain duplicates only allow unique values
when setting a set curly brackets are used {}
"""
my_sets={1,5,3,5,5,5,10,7,11}
#here the set will only store on set of 5
print(my_sets)

#this will show that the values are not stored in any order
for integer in my_sets:
    print(integer)

# print(my_sets[1]) this wont work as with set they dont store the values in a order so there will be nothing for python to print

#to get rid of value you use the method .discard(value) and it will search for that value in the set
my_sets.discard(3)
#to get rid of all elements you can use .clear

#to add a value to a set you can use .add(value)
my_sets.add(12)
#to add lots of vaues use .update([value1,value2,value3])
my_sets.update([1,3,4,5])
