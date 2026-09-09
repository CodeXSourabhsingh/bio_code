import pandas as pd
import numpy as np
import mysql.connector
from config import MYSQL_HOST,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DATABASE

X = int(input('Enter patient id : '))
Y = int(input('Enter Glucose count : '))

data = {
    'Patient_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Glucose': [
        
        85, 90, 95, 100, 105, 110, 115, 120, 125, 130,
        180, 190, 200, 210, 220, 230, 240, 250, 260, 270,
        30, 35, 40, 45, 50, 55, 60, 65, 70, 75
    ]
}

df = pd.DataFrame(data)

glucose_value = df['Glucose'].values
mean_val = np.mean(glucose_value)
std_val = np.std(glucose_value)

lower_bound = mean_val - 2* std_val
upper_bound = mean_val + 2* std_val

outliers = df[(df['Glucose'] <= 70 ) | (df['Glucose'] >= 180 )]

print("Glucose Statistics:")
print(f"Mean: {mean_val:.2f}")
print(f"Std Dev: {std_val:.2f}")
print(f"Normal Range: {lower_bound:.2f} - {upper_bound:.2f}")
print(f" Outliers Detected: {len(outliers)}")
print(outliers)

if Y < 70 :
    print(f" Patient {X} has LOW glucose ({Y}) — UNHEALTHY.")
elif Y > 180 :
    print(f"Patient {X} has HIGH glucose ({Y}) — UNHEALTHY.")
else:
    print(f" Patient {X} has NORMAL glucose ({Y}) — HEALTHY.")


mydb = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)
cursor = mydb.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS biomarker_outliers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        patient_id INT,
        glucose FLOAT,
        status VARCHAR(50),
        normal_range VARCHAR(50),
        detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

insert_query = """
    INSERT INTO biomarker_outliers (patient_id, glucose, status, normal_range)
    VALUES (%s, %s, %s, %s)
"""

outlier_tuples = [
    (patient_id, glucose, 'OUTLIER', f'{lower_bound:.2f} - {upper_bound:.2f}')
    for patient_id, glucose in outliers[['Patient_ID', 'Glucose']].itertuples(index=False, name=None)
]

cursor.executemany(insert_query, outlier_tuples)
mydb.commit()
cursor.close()
mydb.close()
   