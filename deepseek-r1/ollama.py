from openai import OpenAI

# 初始化OpenAI客户端
client = OpenAI(
    base_url='http://localhost:11434/v1/',  # 你的自定义base_url
    api_key='ollama'
)

# 获取用户输入
message = input("输入问题：")

# 使用AI模型处理消息
response = client.chat.completions.create(
    messages=[
        {
            'role': 'system',
            'content': '以中文形式回答，控制字数在200个字以内'
        },
        {
            'role': 'user',
            'content': message
        }
    ],
    model='deepseek-r1:8b',  # 模型名称
    stream=True  # 启用流式输出
)

# 输出AI的回复内容
for chunk in response:
    content = chunk.choices[0].delta.content
    if content is not None:
        print(content, end='', flush=True)
