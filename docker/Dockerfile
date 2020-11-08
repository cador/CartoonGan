FROM cadorai/python:3.6
MAINTAINER youhaolin
WORKDIR /work
COPY requirements.txt /work
RUN apt update
RUN apt-get install ffmpeg -y
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install git+https://www.github.com/keras-team/keras-contrib.git

# docker build -t cadorai/cartoongan:base .
# -i https://pypi.tuna.tsinghua.edu.cn/simple
