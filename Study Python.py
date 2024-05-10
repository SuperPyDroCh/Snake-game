# Импортирую все необходимые библиотеки
import keyboard
import random
import time
from time import sleep

# Начало замера времени
start_time = time.time()

# Функция для мнимой отчистки экрана:
def clear():
    printt('\n' * 100)

# Функция для вывода списка в виде строки:
def printt(text):
    for el in text:
        print(el, end='')

# Функция для создания нового игрового поля:
def set_a_game_field():
    try:
        string_numb = random.randint(0, 9)
        before_before_the_apple = string_numb * ('|' + 39 * ' ' + '|' + '\n')
        before_the_apple = random.randrange(0, 40, 2)
        after_the_apple = '#' + (' ' * (38 - before_the_apple) + '|' + '\n')
        before_the_apple = '|' + ' ' * before_the_apple
        after_after_the_apple = (9 - string_numb) * ('|' + 39 * ' ' + '|' + '\n')
        result = (('_' * 41) + '\n') + before_before_the_apple + (before_the_apple + after_the_apple) + after_after_the_apple + (('‾' * 41) + '\n')
        return result
    except Exception as e:
        printt(f'Ошибка: {e}')

# Глобальная переменная для хранения игрового поля
global game_field_list
game_field = set_a_game_field()

# Движение змейки
def move_the_snake(direction):
    try:
        global game_field_list
        listt = game_field_list
        global game_field
        index = listt.index('@')

        # UP
        if direction == 'UP':
            if listt[index - 42] == ' ':
                listt[index] = ' '
                listt[index - 42] = '@'

        # DOWN
        if direction == 'DOWN':
            if listt[index + 42] == ' ':
                listt[index] = ' '
                listt[index + 42] = '@'

        # RIGHT
        if direction == 'RIGHT':
            if listt[index + 2] == ' ':
                listt[index] = ' '
                listt[index + 2] = '@'
        # LEFT
        if direction == 'LEFT':
            if listt[index - 2] == ' ':
                listt[index] = ' '
                listt[index - 2] = '@'
    except ValueError:
        clear()
        printt('Ошибка')
    except Exception as e:
        printt(f'Ошибка: {e}')
    clear()
    printt(game_field_list)

# Первое появление змейки
game_field_list = list(game_field)
game_field_list[43] = '@'
printt(game_field_list)

# Тестовая часть
move_the_snake("UP")
sleep(0.3)
move_the_snake("DOWN")
while game_field_list[(game_field_list.index('@')) + 2] == ' ':
    sleep(0.1)
    move_the_snake('RIGHT')
sleep(0.3)
move_the_snake('DOWN')
sleep(0.3)
while game_field_list[(game_field_list.index('@')) - 2] == ' ':
    sleep(0.1)
    move_the_snake('LEFT')


# Окончание замера времени
end_time = time.time()
print(f"Всего {end_time - start_time:.2f}!")