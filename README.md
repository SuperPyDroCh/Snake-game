# __САМ КОД НАХОДИТСЯ В ВЕТВИ "master"__

## Snake-game
В этом репозитории я попытаюсь воссоздать классическую игру "Змейка" на Python. 

### Введение 
Я считаю что есть множество способов написать эту простую игру на Python. Лично я выбрал такой путь:
### __Подробное описание кода__
1. Первым шагом я импортирую библиотеки, которые понадобятся для выполнения дальнейшего кода.
2. Далее я создаю простую функцию для "мнимой очистки экрана". Теперь при описании в код функции clear() в терминал выводится сотня пустых строк, что создаёт ощущение очистки терминала полностью.
3. В этом блоке я создаю функцию, при вызове которой она принимает как значение строку, содержащую ограниченное спец. символами игровое поле. __При этом в игровом поле всегда содержится яблоко, обозначенное символом #, и оно всегда расположено по-разному.__
4. В этом блоке я создаю глобальную переменную и записываю в нее игровое поле.
5. В этом блоке я добавляю в левый нижний угол игрового поля змейку, представленную в виде символа "собака"(@). Также Я вывожу это игровое поле в терминал.
6. Это самый большой и трудоемкий блок кода. Я создаю функцию, которая почти полностью отвечает за передвижение змейки по полю.