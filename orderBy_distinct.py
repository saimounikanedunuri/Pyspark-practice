consider df as emp table data in a dataframe

Display all the information of the EMP table?
df.display()

Display unique Jobs from EMP table?
df.withColumn('emp_jobs').distinct().display()

List the emps in the asc order of their Salaries?
df.withColumn('emp_sal').orderBy('asc').display()

List the details of the emps in asc order of the Dptnos and desc of Jobs?
df.withColumn('emp_dept','emp_jobs').orderBy('asc','desc').display()

Display all the unique job groups in the descending order?
df.withColumn('emp_jobs').distinct().orderBy('desc').display()

Display all the information of the EMP table?
df.show()

Display unique Jobs from EMP table?
df.select('emp_jobs').distinct().show()

List the emps in the asc order of their Salaries?
df.orderBy('emp_sal').show() #or below
df.orderBy('emp_sal','asc').show()

List the details of the emps in asc order of the Dptnos and desc of Jobs?
df.orderBy('emp_dept','emp_jobs').orderBy('asc','desc').show()

Display all the unique job groups in the descending order?
df.orderBy('emp_jobs','desc').distinct().show()

Display all the information of the EMP table?
df.show()

Display unique Jobs from EMP table?
df.select('emp_jobs').distinct().show()

List the emps in the asc order of their Salaries?
df.orderBy('emp_sal').show()
#or below
from pyspark.sql.functions import *
df.orderBy(col('emp_sal').asc()).show()

List the details of the emps in asc order of the Dptnos and desc of Jobs?
df.orderBy(col('emp_dept').asc(),col('emp_jobs').desc()).show()

Display all the unique job groups in the descending order?
df.select('emp_jobs').orderBy(col('emp_jobs').desc()).distinct().show()

df.select('emp_jobs').distinct()..orderBy(col('emp_jobs').desc()).show()

df.select('emp_jobs').orderBy(col('emp_jobs').desc()).distinct().show()
Applying .orderBy() before .distinct() may lose the intended sort order due to how Spark optimizes transformations.

Also, the .distinct() should come before .orderBy() to avoid duplicate values interfering with ordering.

✅ Correct version:
df.select('emp_jobs').distinct().orderBy(col('emp_jobs').desc()).show()
