def send_email(message,recipient, *,sender = "university.help@gmail.com" ):
    first_search = sender.find('@')
    second_search = recipient.find('@')
    if first_search <= 0 or second_search <= 0:
        print('Невозможно отправить письмо с адреса', sender, ' на адрес ', recipient)
        return
    elif not sender.endswith(('.com', '.ru','.net')):
        print('Невозможно отправить письмо с адреса', sender, ' на адрес ', recipient)
        return
    elif not recipient.endswith(('.com', '.ru','.net')) :
        print('Невозможно отправить письмо с адреса', sender, ' на адрес ', recipient)
        return
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return
    elif sender != "university.help@gmail.com":
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)
        return
    else:
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
        return

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
        'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')


