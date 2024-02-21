import os
import shutil

path = "test.txt"

try:
     os.remove(path)                     # FileNotFoundError: Damit möglich, einzelne Datein zu löschen   
    # os.rmdir(path)                      # PermissionError: Damit möglich, leere Ordner zu löschen     
    # shutil.rmtee(path)                  # OSError: Damit möglich, Ordner die Datein beinhalten zu löschen
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have a permission to delete that")
except OSError:
    print("You can not delete that usng that function")
else: 
    print(path+" was deleted")