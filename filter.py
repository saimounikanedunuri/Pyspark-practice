Display all the details of all ‘Mgrs’
select * from emps
where emp_designation='Mgrs'

df.select(*).filter(emp_designation='Mgrs').show()

List the emps who joined before 1981.
select * from emps
where extract(year emp_join) <1981

df.select(*).filter(extract(col('emp_join'),year) <1981).show()

List the Empno, Ename, Sal, Daily sal of all emps in the asc order of Annsal.
select Empno, Ename, Sal, (sal/30) as daily_sal
from emps order by sal asc

df.select('Empno', 'Ename', 'Sal', (sal/30) as 'daily_sal').orderBy('Sal').show()

Display the Empno, Ename, job, Hiredate, Exp of all Mgrs
select Empno, Ename, job, Hiredate, Exp 
from emps where Job='Mgr'

df.select('Empno', 'Ename', 'job', 'Hiredate', 'Exp').filter(col('Job')='Mgr').show()

List the Empno, Ename, Sal, Exp of all emps working for Mgr 7369.
select Empno, Ename, Sal, Exp 
from emps where Mgr=7369

df.select('Empno', 'Ename', 'Sal', 'Exp').filter(col('Mgr')=7369).show()
========================================================================================
Display all the details of all ‘Mgrs’
df.filter(col('job')=='Mgr').show()

List the emps who joined before 1981.
df.filter(year(col('join_date' < 1981))).show()

List the Empno, Ename, Sal, Daily sal of all emps in the asc order of Annsal.
df.select('Empno', 'Ename', 'Sal', col('Sal')/30 alias 'Daily_sal').orderBy(col('Sal')*12,asc).show() 

NOT.Display the Empno, Ename, job, Hiredate, Exp of all Mgrs
df.select('Empno', 'Ename', 'job', 'Hiredate', 'Exp').filter(col('job')=='Mgr').show()

List the Empno, Ename, Sal, Exp of all emps working for Mgr 7369.
df.select('Empno', 'Ename', 'Sal','Exp').filter(col('Mgr')==7369).show()
=============================================================================
Display all the details of all ‘Mgrs’
df.filter(col('job')=='Mgr').show()

List the emps who joined before 1981.
df.filter(year(col('join_date')) < 1981).show()

List the Empno, Ename, Sal, Daily sal of all emps in the asc order of Annsal.
df.select('Empno', 'Ename', 'Sal', (col('Sal')/30).alias('Daily_sal')).orderBy((col('Sal')*12).asc()).show() 

NOT.Display the Empno, Ename, job, Hiredate, Exp of all Mgrs
df.select('Empno', 'Ename', 'job', 'Hiredate', 'Exp').filter(col('job')=='Mgr').show()

List the Empno, Ename, Sal, Exp of all emps working for Mgr 7369.
df.select('Empno', 'Ename', 'Sal','Exp').filter(col('Mgr')==7369).show()









