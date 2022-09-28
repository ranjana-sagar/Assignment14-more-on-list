x=input("Enter the element sepreted by comman:")
x=[eval(i) for i in x.split(',')]
for i in x:
    print(i,'=',x.count(i))
