# utf-8

import os
from config import STRUCT_FILE, STRUCT_FOLDER, PATH_ROOT

def verify_folder(folder):
    dirs=[]

    separator = f"{chr(92)}"  # \

    for file in os.listdir(folder):
        absolute_path = os.path.join(folder, file)

        if os.path.isdir(absolute_path):
            folder_name = absolute_path.split(f"{separator}")[-1]
            dirs.append(folder_name)
    
    return dirs


def verify_name(param, ext = None):
    
    long_param =  param.split("-") if not ext else param.split(" ")
    long_struct = STRUCT_FOLDER.split("-") if not ext else STRUCT_FILE.split(" ")

    try: 

        if len(long_param) == len(long_struct):
            print(f"{long_param} --- {long_struct}")
            print(f"{len(long_param)} --- {len(long_struct)}")
            
            if not ext: 
                int(cod)
                cod = long_param[0]
                ready = True if long_param[2].lower() == 'Listo'.lower() else False
                if len(cod) == len(long_struct[0]) and ready:
                    return True
            else:
                return True
        return False

    except ValueError as e:
        print("You have a error in the name structure of your folder ", e)
        return False
    