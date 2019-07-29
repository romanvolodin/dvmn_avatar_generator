## EN: Avatar generator

The script takes an image and generates an avatar - adds a filter, resizes and saves with new name.

### How to run
Python 3.5 and Pillow library are required to run the script. Use the following command to install all requirements:
```bash
$ pip install -r requirements.txt
```
Now you can generate an avatar. Run the following command in the terminal:
```bash
$ python avatar_generator.py input_image.jpg --size 250x250 output_image.png
```
No output means that the avatar has been successfully generated.

### Project goal
The code is written for educational purposes. Training course for web-developers - [Devman](https://dvmn.org).

## RU: Генератор аватарок
Скрипт берет картинку и делает из неё аватарку - накладывает фильтр, ресайзит и сохраняет под новым именем.

### Запуск скрипта
Чтобы запустить скрипт нужен Python 3.5 и библиотека Pillow. Установить нужные зависимости можно следующей командой:
```bash
$ pip install -r requirements.txt
```
Теперь можно создать аватарку. Выполните следующую команду в терминале:
```bash
$ python avatar_generator.py input_image.jpg --size 250x250 output_image.png
```
В случае успешного выполнения скрипт ничего не выводит.

### Цель проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке [Devman](https://dvmn.org).
