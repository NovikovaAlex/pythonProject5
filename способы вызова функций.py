
def send_email(message, recipient, *, sender='university.help@gmail.com' ):
    if sender == 'university.help@gmail.com':
        print ('Письмо успешно отправлено с адреса', sender,'на адрес', recipient)
        return
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'):
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)
        return
    else:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
        'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')

