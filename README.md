thrip  
# Инструкция по установке:  
Склонируй репозиторий к себе  
`git clone https://github.com/wex335/thrip.git`  
Перейди в папку с файлами:  
`cd thrip`  
Установи ниобходимые для работы библиотеки:  
`sudo apt-get install python3-tk`  
`pip3 install pytk`  
Теперь можно запускать:
`python3 realise.py`  
  
Запустятся настройки по умолчанию  

# Инструкция по настройке: 
Пока что все настройки лежат в файле с программой.  
Открываем его через блокнот или любой другой редактор текста
![Settings image](https://sun1-16.userapi.com/impg/RWeE_yjwa-f3hdmVHTRyk5kQVObEfboKRboWBA/aTfOYvm-UIM.jpg?size=672x204&quality=96&sign=94b22bf2883a65429be00400554bbb05&type=album)  

Обо всем попорядку

# p = [0,0,0]

Это инициализация местоположения точек до каких-либо действий. 0 - верхняя точка в окружности. Далее - по часовой стрелке. `p` содержит в себе инициализацию для всех трёх точек  

# width = 700

Этот код указывает на шырину окна, Высота не указывается, т. к. окно квадратное. Также указывает рзмер круга

# cunt =1000 

Эта переменная обозначает кол-во точек, из которых состоит круг. По сути круг - это многоугольник

# evry = 3

Это значение обозначает, какую каждую точку необходимо отрисовывать. Полезно, допустим, когда надо сделать часы, чтоб они шли плавно, а полного круга не было

# speed = (3,2,1)

Этот картеж указывает скорость для точек, так же как и `p` местоположение. 

# delay = 0.02

Это значение - это кол-во секунд, которое нужно ждать программе перед тем, как сдвинуть точки на `speed` точек по часовой стрелке

# arrowcolor = 'red'    
# circlecolor = 'black' 
# onintreecolor = 'blue'

Эти три строки указывают цвет для линий, точек и линий в случае нахождения центра окружности между ними соответственно
