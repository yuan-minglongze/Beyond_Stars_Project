from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

print('尝试打开网站')

# 创建 WebDriver 对象
wd = webdriver.Edge(service=Service(r'C:\Edge_WebDriver\msedgedriver.exe'))

wd.implicitly_wait(10)

wd.get('http://csu.fanya.chaoxing.com/portal')

print('打开网页成功,请登录.登录完成应该自动转跳到学习空间(此时你的网址应该是http://i.mooc.chaoxing.com/,网页标题为"中南大学"),请确保你浏览器打开的网页只有学习空间,然后选择终端,按enter继续')

wd.find_element(By.CLASS_NAME, 'loginSub').click()
element = wd.find_element(By.CLASS_NAME, 'ipt-tel').send_keys('19307493070')
element = wd.find_element(By.CLASS_NAME, 'ipt-pwd').send_keys('1234qwer')
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

wd.switch_to.default_content()
print('成功改变框架')
wd.switch_to.frame('iframe')
print('成功改变框架')
wd.switch_to.frame('ans-attach-online ans-insertvideo-online')
print('成功改变框架')
print('尝试寻找视频资源')
video = wd.find_elements(By.CLASS_NAME, 'vjs-poster')
if video != []:
    print('找到视频')
    element.find_element(By.CLASS_NAME, 'vjs-big-play-button').click()


# print('你想刷第几章?(输入阿拉伯数字1,2,3等),如果想刷多章,不同章需要用空格空开,例如想刷全部十个章节,请输入1 2 3 4 5 6 7 8 9 10按enter')
# numbers1 = input('章序号: ').split( )
# numbers = [int(numbers1[i]) for i in range(len(numbers1))]

# for number in numbers:

#     element = elements[number]
#     element1 = element.find_element(By.)

print('程序结束,按enter结束')
input()