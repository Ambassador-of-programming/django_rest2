from django.core.mail import EmailMessage
from django.conf import settings



def send_msg(email, shop_name, username):
    mail = EmailMessage(
        f"Добро пожаловать {username}", 
        f'Вы создали магазин с названием: {shop_name}', 
        settings.EMAIL_HOST_USER, 
        [email]
    )
    mail.attach_file('mainapp/apps.py')
    mail.send()


