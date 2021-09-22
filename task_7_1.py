import os
lst_folders = {"settings", "mainapp", "adminapp", "authapp"}
dir_path = os.path.join('my_project')
try:
    os.mkdir(dir_path)
    for new_folder in lst_folders:
        path_new = os.path.join(dir_path, new_folder)
        os.makedirs(path_new)
except OSError:
    for new_folder in lst_folders:
        path_new = os.path.join(dir_path, new_folder)
        if not os.path.exists(path_new):
            os.makedirs(path_new)
