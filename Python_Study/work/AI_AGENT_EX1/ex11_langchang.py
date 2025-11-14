"""
랭체인은 LLM을 효과적으로 활용하기 위한 프레임워크
언어로는 파이썬과 자바스크립트로 지원한다.
    - 파이썬 랭체인 : 깃허브 랭체인
    -JS 랭체인 : 랭체인js

    랭체인의 핵심은 프롬포트, 벡터 스토어, 아웃풋 파서, 메모리, LLM도구 등을 
    체인혀대로 연결하여 다양하고 복잡한 작업을 단순화 시키다.

    랭체인 모델은 LLM종류에 따라 다르다
    [오픈API] : pip install langchain[openai]==0.3.27
    [엔트로픽] : pip install langchain[anthropic]==0.3.27
    [구글 제미나이 모델] : pip install -q -U google-genai
    [구글 langchain 모델] : pip install langchain-google-genai
"""

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import random

load_dotenv()

if random.random()<0.5:
    print("Using other AI model")
else:
    model = init_chat_model("cluade-3-5-haiku-latest",model_provider="anthropic")
    result = model.invoke("RAG가 뭐야?")
    print(result)