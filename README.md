# Lyrics-Based Music Recommendation System

This repository contains a lyrics-based music recommendation system that recommends similar songs using semantic meaning, emotional similarity, and topic similarity from song lyrics.

The project uses transformer-based sentence embeddings, emotion classification, topic modeling, and FAISS similarity search to build a fast recommendation pipeline. A Streamlit web app is also included for interactive song recommendation.


## Project Overview

Traditional music recommendation systems often rely on user listening history, ratings, or collaborative filtering. This project focuses on recommending songs based on the actual lyrical content of songs.

The system analyzes lyrics from a large Spotify song dataset and creates recommendations using three main similarity signals:

- Semantic similarity using Sentence-BERT embeddings
- Emotional similarity using a transformer-based emotion classification model
- Topic similarity using LDA topic modeling

The final recommendation score is calculated using a weighted combination of semantic, emotion, and topic similarities.

## Key Features

- Lyrics-based song recommendation
- Semantic embedding generation using `all-MiniLM-L6-v2`
- Emotion analysis using `j-hartmann/emotion-english-distilroberta-base`
- Topic modeling using TF-IDF and Latent Dirichlet Allocation
- Fast similarity search using FAISS
- Interactive Streamlit web application
- Exploratory Data Analysis on song lyrics
- Visualization of emotion and topic distributions

## Dataset

The project uses the Spotify Million Song Dataset file:

```text
spotify_millsongdata.csv
```

Expected dataset columns include:

```text
artist
song
link
text
```

In the notebook, the `link` column is dropped, and the lyrics column `text` is used for preprocessing, embedding generation, emotion analysis, and topic modeling.

Dataset path used in the notebook:

```python
/content/spotify_millsongdata.csv
```

If you run the project locally or on Kaggle, update the dataset path according to your environment.

## Repository Structure

```text
.
├── Music_Recommendation_System.ipynb
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

The notebook generates the trained recommendation data file:

```text
song_recommendation_system.pkl
```

This file may be large, so it is recommended to store it outside GitHub and provide a download link in the README if needed.

## Methodology

The overall workflow of the project is:

1. Load the Spotify lyrics dataset.
2. Drop unnecessary columns.
3. Perform Exploratory Data Analysis.
4. Clean and preprocess lyrics using NLTK.
5. Generate semantic embeddings using Sentence-BERT.
6. Perform emotion analysis using a pretrained transformer model.
7. Extract topic features using TF-IDF and LDA.
8. Normalize embeddings and feature vectors.
9. Build FAISS indexes for fast similarity search.
10. Recommend similar songs using a weighted similarity score.
11. Save processed data and embeddings using Pickle.
12. Build an interactive Streamlit app for user-friendly recommendation.

## Recommendation Strategy

The system combines three types of similarity:

| Similarity Type | Description |
|---|---|
| Semantic Similarity | Measures meaning-based similarity between lyrics using Sentence-BERT |
| Emotion Similarity | Compares emotional tone of songs |
| Topic Similarity | Compares major lyrical topics using LDA |

Default weighting:

```python
semantic_weight = 0.5
emotion_weight = 0.3
topic_weight = 0.2
```

These weights can be adjusted to prioritize lyrical meaning, emotion, or topic relevance.

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Lyrics-Based-Music-Recommendation-System.git
cd Lyrics-Based-Music-Recommendation-System
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Requirements

A suitable `requirements.txt` file can include:

```txt
pandas
numpy
matplotlib
seaborn
plotly
wordcloud
nltk
scikit-learn
torch
transformers
sentence-transformers
faiss-cpu
streamlit
pyngrok
tqdm
```

## How to Run the Notebook

Open Jupyter Notebook:

```bash
jupyter notebook
```

Then run:

```text
Music_Recommendation_System.ipynb
```

If you are using Google Colab, upload the dataset file and update the dataset path if necessary.

## How to Run the Streamlit App

After generating the saved recommendation file:

```text
song_recommendation_system.pkl
```

run:

```bash
streamlit run app.py
```

The app will open in your browser and allow you to search for a song and get similar recommendations.

## Important Security Note

Do not commit personal API keys, tokens, or ngrok authentication tokens to GitHub.

If an ngrok token was accidentally included in the notebook, remove it before pushing the project. Store sensitive values in environment variables instead.

Example:

```python
import os
NGROK_AUTH_TOKEN = os.getenv("NGROK_AUTH_TOKEN")
```

## Files to Ignore

Recommended `.gitignore`:

```gitignore
venv/
.venv/
__pycache__/
.ipynb_checkpoints/
.DS_Store
*.pkl
*.csv
*.zip
.env
```

The dataset and generated model/data files should usually not be pushed to GitHub because they can be large.

## Future Work

Possible improvements include:

- Adding audio feature-based recommendation
- Combining lyrics-based and collaborative filtering methods
- Improving emotion modeling with larger transformer models
- Adding genre, artist, and popularity-based filtering
- Deploying the app on Streamlit Cloud, Hugging Face Spaces, or Render
- Building a full web application with user playlists and saved recommendations

## Author

**Ratul Podder**  
Department of Computer Science and Engineering  
East West University

## Academic Purpose

This project was developed for academic and learning purposes to explore natural language processing, transformer embeddings, topic modeling, emotion analysis, and recommendation systems.
