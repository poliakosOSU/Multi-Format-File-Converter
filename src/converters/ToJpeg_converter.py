from PIL import Image, ExifTags
import os

def Get_FileName(file):

    filename_w_ext = os.path.basename(file)
    original_name, file_extension = os.path.splitext(filename_w_ext)

    # create new name with a process id and a png file extension
    name = original_name
    pid = str(os.getpid())
    extenstion = ".jpg"
    the_file_name = name + "_" + pid + extenstion
    return the_file_name

def ConvertFile(input_file):

    current_dir = os.getcwd()
    file_dir = current_dir
    input_file = file_dir + input_file

    original_image = Image.open(input_file)

    file_name = Get_FileName(input_file)

    try:
        for i in ExifTags.TAGS.keys():
            if ExifTags.TAGS[i] == 'Orientation':
                print("Found it!!!!!!!!")  # for testing
                print(ExifTags.TAGS[i])
                # https://sirv.com/help/resources/rotate-photos-to-be-upright/
                exif = dict(original_image._getexif().items())
                if exif[i] == 3:
                    print("Orientation 3, rotating 180 degrees")  # for testing
                    original_image = original_image.rotate(180, expand=True)
                elif exif[i] == 6:
                    print("Orientation 6, rotating 270 degrees")  # for testing
                    original_image = original_image.rotate(270, expand=True)
                elif exif[i] == 8:
                    print("Orientation 8, rotating 90 degrees")  # for testing
                    original_image = original_image.rotate(90, expand=True)
    except:
        # traceback.print_exec()
        print("Orientation either 0 or EXIF data does not exist")  # for testing

    ret_name = file_name
    save_path = "/media/PngToJpeg/converted/" + file_name
    ret_path = "PngToJpeg/converted/" + file_name

    save_name = file_dir + save_path

    original_image.save(save_name,'JPEG', quality=100)

    return ret_name, ret_path
