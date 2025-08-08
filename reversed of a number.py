num = 12345
print("The original number:",num)
r=0
while num>0:
    
    d = num%10
    r = r*10+d
    num//=10

print("The reversed number is:",r)