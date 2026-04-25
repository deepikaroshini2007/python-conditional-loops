inital_balance =int(input(&quot;Enter a amount&quot;))
print(&quot;1 for deposit&quot;)
print(&quot;2 for withdrawal&quot;)
type = int(input(&quot;enter a type number&quot;))
if type==1:
amount=int(input(&quot;Enter a deposit amount&quot;))
if amount&gt;=1000:
balance=amount+inital_balance
print(&quot;Current balance =&quot;,balance)
else:
print(&quot;Minimum deposit amount is greater than 1000 rupees&quot;)
elif type==2:
rupees=int(input(&quot;Enter a withdrawal amount&quot;))
if rupees&lt;inital_balance and rupees&gt;1000:

remaining=inital_balance-rupees
print(&quot;Current balance =&quot;,remaining)
elif rupees&lt;1000:
print(&quot;minimum withdrawal amount is greater than 1000&quot;)
else:
print(&quot; Not possible...(it must be less than initial bank balance!!)&quot;)
else:
print(&quot;Enter a correct type number&quot;)
