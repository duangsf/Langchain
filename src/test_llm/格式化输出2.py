from langchain_core.output_parsers import SimpleJsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

from src.test import llm

#创建聊天提示模板，要求模型以特定格式回答问题
prompt = ChatPromptTemplate.from_template(
    "进你所能回答用户问题。" #基本命令
    '你必须始终输出一个包含"title","year","director","rating"键的JSON对象。'
    "{question}"
)

# | 是一个管道，左边的输出作为右边的输入
chain = prompt | llm | SimpleJsonOutputParser()
resp = chain.invoke({"question": "请提供电影《盗梦空间》的详细信息"})
print(resp)