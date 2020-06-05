import smtplib as root                                                           import time                                                                      from email.mime.text import MIMEText                                             from email.mime.multipart import MIMEMultipart                                                                                                                    # Clear console                                                                  from os import system, name                                                                                                                                       def clear():                                                                         if name == 'nt':                                                                     _ = system('cls')
    else:
        _ = system('clear')

def main():
        print ("""
developer: @nkitas
tg: @Termuxtop
• ▌ ▄ ·.  ▄▄▄· ▪  ▄▄▌  .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·.
·██ ▐███▪▐█ ▀█ ██ ██•  ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪
▐█ ▌▐▌▐█·▄█▀▀█ ▐█·██▪  ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·
██ ██▌▐█▌▐█ ▪▐▌▐█▌▐█▌▐▌▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌
▀▀  █▪▀▀▀ ▀  ▀ ▀▀▀.▀▀▀  ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀

[1] -> Спам с почты Mail.ru
[2] -> Спам с почты Yandex.ru

        """)

        task = input ('\nВыбирите желаемый сервис:')

        url = ''

        if task == '1':
                url = 'smtp.mail.ru'
        elif task == '2':
                url = 'smtp.yandex.ru'
        else:
                print ('Неправильный номер')

        print ("""\n

[1] -> Спам с одного аккаунта
[2] -> Спам с многих аккаунтов

        """)

        mode = input ('Выбирите режим спама:')

        if mode == '1':

                login = input ('Введите почту с которой будет идти спам:')
                password = input ('Пароль от почты для спама:')

                toaddr = input ('Почта жертвы:')

                topic = input ('Тема:')
                mess = input ('Сообщение:')

                msg = MIMEMultipart()

                msg['Subject'] = topic
                msg['From'] = login
                body = mess

                msg.attach (MIMEText(body, 'plain'))

                server = root.SMTP_SSL (url, 465 )
                server.login (login, password)

                while True:
                        server.sendmail (login, toaddr, msg.as_string() )
                        print ('Сообщение успешно отправлено')
                        time.sleep(10)

        if mode == '2':

                login = input ('Название файла (указывать расширение .txt):')

                passwords, logins = list(), list()

                with open(login, 'r') as file:
                    for line in file:
                        a, b = line.strip().split(':')
                        logins.append(a)
                        passwords.append(b)

                toaddr = input ('Почта жертвы:')

                topic = input ('Тема:')
                mess = input ('Сообщение:')


                for lgn in logins:
                        for psw in passwords:

                                msg = MIMEMultipart()

                                msg['Subject'] = topic
                                msg['From'] = lgn
                                body = mess

                                msg.attach (MIMEText(body, 'plain'))

                                server = root.SMTP_SSL (url, 465 )
                                server.login (lgn, psw)

                                try:
                                        while True:
                                                server.sendmail (lgn, toaddr, msg.as_string() )
                                                print ('Сообщение успешно отправлено')
                                                time.sleep(10)

                                except:
                                        continue





if __name__ == "__main__":
        clear ()
        main()
