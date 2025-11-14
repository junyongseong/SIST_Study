import os
from dotenv import load_dotenv
import anthropic


load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
conversation =[] #대화기록 저장할곳

#사용자의 입력값(프롬포트) 추가
conversation.append({"role":"user","content":"안녕 난 yjun이야"})
conversation.append({"role":"user","content":"내가 누구라 했지?"})

response = client.messages.create(
    model="claude-3-5-haiku-latest",
    max_tokens=1000,
    messages=conversation
)
assistant_message = response.content[0].text
print(assistant_message)

