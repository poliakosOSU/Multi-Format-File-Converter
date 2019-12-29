from PIL import Image, ExifTags
import math
import os


def scaleType(width, height):
    if width >= 2480 and height >= 3508:
        newWidth = float(2380)
        float(width)
        ratio = newWidth / width
        print(ratio)  # just for testing

        float(height)
        newHeight = ratio * height

        if newHeight > height:
            return "height"
        else:
            return "width"
    else:
        print("Scale Type: none")
        return "none"

        # make height 3408, and scale width accordingly


def scaleAccordingToHeight(width, height):
    newHeight = float(3408)
    float(height)
    ratio = newHeight / height
    print("The Ratio Is: %d", ratio)  # for testing

    float(width)
    newWidth = ratio * width

    newWidth = int(math.floor(newWidth))
    newHeight = int(math.floor(newHeight))

    return newWidth, newHeight

    # make width 2408 and scale height acccordingly


def scaleAccordingToWidth(width, height):
    newWidth = float(2380)
    float(width)
    ratio = newWidth / width
    print("+++++++The Ratio Is: %d", ratio)  # for testing

    float(height)
    newHeight = ratio * height

    newWidth = int(math.floor(newWidth))
    newHeight = int(math.floor(newHeight))

    return newWidth, newHeight


# creating new file name and returns original file extension
def Get_FileName_and_Extension(file):
    # getting original file name
    filename_w_ext = os.path.basename(file)
    original_name, file_extension = os.path.splitext(filename_w_ext)

    # create new name with a process id and a pdf file extension
    name = original_name
    pid = str(os.getpid()) # using process id, in case of multiple files with same name are being used
    extenstion = ".pdf"
    the_file_name = name + "_" + pid + extenstion

    return the_file_name, file_extension




# creating blank image
mode = 'RGB'
size = (2480, 3508)
color = (255, 255, 255)
img = Image.new(mode, size, color)

# reading image in
def ConvertFile(input_file):

    current_dir = os.getcwd()
    file_dir = current_dir
    input_file = file_dir + input_file
    print("INPUT FILE")
    print(input_file)

    original_image = Image.open(input_file)

    file_name, file_ext = Get_FileName_and_Extension(input_file)

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

    # getting dimensions of original image
    originalWidth, originalHeight = original_image.size

    # figuring out if we will scale according to height or width
    scaling = scaleType(originalWidth, originalHeight)

    finalHeight = 0
    finalWidth = 0

    # generating new dimensions for the image
    if scaling == "height":
        finalWidth, finalHeight = scaleAccordingToHeight(originalWidth, originalHeight)
    elif scaling == "width":
        finalWidth, finalHeight = scaleAccordingToWidth(originalWidth, originalHeight)
    elif scaling == "none":
        finalWidth = originalWidth
        finalHeight = originalHeight
    else:
        traceback.print_exec()
        sys.exit("Error Occured")

    # resizing original image
    original_image = original_image.resize((finalWidth, finalHeight))

    # positioning img in proper location on page
    if scaling == "height":
        horzMargin = (2480 - finalWidth) / 2
        horzMargin = int(math.floor(horzMargin))
        img.paste(original_image, (horzMargin, 50))
    elif scaling == "width":
        vertMargin = (3508 - finalHeight) / 2
        vertMargin = int(math.floor(vertMargin))
        img.paste(original_image, (50, vertMargin))
    else:
        horzMargin = (2480 - finalWidth) / 2
        horzMargin = int(math.floor(horzMargin))
        vertMargin = (3508 - finalHeight) / 2
        vertMargin = int(math.floor(vertMargin))
        img.paste(original_image, (horzMargin,vertMargin))

    print("FILE NAME: " + file_name) # for testing

    ret_name = file_name

    # checking which file extension we are using
    # in order to know where to save the file
    if file_ext == ".jpg" or ".JPG" or ".jpeg" or ".JPEG":
        save_path = "/media/JpegToPdf/converted/" + file_name
        ret_path = "JpegToPdf/converted/" + file_name
    else: # if png then do following (change if more formats are added)
        save_path = "/media/PngToPdf/converted/" + file_name
        ret_path = "PngToPdf/converted/" + file_name

    save_name = file_dir + save_path



    img.save(save_name, 'PDF', quality=100)

    print("Return Name: " + ret_name) # for testing
    print("Return Path: " + ret_path) # for testing

    # return file name and path to file being returned
    return ret_name, ret_path
