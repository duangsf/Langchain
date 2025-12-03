from test import llm

for chunk in llm.stream("请用三句话介绍 yourself"):
    print(type(chunk))
    print(chunk)