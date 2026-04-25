salary=int(input(&quot;Enter the salary of an employee :&quot;))

leave=int(input(&quot;Enter no of days the employee was absent :&quot;))
if leave&gt;=0 and leave&lt;=2:
print(&quot;Employee salary =&quot;,salary)
elif leave&gt;2:
print(&quot;Employee salary =&quot;,salary-((leave-2)*500))
else:
print(&quot;Invalid leave&quot;)
