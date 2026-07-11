salary=int(input("Enter the salary of an employee :"))
leave=int(input("Enter no of days the employee was absent :"))
if leave>=0 and leave<=2:
   print("Employee salary =",salary)
elif leave>2:
   print("Employee salary =",salary-((leave-2)*500))
else:
   print("Invalid leave")

