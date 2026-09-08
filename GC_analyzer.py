import random
from mysql.connector import connection
import pandas as pd
import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

X = input("Enter organism name : ")
Y = input("Enter DNA sequence:  " ).upper()
z = int(input("Enter window size : "))

Bases = ['A','T','G','C']
random_sequences = random.choices(Bases, k = 100000)

df = pd.DataFrame({'nucleotide':list(Y)})
Bases_counts = df['nucleotide'].value_counts()

window_result = []

for i in range(0, len(df) - z + 1):
    window_chunk = df.iloc[i:i+z]
    filtered_gc = window_chunk.loc[window_chunk['nucleotide'].isin(['G', 'C'])]
    true_gc_percentage = len(filtered_gc) / z * 100

    window_result.append({
        'window_start': i,
        'gc_percentage': true_gc_percentage
    })

result_df = pd.DataFrame(window_result)
print(result_df.head())


mydb = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)

cursor = mydb.cursor()

insert_query = "INSERT INTO sequence_window (window_start, gc_percentage) VALUES (%s, %s);"

data_tuples = [(row['window_start'], row['gc_percentage']) for _, row in result_df.iterrows()]

cursor.executemany(insert_query, data_tuples)

mydb.commit()

cursor.close()





