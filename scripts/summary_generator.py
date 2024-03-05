from tenacity import retry, stop_after_attempt, wait_fixed
import google.generativeai as genai
import pandas as pd

genai.configure(api_key="your_api_key")
genai_model = genai.GenerativeModel('gemini-pro')

@retry(
    stop=stop_after_attempt(5),  # Retry up to 5 times
    wait=wait_fixed(2),  # Wait 2 seconds between retries
    reraise=True  # Re-raise the final error if all retries fail
)
def call_with_retry(genai_model, prompt, generation_config):
    response = genai_model.generate_content(
        prompt, generation_config=generation_config
    )
    return response

def process_string(s):
    items = s.split("Title: ")[:1000]  # Split and take top 1000
    return ";".join(items)

def summarize_text_with_gemini(text):
  text = process_string(text)

  prompt="Given the faculty publication titles generate an introduction of the faculty to recommend the faculty to students, focus on the faculty work and research areas. Make sure to produce introduction only and no additional formatting:\n\n" + text
  response = call_with_retry(
      genai_model, prompt,
      genai.types.GenerationConfig(candidate_count=1,max_output_tokens=475,temperature=1.0))

  try:
    summary = response.text

    return summary
  except Exception as e:
    print(e)
    return ""

professors_data = pd.read_csv("professor_data.csv")
professors_data['Summary'] = professors_data['Combined_Info'].apply(summarize_text_with_gemini)
professors_data = professors_data[professors_data['Summary'] != ""]

professors_data.to_csv("data_with_embedding.csv")
