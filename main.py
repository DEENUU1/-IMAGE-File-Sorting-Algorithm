import shutil
import os
import time
from exif import Image



# This dict represent paths for all months
dirs = {
    '12': 'images/12/',
    '11': 'images/11/',
    '01': 'images/1/',
    '02': 'images/2/',
    '03': 'images/3/',
    '04': 'images/4/',
    '05': 'images/5/',
    '06': 'images/6/',
    '07': 'images/7/',
    '08': 'images/8/',
    '09': 'images/9/',
    '10': 'images/10/',
}

# This path represent folder with all images
source = 'images/'

# Algorithm start with iterate through all files in source folder
def sorting_algorithm(dirs:dict, source:str):

    # This is used for returning program speed
    start_time = time.time()

    for filename in os.listdir(source):
        f = os.path.join(source, filename)

        if os.path.isfile(f):
            file_names = f.replace('images/', '')

            move_to = None

            try:
                with open(f, 'rb') as image_file:
                    my_image = Image(image_file)
                    #This code allows to get month from image
                    date_time = my_image.datetime
                    file_month = date_time[5:7]
                    move_to = dirs.get(file_month)
            # If image doesn't have datetime field program catch exception and continue
            except:
                print(f"This image {filename} doesn't have 'datetime' in exif.")
                print("Move this file manually")
            finally:
                # If image has datetime field is transferred to the appropriate folder as a copy
                # Then program removes image from main folder
                # If the photo has not been moved, it will not be deleted
                if move_to:
                    shutil.copy(f, move_to)
                    print(f"Files successfully transferred {filename} from {source} to {move_to}")
                    os.remove(f)

    # After all program returns the time of the whole process
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Code got executed in {elapsed_time} seconds.')

sorting_algorithm(dirs,source)