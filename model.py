# ---------------------------
# 📌 Import Required Libraries
# ---------------------------
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import BallTree
from sklearn.model_selection import train_test_split

# ---------------------------
# 📌 Load & Preprocess Dataset
# ---------------------------
# Read the CSV file
df = pd.read_csv('set11.csv')

# Combine TranslatedIngredients with Diet for richer features
df['TranslatedIngredients'] = df['TranslatedIngredients'] + ' ' + df['Diet']

# Keep only the relevant columns
df = df[['TranslatedRecipeName', 'TranslatedIngredients', 'TranslatedInstructions']]

# Drop missing values
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Check null values (optional)
print("Missing values:\n", df.isnull().sum())

# ---------------------------
# 📌 Text Preprocessing
# ---------------------------
# Split ingredients into lists
df['TranslatedIngredients'] = df['TranslatedIngredients'].apply(lambda x: x.split())

# Remove extra spaces within ingredients
df['TranslatedIngredients'] = df['TranslatedIngredients'].apply(lambda x: [i.replace(" ", "") for i in x])

# Create 'tag' column for cleaned lowercased ingredients
df['tag'] = df['TranslatedIngredients']
df['tag'] = df['tag'].apply(lambda x: " ".join(x))
df['tag'] = df['tag'].apply(lambda x: x.lower())

# Create a new dataframe with required columns
new_df = df[['TranslatedRecipeName', 'TranslatedInstructions', 'tag']]

# ---------------------------
# 📌 Feature Engineering: TF-IDF
# ---------------------------
# Combine ingredients and instructions into a single feature
new_df['CombinedFeatures'] = new_df['tag'] + ' ' + new_df['TranslatedInstructions']

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(new_df['CombinedFeatures'].values.astype('U'))

# Convert to dense representation for BallTree
dense_tfidf_matrix = tfidf_matrix.toarray()

# Calculate Cosine Similarity Matrix
similarity = cosine_similarity(dense_tfidf_matrix, dense_tfidf_matrix)

# Build BallTree for nearest neighbors search
balltree = BallTree(dense_tfidf_matrix)

# ---------------------------
# 📌 Recipe Recommendation Function
# ---------------------------
def recommend(ingredients, new_df=new_df, vectorizer=vectorizer, balltree=balltree):
    """
    Recommends top 10 recipes based on input ingredients.
    """
    # Convert input ingredients into TF-IDF vector
    input_features = ' '.join(ingredients)
    input_tfidf_vector = vectorizer.transform([input_features]).toarray()

    # Query BallTree for 10 nearest neighbors
    _, indices = balltree.query(input_tfidf_vector, k=10)

    # Get top recommended recipes
    recommended_recipes = new_df.iloc[indices[0]][['TranslatedRecipeName', 'TranslatedInstructions']]
    return recommended_recipes

# ---------------------------
# 📌 Train-Test Split
# ---------------------------
train_data, test_data = train_test_split(new_df, test_size=0.2, random_state=42)

# ---------------------------
# 📌 Evaluation Function
# ---------------------------
def evaluate_recommendation_system(test_data, recommendation_function):
    """
    Evaluate the recommendation system based on accuracy.
    """
    total_recipes = 0
    relevant_recipes = 0

    for _, row in test_data.iterrows():
        ingredients = row['tag'].split()  # Use ingredients from test set

        # Get recommended recipes
        recommended_recipes = recommendation_function(ingredients)

        # Check if actual recipe is in recommended set
        actual_recipe_name = row['TranslatedRecipeName']
        if actual_recipe_name in recommended_recipes['TranslatedRecipeName'].values:
            relevant_recipes += 1

        total_recipes += 1

    # Calculate accuracy
    accuracy = relevant_recipes / total_recipes if total_recipes != 0 else 0
    return accuracy

# ---------------------------
# 📌 Evaluate Recommendation Model
# ---------------------------
accuracy = evaluate_recommendation_system(test_data, recommend)
print(f'✅ Recommendation System Accuracy: {accuracy * 100:.2f}%')

# ---------------------------
# 📌 Test the Recommendation System
# ---------------------------
print("\n🔹 Recommended Recipes:\n")
print(recommend(["chicken", "onion", "garlic"]))
