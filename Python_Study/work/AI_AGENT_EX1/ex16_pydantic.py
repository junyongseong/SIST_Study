
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import random

load_dotenv()

llm = init_chat_model("claude-3-5-haiku-latest",model_provider="anthropic")