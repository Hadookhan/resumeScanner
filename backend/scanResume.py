from openai import OpenAI
from uploadResume import upload_pdf
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)

def respond(file_path):

    parsedPDF = upload_pdf(file_path)

    print(parsedPDF)

    res = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a resume reviewer."},
            {"role": "user", "content": f"Here is my resume:\n\n{parsedPDF}"}
        ]
    )

    print(res.choices[0].message.content)

    return res.choices[0].message.content

