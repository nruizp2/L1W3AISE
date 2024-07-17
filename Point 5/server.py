from fastapi import FastAPI
from vertexai.preview import tokenization
import google.generativeai as genai
from fastapi import Body
import os

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')
tokenizer = tokenization.get_tokenizer_for_model('gemini-1.5-flash')

app = FastAPI()

@app.post("/summarize/")
async def summarize(text: str = Body(..., embed=True)):
    response = model.generate_content(
        "Summarize this text in less than 100 words: " + text)
    return {"summary": response.text}
@app.post("/token/")
async def tokenCount(text: str = Body(..., embed=True)):
    return {"count": tokenizer.count_tokens(text)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)