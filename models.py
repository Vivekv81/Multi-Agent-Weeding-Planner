from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
#from langchain_google_vertexai import ChatVertexAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

gemini_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")