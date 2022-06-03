## Gobang

五子棋小程序
支持玩家对战和人机对战

### 环境依赖

```
pip install -r requirements.txt
```

### 游戏运行

```
python3 src/main.py
```

### 操作指南

#### 目录界面:

通过w/s选择模式
回车确认模式

#### 游玩界面

鼠标点击操作
结束后按任意键返回

#### 退出游戏

暴力点关闭按钮

### 文件结构

```
├─Font  字体素材
├─img   图片素材
└─src   源码
    main.py      主程序
    board.py     棋盘类模块
    graphics.py  图形化与交互模块
    ai02.py      基于搜索的AI模块
-README.md    说明文件
-report.md    实验报告文件
-report.pdf   实验报告pdf
```

### 自定义AI方法

main.py第三行

```python
import ai02 as ai
```

将ai02修改为自定义AI模块
要求模块包含函数:

```python
def get_pos(B:board,typ:int)->tuple:
  pass
# board为定义在board.py中的棋盘类,详见report.md report.pdf
# typ为当前落子类型,取值为board.BLACK(值为1)或board.WHITE(值为2)
# 返回值为二元tuple(x,y)表示落子坐标[0,15]X[0,15]
# 注意事项
#   B为当前棋盘，结束时不应发生变化
#   当返回落子坐标不合法时程序会重复调用直到返回合法坐标,当函数不含随机性时，程序会陷入死循环
```
