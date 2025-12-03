from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI

from env_utils import ALIBABA_API_KEY, ALIBABA_BASE_URL, OPEN_API_KEY, OPEN_API_URL

#调用阿里云百炼的DeepSeek模型   langchain-OpenAI的插件 只能看到模型输出，不能看到模型思考的过程
# llm = ChatOpenAI(
#     model_name="deepseek-r1-0528",
#     temperature=0.5,  #模型随机性，越低越保守和重复，越接近1越有创意
#     api_key=ALIBABA_API_KEY,
#     base_url=ALIBABA_BASE_URL
# )

#使用的langchain-deepseek   调用时可以看到模型思考的过程
llm = ChatDeepSeek(
    model_name="deepseek-r1-0528",
    temperature=0.5,  #模型随机性，越低越保守和重复，越接近1越有创意
    api_key=ALIBABA_API_KEY,
    api_base=ALIBABA_BASE_URL
)

#在线的openai的大模型
# llm = ChatOpenAI(
#     model_name="gpt-4o",
#     temperature=0.5,
#     api_key=OPEN_API_KEY,
#     base_url=OPEN_API_URL
# )

