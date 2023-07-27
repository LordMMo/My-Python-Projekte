# Anfrage 4
# -------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import cx_Oracle
import numpy as np
#import pandas as pd

cx_Oracle.init_oracle_client(lib_dir = r"")

connection = cx_Oracle.connect("")


cursor = connection.cursor()
cursor.execute(""" select query as Himmelsereignisse, COUNT (DISTINCT QUERYTIME) AS Anzahl
from AOLDATA.QUERYDATA where QUERY like '%meteorites%' or QUERY like '%lunar 
eclipse%' or QUERY like '%shooting stars%'
Group by query order by Anzahl desc """)


x = []
y = []
i = 1


for row in cursor:
    x.append(row[0])
    y.append(int(row[1]))
    i+=1
    if i == 10 : break


labels = ['March']


r = np.arange(len(labels))
width = 0.22
fig, ax = plt.subplots(figsize=(8, 5))



plt.bar(x, y, color = 'red')
plt.xlabel("Query")
plt.ylabel("Anzahl")
plt.xticks(rotation=10)
plt.suptitle('Wie oft wurde nach Himmelsereignissen (Finsternis, Meteoriten, Sternschnuppen etc.) gesucht?')

plt.show()




print(x)
print(y)

ax.set_xticks(r)
ax.set_xticklabels(labels)
ax.legend()

