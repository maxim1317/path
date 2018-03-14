# Поиск кратчайшего маршрута с обходом препятствий

## Алгоритм

1. По заданным параметрам (сторона квадрата, отступ от начала координат) произвольным образом _генерируются_ точки, они же - _окружности_
2. Строятся все возможные, не пересекающие другие окружности и границы, _касательные_ к и между окружностями
3. У каждой окружности точки касания соединяются _дугами_
4. Из дуг, касательных и их длин составляется _взвешенный граф_
5. С помощью _алгоритма Дейкстры_ ищется кратчайший маршрут
6. Происходит отрисовка сцены

## Подробности реализации

Прога написана на _Python 3.6.4_ с использованием _pygame_ для отрисовки и _NetworkX_ для работы с графами (да, я поленился писать свой велосипед). 

Почему Питон? - я никогда на нем особо не писал, а тут подвернулась возможность потыкать

## Что готово

В принципе, программа работает для большинства случаев. Я бы сказал, точнее, что написана основа программы. Визуализация тоже, по большей части, готова. Сейчас, попробую картинку впихнуть

...

о, готово

![alt text](png/fig.png)

## Чего нет

- Основные проблемы у меня с _дугами_ - я не дописал функцию проверки _пересечения с границами_ квадрата. И они пока _отображаются отрезками_
- У меня нет проверки на _отсутствие решений_ - программа просто вываливается с ошибкой, хотя это не долго поправить
- Пока _точки задаются_ только _рандомом_
- Да и вообще, пока у программы _нулевая интерактивность_ - все _параметры_ вводятся _через код_ программы. _Отображение_ касательных тоже _выключается комментированием_ сооответсвующих строк.

## Как запустить

### Понадобится

- Python 3
- Pygame
- NetworkX
- NumPy

Опционально:

- nxpd (для отрисовки графа картинкой)
- colored_traceback (разукрашенный вывод ошибок, а то скучно)

Полная версия в [requirements.txt](requirements.txt)

### Запуск

Если у вас _Linux_, то, в принципе, после установки зависимостей командой
```
pip3 install <requirement>
```
можно запустить программу командой `make`. По крайней мере, у меня работает.

Если у вас _не Linux_, то тут я должен признаться, что мне лень проверять работу на других системах, но, если надо, я попробую что-то с этим сделать.

## Что где

- __src/__
    + [main.py](src/main.py) - тут происходит _отрисовка_, _вызов функций_ и тут _задаются параметры_
    + [generator.py](src/generator.py) - тут _генерируются координаты точек_
    + [classes.py](src/classes.py) - тут описание _классов_
    + [calculations.py](src/calculations.py) - тут всякие побочные _вычисления _типа _расстояний_ и проверок на _пересечения_
    + [tangent.py](src/tangent.py) - тут ищутся _касательные_
    + [graph.py](src/graph.py) - тут просто из кусочков сращивается _граф_

- __png/__
    + [fig.png](png/fig.png) - это просто _картинка_ из данного Readme

- __gens/__
    + gens/circlelist.gen - этот файлик появляется и обновляется при каждом запуске, сюда складываются _координаты точек_. Просто почитать.