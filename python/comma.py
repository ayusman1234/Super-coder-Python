ara = list(map(int,input().split(",")))
num1 = sum(ara[:ara.index(5)])+sum(ara[ara.index(8)+1:])
print(num1)
l = ara[ara.index(5):ara.index(8)+1]
print(l)
num2 = ""
for i in l:
    num2+=str(i)
print(int(num2)+num1)
