from exif import Image
import shutil
import os
import time

start_time = time.time()

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

source = 'images/'

for filename in os.listdir(source):
    f = os.path.join(source, filename)

    if os.path.isfile(f):
        file_names = f.replace('images/', '')

        try:
            with open(f, 'rb') as image_file:
                my_image = Image(image_file)

                date_time = my_image.datetime
                file_month = date_time[5:7]

                move_to = dirs.get(file_month)
        except:
            print(f"This image {filename} doesn't have 'datetime' in exif.")
            print("Move this file manually")
        finally:
            if move_to:
                shutil.copy(f, move_to)
                print(f"Files successfully transferred {filename} from {source} to {move_to}")
                os.remove(f)


end_time = time.time()

elapsed_time = end_time - start_time

print(f'Code got executed in {elapsed_time} seconds.')