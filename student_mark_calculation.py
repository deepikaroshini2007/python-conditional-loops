m1=int(input(&quot;enter mark 1:&quot;))
m2=int(input(&quot;enter mark 2:&quot;))
m3=int(input(&quot;enter mark 3:&quot;))
m4=int(input(&quot;enter mark 4:&quot;))
m5=int(input(&quot;enter mark 5:&quot;))
total=m1+m2+m3+m4+m5
per=total/5
print(&quot;The aggregate(total)=&quot;,total)
print(&quot;Percentage =&quot;,per)
if per&gt;=90:

print(&quot;Grade is O&quot;)
elif per&gt;=80 and per&lt;90:
print(&quot;Grade is A+&quot;)
elif per&gt;=70 and per&lt;80:
print(&quot;Grade is A&quot;)
elif per&gt;=60 and per&lt;70:
print(&quot;Grade is B+&quot;)
elif per&gt;=55 and per&lt;60:
print(&quot;Grade is B&quot;)
elif per&gt;=50 and per&lt;55:
print(&quot;Grade is C&quot;)
else:
print(&quot;fail&quot;)
