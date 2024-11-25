import os
from pars import *
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

tweet_prompt = PromptTemplate.from_template("""
                                            You are an expert Data analyst who can analyse the information and get insights from data very well and provide great insights about the entire report in a structured manner:
                                            here Im providing you a HTML template report of a data analytic file ->>{topic}<<-
                                            
                                            You are task understand the insights from the document and give me the most important insights from the file about the data in a structured way""")

tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt, verbose=True)
def read_html_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

if __name__=="__main__":
    

# Example usage
    file_path = 'data.json'  # Update with the path to your JSON file
    topic = load_json(file_path)
    topic = explore_json(topic)

    resp = tweet_chain.run(topic=topic)
    print(resp)