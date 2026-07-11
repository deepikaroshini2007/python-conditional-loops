m1=int(input("enter mark 1:"))
m2=int(input("enter mark 2:"))
m3=int(input("enter mark 3:"))
m4=int(input("enter mark 4:"))
m5=int(input("enter mark 5:"))
total=m1+m2+m3+m4+m5
per=total/5
print("The aggregate(total)=",total)
print("Percentage =",per)
if per>=90:
    print("Grade is O")
elif per>=80 and per<90:
    print("Grade is A+")
elif per>=70 and per<80:
    print("Grade is A")
elif per>=60 and per<70:
    print("Grade is B+")
elif per>=55 and per<60:
    print("Grade is B")
elif per>=50 and per<55:
    print("Grade is C")
else:
    print("fail")

