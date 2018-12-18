import smtplib
from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
 
#设置smtplib所需的参数
sender = "test@139.com" #发送邮箱
user = 'test@139.com' #邮箱登录名
password = 'test' #邮箱密码
smtpserver = 'smtp.139.com'   #smtp服务器

#receivers 可以是一个list
receivers = ['test@qq.com']   #接收邮箱

#构造邮件对象MIMEMultipart对象
subject = '这是自动发送测试邮件'  #邮箱标题
msg = MIMEMultipart('mixed')
msg['Subject'] = Header(subject, 'utf-8').encode()
msg['from'] = sender  
msg['to'] =  ";".join(receivers)

#构造纯文本邮件内容
text = '这里是发送的邮件的主要的内容。'
text_plain = MIMEText(text,'plain','utf-8')
msg.attach(text_plain)

#构造图片发送
sendimagefile=open(r'C:\Users\Administrator\Desktop\test\11.png','rb').read()
image = MIMEImage(sendimagefile)
image.add_header('Content-ID','<image1>')
image["Content-Disposition"] = 'attachment; filename="11.png"'
msg.attach(image)
'''
#构造html
html = """
<html>  
  <head></head>  
  <body>  
    <p>Hi!<br>  
       How are you?<br>  
       Here is the <a href="http://www.baidu.com">link</a> you wanted.<br> 
    </p> 
  </body>  
</html>  
"""    
text_html = MIMEText(html,'html', 'utf-8')
text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'   
msg.attach(text_html) 
'''

#构造附件
sendfile=open(r'C:\Users\Administrator\Desktop\test\upload_file.txt','rb').read()
text_att = MIMEText(sendfile, 'base64', 'utf-8') 
text_att["Content-Type"] = 'application/octet-stream'  
#以下附件可以重命名成aaa.txt  
#text_att["Content-Disposition"] = 'attachment; filename="aaa.txt"'
#另一种实现方式
text_att.add_header('Content-Disposition', 'attachment', filename='upload_file.txt')
msg.attach(text_att)

smtp = smtplib.SMTP() 
smtp.connect(smtpserver,25) 
smtp.login(user,password) 
smtp.sendmail(sender,receivers,msg.as_string())
smtp.quit()
print('邮件已成功发送了')
