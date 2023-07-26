# Anfrage 1
# -------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import cx_Oracle
import numpy as np
#import pandas as pd


cx_Oracle.init_oracle_client(lib_dir = r"C:\Users\User\Desktop\instantclient_19_11")

connection = cx_Oracle.connect("S906463","1", "localhost/rispdb1")


cursor = connection.cursor()
cursor.execute("""
        SELECT query, count(distinct querytime) as Anzahl FROM AOLDATA.QUERYDATA WHERE QUERY in (select Weltraumorganisation.name from Weltraumorganisation where Weltraumorganisation.name = querydata.query)
        group by query order by Anzahl desc """)

x = []
y = []


for row in cursor:
    x.append(row[0])
    y.append(int(row[1]))


labels = ['March']


r = np.arange(len(labels))
width = 0.1
fig, ax = plt.subplots(figsize=(8, 5))



plt.bar(x, y,color='red')
plt.xlabel("Weltraumorganisation")
plt.ylabel("Anzahl")
plt.xticks(rotation=10)
plt.suptitle('Welche Weltraumorganisation wurde am meisten gesucht?')

plt.show()




print(x)
print(y)

ax.set_xticks(r)
ax.set_xticklabels(labels)
ax.legend()

