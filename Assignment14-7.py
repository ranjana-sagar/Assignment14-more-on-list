x=input("Enter the number sepreted by comman:")
x=[eval(i) for i in x.split(',')]
print(x)
b=[]
for i in x:
    if type(i)==int:
        b.append(i)
print(b)        
        
