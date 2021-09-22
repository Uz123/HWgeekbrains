import os
import shutil

root_folder = 'my_project'
tem_folder = 'templates'
for root, dirs, files in os.walk(root_folder):
    if tem_folder in dirs and root != root_folder:
        for fl in os.listdir(os.path.join(root, tem_folder)):
            shutil.copytree(os.path.join(root, tem_folder, fl),
                            os.path.join(root_folder, tem_folder, fl))
