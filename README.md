# 🎌 Anime Recommendation System

A beginner-friendly **content-based anime recommendation system** that suggests similar anime based on genre similarity.

## 📌 Project Overview

This project uses **TF-IDF vectorization** on anime genres and **cosine similarity** to recommend anime similar to a user’s favorite show.  
A simple **Streamlit web app** is built for interactive recommendations.

---

## 🚀 Features

- Search anime by name  
- Get similar anime recommendations  
- Sorted by highest average score  
- Clean dark-themed Streamlit UI  

---

## 🛠 Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  

---

## 📂 Dataset

Source: Anime dataset (e.g., MyAnimeList / AniList)

Used columns:
- `id`
- `title`
- `genres`
- `averageScore`
- `format`
- `popularity`

---

## ⚙️ How It Works

1. Genres converted to text format  
2. TF-IDF vectorization applied on genres  
3. Cosine similarity computed between all anime  
4. Given an input anime → most similar anime returned  

---

## ▶️ Run the Project

### Install requirements

pip install -r requirements.txt

### Run Streamlit App

streamlit run app.py

---

## 📁 Saved Files

- `cleaned_anime.csv` → preprocessed dataset  
- `cosine_sim.pkl` → similarity matrix  
- `app.py` → Streamlit web app  

---

## 🎯 Future Improvements

- Add anime poster images  
- Hybrid model (ratings + genres)  
- User login & personal recommendations  

---

## ❤️ Acknowledgment

Built as a beginner Machine Learning project using Streamlit.
