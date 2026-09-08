import pandas as pd 
import datetime as dt
import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

X = int(input('Enter patient id : '))
Y = int(input('Enter patient age : '))
Z = input('Enter disease state : ')
D = int(input('Enter cancer stage : '))
E = float(input('Enter baseline measurement : '))

patient_data = {'id': X, 'age': Y, 'disease_state': Z, 'cancer_stage': D, 'baseline_measurement': E}
patient_collection = [
    {'id': 101, 'age': 41, 'disease_state': 'breast cancer', 'cancer_stage': '1', 'baseline_measurement': 1.25},
    {'id': 102, 'age': 55, 'disease_state': 'breast cancer', 'cancer_stage': '2', 'baseline_measurement': 1.8},
    {'id': 103, 'age': 63, 'disease_state': 'lung cancer', 'cancer_stage': '3', 'baseline_measurement': 2.1},
    {'id': 104, 'age': 38, 'disease_state': 'melanoma', 'cancer_stage': '4', 'baseline_measurement': 0.95},
    {'id': 105, 'age': 71, 'disease_state': 'breast cancer', 'cancer_stage': '2', 'baseline_measurement': 3.4},
    {'id': 106, 'age': 45, 'disease_state': 'breast cancer', 'cancer_stage': '1', 'baseline_measurement': 1.12},
    {'id': 107, 'age': 52, 'disease_state': 'breast cancer', 'cancer_stage': '3', 'baseline_measurement': 1.65},
    {'id': 108, 'age': 68, 'disease_state': 'lung cancer', 'cancer_stage': '2', 'baseline_measurement': 2.4},
    {'id': 109, 'age': 35, 'disease_state': 'melanoma', 'cancer_stage': '1', 'baseline_measurement': 0.85},
    {'id': 110, 'age': 72, 'disease_state': 'breast cancer', 'cancer_stage': '4', 'baseline_measurement': 4.1},
    {'id': 111, 'age': 40, 'disease_state': 'breast cancer', 'cancer_stage': '2', 'baseline_measurement': 1.35},
    {'id': 112, 'age': 58, 'disease_state': 'breast cancer', 'cancer_stage': '1', 'baseline_measurement': 1.95},
    {'id': 113, 'age': 61, 'disease_state': 'lung cancer', 'cancer_stage': '4', 'baseline_measurement': 2.25},
    {'id': 114, 'age': 39, 'disease_state': 'melanoma', 'cancer_stage': '3', 'baseline_measurement': 0.75},
    {'id': 115, 'age': 74, 'disease_state': 'breast cancer', 'cancer_stage': '3', 'baseline_measurement': 3.8},
    {'id': 116, 'age': 42, 'disease_state': 'breast cancer', 'cancer_stage': '1', 'baseline_measurement': 1.45},
    {'id': 117, 'age': 56, 'disease_state': 'breast cancer', 'cancer_stage': '2', 'baseline_measurement': 1.7},
    {'id': 118, 'age': 64, 'disease_state': 'lung cancer', 'cancer_stage': '3', 'baseline_measurement': 2.15},
    {'id': 119, 'age': 37, 'disease_state': 'melanoma', 'cancer_stage': '2', 'baseline_measurement': 0.9},
    {'id': 120, 'age': 70, 'disease_state': 'breast cancer', 'cancer_stage': '4', 'baseline_measurement': 3.15},
    {'id': 121, 'age': 43, 'disease_state': 'breast cancer', 'cancer_stage': '2', 'baseline_measurement': 1.55},
    {"id": 122, "age": 48, "disease_state": "breast cancer", "cancer_stage": "1", "baseline_measurement": 1.1},
    {"id": 123, "age": 59, "disease_state": "breast cancer", "cancer_stage": "3", "baseline_measurement": 1.9},
    {"id": 124, "age": 66, "disease_state": "lung cancer", "cancer_stage": "2", "baseline_measurement": 2.6},
    {"id": 125, "age": 31, "disease_state": "melanoma", "cancer_stage": "1", "baseline_measurement": 0.65},
    {"id": 126, "age": 75, "disease_state": "breast cancer", "cancer_stage": "4", "baseline_measurement": 4.5},
    {"id": 127, "age": 46, "disease_state": "breast cancer", "cancer_stage": "2", "baseline_measurement": 1.2},
    {"id": 128, "age": 51, "disease_state": "breast cancer", "cancer_stage": "1", "baseline_measurement": 1.75},
    {"id": 129, "age": 62, "disease_state": "lung cancer", "cancer_stage": "4", "baseline_measurement": 2.35},
    {"id": 130, "age": 34, "disease_state": "melanoma", "cancer_stage": "3", "baseline_measurement": 0.8},
    {"id": 131, "age": 73, "disease_state": "breast cancer", "cancer_stage": "3", "baseline_measurement": 3.6},
    {"id": 132, "age": 44, "disease_state": "breast cancer", "cancer_stage": "1", "baseline_measurement": 1.3},
    {"id": 133, "age": 57, "disease_state": "breast cancer", "cancer_stage": "2", "baseline_measurement": 1.85},
    {"id": 134, "age": 65, "disease_state": "lung cancer", "cancer_stage": "3", "baseline_measurement": 2.2},
    {"id": 135, "age": 36, "disease_state": "melanoma", "cancer_stage": "2", "baseline_measurement": 0.7},
    {"id": 136, "age": 69, "disease_state": "breast cancer", "cancer_stage": "4", "baseline_measurement": 3.25},
    {"id": 137, "age": 47, "disease_state": "breast cancer", "cancer_stage": "2", "baseline_measurement": 1.6},
    {"id": 138, "age": 53, "disease_state": "breast cancer", "cancer_stage": "1", "baseline_measurement": 1.4},
    {"id": 139, "age": 67, "disease_state": "lung cancer", "cancer_stage": "3", "baseline_measurement": 2.55},
    {"id": 140, "age": 33, "disease_state": "melanoma", "cancer_stage": "1", "baseline_measurement": 0.6},
    {"id": 141, "age": 70, "disease_state": "breast cancer", "cancer_stage": "3", "baseline_measurement": 3.9},
    {"id": 142, "age": 49, "disease_state": "breast cancer", "cancer_stage": "2", "baseline_measurement": 1.5},
    {"id": 143, "age": 54, "disease_state": "breast cancer", "cancer_stage": "1", "baseline_measurement": 2.0},
    {"id": 144, "age": 60, "disease_state": "lung cancer", "cancer_stage": "4", "baseline_measurement": 2.7},
    {"id": 145, "age": 32, "disease_state": "melanoma", "cancer_stage": "2", "baseline_measurement": 0.5},
    {"id": 146, "age": 72, "disease_state": "breast cancer", "cancer_stage": "4", "baseline_measurement": 4.2},
    {"id": 147, "age": 50, "disease_state": "breast cancer", "cancer_stage": "2", "baseline_measurement": 1.38},
    {"id": 148, "age": 41, "disease_state": "breast cancer", "cancer_stage": "1", "baseline_measurement": 1.25},
    {"id": 149, "age": 55, "disease_state": "breast cancer", "cancer_stage": "2", "baseline_measurement": 1.8},
    {"id": 150, "age": 63, "disease_state": "lung cancer", "cancer_stage": "3", "baseline_measurement": 2.1},
    {"id": 151, "age": 38, "disease_state": "melanoma", "cancer_stage": "4", "baseline_measurement": 0.95},
    {"id": 152, "age": 71, "disease_state": "breast cancer", "cancer_stage": "2", "baseline_measurement": 3.4},
    {"id": 153, "age": 45, "disease_state": "breast cancer", "cancer_stage": "1", "baseline_measurement": 1.12},
    {"id": 154, "age": 52, "disease_state": "breast cancer", "cancer_stage": "3", "baseline_measurement": 1.65},
    {"id": 155, "age": 68, "disease_state": "lung cancer", "cancer_stage": "2", "baseline_measurement": 2.4},
    {"id": 156, "age": 35, "disease_state": "melanoma", "cancer_stage": "1", "baseline_measurement": 0.85},
    {"id": 157, "age": 72, "disease_state": "breast cancer", "cancer_stage": "4", "baseline_measurement": 4.1},
    {"id": 158, "age": 40, "disease_state": "breast cancer", "cancer_stage": "2", "baseline_measurement": 1.35},
    {"id": 159, "age": 58, "disease_state": "breast cancer", "cancer_stage": "1", "baseline_measurement": 1.95},
    {"id": 160, "age": 61, "disease_state": "lung cancer", "cancer_stage": "4", "baseline_measurement": 2.25},
    {"id": 161, "age": 39, "disease_state": "melanoma", "cancer_stage": "3", "baseline_measurement": 0.75},
    {"id": 162, "age": 74, "disease_state": "breast cancer", "cancer_stage": "3", "baseline_measurement": 3.8},
    {"id": 163, "age": 42, "disease_state": "breast cancer", "cancer_stage": "1", "baseline_measurement": 1.45},
    {"id": 164, "age": 56, "disease_state": "breast cancer", "cancer_stage": "2", "baseline_measurement": 1.7},
    {"id": 165, "age": 64, "disease_state": "lung cancer", "cancer_stage": "3", "baseline_measurement": 2.15},
    {"id": 166, "age": 37, "disease_state": "melanoma", "cancer_stage": "2", "baseline_measurement": 0.9},
    {"id": 167, "age": 70, "disease_state": "breast cancer", "cancer_stage": "4", "baseline_measurement": 3.15},
    {"id": 168, "age": 43, "disease_state": "breast cancer", "cancer_stage": "2", "baseline_measurement": 1.55},
    {"id": 169, "age": 48, "disease_state": "breast cancer", "cancer_stage": "1", "baseline_measurement": 1.1},
    {"id": 170, "age": 59, "disease_state": "breast cancer", "cancer_stage": "3", "baseline_measurement": 1.9},
    {"id": 171, "age": 66, "disease_state": "lung cancer", "cancer_stage": "2", "baseline_measurement": 2.6},
    {"id": 172, "age": 31, "disease_state": "melanoma", "cancer_stage": "1", "baseline_measurement": 0.65},
    {"id": 173, "age": 75, "disease_state": "breast cancer", "cancer_stage": "4", "baseline_measurement": 4.5},
    {"id": 174, "age": 46, "disease_state": "breast cancer", "cancer_stage": "2", "baseline_measurement": 1.2},
    {"id": 175, "age": 51, "disease_state": "breast cancer", "cancer_stage": "1", "baseline_measurement": 1.75},
    {"id": 176, "age": 62, "disease_state": "lung cancer", "cancer_stage": "4", "baseline_measurement": 2.35},
    {"id": 177, "age": 34, "disease_state": "melanoma", "cancer_stage": "3", "baseline_measurement": 0.8},
    {"id": 178, "age": 73, "disease_state": "breast cancer", "cancer_stage": "3", "baseline_measurement": 3.6},
    {"id": 179, "age": 44, "disease_state": "breast cancer", "cancer_stage": "1", "baseline_measurement": 1.3},
    {"id": 180, "age": 57, "disease_state": "breast cancer", "cancer_stage": "2", "baseline_measurement": 1.85},
    {"id": 181, "age": 65, "disease_state": "lung cancer", "cancer_stage": "3", "baseline_measurement": 2.2},
    {"id": 182, "age": 36, "disease_state": "melanoma", "cancer_stage": "2", "baseline_measurement": 0.7},
    {"id": 183, "age": 69, "disease_state": "breast cancer", "cancer_stage": "4", "baseline_measurement": 3.25},
    {"id": 184, "age": 47, "disease_state": "breast cancer", "cancer_stage": "2", "baseline_measurement": 1.6},
    {"id": 185, "age": 53, "disease_state": "breast cancer", "cancer_stage": "1", "baseline_measurement": 1.4},
    {"id": 186, "age": 67, "disease_state": "lung cancer", "cancer_stage": "3", "baseline_measurement": 2.55},
    {"id": 187, "age": 33, "disease_state": "melanoma", "cancer_stage": "1", "baseline_measurement": 0.6},
    {"id": 188, "age": 70, "disease_state": "breast cancer", "cancer_stage": "3", "baseline_measurement": 3.9},
    {"id": 189, "age": 49, "disease_state": "breast cancer", "cancer_stage": "2", "baseline_measurement": 1.5},
]

patient_collection.append(patient_data)

df = pd.DataFrame(patient_collection)   
eligible_patients = df[(df['age'] >= 40) & (df['age'] <= 70) & (df['disease_state'] == 'breast cancer') & (df['cancer_stage'].isin(['1', '2'])) & (df['baseline_measurement'] < 50.0)]
print(eligible_patients)

if X in eligible_patients['id'].values:
    print(f"\n Patient {X} is ELIGIBLE for the trial.")
else:
    print(f"\n Patient {X} is NOT ELIGIBLE for the trial.")
    print(" Reason: Age, stage, disease, or baseline does not match criteria.")



mydb = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)
cursor = mydb.cursor()

insert_query = "INSERT INTO patient_data (patient_id, age, disease_state, cancer_stage, baseline_measurement) VALUES (%s, %s, %s, %s, %s)"
data_tuples = [(p['id'], p['age'], p['disease_state'], p['cancer_stage'], p['baseline_measurement']) for p in eligible_patients.to_dict('records')]

cursor.executemany(insert_query, data_tuples)

mydb.commit()

print("Data inserted successfully into mysql vault")