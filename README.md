# bio_code
# Bioinformatics Portfolio — 9 Projects in 7 Days

This repository contains 8 working bioinformatics projects built using Python, Pandas, and MySQL.

## Projects
1. GC Content Analyzer — DNA sequence analysis
2. RNA→Protein Translator — Universal genetic code translator
3. Clinical Trial Cohort Filter — Patient filtering for trials
4. PCR Primer Tm Calculator — Salt-corrected melting temperature
5. Genetic Cross Simulator — Mendelian inheritance (F2)
6. Bacteria Growth Simulation — Population dynamics
7. Biomarker Outlier Detector — Anomaly detection in biological data
8. Univariate Data Summary — Statistical summaries
9. Evolution Engine - Bacterial resistance simulation with plasmid conjugation and penicillin selection

## 1. GC Content Analyzer

**What it does:** Calculates GC content across a DNA sequence using a sliding window.

**How to use:**
```bash
python GC_analyzer.py
```

· Enter a DNA sequence (e.g., ATCGATCGATCG)
· Enter a window size (e.g., 5)
· The tool outputs GC% for each window.

Tech: Python, Pandas, MySQL

---

2. RNA→Protein Translator

What it does: Translates an RNA sequence into a protein using the 64-codon table.

How to use:

```bash
python RNA_to_Protein_translation_engine.py
```

· Enter an RNA sequence (e.g., AUGGCUUAA)
· The tool scans for AUG (start), translates to a peptide, and stops at UAA, UAG, or UGA.
· Results are logged to MySQL.

Tech: Python, Pandas, MySQL

---

3. Clinical Trial Cohort Filter

What it does: Filters eligible patients for clinical trials based on age, disease, stage, and biomarkers.

How to use:

```bash
python Clinical_trial_cohort_filter.py
```

· Enter patient data (age, disease, stage, biomarker values).
· The tool returns matching patients.

Tech: Python, Pandas, MySQL

---

4. PCR Primer Tm Calculator

What it does: Calculates the melting temperature of a PCR primer using the SantaLucia formula with salt correction.

How to use:

```bash
python The_PCR_primer_Tm_calculator.py
```

· Enter a primer sequence (e.g., ATCGATCGATCG)
· Enter salt concentration (e.g., 0.05)
· The tool outputs the Tm in °C.

Tech: Python, Math

---

5. Genetic Cross Simulator

What it does: Simulates Mendelian inheritance for F1 and F2 generations (dihybrid cross).

How to use:

```bash
python Dihybrid_Popgene_Simulator.py
```

· Enter parent genotypes (e.g., AaBb and AaBb)
· The tool outputs genotype and phenotype ratios for F1 and F2.

Tech: Python, Pandas, MySQL

---

6. Bacteria Growth Simulation

What it does: Simulates 24-hour bacterial population growth under nutrient and temperature conditions.

How to use:

```bash
python The_Bacterial_Growth_&_Nutrient_Decay_Tracker.py
```

· Enter initial population (e.g., 10000)
· Enter nutrient level (e.g., 10)
· Enter temperature (e.g., 37)
· The tool outputs a 24-hour population curve.

Tech: Python, Pandas, Matplotlib

---

7. Biomarker Outlier Detector

What it does: Detects unhealthy patients based on glucose levels (below 70 or above 180).

How to use:

```bash
python biomaker_outliner.py
```

· Enter glucose values (e.g., 95 110 60 200)
· The tool flags values outside the normal range.

Tech: Python, Pandas, NumPy, MySQL

---

8. Univariate Data Summary

What it does: Calculates mean, median, mode, min, max, range, variance, and standard deviation for any numerical dataset.

How to use:

```bash
python univariate_data_summary.py
```

· Enter numbers separated by space (e.g., 50 60 80 70 100 120)
· The tool outputs all statistical measures and logs to MySQL.

Tech: Python, NumPy, MySQL

---

9. Evolution Engine

What it does: Simulates bacterial evolution and antibiotic resistance spread under penicillin selection pressure.

How to use:

```bash
python Evolution_Engine.py
```

· Enter bacteria name (e.g., E. coli)
· Enter initial population (e.g., 10000)
· Enter % resistant bacteria (e.g., 20)
· Enter conjugation rate (e.g., 0.02)
· Enter penicillin concentration (e.g., 3)
· Enter simulation hours (e.g., 72)
· Enter temperature (e.g., 37)
· Enter nutrient level (e.g., 10)
· The tool outputs growth curves, resistance spread, and logs to MySQL.

Tech: Python, Pandas, NumPy, Matplotlib, MySQL

---


---

How to Run Any Project

1. Clone the repository:
   ```bash
   git clone https://github.com/CodeXSourabhsingh/bio_code.git
   cd bio_code
   ```
2. Create a config.py file with your MySQL credentials:
   ```python
   MYSQL_HOST = "localhost"
   MYSQL_USER = "your_user"
   MYSQL_PASSWORD = "your_password"
   MYSQL_DATABASE = "bio_simulations"
   ```
3. Install the required libraries:
   ```bash
   pip install pandas numpy matplotlib mysql-connector-python
   ```
4. Run any project:
   ```bash
   python <project_name>.py
   ```

---

Design Philosophy

Every tool in this repository is built with three principles:

· Universal: Works with any organism, any dataset, any domain.
· Simple: Readable code beats clever code.
· Productive: Built to solve a real problem, not to impress.

---


## Tech Stack
- Python
- Pandas
- MySQL
- Matplotlib
- Git / GitHub

## Author
Sourabh Singh — [LinkedIn](https://www.linkedin.com/in/sourabh-singh-7b1249434/) | 
