Display all the details of the emps whose Comm. Is more than their Sal.
df.filter(col('comm')>col('sal')).show()

List the emps in the asc order of Designations of those joined after the second half- of 1981.
df.filter(col('joined')>'1981-06-30').orderBy('designation').asc().show()

Not.List the emps along with their Exp and Daily Sal is more than Rs.100.
df.select('emp_name','exp',(col('sal')/30).alias('daily_sal')).filter((col('sal')/30)>100).show()

List the emps who are either ‘CLERK’ or ‘ANALYST’ in the Desc order.
df.filter('designation').in(‘CLERK’,‘ANALYST’).orderBy('designation').desc().show()

List the emps who joined on 1-MAY-81,3-DEC-81,17-DEC-81,19-JAN-80 in asc order of seniority.
df.filter('joined').in('1981-05-01','1981-12-03','1981-12-17','1980-01-19').orderBy('joined').asc().show()
----------------------------------------------------------------------
Display all the details of the emps whose Comm. Is more than their Sal.
df.filter(col('comm')>col('sal')).show()

List the emps in the asc order of Designations of those joined after the second half- of 1981.
df.filter(col('joined')>'1981-06-30').orderBy(col('designation').asc()).show()

Not.List the emps along with their Exp and Daily Sal is more than Rs.100.
df.select('emp_name','exp',(col('sal')/30).alias('daily_sal')).filter((col('sal')/30)>100).show()

List the emps who are either ‘CLERK’ or ‘ANALYST’ in the Desc order.
df.filter(col('designation').isin(‘CLERK’,‘ANALYST’)).orderBy(col('designation').desc()).show()

List the emps who joined on 1-MAY-81,3-DEC-81,17-DEC-81,19-JAN-80 in asc order of seniority.
df.filter(col('joined').isin('1981-05-01','1981-12-03','1981-12-17','1980-01-19')).orderBy(col('joined').asc()).show()
