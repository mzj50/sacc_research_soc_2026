#这里是程序的交互模块，也是主模块，这里通过构建由操作者输入命令的环境搭建交互性
#导入写好的爬虫模块


#为了提供更好的操作体验，引入延时来给操作者看清文字的时间
import time

import spid
from saver import save_all
import emailsender
import scheduled_email

def start_order():
    print('\n'+'='*50)
    time.sleep(1.5)
    print('''尊敬的操作员：
    您好！
    欢迎来到操作总台，在这里输入操作指令，即可启动整个爬虫和保存程序。
    接下来，我将聆听您的指令。''')
    time.sleep(3)
    while True:
    #通过while True语句搭建无限循环，提供错误输入指令后重新启动的机会，更为便捷
            choice = input("您是否想要启动爬虫系统？（输入 ‘是’ 或 ‘否’）：") #.strip()
            if choice == '是':
                print("收到指令，程序即将启动！")
                time.sleep(1)
                # 调用爬虫模块的主函数
                data  = spid.run_spider()
                if data:
                    feedback = "爬虫任务顺利完成。"
                    print(feedback)
                    return data,feedback
                else:
                    feedback = "爬虫任务未完成，请查看上方错误信息。"
                    print(feedback)
                    return None,feedback
    # 执行后退出循环（也可以询问是否继续）
            elif choice == '否':
                print(" 已取消操作，程序退出。")
                return None,"已取消操作，程序退出。"
            else:
                print("输入无效，请重新输入 ‘是’ 或 ‘否’。")
                time.sleep(3)

def save_order():
    data, feedback = start_order()
    if feedback == "爬虫任务顺利完成。":
        print('\n'+'='*50)
        time.sleep(1.5)
        while True:
            choice = input("您是否想要保存数据？（输入 ‘是’ 或 ‘否’）：") #.strip()
            if choice == '是':
                print("收到指令，程序即将启动！")
                time.sleep(1)
               
                save_all(data,'data.csv','data.json')
                print ('数据已保存，文件名为data.csv和data.json')
                break
            elif choice == '否':
                print(" 已取消操作，程序退出。")
                break
            else:
                print("输入无效，请重新输入 ‘是’ 或 ‘否’。")
                time.sleep(3)

def email_send_order():
    data, feedback = start_order()
    if feedback == "爬虫任务顺利完成。":
        print('\n'+'='*50)
        time.sleep(1.5)
        while True:
            choice = input("您是否想要发送邮件？（输入 ‘是’ 或 ‘否’）：") #.strip()
            if choice == '是':
                print("收到指令，程序即将启动！")
                time.sleep(1)
                # 调用发送邮件的函数
                save_all(data,'data.csv','data.json')  # 保存数据到文件
                emailsender.send_email()
                break
            elif choice == '否':
                print(" 已取消操作，程序退出。")
                break
            else:
                print("输入无效，请重新输入 ‘是’ 或 ‘否’。")
                time.sleep(3)

def scheduled_email_order():
    data, feedback = start_order()
    if feedback == "爬虫任务顺利完成。":
        print('\n'+'='*50)
        time.sleep(1.5)
        while True:
            choice = input("您是否想要设置定时发送邮件？（输入 ‘是’ 或 ‘否’）：") #.strip()
            if choice == '是':
                print("收到指令，程序即将启动！")
                time.sleep(1)
                # 调用定时发送邮件的函数
                save_all(data,'data.csv','data.json')  # 保存数据到文件
                scheduled_email.start_scheduled_email()  # 启动定时发送邮件
                break
            elif choice == '否':
                print(" 已取消操作，程序退出。")
                break
            else:
                print("输入无效，请重新输入 ‘是’ 或 ‘否’。")
                time.sleep(3)



# 当直接运行此文件时，启动交互
if __name__ == "__main__":
    # 可以选择运行哪个功能
    print("请选择功能：")
    print("1. 仅爬取数据")
    print("2. 爬取并保存数据")
    print("3. 爬取数据并发送邮件")
    print("4. 爬取数据并设置定时发送邮件")
    
    choice = input("请输入数字选择（1/2/3/4）：")
    
    if choice == '1':
        start_order()
    elif choice == '2':
        save_order()
    elif choice == '3':
        email_send_order()
    elif choice == '4':
        scheduled_email_order()
    else:
        print("无效选择！")
        

