# Импортирую все необходимые библиотеки:
from pynput import keyboard
from time import sleep
from sys import exit
import pyfiglet
# В том числе и функции из func.py:
from func import clear, printt, set_a_game_field




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
def show():
    global game_field_list
    game_field_list = list(game_field)
    game_field_list[43] = '@'
    printt(game_field_list)

def bot1():
    global game_field_list
    # Не оптимизировано:
    while True:
        move('RIGHT', 19)
        move('DOWN', 1)
        move('LEFT', 19)
        move('DOWN', 1)

def bot2():
    global game_field_list
    # Оптимизировано:
    apple = game_field_list.index('#')
    apple1 = apple // 42 - 1
    if apple1 > 0:
        move('DOWN', apple1)
    move('RIGHT', 19)
    print(apple, apple1)

def userkeyboard():
    global game_field_list
    # Распознавание нажатия клавиш
    def on_press(key):
        try:
            # Обработка нажатия клавиши
            if key == keyboard.Key.down:
                move_the_snake('DOWN')
            elif key == keyboard.Key.right:
                move_the_snake('RIGHT')
            elif key == keyboard.Key.up:
                move_the_snake('UP')
            elif key == keyboard.Key.left:
                move_the_snake('LEFT')
        except AttributeError:
            clear()

    # Создание слушателя события
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # Запуск слушателя
    listener.join()  # Удержание основного потока



