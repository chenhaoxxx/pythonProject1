"""sort files in FilesToSort- 1"""

import os
import shutil
FOLDER_TO_SORT = 'FilesToSort'


def main():
    os.chdir('..')
    os.chdir(FOLDER_TO_SORT)
    files_to_sort = [f for f in os.listdir('.') if os.path.isfile(f)]  # ignores folders
    for filename in files_to_sort:
        file_extension = filename.split('.')[-1]
        try:
            os.mkdir(file_extension)
        except FileExistsError:
            pass
        print("{}/{}".format(file_extension, filename))
        shutil.move(filename, file_extension + '/' + filename)


main()