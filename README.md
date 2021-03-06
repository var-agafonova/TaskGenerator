# TaskGenerator

Программа реализует работу генератора условий заданий по программированию на языке `Pascal` и прототипов решений этих задач.

Для запуска программы необходимо выполнить команду:

```
$ python main_gen.py 
```

* Модуль `io_gen` реализует интервейс программы.  
* Модули `lgraph` (и node вспомогательный к нему) описывает класс l-графа, используемый в основной программе.  
* Модули `express_task`, `cond_tasks` и `cycle_tasks` описывают классы различных типов задач по программированию.  
* Модуль main_gen является связующим звеном между интерфейсом и функционалом программы.  

При запуске программы открывается пользовательское окно с интуитивно понятным интерфейсом для работы с программой.

Система позволяет генерировать задания в двух режимах: случайное задание или задание конкретного типа (по нажатию на разные кнопки).
