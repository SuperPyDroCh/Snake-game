# Импортирую все необходимые библиотеки
import keyboard as key
import random
import time
from time import sleep
from sys import exit
import pyfiglet

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
        index = listt.index('@')

        # UP
        if direction == 'UP':
            step = -42
            if listt[index + step] == ' ':
                listt[index] = ' '
                listt[index + step] = '@'
            elif listt[index + step] == '#':
                clear()
                print(pyfiglet.figlet_format('You win!'))
                exit()

        # DOWN
        if direction == 'DOWN':
            step = 42
            if listt[index + step] == ' ':
                listt[index] = ' '
                listt[index + step] = '@'
            elif listt[index + step] == '#':
                clear()
                print(pyfiglet.figlet_format('You win!'))
                exit()

        # RIGHT
        if direction == 'RIGHT':
            step = 2
            if listt[index + step] == ' ':
                listt[index] = ' '
                listt[index + step] = '@'
            elif listt[index + step] == '#':
                clear()
                print(pyfiglet.figlet_format('You win!'))
                exit()

        # LEFT
        if direction == 'LEFT':
            step = -2
            if listt[index + step] == ' ':
                listt[index] = ' '
                listt[index + step] = '@'
            elif listt[index + step] == '#':
                clear()
                print(pyfiglet.figlet_format('You win!'))
                exit()
    except ValueError:
        clear()
        printt('Ошибка')
    except Exception as e:
        printt(f'Ошибка: {e}')
    clear()
    printt(game_field_list)

# Движение змейки x2
def move(direction, steps):
    for i in range(steps):
        sleep(0.1)
        move_the_snake(direction)

# Первое появление змейки
game_field_list = list(game_field)
game_field_list[43] = '@'
printt(game_field_list)

# Тестовая часть
move('DOWN', 1)
move('RIGHT', 19)
move('UP', 1)
move('LEFT', 19)

# Распознавание нажатия клавиш



# Окончание замера времени
end_time = time.time()
print(f"Всего {end_time - start_time:.2f}!")