# bio_code

## Bioinformatics Portfolio — 9 Projects in 6 Days

This repository contains 9 working bioinformatics projects built using Python, Pandas, and MySQL. Each tool is production-ready, well-documented, and designed to solve real-world biological and clinical problems.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- MySQL Server (running locally or remote)
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/CodeXSourabhsingh/bio_code.git
   cd bio_code
   ```

2. **Install dependencies:**
   ```bash
   pip install pandas numpy matplotlib mysql-connector-python
   ```
   
   Or use `requirements.txt` if available:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure MySQL credentials:**
   Create a `config.py` file in the root directory:
   ```python
   MYSQL_HOST = "localhost"
   MYSQL_USER = "your_user"
   MYSQL_PASSWORD = "your_password"
   MYSQL_DATABASE = "bio_simulations"
   ```
   
   ⚠️ **Important:** Add `config.py` to `.gitignore` to avoid committing credentials.

4. **Run any project:**
   ```bash
   python <project_name>.py
   ```

---

## 📋 Table of Contents

- [Key Features](#key-features)
- [Projects Overview](#projects-overview)
- [Project Details](#project-details)
- [Tech Stack](#tech-stack)
- [Design Philosophy](#design-philosophy)
- [Author](#author)

---

## ✨ Key Features

- ✅ **9 production-ready bioinformatics tools**
- ✅ Complete end-to-end workflows (input → analysis → database logging)
- ✅ Interactive CLI interfaces
- ✅ MySQL integration for persistent result storage
- ✅ Visualization support (Matplotlib charts & graphs)
- ✅ Modular, readable code designed for clarity over cleverness
- ✅ Real-world problem solving in genetics, clinical trials, and microbiology

---

## 📚 Projects Overview

| # | Project | Purpose | Tech Stack |
|---|---------|---------|-----------|
| 1 | GC Content Analyzer | DNA sequence analysis | Python, Pandas, MySQL |
| 2 | RNA→Protein Translator | Universal genetic code translator | Python, Pandas, MySQL |
| 3 | Clinical Trial Cohort Filter | Patient filtering for trials | Python, Pandas, MySQL |
| 4 | PCR Primer Tm Calculator | Salt-corrected melting temperature | Python, Math |
| 5 | Genetic Cross Simulator | Mendelian inheritance (F2) | Python, Pandas, MySQL |
| 6 | Bacteria Growth Simulation | Population dynamics | Python, Pandas, Matplotlib |
| 7 | Biomarker Outlier Detector | Anomaly detection in biological data | Python, Pandas, NumPy, MySQL |
| 8 | Univariate Data Summary | Statistical summaries | Python, NumPy, MySQL |
| 9 | Evolution Engine | Bacterial resistance & plasmid conjugation | Python, Pandas, NumPy, Matplotlib, MySQL |

---

## 🔬 Project Details

### 1. GC Content Analyzer

**What it does:** Calculates GC content across a DNA sequence using a sliding window approach.

**How to use:**
```bash
python GC_analyzer.py
```

**Workflow:**
- Enter a DNA sequence (e.g., `ATCGATCGATCG`)
- Enter a window size (e.g., `5`)
- Tool outputs GC% for each window position

**Tech:** Python, Pandas, MySQL

---

### 2. RNA→Protein Translator

**What it does:** Translates an RNA sequence into a protein using the 64-codon universal genetic code table.

**How to use:**
```bash
python RNA_to_Protein_translation_engine.py
```

**Workflow:**
- Enter an RNA sequence (e.g., `AUGGCUUAA`)
- Tool scans for AUG (start codon)
- Translates to peptide sequence
- Stops at UAA, UAG, or UGA (stop codons)
- Results logged to MySQL

**Tech:** Python, Pandas, MySQL

---

### 3. Clinical Trial Cohort Filter

**What it does:** Filters eligible patients for clinical trials based on multiple criteria: age, disease, stage, and biomarker values.

**How to use:**
```bash
python Clinical_trial_cohort_filter.py
```

**Workflow:**
- Enter patient demographics and biomarker data
- Tool applies inclusion/exclusion criteria
- Returns matching eligible patients

**Tech:** Python, Pandas, MySQL

---

### 4. PCR Primer Tm Calculator

**What it does:** Calculates the melting temperature of a PCR primer using the SantaLucia formula with salt correction.

**How to use:**
```bash
python The_PCR_primer_Tm_calculator.py
```

**Workflow:**
- Enter primer sequence (e.g., `ATCGATCGATCG`)
- Enter salt concentration (e.g., `0.05` M)
- Tool outputs Tm in °C

**Tech:** Python, Math

---

### 5. Genetic Cross Simulator

**What it does:** Simulates Mendelian inheritance patterns for F1 and F2 generations using dihybrid crosses.

**How to use:**
```bash
python Dihybrid_Popgene_Simulator.py
```

**Workflow:**
- Enter parent genotypes (e.g., `AaBb` × `AaBb`)
- Tool generates F1 and F2 populations
- Outputs genotype and phenotype ratios with analysis

**Tech:** Python, Pandas, MySQL

---

### 6. Bacteria Growth Simulation

**What it does:** Simulates 24-hour bacterial population growth under varying nutrient and temperature conditions.

**How to use:**
```bash
python The_Bacterial_Growth_&_Nutrient_Decay_Tracker.py
```

**Workflow:**
- Enter initial population (e.g., `10000`)
- Enter nutrient level (e.g., `10`)
- Enter temperature (e.g., `37°C`)
- Tool outputs 24-hour population growth curve

**Tech:** Python, Pandas, Matplotlib

---

### 7. Biomarker Outlier Detector

**What it does:** Detects unhealthy patients by flagging glucose levels outside the normal range (< 70 or > 180 mg/dL).

**How to use:**
```bash
python biomaker_outliner.py
```

**Workflow:**
- Enter glucose values (e.g., `95 110 60 200`)
- Tool identifies abnormal values
- Flags patients requiring intervention

**Tech:** Python, Pandas, NumPy, MySQL

---

### 8. Univariate Data Summary

**What it does:** Calculates comprehensive statistical summaries: mean, median, mode, min, max, range, variance, and standard deviation.

**How to use:**
```bash
python univariate_data_summary.py
```

**Workflow:**
- Enter numbers separated by space (e.g., `50 60 80 70 100 120`)
- Tool computes all statistical measures
- Results logged to MySQL for analysis

**Tech:** Python, NumPy, MySQL

---

### 9. Evolution Engine

**What it does:** Simulates bacterial evolution and antibiotic resistance spread under penicillin selection pressure, including plasmid conjugation dynamics.

**How to use:**
```bash
python Evolution_Engine.py
```

**Workflow:**
- Enter bacteria name (e.g., `E. coli`)
- Enter initial population (e.g., `10000`)
- Enter % resistant bacteria (e.g., `20%`)
- Enter conjugation rate (e.g., `0.02`)
- Enter penicillin concentration (e.g., `3` units)
- Enter simulation hours (e.g., `72`)
- Enter temperature (e.g., `37°C`)
- Enter nutrient level (e.g., `10`)
- Tool outputs growth curves, resistance spread graphs, and logs to MySQL

**Tech:** Python, Pandas, NumPy, Matplotlib, MySQL

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Data Processing:** Pandas, NumPy
- **Database:** MySQL
- **Visualization:** Matplotlib
- **Version Control:** Git / GitHub

---

## 💡 Design Philosophy

Every tool in this repository is built with three core principles:

1. **Universal:** Works with any organism, any dataset, any domain.
2. **Simple:** Readable code beats clever code.
3. **Productive:** Built to solve a real problem, not to impress.

---

## 👤 Author

**Sourabh Singh**

- [LinkedIn](https://www.linkedin.com/in/sourabh-singh-7b1249434/)
- [GitHub](https://github.com/CodeXSourabhsingh)

---

## 📄 License

[Add your license here - MIT, Apache 2.0, etc.]

---

## 💬 Contributing

Contributions are welcome! Feel free to submit issues and pull requests to improve these tools.

