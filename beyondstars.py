
telephone = "19307493070"
password = "1234qwer"
path = r'C:\Edge_WebDriver\msedgedriver.exe'


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
    icons = element.find_elements(By.CLASS_NAME, 'catalog_tishi56')
    if icons == []:
        print(f'检测到未完成章节:{element.text}个未完成任务数')
        break
    else:
        print(f'检测结果:{element.text}已完成')
        
        
print('开始自动刷课')

element.click()


speed = 1
 

while(1):
    wd.switch_to.default_content()
    print('成功进入默认框架')
    
    wd.switch_to.frame('iframe')
    print('成功进入网页框架')
    try:
        wd.switch_to.frame(wd.find_element(By.CSS_SELECTOR, '[jobid]'))
        print('成功进入视频框架')
        print('尝试寻找视频资源')
        videos = wd.find_elements(By.CLASS_NAME, 'vjs-big-play-button')
        if videos != []:
            
            print('找到视频,开始播放')
            for video in videos:
                
                complete = 0
                video.click()
                
            if speed == 1:
                #转2倍速
                a = wd.find_element(By.CSS_SELECTOR, '[title="播放速度"]')
                
                for i in range(0,3):
                    
                    a.click()
                    
                speed = 2
            
            
            #尝试答题
            while(1):
                time.sleep(1)
                try:
                    element = wd.find_element(By.CLASS_NAME, 'tkTopic_title')
                    print('找到问题')
                
                    while(1):
                        for i in [1,2,3,4]:
                            time.sleep(1)
                            try:
                                wd.find_element(By.CSS_SELECTOR, f'.tkItem_ul > li:nth-child({i})').click()
                                print(f'尝试第{i}项')
                                wd.find_element(By.ID, 'videoquiz-submit').click()
                                print('点击提交')
                                
                            except:
                                try:
                                    wd.find_element(By.ID, 'videoquiz-continue').click()
                                    print('点击继续')
                                except:
                                    pass
                        element = wd.find_element(By.CSS_SELECTOR, '[aria-valuenow]')
                        if element.get_attribute('aria-valuenow') == "100.00":
                            complete = 1
                            break
                except: 
                    if complete == 1:
                        break
    except:
        pass
                                
                                
                            
            
    finally:
        wd.switch_to.default_content()
        print('成功进入默认框架')
        wd.find_element(By.ID, 'prevNextFocusNext').click()
        print('进入下一节')
        try:
            time.sleep(2)
            wd.find_element(By.ID, 'popHeadFocusImg').click()
            break
        except:
            pass
        finally:
            pass


# print('你想刷第几章?(输入阿拉伯数字1,2,3等),如果想刷多章,不同章需要用空格空开,例如想刷全部十个章节,请输入1 2 3 4 5 6 7 8 9 10按enter')
# numbers1 = input('章序号: ').split( )
# numbers = [int(numbers1[i]) for i in range(len(numbers1))]

# for number in numbers:

#     element = elements[number]
#     element1 = element.find_element(By.)

print('检测到无法完成节点,程序结束,在终端中按enter结束')
input()