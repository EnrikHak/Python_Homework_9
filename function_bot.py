from datetime import datetime
from sys import exit


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет, друг!Как дела, что нового?')


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!!!')


def time(update, context):
    context.bot.send_message(update.effective_chat.id, (f'{datetime.now().time()}'))


#   Напишите бота, удаляющего из текста все слова, содержащие "абв". (текст вводит пользователь)

def abc(update, context):
    text = update.message.text
    t_without = " ".join(list(filter(lambda x: 'абв' not in x.lower(), text.split())))
    context.bot.send_message(update.effective_chat.id, t_without)


#   Игра в конфеты

""" def check_win(update, context):
    if m == 1 and n == 0:
        return 'Выиграл бот'
    elif m == 0 and n == 0:
        return 'Выиграл пользователь'
    return None """


""" j = 0 # 0 - ходит пользователь, 1 - ход бота
n = 60
while n > 0:
    if n >= 28:
        count_user = int(input("Сколько Вы хотите взять конфет?(от 1 до 28): "))
        while count_user < 1 or count_user > 28:
            count_user = int(input("Вы ошиблись, попробуйте заново\nСколько Вы хотите взять конфет?(от 1 до 28): "))
    else:
        count_user = int(input(f"Сколько Вы хотите взять конфет?(от 1 до {n}): "))
        while count_user < 1 or count_user > n:
            count_user = int(input(f"Вы ошиблись, попробуйте заново\nСколько Вы хотите взять конфет?(от 1 до {n}): "))
    
    n = n - count_user
    print(f'Вы взяли: {count_user}\nОсталось {n} конфет')
    result = check_win(j, n)
    if result:
        print(result)
        exit()
    j = 1
    count_bot = n % 29 # 0 - бот проиграл
    if count_bot == 0:
        count_bot = 1
    n = n - count_bot
    print(f'Бот взял: {count_bot}\nОсталось {n} конфет')
    result = check_win(j, n)
    j = 0
    if result:
        print(result)
        exit()
 """