import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time
import os

import pandas as pd
from dotenv import load_dotenv

import spid

def send_email():
    # 获取当前脚本所在的文件夹路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 拼接出 data.csv 的完整路径
    file_path = os.path.join(script_dir, 'data.csv')
    load_dotenv()
    # 打开文件
    with open(file_path, 'rb') as f:
        file_data = f.read()
    try:
        con = smtplib.SMTP_SSL('smtp.qq.com',465,timeout=10)
        # 在 load_dotenv() 之后
        EMAIL_SENDER = os.getenv('EMAIL_SENDER', '').strip()
        EMAIL_AUTH_CODE = os.getenv('EMAIL_AUTH_CODE', '').strip()
        EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER', '').strip()
    
        con.login(EMAIL_SENDER, EMAIL_AUTH_CODE)
        time.sleep(2.14)
        msg = MIMEMultipart()
        subject = Header('爬虫数据','utf-8').encode()
        msg['Subject'] = subject
        msg['From'] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        data = spid.run_spider()
        df = pd.DataFrame(data)
        html_table = df.to_html(index=False)
        html_content = f'''
        <html>
        <head><style>table {{border-collapse: collapse; width: 100%;}} th, td {{border: 1px solid black; padding: 8px; text-align: left;}}</style></head>
        <h1>爬虫数据报告</h1>
        <body>
        <p>尊敬的导师：</p>
        <p>您好！以下是本次爬虫任务获取的数据报告，请查阅。</p>
        <p>以下是爬取的数据：</p>
        {html_table}
        <p>附件中包含了完整的爬取数据文件，供您进一步分析和使用。</p>
        <p>如有任何问题或需要进一步的信息，请随时与我联系。</p>
        <p>谢谢！</p>
        <p>最后，祝您工作顺利，生活愉快！</p>
        <p>此致</p>
        </body>
        </html>'''
        msg.attach(MIMEText(html_content, 'html', 'utf-8'))
        result = open(file_path,'rb').read()
        file = MIMEText(result,'base64','utf-8')
        file['Content-Disposition'] = 'attachment; filename="data_got_by_spider.csv"'
        msg.attach(file)
        con.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print('邮件发送成功！')
        time.sleep(3)
        con.quit()
        print('已安全退出程序')
    except Exception as e:
        print(f'ERROR:{e}')
        
    # import os
    # print(f"当前工作目录: {os.getcwd()}")
    # print(f"该目录下的文件列表: {os.listdir('.')}")

if __name__ == "__main__":
    send_email()