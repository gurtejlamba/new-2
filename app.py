import os
import google.generativeai as genai
import gradio

from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv("API_KEY")

genai.configure(api_key=API_KEY)


model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])

def chat_with_bot(question):
    if question.strip() == "":
        return "Please ask a valid question."
    response = chat.send_message(question)
    return response.text

interface = gradio.Interface(
    fn=chat_with_bot,
    inputs=gradio.Textbox(lines=2, placeholder="Enter your question here..."),
    outputs=gradio.Textbox(),
    title="Generative AI Chatbot",
    description="Ask anything to the chatbot powered by Google Generative AI made by gurtej."
)


interface.launch(share=True)