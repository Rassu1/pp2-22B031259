"""
Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
Проверить существование, читаемость, возможность записи и исполняемость указанного пути
На запись и выполнение заданного пути - это означает, что программа проверяет, имеет ли пользователь права на запись и выполнение файлов в указанном пути.

"Запись" относится к тому, может ли пользователь записывать новые файлы или изменять существующие файлы в данном каталоге.

"Выполнение" относится к тому, может ли пользователь запускать (выполнять) файлы, находящиеся в данном каталоге как исполняемые файлы. Если файл является исполняемым, то пользователь может запустить его в терминале или в командной строке, набрав имя файла.
"""
import os

path = 'C:\\Users\\User\\PycharmProjects\\pythonProject\\TSIS_5\\RegEx\\rows.txt'
print('Exist:', os.access(path, os.F_OK))
print('Readable:', os.access(path, os.R_OK))
print('Writable:', os.access(path, os.W_OK))
print('Executable:', os.access(path, os.X_OK))