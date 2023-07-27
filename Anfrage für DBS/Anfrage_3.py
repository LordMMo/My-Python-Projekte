# Anfrage 3
# -------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import cx_Oracle
import numpy as np
#import pandas as pd

cx_Oracle.init_oracle_client(lib_dir = r"")

connection = cx_Oracle.connect("")


cursor = connection.cursor()
cursor.execute(""" 
        select zeit, sum(Anzahl) from uhr
        where query like '%space%mission%'
        group by zeit
        order by zeit asc """)


ANZ = []
ZEIT_SQL = []

for row in cursor:
    ANZ.append(row[1])
    ZEIT_SQL.append(row[0])

UHRZEIT = ['00', '01', '04', '16', '19', '21', '22', '23']

ANZ_ZEIT = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(ANZ)):
    if (int(ZEIT_SQL[i]) == 0):
        ANZ_ZEIT[0] += ANZ[i]
    elif (int(ZEIT_SQL[i]) == 1):
        ANZ_ZEIT[1] += ANZ[i]
    elif (int(ZEIT_SQL[i]) == 4):
        ANZ_ZEIT[2] += ANZ[i]
    elif (int(ZEIT_SQL[i]) == 16):
        ANZ_ZEIT[3] += ANZ[i]
    elif (int(ZEIT_SQL[i]) == 19):
        ANZ_ZEIT[4] += ANZ[i]
    elif (int(ZEIT_SQL[i]) == 21):
        ANZ_ZEIT[5] += ANZ[i]
    elif (int(ZEIT_SQL[i]) == 22):
        ANZ_ZEIT[6] += ANZ[i]
    elif (int(ZEIT_SQL[i]) == 23):
        ANZ_ZEIT[7] += ANZ[i]

# matplotlib style
plt.style.use('classic')
colors = ['red', 'green']

# plot
plt.plot(UHRZEIT, ANZ_ZEIT, color='lime')
plt.scatter(UHRZEIT, ANZ_ZEIT, color='red')

# Titel des Diagramms
plt.title("Zu welcher Uhrzeit wurden die meisten Anfragen zu 'space missions' gestellt?")

plt.ylabel("Anzahl")
plt.xlabel("Uhrzeit")

plt.legend(labels=['Anzahl der Suchergebnisse'])

plt.show()
