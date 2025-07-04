# Movie Recommender System

A content-based movie recommendation engine that suggests similar movies using cosine similarity and metadata analysis. The system provides an interactive web interface built with Streamlit for real-time movie selection and recommendation display.

## Overview

This project implements a content-based filtering approach to recommend movies based on their metadata features. The system analyzes movie attributes such as genres, cast, crew, and plot summaries to identify similar titles and provide the top 5 recommendations for any selected movie.

## Features

- Content-based movie recommendation using cosine similarity
- Interactive web interface with real-time recommendations
- Top 5 similar movie suggestions based on user input
- Efficient similarity computation using scikit-learn
- Clean and responsive Streamlit interface

## Technologies

- Python 3.7+
- Streamlit
- Scikit-learn
- Pandas
- NumPy

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

## Algorithm

The recommendation system follows these steps:

1. **Data Preprocessing**: Load and clean movie metadata from the dataset
2. **Feature Engineering**: Combine relevant features (genres, cast, crew, overview) into text representations
3. **Vectorization**: Convert text data to numerical vectors using TF-IDF vectorization
4. **Similarity Calculation**: Compute cosine similarity between movie feature vectors
5. **Recommendation**: Return top 5 movies with highest similarity scores

## Dataset Requirements

The system expects a CSV file with the following columns:
- title: Movie title
- genres: Movie genres
- cast: Cast information
- crew: Crew details
- overview: Plot summary

## Configuration

The number of recommendations and similarity threshold can be adjusted in the `recommender.py` file. Additional metadata fields can be incorporated by modifying the feature engineering pipeline.

