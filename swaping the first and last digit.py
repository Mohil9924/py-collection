n = 12345

print("The number is:",n)

ld = n%10
temp = 0
fd = n

while fd >= 10:
    fd//=10
    
temp = fd
fd = ld
ld = temp


print("The last digit after swaping is:",ld)
print("The first digit after swaping is:",fd)