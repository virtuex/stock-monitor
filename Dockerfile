FROM virtuex/stock-monitor:v-1.0
ADD main.py /main.py
RUN #sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
RUN #apt-get update
RUN #apt-get install -y python3
RUN #apt-get install -y python3-pip
RUN pip3 install requests -i https://pypi.mirrors.ustc.edu.cn/simple/
CMD watch -n 1 'python3 /main.py'