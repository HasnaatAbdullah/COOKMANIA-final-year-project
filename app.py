from flask import Flask, request, jsonify 
import pickle 
import pandas 
import numpy as np 
app = Flask(  name  ) 
# Load the dictionary from the pickle file 
with open('model11.pkl', 'rb') as file: 
loaded_objects = pickle.load(file) 
new_df = loaded_objects['new_df'] 
vectorizer = loaded_objects['vectorizer'] 
balltree = loaded_objects['balltree'] 
# Your existing code for the recommend function 
def recommend(ingredients, new_df, vectorizer, balltree): 
# Convert input ingredients to a TF-IDF vector 
input_features = ' '.join(ingredients) 
input_tfidf_vector = vectorizer.transform([input_features]).toarray() 
# Query BallTree for nearest neighbors 
_, indices = balltree.query(input_tfidf_vector, k=10) 
# Get the recommended recipes details 
recommended_recipes = 'TranslatedInstructions']] 
return recommended_recipes 
# API endpoint for recommendation 
@app.route('/') 
def hello_world(): 
return 'hello hasnat' 
new_df.iloc[indices[0]][['TranslatedRecipeName', 
@app.route('/recommend', methods=['POST']) 
def get_recommendations(): 
# Get ingredients from the form data 
ingre1 = request.form.get('ingre1') 
ingre2 = request.form.get('ingre2') 
ingre3 = request.form.get('ingre3') 
ingredients = [ingre1, ingre2, ingre3] 
# Call the recommend function with the required arguments 
recommended_recipes = recommend(ingredients, new_df, vectorizer, balltree) 
# Format recommendations as a list of strings 
recommendations_list = [] 
for index, row in recommended_recipes.iterrows(): 
recommendation_string 
f"{row['TranslatedRecipeName']}:\n{row['TranslatedInstructions']}\n" 
recommendations_list.append(recommendation_string) 
# Join the list into a single string with line breaks 
recommendations_text = '\n'.join(recommendations_list) 
return jsonify({'recommendations': recommendations_text}) 
@app.route('/recommend1', methods=['POST']) 
def recommendations(): 
# Get ingredients from the form data 
ingre1 = request.form.get('ingre1') 
ingre2 = request.form.get('ingre2') 
ingre3 = request.form.get('ingre3') 
ingre4 = request.form.get('ingre4') 
ingre5 = request.form.get('ingre5') 
ingredients = [ingre1, ingre2, ingre3,ingre4, ingre5] 
# Call the recommend function with the required arguments 
recommended_recipes = recommend(ingredients, new_df, vectorizer, balltree) 
# Format recommendations as a list of strings 
recommendations_list = [] 
for index, row in recommended_recipes.iterrows(): 
recommendation_string 
f"{row['TranslatedRecipeName']}:\n{row['TranslatedInstructions']}\n" 
recommendations_list.append(recommendation_string) 
# Join the list into a single string with line breaks 
recommendations_text = '\n'.join(recommendations_list) 
return jsonify({'recommendations': recommendations_text}) 
@app.route('/recommend2', methods=['POST']) 
def getrecommendations(): 
# Get ingredients from the form data 
ingre1 = request.form.get('ingre1')  
ingre2 = request.form.get('ingre2') 
ingre3 = request.form.get('ingre3') 
ingre4 = request.form.get('ingre4') 
ingre5 = request.form.get('ingre5') 
ingre6 = request.form.get('ingre6') 
ingre7 = request.form.get('ingre7') 
ingre8 = request.form.get('ingre8') 
ingredients = [ingre1, ingre2, ingre3,ingre4, ingre5,ingre6,ingre7, ingre8] 
recommended_recipes = recommend(ingredients, new_df, vectorizer, balltree) 
# Format recommendations as a list of strings 
recommendations_list = [] 
for index, row in recommended_recipes.iterrows(): 
recommendation_string 
f"{row['TranslatedRecipeName']}:\n{row['TranslatedInstructions']}\n" 
recommendations_list.append(recommendation_string) 
# Join the list into a single string with line breaks 
recommendations_text = '\n'.join(recommendations_list) 
return jsonify({'recommendations': recommendations_text}) 
if  name == ' main ': 
app.run(debug=True) 

