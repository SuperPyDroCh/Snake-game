# Пока я добавил функцию для движения змейки только вверх и вниз.

# Импортирую все необходимые библиотеки
import keyboard
from time import sleep
import random

# Функция для мнимой отчистки экрана:
def clear():
    print('\n' * 100)

# Функция для создания нового игрового поля:
def set_a_game_field():
    try:
        string_numb = random.randint(0, 9)
        before_before_the_apple = string_numb * ('|' + 40 * ' ' + '|' + '\n')
        before_the_apple = random.randint(0, 39)
        after_the_apple = '#' + (' ' * (39 - before_the_apple) + '|' + '\n')
        before_the_apple = '|' + ' ' * before_the_apple
        after_after_the_apple = (9 - string_numb) * ('|' + 40 * ' ' + '|' + '\n')
        result = (('_' * 42) + '\n') + before_before_the_apple + (before_the_apple + after_the_apple) + after_after_the_apple + (('‾' * 42) + '\n')
        return result
    except Exception as e:
        print(f'Ошибка: {e}')

# Глобальные переменные для хранения игрового поля
global game_field_list
global game_field
game_field = set_a_game_field()

# Первое появление змейки
game_field_list = list(game_field)
game_field_list[44] = '@'
game_field2 = ''.join(game_field_list)
print(game_field2)

# Движение змейки
def move_the_snake(direction):
    try:
        global game_field_list
        listt = game_field_list
        global game_field
        index = listt.index('@')
        if direction == 'up':
            if listt[index - 43] == ' ':
                listt[index] = ' '
                listt[index - 43] = '@'
        game_fieldd = ''.join(listt)
    except ValueError:
        clear()
        print('Ошибка')
    except Exception as e:
        print(e)
    clear()
    print(game_fieldd)


sleep(1)
move_the_snake("up")