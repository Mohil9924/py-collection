my_list = [1,1,2,2,3,3,4,4,5,5]

print("Before removing the duplicates:",my_list)
my_list = list(dict.fromkeys(my_list))

print("After removing the duplicates:",my_list) 


