"""
Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
"""
import os

file_path = "C:\\Users\User\\PycharmProjects\\pythonProject\\TSIS_6\\Directories and files\\to_delete.txt"

if os.path.exists(file_path):
    if os.path.isfile(file_path):
        if os.access(file_path, os.R_OK):
            os.remove(file_path)
            print(f"Файл {file_path} успешно удален")
        else:
            print(f"Ошибка доступа к файлу {file_path}")
    else:
        print(f"{file_path} не является обычным файлом")
else:
    print(f"{file_path} не существует")