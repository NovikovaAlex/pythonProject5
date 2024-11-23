team1_num = 5
team2_num = 6
pirs_str = 'В команде Мастера кода участников:%d!' % team1_num

pirs_str2 =  "Итого сегодня в командах участников:%(team1)d и %(team2)d!" % ({'team1':team1_num,'team2': team2_num})

score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'
    return result

def tasks_total():
    tasks = score_1 + score_2
    return tasks

def time_avg():
    time = (team1_time + team2_time)/ tasks_total()
    time_red = round(time,1)
    return time_red


print(pirs_str)
print(pirs_str2)
print('Команда Волшебники данных решила задач:{}'.format(score_2))
print('Волшебники данных решили задачи за {}'.format(team1_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: победа команды:{challenge_result()}!')
print(f'Сегодня было решено {tasks_total()} задач, в среднем по {time_avg()} секунды на задачу!')