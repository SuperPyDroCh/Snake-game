# Импортирую все необходимые библиотеки:
import keyboard as key
import time
from time import sleep
from sys import exit
import pyfiglet
# В том числе и функции из func.py:
from func import clear, printt, set_a_game_field



# Начало замера времени
start_time = time.time()


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
                end_time = time.time()
                print(f"Всего {end_time - start_time:.2f}!")
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
                end_time = time.time()
                print(f"Всего {end_time - start_time:.2f}!")
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
                end_time = time.time()
                print(f"Всего {end_time - start_time:.2f}!")
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
                end_time = time.time()
                print(f"Всего {end_time - start_time:.2f}!")
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
while True:
    move('DOWN', 1)
    move('RIGHT', 19)
    move('DOWN', 1)
    move('LEFT', 19)

# Распознавание нажатия клавиш

