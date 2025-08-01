list1 = [1,2,3,4,5]
list2 = [3,4,6,7,8]
print("The first list:",list1)
print("The second list",list2)
common = list(set(list1) & set(list2) )
print("The common items is:",common)