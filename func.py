import random

# Функция для вывода списка в виде строки:
def printt(text):
    for el in text:
        print(el, end='')

# Функция для мнимой отчистки экрана:
def clear():
    printt('\n' * 100)

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