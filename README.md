# 股票盯盘工具
- 添加股票
修改`main.py`中的`all_stck`字典，将要盯盘的股票在其中编辑即可。
- 发布镜像
```shell
chmod +x buildImage.sh & ./buildImage.sh
```
- 启动工具
```shell
docker run --name stock-monitor -it virtuex/stock-monitor:v-1.0
```