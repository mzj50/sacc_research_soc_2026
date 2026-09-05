import schedule
import time
from emailsender import send_email

def job():
    print(f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] 开始发送定时邮件...')
    send_email()

def start_scheduled_email():
    # 设置每天17:00执行
    schedule.every().day.at('17:00').do(job)

    print('定时邮件服务已启动，将在每天17:00发送邮件')
    print('按 Ctrl+C 停止程序')

    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        print('\n程序已停止')

if __name__ == '__main__':
    start_scheduled_email()