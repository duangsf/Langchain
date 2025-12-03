from src.test import llm

resp = llm.invoke("请用三句话介绍 yourself")
print(type(resp))
print(resp)