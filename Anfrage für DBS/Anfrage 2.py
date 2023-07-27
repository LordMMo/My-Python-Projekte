# Anfrage 2
# -------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import cx_Oracle
import numpy as np
#import pandas as pd

cx_Oracle.init_oracle_client(lib_dir = r"")

connection = cx_Oracle.connect("")


cursor = connection.cursor()
cursor.execute("""select distinct clickurl, query, count(distinct querytime) as Anzahl from AOLDATA.QUERYDATA where query not like '%my%space%' and query like '%space%' and clickurl is not null
group by clickurl, query
order by count(distinct querytime) desc """)



x = []
y = []
i = 1

for row in cursor:
    x.append(row[1])
    y.append(int(row[2]))
    i+=1
    if i == 10 : break



labels = ['March']


r = np.arange(len(labels))
width = 0.22
fig, ax = plt.subplots(figsize=(8, 5))



plt.bar(x, y, color = 'black')
plt.xlabel("Click-URL")
plt.ylabel("Anzahl")
plt.xticks(rotation=10)
plt.suptitle('Was wird im Zusammenhang mit “space” gesucht?')

plt.show()




print(x)
print(y)

ax.set_xticks(r)
ax.set_xticklabels(labels)
ax.legend()
