import os

from config import PATH_ROOT

from functions import verify_folder, verify_name

# path  = "{}/pruebas".format(PATH_ROOT)
folder = "C:/dev/Apps/binder-reformer/pruebas/0000-CURSO DE PYTHON/Unidad 3"
# def verify_folder(folder):
#     dirs=[]

#     separator = f"{chr(92)}"  # \

#     for file in os.listdir(folder):
#         absolute_path = os.path.join(folder, file)
#         print(absolute_path)
#         if os.path.isdir(absolute_path):
#             folder_name = absolute_path.split(f"{separator}")[-1]
#             dirs.append(folder_name)
    
#     return dirs

print(verify_folder(folder))