import re
print("Hello to Dx this program will solve any integration problem ")
print("Please Read Documentation First")
print("Lets get started \nEnter the integrating part  ")
i=1
j=0
integrating=input("Enter your input")
Total=integrating.split('+')
for plus in Total:
    minuses=plus.split('-')
    Total[j]=minuses[0] #assigning the first term to Total List
    j=j+1
    while i<=len(minuses)-1:
        Total.append(minuses[i])
        i=i+1
print('\n\n Now enter the integrating factor\n')
dx=input()
final=[]
print('\n')
for integrating in Total:
    this=[]
    x=0
    i=0
    pos=integrating.find('^')+1#finding power positon
    y=integrating[pos:]#slicing the power form the terms
    y=int(re.findall('[0-9]+',y)[0])
    x=int(re.findall('[0-9]+',integrating[0:pos])[0])
    y=y+1
    this.append(x)
    this.append('/')
    this.append(y)

    for z in integrating[0:pos-1]:
        try:
            z=int(z)#if the part of term is a integer it is not added in the output
        except:
            if z!=dx:
                this.append(z)#only the terms which are not integrating factor are added in the List
    this.append(" x^")
    this.append(y)
    final.append(this)
while i<len(final):
    final[i]=''.join(str(e) for e in final[i])
    i=i+1
print(final)

