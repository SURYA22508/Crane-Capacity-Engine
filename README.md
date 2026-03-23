# Crane-Capacity-Engine
# 🏗️ Advanced Crane Load Configuration Analyzer

---

## 🚀 Overview

Working with crane load charts can be challenging. They involve multiple configurations, complex parameters, and a lot of manual effort to interpret correctly.

This project simplifies that process by building an interactive application that helps users quickly find the **safe lifting capacity** based on real crane data.

Using **Python, Pandas, and Streamlit**, the system converts traditional load charts into an easy-to-use digital tool.

---

## 🎯 Problem Statement

In real-world crane operations:

* Reading load charts manually is difficult
* Small mistakes can lead to unsafe lifting decisions
* Finding the right configuration takes time

👉 This project solves these issues by providing **quick and accurate results based on user input**.

---

## ✨ Key Features

* 🏗️ Supports multiple crane configurations
* 📊 Handles large datasets (1000+ configurations)
* 🔍 Filters data dynamically based on user inputs
* 📄 Automatically connects configurations to load chart pages
* ⚡ Provides instant lifting capacity results
* 🎛️ Clean and interactive UI using Streamlit

---
UI
<img width="1909" height="996" alt="Screenshot 2026-03-23 203541" src="https://github.com/user-attachments/assets/c5d593cf-cf8f-442f-9dd8-58e5917ad369" />


## 🧠 How It Works

### 🔹 Step 1: Data Preparation

Multiple datasets (`upto1000.csv`, `upto2000.csv`, `upto2201.csv`) are combined into a single dataset for analysis.

### 🔹 Step 2: User Input

The user selects parameters like:

* Boom Length
* Boom Angle
* Jib Length
* Counterweight
* Superlift Radius

The system filters matching configurations in real time.

### 🔹 Step 3: Page Mapping

Each configuration is linked to a specific load chart page using stored data.

### 🔹 Step 4: Capacity Calculation

* Preprocessed dictionaries (`dic.pkl`) store load chart tables
* The user selects:

  * Capacity column
  * Radius

👉 The system returns the **exact lifting capacity in tonnes**

---

## 🖥️ Application Workflow

1. Select crane parameters
2. System filters valid configurations
3. Choose:

   * Capacity column
   * Radius
4. Get:

   * ✅ Lifting capacity
   * 📄 Corresponding chart reference

---

## ⚙️ Tech Stack

* Python
* Streamlit
* Pandas
* NumPy
* Pickle
* pdfplumber

---

## ▶️ Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/advanced-crane-analyzer.git
cd advanced-crane-analyzer
pip install -r requirements.txt
streamlit run app.py
```

---

## 💡 Real-World Use Cases

* Construction planning
* Crane operation safety
* Load verification
* Engineering learning and analysis

---

## 🚀 Future Improvements

* Add visual graphs for better understanding
* Deploy as a web application
* Add overload warnings
* Build smart recommendation system

---

## 👨‍💻 Author

**Surya Vardhan**

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

---

## 📌 Final Note

This project shows how combining **engineering knowledge with data and software** can make complex tasks simpler and more reliable.
