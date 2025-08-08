num = 123

p=1

while num>0:
    
    d = num%10
    p*=d
    num//=10
    
print("The product of digital:",p)