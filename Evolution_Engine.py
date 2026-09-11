import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE


print(" Bacterial Evolution Simulator")

organism = input("Enter bacteria name : ")
initial_population = int(input("Enter initial population: "))
resistant_percent = float(input("Enter % of resistant bacteria : "))
conjugation_rate = float(input("Enter conjugation rate : "))
penicillin = float(input("Enter penicillin concentration : "))
hours = int(input("Enter simulation hours: "))
temperature = float(input("Enter temperature (°C): "))
nutrients = float(input("Enter nutrient level : "))

resistant_count = int(initial_population * (resistant_percent / 100))
normal_count = initial_population - resistant_count

resistant_growth_rate = 0.08
normal_growth_rate = 0.12


data = {
    'Hour': [],
    'Total_Population': [],
    'Resistant': [],
    'Normal': [],
    'Resistant_Percent': []
}

temp_factor = 0.0
if 5 <= temperature <= 50:
    temp_factor = max(0, 1 - ((temperature - 37) / 20) ** 2)  
kill_rate = min(0.9, penicillin * 0.15) if penicillin > 0 else 0.0

for hour in range(1, hours + 1):

    normal_count = int(normal_count * (1 + (normal_growth_rate * temp_factor)))
    normal_count = int(normal_count * (1 - kill_rate))

    resistant_count = int(resistant_count * (1 + (resistant_growth_rate * temp_factor)))

   
    if normal_count > 0 and resistant_count > 0:
        transferred = int(normal_count * conjugation_rate)
        if transferred > normal_count:
            transferred = normal_count
        normal_count = normal_count - transferred
        resistant_count = resistant_count + transferred
    total_population = normal_count + resistant_count
    if nutrients > 0 and total_population > 1000000:
        growth_cap = nutrients * 100000
        if total_population > growth_cap:
            excess = total_population - growth_cap
            if normal_count > 0:
                normal_count = max(0, normal_count - excess)
            else:
                resistant_count = max(0, resistant_count - excess)

    total_population = normal_count + resistant_count
    resistant_percent = (resistant_count / total_population) * 100 if total_population > 0 else 0
    data['Hour'].append(hour)
    data['Total_Population'].append(total_population)
    data['Resistant'].append(resistant_count)
    data['Normal'].append(normal_count)
    data['Resistant_Percent'].append(resistant_percent)

df = pd.DataFrame(data)
print("Simulation Complete!")
print(f"Total Population: {df['Total_Population'].iloc[-1]}")
print(f"Resistant: {df['Resistant'].iloc[-1]}")
print(f"Normal: {df['Normal'].iloc[-1]}")
print(f"Resistant %: {df['Resistant_Percent'].iloc[-1]:.2f}%")

plt.style.use("ggplot")
plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
plt.plot(df['Hour'], df['Total_Population'], label='Total', color='blue', linewidth=2)
plt.plot(df['Hour'], df['Resistant'], label='Resistant', color='green', linewidth=2)
plt.plot(df['Hour'], df['Normal'], label='Normal', color='red', linewidth=2)
plt.xlabel('Time (Hours)')
plt.ylabel('Population')
plt.title('Bacterial Growth Over Time')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
final_data = [df['Resistant'].iloc[-1], df['Normal'].iloc[-1]]
plt.bar(['Resistant', 'Normal'], final_data, color=['green', 'red'], edgecolor='black')
plt.xlabel('Bacteria Type')
plt.ylabel('Population')
plt.title('Final Population: Resistant vs Normal')

plt.subplot(2, 2, 3)
plt.scatter(df['Hour'], df['Resistant_Percent'], color='purple', s=50)
plt.xlabel('Time (Hours)')
plt.ylabel('Resistant %')
plt.title('Resistance Spread Over Time')
plt.grid(True)

plt.subplot(2, 2, 4)
plt.text(0.1, 0.8, f'Organism: {organism}', fontsize=12)
plt.text(0.1, 0.7, f'Initial Population: {initial_population}', fontsize=12)
plt.text(0.1, 0.6, f'Penicillin: {penicillin}', fontsize=12)
plt.text(0.1, 0.5, f'Final Total: {df["Total_Population"].iloc[-1]}', fontsize=12)
plt.text(0.1, 0.4, f'Final Resistant: {df["Resistant"].iloc[-1]}', fontsize=12)
plt.text(0.1, 0.3, f'Resistant %: {df["Resistant_Percent"].iloc[-1]:.2f}%', fontsize=12)
plt.axis('off')
plt.title('Simulation Summary')

plt.tight_layout()
plt.savefig('bacterial_evolution.png', dpi=300)
plt.show()

mydb = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)
cursor = mydb.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS bacterial_evolution (
        id INT AUTO_INCREMENT PRIMARY KEY,
        organism VARCHAR(100),
        initial_population INT,
        penicillin FLOAT,
        final_total INT,
        final_resistant INT,
        final_normal INT,
        resistant_percent FLOAT,
        logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")


final_total = int(df['Total_Population'].iloc[-1])
final_resistant = int(df['Resistant'].iloc[-1])
final_normal = int(df['Normal'].iloc[-1])
resistant_percent = float(df['Resistant_Percent'].iloc[-1])


insert_query = """
    INSERT INTO bacterial_evolution (
        organism, initial_population, penicillin,
        final_total, final_resistant, final_normal, resistant_percent
    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
values = (
    organism,
    initial_population,
    penicillin,
    final_total,
    final_resistant,
    final_normal,
    resistant_percent
)

print('values being iserted:', values)
print("data types:", [type(v) for v in values])

cursor.execute(insert_query, values)
mydb.commit()
mydb.close()

print(" Resistant bacteria survived and evolved.")
print(" Check your graphs and MySQL table.")
