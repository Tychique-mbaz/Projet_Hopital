
from fastapi import UploadFile
import pathlib, shutil
import shortuuid
import os

class UploadFileHandler:

    def __init__(self, base_path: str):

        try:
            self.base_path = pathlib.Path(base_path)
            self.base_path.mkdir(parents=True)
        except FileExistsError:
            pass


    def remove(self, row):
        
        try :
            pathlib.Path(row.chemin_fichier).unlink(True)
        except AttributeError :
            pass

    
    def save(self, upload_file: UploadFile | None, old_path: str='') -> str:

        if old_path != '' :
            pathlib.Path(old_path).unlink(True)

        filename = shortuuid.ShortUUID().random(10)

        if upload_file != None:
            print(upload_file.content_type)
            extension = upload_file.content_type.split('/')[1]
            path = f'{self.base_path}{os.path.sep}{filename}.{extension}'
            with open(path, 'wb') as local_file :
                shutil.copyfileobj(upload_file.file, local_file)
        else : 
            extension = 'png'
            path = f'{self.base_path}{os.path.sep}{filename}.{extension}'
            shutil.copy(f'static{os.path.sep}default_profile.png', path)
        return path

