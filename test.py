from langchain.chat_models import init_chat_model
from langchain_core.rate_limiters import InMemoryRateLimiter
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

#速率限制
rate_limiter = InMemoryRateLimiter(
    requests_per_second=0.1,  # 每秒请求数 10秒请求1次
    check_every_n_seconds=0.1,  #100ms 检查一次是否允许发出请求
    max_bucket_size=10, #控制最大的突发请求数
)

model = init_chat_model(
    model_name="deepseek-r1-0528",
    model_provider="openai",
    api_key=ALIBABA_API_KEY,
    base_url=ALIBABA_BASE_URL,
    rate_limiter=rate_limiter
)

