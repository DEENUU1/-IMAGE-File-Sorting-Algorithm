from exif import Image
import shutil

source = 'images/'
move_to = 'images/11/'
month = []

with open(source + 'IMG_7274.JPG', 'rb') as image_file:
    my_image = Image(image_file)

if my_image.has_exif == True:
    date_time = my_image.datetime
    for x in date_time:
        month.append(x)
    y = ''.join(month)
    file_month = y[5:7]

    if file_month == '11':
        shutil.copy(source+'IMG_7274.JPG', move_to)
        print('Udało się przenieść plik')

else:
    print("This picture doesn't have exif")


