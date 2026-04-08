FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 默认命令：运行测试
# 注意：这里我们依赖外部传入的环境变量来决定浏览器
CMD ["sh", "-c", "pytest --alluredir=./reports/allure-results -v"]