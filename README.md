# __САМ КОД НАХОДИТСЯ В ВЕТВИ *master*!!!__
Если что-то не понравится - читаем описание профиля.
___
## Snake-game
В этом репозитории я попытаюсь воссоздать классическую игру "Змейка" на Python. 
___
### Введение:
Я считаю что есть множество способов написать эту простую игру на Python. В основном, конечно, отличия не привысят смены последовательности, но в обработке движения змеи можно поступить по-разному. Лично я выбрал такой путь:
### __Подробное описание кода:__
1. Первым шагом я импортирую библиотеки, которые понадобятся для выполнения дальнейшего кода.
2. Далее я создаю простую функцию для "мнимой очистки экрана". Теперь при описании в код функции clear() в терминал выводится сотня пустых строк, что создаёт ощущение очистки терминала полностью.
3. В этом блоке я создаю функцию, при вызове которой она принимает как значение строку, содержащую ограниченное спец. символами игровое поле. __При этом в игровом поле всегда содержится яблоко, обозначенное символом #, и оно всегда расположено по-разному.__
4. В этом блоке я создаю глобальную переменную и записываю в нее игровое поле.
5. В этом блоке я добавляю в левый нижний угол игрового поля змейку, представленную в виде символа "собака"(@). Также я вывожу это игровое поле в терминал.
6. Это самый большой и трудоемкий блок кода. Я создаю функцию, которая почти полностью отвечает за передвижение змейки по полю. В эту огромную функцию я решил сразу включить обработку и движения и действий при попадании змеи на стенку или яблока. По-моему это вряд-ли является самым оптимальным путем, но таков мой путь.


___

> # ___Things to do:___
> * [X] *Составить функцию для создания игрового поля и яблока. Учесть, что яблоко должно иметь разное расположение при каждой генерации.*
> * [X] *Вывести на терминал игровое поле и создать необходимые в дальнейшем переменные.*
> * [ ] *Создать функцию для обработки всех движений змейки.*
> * [ ] *Обработать нажатие клавиш и дописать остальные мелкие элементы, необходимые для полноценной игры.*
> * [ ] *Решить, хватит ли моему проекту такого функционала, или мне придется реализовывать постоянное движение змейки с определенной скоростью.*