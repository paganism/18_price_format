# Форматирование цены

Скрипт форматирует цену для более наглядного отображения. Например, цену 259,500000 преобразует в 259.50


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python3.5 format_price.py --price 259,500000

259.50

```

Для использования в другом проекте необходимо:


```bash

from format_price import format_price

print(format_price(price))

```



# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
