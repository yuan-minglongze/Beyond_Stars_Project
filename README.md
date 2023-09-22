# beyondstars project

## 这是什么?

这是完全由我自主编写的中南大学2023年秋近代史纲要mooc刷课小程序.

使用python语言和selenium库,进行网页自动操作.

## 目前已实现的功能

自动打开网站,自动登录,自动检测当前学习进度,自动继续学习,自动播放视频,自动调整为2倍速,自动回答单选题,视频播放完成后自动跳转到下一小节.
直到遇到多选题或者章节测试.


## 如何使用

首先你需要准备运行环境,包括

- **python**
- selenium库
- **Microsoft edge(windows10,11自带浏览器)**
- **Microsoft edge webdriver**
- 一个python编辑器(为了方便大家,在这里使用python IDLE)


其中我加粗的是需要大家自行下载的(不过edge应该都有吧,所以大多数人应该只需要下载python和webdriver),你可以点击下面的链接自行下载


[Python(包含python IDLE) 下载](https://www.python.org/downloads/)


[Microsoft Edge 下载](https://www.microsoft.com/zh-cn/edge/download)


[Microsoft Edge WebDriver 下载](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)  (注意这个下载下来是一个压缩文件,直接解压缩就是webdriver本体,不需要安装)


或者你嫌下载速度慢,我已经把安装程序(再次强调,webdriver不需要安装,我打包的就是webdriver本身)打包为.zip了,大家直接在github下载下来解压缩再安装就可以了.

其中python的安装特别要注意,在启动python安装程序后,你会看到如下界面:

![image](https://github.com/yuan-minglongze/beyondstars/assets/129572345/4799516f-4df4-4b51-974c-f38facb667c7)

红箭头指的那个选项***一定要勾选*** ***一定要勾选*** ***一定要勾选*** (你看到的可能是3.11或者3.12),如果你忘记了勾选,请卸载掉重新安装.




## 目前未实现的功能

- 不能避免网页检测(这个我目前的技术力应该做不了)
- 几乎不能完成多选题作答(但是ABCD全选的题目可以自动答)
- 章节测试没有实现自动(进入测试时网页会强行停止外部程序,不能完全自动化,大家直接搜答案吧)
