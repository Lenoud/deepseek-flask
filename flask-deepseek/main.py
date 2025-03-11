from config import Seting
from openai import OpenAI
from flask import Flask, render_template, request, Response

app = Flask(__name__)

# 初始化OpenAI客户端
client = OpenAI(
    base_url=Seting.Base_url,
    api_key=Seting.Api_key
)


@app.route('/')
def index():
    """渲染问答页面"""
    return render_template('index.html')


@app.route('/ask', methods=['GET', 'POST'])
def ask_question():
    """处理问答请求（支持GET/POST）"""
    # 根据请求类型获取参数
    question = request.args.get('question') if request.method == 'GET' \
        else request.form.get('question')

    # 保持原有generate_stream逻辑...

    def generate_stream():
        # 调用AI模型获取流式响应
        response = client.chat.completions.create(
            messages=[
                {'role': 'system', 'content': Seting.Preface},
                {'role': 'user', 'content': question}
            ],
            model=Seting.Model,
            stream=Seting.Stream
        )

        # 流式返回响应内容
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                yield f"data: {content}\n\n"

    return Response(generate_stream(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(host=Seting.Host, port=Seting.Port, debug=Seting.Debug)
