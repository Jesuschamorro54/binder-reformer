
import os
from functions import verify_folder, verify_name
from config import PATH_ROOT
import os


folder = "{}/pruebas".format(PATH_ROOT)
name = 'CLASE 1.1 (CLASS NAME)'

print("Lista de Carpetas: ", verify_folder(folder))

print("\nNombre del curso: ", verify_name(name, '.mp4'))
