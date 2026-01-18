import streamlit as st
import pandas as pd
import pickle

# ---------- Load Data ----------
df = pd.read_csv("cleaned_anime.csv")
cosine_sim = pickle.load(open("cosine_sim.pkl", "rb"))

# ---------- Page Config ----------
st.set_page_config(page_title="Anime Recommender", page_icon="🎌", layout="wide")

# ---------- CSS Styling ----------
st.markdown("""
<style>
body {background-color: #0f1117;}

.stTextInput label {color: white;}

.card {
    background-color: #1c1f26;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 15px;
    color: white;
}

.card h4 {
    color: #ffffff;
    margin-bottom: 5px;
}

.card p {
    color: #dddddd;
    margin: 2px 0;
}
</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.title("🎌 Anime Recommendation System")
st.write("Type an anime name and get similar recommendations ✨")

# ---------- Search Box ----------
user_input = st.text_input("Search Anime")

# ---------- Live Suggestions ----------
if user_input:
    suggestions = df[df['title'].str.lower().str.contains(user_input.lower())]['title'].head(5)
    if not suggestions.empty:
        st.write("Suggestions:")
        for s in suggestions:
            st.write("•", s)

# ---------- Recommendation Function ----------
def recommend(title, top_n=6):
    title = title.lower()
    matches = df[df['title'].str.lower().str.contains(title)]
    
    if matches.empty:
        return pd.DataFrame()
    
    idx = matches.index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    anime_indices = [i[0] for i in sim_scores]
    
    result = df[['title','genres','averageScore','format']].iloc[anime_indices]
    result = result.sort_values(by='averageScore', ascending=False)
    
    return result

# ---------- Button ----------
if st.button("Recommend 🚀"):
    if user_input.strip() == "":
        st.warning("Please type an anime name")
    else:
        recommendations = recommend(user_input)

        if recommendations.empty:
            st.error("Anime not found in dataset")
        else:
            st.subheader("Recommended For You 🍿")

            for _, row in recommendations.iterrows():
                st.markdown(f"""
                <div class="card">
                    <h4>{row['title']}</h4>
                    <p><b>Genres:</b> {row['genres']}</p>
                    <p><b>Format:</b> {row['format']}</p>
                    <p>⭐ <b>Score:</b> {row['averageScore']}</p>
                </div>
                """, unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")
