my_list = [2,3,4,5,6]
#list are a collection of data

print(my_list)

#index of a list always start with zero
print(my_list[0])#this should return the first value

#can get a range using : ([0:2]) it will start with 0 value and stop and the value before 2
print(my_list[0:2])

#adding a value to the end of the list .append(value)
my_list.append(2)
print(my_list)

#replacing a value in the list can be done like this index list[0]= 1 this will reset the value stored at that location
my_list[0] = 10
print(my_list)

#inserting a value using .insert(2,100) method, 2 being the index and the later being where it is inserted at then all other values after will be updated
my_list.insert(1,2)
print(my_list)

#to remove a know value .remove method is used which search the list for the value inside and remove all instaces of that value
my_list.remove(2)
print(my_list)

#to remove value at a certain index use .pop()with the value being the index you want value to be removed
my_list.pop(1)
print(my_list)
#sorting value from smallest to greatest is done using .sort()
my_list.sort()



