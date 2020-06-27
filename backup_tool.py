import os
import time
import zipfile

while True:

    source = input('Введите сохраняемую дирректорию (по умолчанию рабочая дирректория):\n')
    if len(source) == 0:
        source = "C:\\My Documents"
    elif not os.access(source, os.F_OK):
        print('Ошибка: убедитесь в правильности адресса')
        source = "C:\\My Documents"

    target_dir = input('Введите дирректорию бекапа (по умолчанию D:\\backup):\n')
    if len(target_dir) == 0:
        target_dir = 'D:\\backup'
    elif not os.access(target_dir, os.F_OK):
        target_dir = 'D:\\backup'
        print('Ошибка: убедитесь в правильности адресса')
 
    now = '{}_{}'.format(time.strftime('%Y%m%d'), time.strftime('%H%M%S'))
    full_target = target_dir + os.sep + now + '.zip'
    print(full_target)


    z = zipfile.ZipFile(full_target, 'w')
    for root, dirs, files in os.walk(source):
        for file in files:
            z.write(os.path.join(root,file))
        for dir in dirs:
            z.write(os.path.join(root,dir))
    z.close()
 
    logic = input('Сохранить еще файлы?\nда \\ не: ')
    if logic == 'не':
        break
