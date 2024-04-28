# Radars

# Описание
Решение задачи для хакатона Phystech Radar Tech Challange.  
Программа реализует алгоритм решения задачи целочисленного программирования (более точно, maximum weight clique problem).  
Алгоритм использует симплекс-метод + метод ветвей и границ для поиска k = 5 лучших решений задачи.  

## Инструкция по запуску для всех пользователей
Основное решение находится в файле K_BLP.py  
Входные данные для скрипта передаются аргументом в формате csv.  
В файле должна быть указана матрица смежности графа (матрица верхнетреугольная, строки матрицы указаны через перенос строки) и веса вершин (последней строчкой файла).  
  
запуск скрипта из командной строки имя файла аргументом:
```shell
python K_BLP.py input_with_weights.csv
```

Пример входных данных: input.csv
```
0,0,1,1
0,0,1,0
0,0,0,0
0,0,0,0
1.2456,2.1242,0.2345,1.0233
```

## Инструкция по запуску для пользователей linux
Разархивируйте папку linux. Основной файл K_BLP.cc. Для компиляции необходимо ввести следующую команду (заменив пути на ваши) 
```bash
g++ -g K_BLP.cc -o K_BLP_linux -I/home/path/or-tools_x86_64_Ubuntu-22.04_cpp_v9.9.3963/include -L/home/path/or-tools_x86_64_Ubuntu-22.04_cpp_v9.9.3963/lib -lortools -labsl_strings -labsl_synchronization -lpthread -ldl
```

После это ввести аргументами имя файла и число наилучших оптимальных решений
```bash
./K_BLP_linux input_with_weights.csv 5
```

## Решение 

Найденное решение для данного файла input_with_weights.csv

Solution 1:
Objective value = 93.5302

1 0 0 1 1 1 0 0 0 1 1 1 1 1 0 0 1 0 1 1 0 1 1 0 1 1 1 1 

Solution 2:
Objective value = 93.4908

1 0 0 1 1 1 0 0 0 0 1 1 1 1 0 0 1 0 1 1 0 1 1 0 1 1 1 1 

Solution 3:
Objective value = 92.9703

1 0 0 1 1 1 0 0 0 1 1 1 1 1 0 0 1 0 1 1 0 1 1 0 1 1 1 0 

Solution 4:
Objective value = 92.9309

1 0 0 1 1 1 0 0 0 0 1 1 1 1 0 0 1 0 1 1 0 1 1 0 1 1 1 0 

Solution 5:
Objective value = 92.8271

1 0 0 1 1 1 0 0 0 1 1 1 0 1 0 0 1 0 1 1 0 1 1 0 1 1 1 1

## Время (без учета подключения библотек)

K_BPL на python с ortools --- 32мс

K_BPL на python с pulp --- 0.3с

K_BPL на c++ с ortools --- 12мс
