from pydantic import BaseModel, Field
from test import llm
class Movie(BaseModel):  #数据模型类  schema类
    """电影详细"""
    title: str = Field(..., description="电影名称")
    year: int = Field(..., description="电影发行年份")
    director: str = Field(..., description="电影导演")
    rating: float = Field(..., description="电影评分（满分10分）")
#一些LangChain聊天模型支持.with_structured_output()方法。 该方法只需要一个模式作为输入，并返回一个字典或Pydantic对象。
#include_raw=True可以输出原始的模型输出AIMessage
model_with_structure = llm.with_structured_output(Movie, include_raw=True)
response = model_with_structure.invoke("提供电影《盗梦空间》的详细信息")
print(response)