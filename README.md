# 🍳 COOKMANIA – Intelligent Recipe Recommendation System
*A Machine Learning-Powered Mobile Application for Personalized Cooking Experiences*

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)
![Android](https://img.shields.io/badge/Android%20Studio-IDE-orange)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-TF--IDF%20%7C%20Cosine%20Similarity-yellow)

---

## 📌 **Abstract**
**Cookmania** is an **Android-based recipe recommendation system** powered by **Machine Learning**.  
The app allows users to enter **available ingredients** and instantly recommends **personalized recipes**.  
It leverages **TF-IDF vectorization**, **Cosine Similarity**, and **BallTree algorithms** to deliver accurate and efficient results.  

The goal is to:
- Minimize **food waste** 🥗
- Enhance **cooking efficiency** ⏳
- Improve **user experience** 📱

---

## **1. Introduction**
Cooking is a daily necessity but can be **time-consuming** when recipe decisions depend on missing ingredients.  
Most existing apps **don’t consider ingredient availability**, forcing users to search manually.  
**Cookmania** solves this problem by using **machine learning** to provide **real-time recipe recommendations**.

### **Key Highlights**
- 📱 Mobile app developed with **Android Studio**
- ⚡ Real-time ML-based **recipe recommendations**
- 🧠 **Flask + Python APIs** integrated with the app
- 🎨 User-friendly, intuitive interface

---

## **2. Problem Statement**
- Existing cooking apps provide **generic recipe lists** but lack **ingredient-based personalization**.
- Users waste **time**, **effort**, and **ingredients** when recipes require unavailable items.
- **Cookmania** solves this by:
  - Accepting **ingredients from the user**
  - Recommending recipes based on what’s available
  - Helping minimize **food waste**

---

## **3. Objectives**
- 🥘 **Personalized Recommendations** → Suggest recipes based on available ingredients  
- 🌱 **Food Waste Reduction** → Reduce unused ingredients  
- 🧠 **Machine Learning Integration** → Use **TF-IDF + Cosine Similarity + BallTree**  
- 📱 **Seamless Mobile Experience** → Easy-to-use Android app  
- 🔄 **Scalability** → Future-ready design for multilingual recipes & image-based recognition  

---

## **4. System Architecture**
The **Cookmania** system is built on three core layers:

### **1. Frontend (Mobile App)**
- Built using **Android Studio (Java + XML)**
- Ingredient input & recipe display interface

### **2. Backend (API & Model)**
- Powered by **Flask**
- Handles API requests, model integration & result generation

### **3. Machine Learning Model**
- Uses **TF-IDF** for vectorizing ingredients  
- Employs **Cosine Similarity + BallTree** for optimized recipe matching  
- Dataset includes **multi-cuisine translated recipes**

---

## **5. Methodology**

### **Step 1 — Dataset Collection**
- Gathered a **multi-cuisine recipe dataset** including names, instructions, and ingredients.

### **Step 2 — Data Preprocessing**
- Removed duplicates & missing values  
- Tokenized ingredient lists  
- Converted text to lowercase for **consistency**

### **Step 3 — Model Training**
- **TF-IDF Vectorizer** → Converts recipes into numerical vectors  
- **Cosine Similarity** → Measures closeness of ingredients  
- **BallTree** → Optimizes nearest-neighbor searches

### **Step 4 — API Development**
- Built **Flask REST APIs**  
- Integrated trained ML model with Android app

### **Step 5 — Mobile App Development**
- Developed an intuitive UI in **Android Studio**  
- Allows users to **input ingredients** and **get recommendations instantly**

---

## **6. Tools & Technologies**

| **Category**      | **Technologies Used**                  |
|-------------------|---------------------------------------|
| **Languages**     | Python, Java, XML                     |
| **Frameworks**    | Flask, Volley API                     |
| **Libraries**     | Scikit-learn, Pandas, NumPy           |
| **Database**      | SQLite                                |
| **IDE & Tools**   | Android Studio, PyCharm, Google Colab, Postman, Ngrok |
| **Version Control** | Git & GitHub                        |

---

## **7. Results**

| **Model**                   | **Accuracy** | **Recommendation Speed** |
|----------------------------|--------------|---------------------------|
| TF-IDF + Cosine Similarity | 91%          | Fast                      |
| TF-IDF + BallTree          | **93%**      | **Optimized**             |
| Traditional Search         | 70%          | Slow                      |

> **Cookmania achieved 93% accuracy** using **TF-IDF + BallTree** for ingredient-based recipe recommendations.

---

## **8. Future Enhancements**
- 🌐 **Multi-language Recipes** → Support for global cuisines  
- 🥗 **Ingredient Image Recognition** → Predict ingredients from photos  
- 📊 **Nutrition-based Recommendations** → Healthier and customized recipes  
- 🌍 **International Datasets** → Broader collection of cuisines  
- ☁️ **Cloud Deployment** → Host API for global scalability

---

## **9. How to Run the Project**

### **Step 1 — Clone the Repository**
```bash
git clone https://github.com/yourusername/cookmania.git
cd cookmania
