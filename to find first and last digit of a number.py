n = 12345

print("The number is:",n)
ld = n%10

fd = n

while fd >= 10:
    fd//=10
     
print("The last digit is:",ld)
print("The first digit is:",fd)