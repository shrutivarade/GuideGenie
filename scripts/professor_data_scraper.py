import pandas as pd
import requests, re, sqlite3
from bs4 import BeautifulSoup

from scholarly import scholarly
import time

base_url = 'https://www.umb.edu/directory/?page='
num_pages = 365
regex_pattern = r'<span id="card-heading" class="button-cta card-heading">(.*?)<\/span>\s*<\/a>\s*<div class="card-role"><strong>Titles:<\/strong>\s*<p class="add-filter" data-category="(.*?)">(.*?)<\/p>\s*<\/div>\s*<div class="card-department"><strong>Departments:<\/strong>\s*<p class="add-filter" data-category="(.*?)">(.*?)<\/p>\s*<\/div>\s*<div class="card-email"><strong>Email:<\/strong>\s*<p class="add-filter" data-category="(.*?)">(.*?)<\/p>'

# Compile the regex pattern
regex = re.compile(regex_pattern)

# Initialize a list to store the extracted data
extracted_data = []

final_df = pd.DataFrame()

# Loop through each page
for page_num in range(1, num_pages + 1):
    page_url = base_url + str(page_num)
    print(page_url)
    response = requests.get(page_url)

    if response.status_code == 200:
        html_content = response.text

        # Apply the regex pattern to extract data
        matches = regex.findall(html_content)

        # Extend the extracted data list
        # extracted_data.extend(matches)

        df = pd.DataFrame(matches, columns=['Faculty Name', 'Title Category', 'Title', 'Department Category', 'Department', 'Email Category', 'Email'])
        final_df = final_df.append(df, ignore_index=True)
    else:
        print(f"Failed to fetch page {page_num}")

# Print the DataFrame or further process it
final_df.drop_duplicates(inplace=True)
final_df.drop(columns=['Title Category', 'Department Category', 'Email'], inplace=True)
final_df = final_df[final_df['Title'].str.contains('Professor', case=False, na=False)]
final_df.to_csv("professor_data.csv")

final_df.set_index('id', inplace=True)
final_df['Publication'] = None

def get_faculty_publication(name):
  search_query = scholarly.search_author(f'{name}')
  try:
    author = scholarly.fill(next(search_query))
    return ', Title: '.join([pub['bib']['title'] for pub in author['publications']])
  except:
    return ""

for index, row in final_df.iterrows():
    publication_value = get_faculty_publication(row['Faculty Name'])
    publication_value = "Title: " + publication_value
    final_df["Publication"][index] = publication_value
    final_df.to_csv("professor_data.csv")