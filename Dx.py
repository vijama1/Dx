import re
print("Hello to Dx this program will solve any integration problem ")
print("Please Read Documentation First")
print("lets get started \nEnter the integrating part  ")
i=1
j=0
integrating=input()
Total=integrating.split('+')
for plus in Total:
    minuses=plus.split('-')
    Total[j]=minuses[0]
    j=j+1
    while i<=len(minuses)-1:
        Total.append(minuses[i])
        i=i+1
print(Total)
print('\n\n Now enter the integrating factor\n')
dx=input()
final=[]
print('\n')
for integrating in Total:
    i=0
    this=[]
    x=0
    y=re.findall('[0-9]+',integrating)
    for factor in integrating:
        if factor==dx:
            x=x+1
    y=int(y[0])
    x=x+1
    y=y*(x)
    this.append(y)
    for z in integrating:
        try:
            z=int(z)
        except:
            if z!=dx:
                this.append(z)

    while i<x:
        this.append(dx)
        i=i+1
    final.append(this)

print(final)






input()
