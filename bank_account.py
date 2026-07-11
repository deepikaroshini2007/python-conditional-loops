inital_balance =int(input("Enter a amount"))
print("1 for deposit")
print("2 for withdrawal")
type = int(input("enter a type number"))
if type==1:
   amount=int(input("Enter a deposit amount"))
   if amount>=1000:
      balance=amount+inital_balance
      print("Current balance =",balance)
   else:
      print("Minimum deposit amount is greater than 1000 rupees")
elif type==2:
   rupees=int(input("Enter a withdrawal amount"))
   if rupees<inital_balance and rupees>1000:

      remaining=inital_balance-rupees
      print("Current balance =",remaining)
   elif rupees<1000:
      print("minimum withdrawal amount is greater than 1000")
   else:
      print(" Not possible...(it must be less than initial bank balance!!)")
else:
   print("Enter a correct type number")
