#
# 
# Hello World!
#
#
# 这是一个刷中南大学2023年秋近代史纲要mooc的小程序
# 这个程序会单独打开一个浏览器窗口并进行自动刷课
#
# 请注意,这个文件只能帮你自动进行操作,并不能避开网站检测,
# 启动后需要你停留在打开的网页(就像是你自己在刷课一样),鼠标指针不能离开网页,也不能切换活动窗口,否则视频会暂停
# 使用前请仔细阅读"https://github.com/yuan-minglongze/beyondstars"中的readme.md

# 如果你已经按照readme.md操作过了,我们下面来做运行前的最后准备

# 1. 请将下面的字符串内容改为你登录学习平台的电话号码,注意这是一个字符串,不要把引号和引号前面的r搞没了
telephone = r"your telephone number"
# 2. 请将下面字符串内容改为你的密码,同样注意这是一个字符串,也不要把引号和r搞没了
password = r"your password"
# 3. 最后请将下面字符串内容改为你刚下载的msedgedriver.exe在你电脑中的地址,不知道地址怎样写的话请自行百度
path = r'C:\Edge_WebDriver\msedgedriver.exe'
# 4. 按F5(如果你用的是IDLE)运行这个脚本,不要再进行任何操作.直到程序新打开的浏览器被关闭,或者遇到多选题,章节测试,或者你向让程序暂停的任意时刻

# 如果程序运行的有问题,别忘了在命令行中按ctrl + C可以停止程序运行,本程序没有设置自动停止的方法


from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

print('尝试打开网站')

# 创建 WebDriver 对象
wd = webdriver.Edge(service=Service(path))

wd.maximize_window() 

wd.implicitly_wait(5)

wd.get('http://csu.fanya.chaoxing.com/portal')

print('打开网页成功')

wd.find_element(By.CLASS_NAME, 'loginSub').click()
element = wd.find_element(By.CLASS_NAME, 'ipt-tel').send_keys(telephone)
element = wd.find_element(By.CLASS_NAME, 'ipt-pwd').send_keys(password)
element = wd.find_element(By.ID, 'phoneLoginBtn').click()

while(1):
#    input('>')
    for handle in wd.window_handles:
    # 先切换到该窗口
        wd.switch_to.window(handle)
        is_web_right = '中南大学' == wd.title
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
        if is_web_right:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
            print('找到目标网站')
            break
    if is_web_right:
        break
    else:
        print('未找到目标网站,请重试')
        
        
print('尝试打开课程')
wd.switch_to.frame('frame_content')

element = wd.find_element(By.CSS_SELECTOR, '[title="【2023秋】中国近现代史纲要"]')
element.click()
wd.switch_to.default_content()#切换框架
print("打开课程成功")



print('尝试进入课程网站和"章节"菜单')
for handle in wd.window_handles:
    # 先切换到该窗口
        wd.switch_to.window(handle)
        is_web_right = '【2023秋】中国近现代史纲要' == wd.title
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
        if is_web_right:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
            print('找到目标网站')
            break
        
element = wd.find_element(By.CSS_SELECTOR, '[title="章节"]')
element.click()
print('已进入章节菜单')




print('正在载入章节信息')
wd.switch_to.frame('frame_content-zj')
elements = wd.find_elements(By.TAG_NAME, "li")
print('输出章节列表')
for element in elements:
    print(element.text)
print('章节信息载入完成')



print('正在检测进度,可能耗时较长,请稍等...')
for element in elements:
    print(f'正在检测{element.text}')
    hint = element.find_element(By.CLASS_NAME, 'bntHoverTips')
    print(hint.get_attribute("textContent"))
    if hint.get_attribute("textContent") == '已完成':
        print(f'检测结果:{element.text}已完成')
        
    else:
        print(f'检测到未完成章节')
        break 
        
        
print('开始自动刷课,首先进入课程')

element.click()

print('已进入该课程')


speed = 1


while(1):   #进入每一个小节

    wd.switch_to.default_content()
    print('成功进入默认框架')
    
    wd.switch_to.frame('iframe')
    print('成功进入网页框架')
  
    try:#尝试寻找视频
        print('尝试进入视频')  
        wd.switch_to.frame(wd.find_element(By.CSS_SELECTOR, '.ans-insertvideo-online'))
        print('成功进入视频框架')
        
        print('尝试寻找视频资源')
        video = wd.find_element(By.CLASS_NAME, 'vjs-big-play-button')   
        print('找到视频,开始播放')
            
        complete = 0    #记录视频是否播放完成
        
        i = 0           #记录目前为第几选项
        
        video.click()   #开始播放视频
            
        if speed == 1:  #转2倍速
            
            a = wd.find_element(By.CSS_SELECTOR, '[title="播放速度"]')
            
            for m in range(0,3):
                
                a.click()
                
            speed = 2
        
        
        #尝试答题
        while(1):

            try:        #尝试找题
                
                print("尝试找题")
                element = wd.find_element(By.CLASS_NAME, 'tkTopic_title')
                time.sleep(1)
                print('找到问题')
                
                wd.find_element(By.CSS_SELECTOR, f'.tkItem_ul > li:nth-child({i % 4 + 1})').click()
                print(f'选中第{i % 4 + 1}项')

                print('点击提交')
                try:    #继续选择到提交按钮消失
                    while(1):
                        time.sleep(0.5)
                        i += 1
                        wd.find_element(By.CSS_SELECTOR, f'.tkItem_ul > li:nth-child({i % 4 + 1})').click()
                        print(f'选中第{i % 4 + 1}项')
                        wd.find_element(By.ID, 'videoquiz-submit').click()
                        print('尝试提交')
                        
                except:     #提交按钮消失后尝试点击继续
                    try:        #尝试点击一次继续
                            wd.find_element(By.ID, 'videoquiz-continue').click()
                            print('点击继续')

                            
                    except:     #一次都没有,说明答对
                        pass
                    finally:    #有继续,说明答错,继续点到没有继续按钮
                        try:
                            while(1):
                                wd.find_element(By.ID, 'videoquiz-continue').click()
                                print('点击继续')
                        except:
                            pass
                        
            except:    #没找到题或者题目完成,判断视频是否播放完
                if wd.find_element(By.CSS_SELECTOR, '[aria-valuenow]').get_attribute('aria-valuenow') == "100.00":
                    complete = 1
                    print('视频结束')
                    
                    break
    except:
        pass
    finally:
        wd.switch_to.default_content()
        print('成功进入默认框架')
        wd.find_element(By.ID, 'prevNextFocusNext').click()
        print('进入下一节')
        # try:    #判断是否有未完成任务,有的话退出程序
        #     time.sleep(2)
        #     wd.find_element(By.ID, 'popHeadFocusImg').click()
        #     break
        # finally:
        #      pass
         
         
print('检测到无法完成节点,程序停止,在终端中按enter结束程序')
input()

# # print('你想刷第几章?(输入阿拉伯数字1,2,3等),如果想刷多章,不同章需要用空格空开,例如想刷全部十个章节,请输入1 2 3 4 5 6 7 8 9 10按enter')
# # numbers1 = input('章序号: ').split( )
# # numbers = [int(numbers1[i]) for i in range(len(numbers1))]

# # for number in numbers:

# #     element = elements[number]
# #     element1 = element.find_element(By.)

