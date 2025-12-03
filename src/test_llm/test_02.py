from src.test import llm

# for chunk in llm.stream("请用三句话介绍 yourself"):
#     print(type(chunk))
#     print(chunk)

full = None
for chunk in llm.stream("请用三句话介绍 yourself"):
    full = chunk if full is None else full + chunk
    print(full.text)