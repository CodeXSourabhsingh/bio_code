import numpy as np
import mysql.connector 
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE


data = list(map(float, input("Enter glucose values separated by space: ").split()))

n = len(data)
mean_val = np.mean(data)
median_val = np.median(data)

freq = {}
for x in data:
    freq[x] = freq.get(x, 0) + 1
mode_val = max(freq, key=freq.get)

min_val = np.min(data)
max_val = np.max(data)
range_val = max_val - min_val
variance_val = np.var(data)
std_val = np.std(data)

print("Univariate Data Summary")
print(f" Mean: {mean_val:.2f}")
print(f" Median: {median_val:.2f}")
print(f" Mode: {mode_val:.2f}")
print(f" Min: {min_val:.2f}")
print(f" Max: {max_val:.2f}")
print(f" Range: {range_val:.2f}")
print(f" Variance: {variance_val:.2f}")
print(f" Standard Deviation: {std_val:.2f}")

if n == 1 :
    print("NOTE : only one date point enterd . variance and std dev are zero by defination. ")


mydb = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)
cursor = mydb.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS univariate_summary (
        id INT AUTO_INCREMENT PRIMARY KEY,
        num_values INT,
        mean_val FLOAT,
        median_val FLOAT,
        mode_val FLOAT,
        min_val FLOAT,
        max_val FLOAT,
        range_val FLOAT,
        variance_val FLOAT,
        std_val FLOAT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

insert_query = """
    INSERT INTO univariate_summary (num_values, mean_val, median_val, mode_val, min_val, max_val, range_val, variance_val, std_val)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
values = (n, mean_val, median_val, mode_val, min_val, max_val, range_val, variance_val, std_val)

  
cursor.execute(insert_query, values)

mydb.commit()

mydb.close()
