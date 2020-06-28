import os
import time
import zipfile

while True:

    # просим ввести дирректорию
    while True:
        source = input('Введите сохраняемую дирректорию (по умолчанию рабочая дирректория):\n')
        if len(source) == 0:    # если пользователь ничего не ввел, то беруться значения по умолчанию
            source = "C:\\My Documents"
            break
        elif not os.access(source, os.F_OK):    # если дирректория не правильнаю, то проосим ввести еще раз
            print('Ошибка: убедитесь в правильности адресса')
        else:   # если все верно, то значение сохраняются
            break

    # тоже самое
    while True:
        target_dir = input('Введите дирректорию бекапа (по умолчанию D:\\backup):\n')
        if len(target_dir) == 0:
            target_dir = 'D:\\backup'
            break
        elif not os.access(target_dir, os.F_OK):
            print('Ошибка: убедитесь в правильности адресса')
        else:
            break

    now = '{}_{}'.format(time.strftime('%Y%m%d'), time.strftime('%H%M%S'))
    full_target = target_dir + os.sep + now + '.zip'
    print(full_target)

    z = zipfile.ZipFile(full_target, 'w')   # создаем архив
    for root, dirs, files in os.walk(source):   # выводим список файлов и папок сохраняемой папки
        for file in files:
            z.write(os.path.join(root,file))    # сохраняем файлы
        for dir in dirs:
            z.write(os.path.join(root,dir))     # сохраняем папки
    z.close()   # закрываем архив
 
    logic = input('Сохранить еще файлы?\nда \\ не: ')
    if logic == 'не':
        break
