# Пока я добавил функцию для движения змейки только вперед и назад.

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

# Глобальная переменная для хранения игрового поля
global game_field
game_field = set_a_game_field()

# Первое появление змейки
game_field1 = list(game_field)
game_field1[44] = '@'
game_field1 = ''.join(game_field1)
print(game_field1)

# Движение змейки
def move_the_snake(direction):
    global game_field
    if direction == 'down':
        game_field1 = list(game_field)
        # Проверка на наличие препятствий
        if game_field1[44 + 43] == '‾':
            clear()
            print('Game over!')
        elif game_field1[44 + 43] == '_':
            clear()
            print('Game over!')
        elif game_field1[44 + 43] == '|':
            clear()
            print('Game over!')
        else:
            game_field1[44 + 43] = '@'
            game_field1 = ''.join(game_field1)
            print(game_field1)
    elif direction == 'up':
        game_field1 = list(game_field)
        # Проверка на наличие препятствий
        if game_field1[44 - 43] == '‾':
            clear()
            print('Game over!')
        elif game_field1[44 - 43] == '_':
            clear()
            print('Game over!')
        elif game_field1[44 - 43] == '|':
            clear()
            print('Game over!')
        else:
            game_field1[44 - 43] = '@'
            game_field1 = ''.join(game_field1)
            print(game_field1)

sleep(1)
move_the_snake("down")
move_the_snake("up")