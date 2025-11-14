"""
LLM은 기본적으로 요청에 대한 응답을 두가지 형태로 제공함
1) 요청에 대한 응답을 한번에 반환하는 방법(앞의 예제의경우)
2) 요청에 대한 결과를 계속해서 흘려보내는 방법 (스트리밍 방식)

**스트리밍(Streaming)
    데이터를 실시간으로 전송하고 수신하는 방식
pip install rich
"""
import os
import anthropic
import rich
from dotenv import load_dotenv


load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

prompt = "대한민국의 수도는 서울인가여 인천인가여? 부산아닌가여?"
"""
    With로 인해서 __enter__()와 exit__()자동으로 호출됨
    __enter__() :함수에서 스트리밍 세션이 시작됨
    __exit__() : 함수에서 스트림을 안전하게 닫도록 보장함
"""
with client.messages.stream(
    messages=[{"role":"user","content":prompt}],
    model="claude-3-5-haiku-latest",
    max_tokens=500,
)as stream:
    for event in stream :
        if event.type =="text":
            print(event.text, end="")
    print("----------------------------")