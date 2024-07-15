from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from collections import deque
wd = webdriver.Chrome()
wd.get('https://www.sztu.edu.cn/')
wd.implicitly_wait(180)


def get_basic_information():
    stu_id=input('\n请输入学号：')
    # class_id_name=[]
    # teacher=[]
    # class_num=input('要抢几节课？：')
    # for i in range(class_num):
    class_names_queue=deque()
    teacher_names_queue = deque()
    while True:
        class_id_name=input('请输入课程名或者是课程编号，没有了输入‘okok’：')
        if 'okok' in class_id_name:
            print('课程信息输入结束')
            break
        class_names_queue.append(class_id_name)
        teacher_names_queue.append(input('请输入老师名称：'))
    # return(stu_id,class_names_queue,teacher_names_queue)
    enter_select_class_screm(stu_id)
    choose_the_class(class_names_queue,teacher_names_queue)

def enter_select_class_screm(stu_id):
    # 点击内网部到达统一认证
    wd.find_element(By.CSS_SELECTOR,'#nbw > span').click()
    sleep(1)
    # 切换到新窗口
    try:
        wd.switch_to.window(wd.window_handles[-1])
        if '系统' in wd.title:
            print('成功进入认证页面')
    except:
        print('没有成功进入认证页面')

    # 输入学号
    wd.find_element(By.CSS_SELECTOR, '#fs41_username').send_keys(stu_id)
    # sleep(0.2)
    # 点击获取验证码
    wd.find_element(By.CSS_SELECTOR, '#smsBtn1').click()

    # while True:
    code=input('验证码是多少：')
    # 输入验证码
    wd.find_element(By.CSS_SELECTOR, '#sms1_otpOrSms').send_keys(code)
    sleep(0.2)


    try :
        # 点击登录
        wd.find_element(By.CSS_SELECTOR, '#smsLoginBtn').click()
        sleep(10)
        wd.switch_to.window(wd.window_handles[-1])
        if '技术大学' in wd.title:
            print('成功登入内网部门，wd也已成功转到')
        else:
            print('登录失败')
    except:
        print('异常')


    # 点击教务
    wd.find_element(By.CSS_SELECTOR, 'body > div > div > div.right > div > div.right_nav_box_list > div:nth-child(1) > div.list_body > div.nav > span:nth-child(7) > a').click()
    sleep(3) #这里可能也要等久一些
    wd.switch_to.window(wd.window_handles[-1])
    print(wd.title)

    # 点击进入选课1
    wd.find_element(By.CSS_SELECTOR, '#dataList > tbody > tr:nth-child(1) > td > a').click()
    sleep(3)
    wd.switch_to.window(wd.window_handles[-1])
    print(wd.title)

    # 点击进入选课2
    wd.find_element(By.CSS_SELECTOR, '#attend_class > tbody > tr:nth-child(2) > td:nth-child(4) > a').click()
    sleep(3)
    wd.switch_to.window(wd.window_handles[-1])



    # 点击进入选课3（选课界面）
    while True:
        wd.find_element(By.CSS_SELECTOR, 'body > form > div > div > input.edu-btn.primary').click()
        sleep(0.2)
        old_handle=wd.current_window_handle
        wd.switch_to.window(wd.window_handles[-1])
        if wd.current_window_handle != old_handle:
            print('成功进入选课')
            break
        else:
            print('人太多啦，重新访问ing')


# print('把所有handles都打印出来')
# handles=wd.window_handles
# for handle in handles:
#     print(handle)


def choose_the_class(class_id_names,teacher):
    # 点击公选
    wd.find_element(By.CSS_SELECTOR, '#topmenu > li:nth-child(3) > a').click()
    sleep(0.3)
    wd.switch_to.frame('mainFrame')
    sleep(0.2)

    # 通过课程名和或者课程编号和老师姓名选课
    while True:
        # 先清楚再输入
        element_class=wd.find_element(By.CSS_SELECTOR, '#kcxx')
        element_class.clear()
        element_class.send_keys(class_id_names.popleft())
        sleep(0.1)
        element_teacher=wd.find_element(By.CSS_SELECTOR, '#skls')
        element_teacher.clear()
        element_teacher.send_keys(teacher.popleft())
        # 点击查询
        wd.find_element(By.CSS_SELECTOR, 'body > div.search-form-content > input.button').click()
        # 查找可以点击的元素们,
        # 我这里只选择第一个可选的课，其实可以完善一下
        wd.find_element(By.CSS_SELECTOR, 'div[id*="20242025"]').click()
        # 弹窗确认
        wd.switch_to.alert.accept()
        sleep(0.5)

        if class_id_names.len()==0:
            print('所有选课已完成')



if __name__=='__main__':
    get_basic_information()




input('程序结束')
sleep(500)