from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableParallel, RunnableLambda
from langchain_anthropic import ChatAnthropic
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
api_key= os.getenv("ANTHROPIC_API_KEY")

def is_english(x:dict)->bool:
    """입력 딕셔너리의 'word'키에 해당하는 값이 영이인지 확인"""
    return all (ord(char)<128 for chat in x["word"])
###해석 ########################
# x["word"]:dict에서 :"word"라는 키의 문자영 값을 가져옴
# for char in x["word"] 문자열의 각 문자를 하나씩 가져와서 반복 수행
# ord(char): 해당 문자의 유니코드 숫자값을 가져옴
# ord(char) <128: 아스키 코드 범위 (0~127)안에 있으면 True

#영어일때 사용할 프롬포트
english_prompt