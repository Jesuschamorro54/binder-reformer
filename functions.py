# utf-8

import os
from config import STRUCT_FILE, STRUCT_FOLDER, PATH_ROOT

def verify_folder(folder):
    dirs=[]

    separator = f"{chr(92)}"  # \

    for file in os.listdir(folder):
        absolute_path = os.path.join(folder, file)

        if not os.path.isdir(absolute_path):
            # folder_name = absolute_path.split(f"{separator}")[-1]
            # dirs.append(folder_name)
            return False
        else:
            pass
            
    return True


def verify_name(param, ext = None):
    
    array_param =  param.split("-") if not ext else get_array_name(param)
    array_struct = STRUCT_FOLDER.split("-") if not ext else get_array_name(STRUCT_FILE)

    try: 
        if len(array_param) == len(array_struct):
            if not ext: 
                cod = array_param[0]
                int(cod)
                ready = True if array_param[2].lower() == 'Listo'.lower() else False
                if len(cod) == len(array_struct[0]) and ready:
                    return True
            else:
                if len(array_param) == len(array_struct):
                    return True
        return False

    except ValueError as e:
        print("You have a error in the name structure of your folder or file", e)
        return False

def get_array_name(param):
    name = [] 
    array = param.split(" ")
    arrcl = array[2:]
       
    if '(' in arrcl[0] and ')' in arrcl[-1]:
        name = [array[0], array[1], ' '.join(arrcl)]
        return name
    return None