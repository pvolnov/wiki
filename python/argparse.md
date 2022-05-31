```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--proxy", default=None, dest="proxy",
                    help="Proxy for run selenium and creating reauests in format: socks5://login:pass@ip:port",
                    type=str)
parser.add_argument("--server", default="dig7.neafiol.site", dest="selenoid_ip",
                    help="Proxy for run selenium and creating reauests in format: socks5://login:pass@ip:port",
                    type=str)

args = parser.parse_args()
proxy = args.proxy
```

* **Action** 
    - `store` - просто сохраняет значение аргумента. Это действие по умолчанию: `-f 121 > 121`
    - `store_const` - сохраняет значение, указанное ключевым аргументом const. Действие store_const чаще всего используется с необязательными параметрами, указывающими какой-то флаг: `-f > "const_val"`
    - `store_true` и `store_false` - это особые случаи, когда store_const используется для хранения значений True и False соответственно. Кроме того, они создают значения по умолчанию False и True соответственно. `-f > True` 
    - `append` - сохраняет список и добавляет в него значение каждого параметра командной строки. Это полезно, когда параметр указывается несколько раз: `--foo 1 --foo 2 > [1, 2]`
    - `count` - подсчитывает, сколько раз встречается какой то параметр в командной строке. Например, это полезно для повышения уровня детализации `-vvv > 3`
    - `extend` - сохраняет список и расширяет значение каждого параметра командной строки до списка: `--foo f1 --foo f2 f3 f4 > ['f1', 'f2', 'f3', 'f4']`
    
* **nargs** - количество параметров командной строки, которые следует использовать,
* **const** - постоянное значение, требуемое некоторыми action и nargs,
* **default** - значение, полученное, если опция отсутствует в командной строке,
* **type** - тип, в который должен быть преобразован параметр/опция командной строки,
* **choices** - контейнер допустимых значений для параметра/опции,
* **required** - можно ли опустить параметр командной строки (только для опций),
* **help** - краткое описание того, что делает параметр/опция,
* **metavar** - имя параметра/опции в сообщениях об использовании,
* **dest** - имя параметра/опции, которое будет добавлено к объекту.



[Документация](https://docs-python.ru/standart-library/modul-argparse-python/metod-add-argument-obekta-argumentparser/)