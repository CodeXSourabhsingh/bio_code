import random
import pandas as pd
import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

while True:
    try:
         pop_size = int(input('enter F2 population size: '))
         if pop_size>0:
              break
    except:
         print('invalid input!')

F2_population = []
for i in range (pop_size):
    off_spring = [
                   random.choice(['R','r']),
                   random.choice(['R','r']),
                   random.choice(['Y','y']),
                   random.choice(['Y','y'])          
     ]
    F2_population.append(off_spring)

df = pd.DataFrame(F2_population,columns = ['shape1','shape2','colour1','colour2'])

def classify_phenotype(row):
     if row['shape1'] == 'R' or row['shape2'] == 'R' :
          shape = 'round'
     else:
          shape = 'wrinkled'
     if row['colour1'] == 'Y' or row['colour2'] == 'Y':
          colour = 'yellow'
     else:
          colour = 'green'
     return f"{shape} {colour}" 

df['phenotype'] = df.apply(classify_phenotype,axis=1)
print(df['phenotype'].value_counts())


mydb = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)
cursor = mydb.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS dihybrid_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    total_population INT,
    round_yellow INT,
    round_green INT,
    wrinkled_yellow INT,
    wrinkled_green INT)
    """)
counts = df['phenotype'].value_counts()
ry = int(counts.get('Round Yellow',0))
rg = int(counts.get('Round Green',0))
wy = int(counts.get('Wrinkled Yellow',0))
wg = int(counts.get('Wrinkled Green',0))

sql = """
INSERT INTO dihybrid_history(total_population,round_yellow,round_green,wrinkled_yellow,wrinkled_green)
VALUES(%s,%s,%s,%s,%s)
"""
cursor.execute(sql, (pop_size,ry,rg,wy,wg))
mydb.commit()

cursor.close()
mydb.close()

print('data succesfully logged into mysql')

