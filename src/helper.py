import fitz # PyMuPDF 
from dotenv import load_dotenv
import requests

load_dotenv()




def exttract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.

    Args:
        uploaded_file(str): The path to the PDf file.

    Returns:
        str: The extracted text.
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text= ""
    for page in doc:
        text += page.get_text()
    return text



def ask_ollama(prompt,max_tokens=500):
    """
    Sends a prompt to the local Ollama model and returns the response.
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "tinyllama",   # use your installed model
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error: {response.text}"


