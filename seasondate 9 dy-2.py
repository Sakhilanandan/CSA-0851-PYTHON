month=input("enter mmonth:")
day=int(input("enter day"))
if(month=="Mar"and day>19) or (month=="Apr")or (month=="May") or (month=="June" and day<21):
    season= "Summer"
elif(month=="Jun"and day>20) or (month=="Jul")or (month=="Aug") or (month=="Sep" and day<21):
    season="Spring"
elif(month=="Sep"and day>19) or (month=="Oct")or (month=="Nov") or (month=="Dec" and day<21):
    season="Fall"
else:
    season="Winter"
print("the season cuurent",season)    
    
