year=eval(input("enter year:"))
if year <=0 or year == float:
    print("invalid")    
if year%400== 0:
    print("is aleap year",year+4)
elif year%100== 0:
    print("is not a leap year:")
elif year%4== 0:
    print("is aleapyear:")
else :
   print("not leapyear:")
   m=year%4
   print("previous leap year",year-m)

