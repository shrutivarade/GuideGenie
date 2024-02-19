# GuideGenie

Preliminary Machine learning project to recommend a Professor to a student from a network of professors looking for a mentor or a guide. 

## Demo
Here's a short demo video of our web app.


![GuideGenie Demo](https://github.com/shrutivarade/GuideGenie/assets/21153844/09ed2d5e-d072-46f6-9d28-4bf04b274ae7)

## Quickstart

### Create an environment

```bash
python -m venv <venv>
```

### Activate the virtual environment.

For Windows
```bash
<venv>\Scripts\activate.bat
```

For MacOS and Linux
```bash
source <venv>/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the streamlit app

```bash
streamlit run main.py
```

## Additional scripts

### Web scraping
Original data was scraped from the university website. 

Run the below command from the project directory to scrap the professor's data. A professor_data.csv file will be generated. 

```bash
python scripts/professor_data_scraper.py
```

### Professor Embedding
Gemini AI was used to generate embeddings of professor data. \
Note: You need to replace it with your Gemini-AI API key. 

Run the below command from the project directory to generate embedding of the professor's data. A data_with_embedding.csv file will be generated. 

```bash
python scripts/embedding_generator.py
```

### Contributors
<a href="https://github.com/navkar98">
  <img src="https://github.com/navkar98.png" width="50" height="50" alt="Contributor Name">
</a>
<a href="https://github.com/shrutivarade">
  <img src="https://github.com/shrutivarade.png" width="50" height="50" alt="Contributor Name">
</a>
<a href="https://github.com/SamyakGangwal">
  <img src="https://github.com/SamyakGangwal.png" width="50" height="50" alt="Contributor Name">
</a>
<a href="https://github.com/kunalsahjwani">
  <img src="https://github.com/kunalsahjwani.png" width="50" height="50" alt="Contributor Name">
</a>
