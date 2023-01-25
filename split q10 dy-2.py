str1=input("str1:")
str2=input("str2:")
s1=list(str1.split(" "))
s2=list(str2.split(" "))
for i in s1:
    if i in s2:
        s1.remove(i)
        s2.remove(i)
print(*s1)
print(*s2)
