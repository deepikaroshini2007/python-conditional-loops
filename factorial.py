n=int(input(&quot;enter the number=&quot;))
fact=1
if n&lt;0:
print(&quot;Factorial not possible&quot;)
else:
for i in range(1,n+1):
fact=fact*i
print(&quot;The factorial of&quot;,n,&quot;is&quot;,fact)
