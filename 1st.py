arr=[] 
total=0;
counter=0
values=int(input("enter number of times you run around a racetrack:"))
for i in range(values):
    timeOfLap=int(input("enter the lap time for each round:"))
    arr.append(timeOfLap)
    total+=timeOfLap
    counter+=1
fast=max(arr)
print("fastest lap time",fast)
slow=min(arr)
print("slowest lap time",slow)
print("average lap time:",total/counter)
years=int(input("enter number of years "))
total=0
for i in range(1,years+1):
    for j in range(1,13):
        rain=float(input("enter inches of rainfall "))
        total+=rain
    a=j*years
    average=total//a
    print("total inches of rainfall ",total)
    print("total number of months in a year ",j)
    print("average rainfall per month ",average,"%")