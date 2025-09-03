🍳 COOKMANIA – Intelligent Recipe Recommendation System

A Machine Learning-Powered Mobile Application for Personalized Cooking Experiences

📌 Abstract

Cookmania is an Android-based recipe recommendation system powered by Machine Learning.
The application allows users to enter available ingredients and recommends suitable recipes instantly.
It leverages TF-IDF vectorization, Cosine Similarity, and BallTree algorithms to provide personalized and accurate recommendations.
The system also aims to reduce food waste, improve cooking efficiency, and enhance user experience by offering curated recipes based on real-time ingredient availability.

1. Introduction

Cooking is one of the most essential yet time-consuming daily activities. Most recipe platforms only allow keyword searches or predefined filters, but they fail to consider available ingredients.
Cookmania bridges this gap by using a machine learning-driven recommendation engine that analyzes the user’s ingredients and suggests recipes accordingly.

Key Highlights:

Built as a mobile application using Android Studio

Backend powered by Flask & Python APIs

Real-time ML-based recipe recommendation

Interactive and user-friendly interface

2. Problem Statement

Existing cooking apps provide generic recipe lists but lack ingredient-based personalization.
Users often struggle when they don’t have all ingredients for a recipe, resulting in wasted food, effort, and time.
Cookmania solves this problem by analyzing the ingredients users already have and recommending the best possible dishes — minimizing food waste and improving cooking efficiency.

3. Objectives

🥘 Personalized Recommendations → Suggest recipes based on user-provided ingredients

🌱 Food Waste Reduction → Help users utilize existing ingredients efficiently

🧠 Machine Learning Integration → Use TF-IDF and Cosine Similarity for accurate recommendations

📱 Seamless Mobile Experience → Build an intuitive Android app with clean UI

🔄 Scalable Design → Prepare architecture for future improvements like multilingual recipes & image recognition

4. System Architecture

The Cookmania system is divided into three main layers:

1. Frontend (User Interface)

Built using Android Studio (XML & Java)

Ingredient input & recipe display interface

2. Backend (API & Model Integration)

Built using Flask

Handles API requests, model integration & response delivery

3. Machine Learning Model

Uses TF-IDF Vectorization to represent recipes

Employs Cosine Similarity + BallTree for efficient recipe matching

Dataset includes multi-cuisine recipes with translated ingredients

5. Methodology
Step 1: Dataset Collection

Gathered a diverse dataset of multi-cuisine recipes with names, instructions, and ingredients

Step 2: Data Preprocessing

Removed duplicates & missing values

Cleaned and tokenized ingredient lists

Converted text into lowercase for uniformity

Step 3: Model Training

TF-IDF Vectorizer → Converts recipes into numerical vectors

Cosine Similarity → Measures similarity between ingredients

BallTree Algorithm → Optimizes search for nearest recipes

Step 4: API Development

Implemented REST APIs in Flask

Integrated the trained model with Android application

Step 5: Mobile App Development

Built using Android Studio

Simple UI to input ingredients and display recommendations

6. Tools & Technologies
Category	Technologies Used
Languages	Python, Java, XML
Frameworks	Flask, Volley API
Libraries	Scikit-learn, Pandas, NumPy
Database	SQLite
IDE & Tools	Android Studio, PyCharm, Google Colab, Postman, Ngrok
Version Control	Git & GitHub
7. Results
Model	Accuracy	Recommendation Speed
TF-IDF + Cosine Similarity	91%	Fast
TF-IDF + BallTree	93%	Optimized
Traditional Search	70%	Slow

Cookmania achieved a 93% accuracy with optimized TF-IDF & BallTree-based recipe recommendations.

8. Future Enhancements

🌐 Multi-language Support → Recipes in multiple languages

🥗 Ingredient Image Recognition → Predict ingredients using images

📊 Advanced Personalization → Nutrition-based recommendations

🌍 International Recipes → Expand dataset to include global cuisines

☁️ Cloud Deployment → Host the API for large-scale usage

9. How to Run the Project
Step 1 — Clone the Repository
git clone https://github.com/yourusername/cookmania.git
cd cookmania

Step 2 — Install Dependencies
pip install -r requirements.txt

Step 3 — Run the Flask Server
python app.py

Step 4 — Launch the Mobile App

Open the Cookmania project in Android Studio

Configure your API URL

Run the app on an emulator or physical device

10. Authors

👨‍💻 Hasnaat Abdullah
📧 Email: hasnatmughal17131@gmail.com

