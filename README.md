
# Movie Recommendation System 🎥
A Movie Recommendation System that suggests movies tailored to user preferences, using collaborative filtering and metadata. Explore movies with a simple, user-friendly interface and dynamic recommendations!


## 🌟Features

- 🎬 Personalized Suggestions: Receive movie recommendations based on your input.
- 🖼️ Visual Appeal: View posters of recommended movies.
- ⚡ Efficient Algorithm: Powered by collaborative filtering for accurate results.
- 🌐 API Integration: Fetch movie posters and metadata dynamically from APIs.


## 🛠️Tech Stack

**Frontend:** Streamlit for the interactive UI.

**Backend:** Python with Pandas and NumPy for data manipulation and similarity computation.

**APIs:** OMDB API for fetching movie details and posters.

## ⚙️ How It Works

### Dataset
A curated dataset of movies, including:
- Titles
- Genres
- Movie IDs

### Recommendation Engine
1. **Input**: Select a movie from the dropdown menu.
2. **Computation**:
   - Calculates similarities between movies using a pre-computed similarity matrix.
   - Identifies and displays the top 5 most similar movies.

### Poster Fetching
- Movie posters are dynamically fetched via API requests to enhance the user experience.
## 🚀 Getting Started

### Prerequisites
To run this project, ensure you have the following installed:

- **Python 3.7 or above**: Install Python from [python.org](https://www.python.org/).
- **OMDB API Key**: 
  - Sign up at [OMDB API](https://www.omdbapi.com/apikey.aspx) to get your API key.
  - Once you have the key, it will be used to fetch movie data and posters.


## License

[This project is licensed under the MIT License. See the LICENSE file for details.](https://choosealicense.com/licenses/mit/)


## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```


## 🚀 About Me
**Developer** : Akhilesh Kumar Pandey

**E-Mail**: akhileshpandey878889@gmail.com

**github**: https://github.com/Akhileshpandey21