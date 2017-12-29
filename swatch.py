#image-analysis.py
#Written by Shaikat Islam

#libraries
from PIL import Image
import numpy as np
import cv2
import sys
import imageio

##Globals
#filename to be inputted by user
file_name = ""
#img as array
image_arr = []
#average color frame for vid
avg_vf = []
#avg color per row (image)
image_arr_row = []
#avg color per col (image)
image_arr_col = []
#dimensions of image
height = 0
width = 0
size = 0
#num frames in vid
frame_count = 0
frame_width = 0
frame_height = 0
v_size = 0
#avg colors for entire image
red = 0
green = 0
blue = 0

#Functions

#opens image and creates array of pixels in image_arr
def open_image():
    global file_name
    file_name = input("What is the name of the image to be analyzed?\n")
    #im = Image.open(file_name)

    file_not_open = True
    while file_not_open:
        try:
            #create image object
            im = Image.open(file_name)
            file_not_open = False
        except IOError:
            file_name = input("Error: File does not appear to exist. Try again:\n")


    #fill globals with applicable data
    size_tup = im.size
    global height
    global width
    global size
    height = size_tup[0]
    width = size_tup[1]
    size = height * width
    print("File Attributes:")
    print("Image width:" , end = " ")
    print(width)
    print("Image height:" , end = " ")
    print(height)
    #fill 2d array with pixel data
    global image_arr
    image_arr = np.array(im)

#opens video and processes frames into array
def process_vid():
    global file_name
    file_not_open = True
    file_name = input("What is the name of the video file to be analyzed?\n")
    #vid = imageio.get_reader(file_name, 'ffmpeg')
    while file_not_open:
        try:
            vid = imageio.get_reader(file_name, 'ffmpeg')
            file_not_open = False
        except IOError:
            file_name = input("Error: File does not appear to exist. Try again:\n")

    #create VideoCapture object
    cap = cv2.VideoCapture(file_name)
    global frame_count
    global frame_width
    global frame_height
    global avg_vf
    global v_size
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    v_size = frame_width * frame_height
    print("Framecount:" , end = " ")
    print(frame_count)
    print("Frame width:" , end = " ")
    print(frame_width)
    print("Frame height:" , end = " ")
    print(frame_height)
    print("The frame division factor determines which frames are", end = " ")
    print("analyzed in a video. The smaller the framecount, the", end = " ")
    print("smaller the frame division factor should be.")
    print("The greater the framecount, the greater the frame", end = " ")
    print("division factor should be.")
    print("If a video is very large and has many frames, it will", end = " ")
    print("take a while to render an image if the frame division", end = " ")
    print("factor is low.")
    v_div = int(input("Enter frame division factor:"))
    while v_div <= 0 or v_div > frame_count:
        print("This is not a vald input for frame division factor.")
        print("Please enter a value greater than 0 and less than", end = " ")
        print(frame_count)
        v_div = int(input("Please enter value: "))
    print(frame_count)
    frame_arr = []
    for i in range(frame_count):
        if i % v_div == 0:
            print("Frame "+""+str(i)+"/"+str(frame_count)+" analyzed...", end='\r')
            frame = vid.get_data(i)
            frame_arr = np.array(frame)
            avg_vf.append(v_calc_avg_color(frame_arr))

    #close video file
    cap.release()


#returns image of processed video file
def v_create_images():
    v_width = int(input("How wide would you like the resulting image to be? "))
    while v_width <= 0 or v_width > 4320:
        print("This is not a vald input for width.")
        v_width = int(input("Please enter a value greater than 0 and less than 4320."))

    #image created from iterated video frames
    count = len(avg_vf)
    v_img = Image.new('RGB', (v_width, count))
    ld_v_img = v_img.load()

    for x in range(v_width):
        for y in range(count):
            ld_v_img[x,y] = (avg_vf[y][0], avg_vf[y][1], avg_vf[y][2])
    v_img.save("video_result.jpg", "JPEG")


def v_calc_avg_color(arr):
    r = 0
    g = 0
    b = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            r = r + arr[i][j][0]
            g = g + arr[i][j][1]
            b = b + arr[i][j][2]
    r = r / v_size
    g = g / v_size
    b  = b / v_size
    red = 0
    green = 0
    blue = 0
    #for individual frame processing
    red = int(round(r))
    green = int(round(g))
    blue = int(round(b))
    #returns an array of colors for video frames (need more processing)
    rgb = []
    rgb.append(red)
    rgb.append(green)
    rgb.append(blue)
    return rgb

#calculates avg color for an image
def calc_avg_color(arr):
    r = 0
    g = 0
    b = 0
    for i in range(width):
        for j in range(height):
            r = r + arr[i][j][0]
            g = g + arr[i][j][1]
            b = b + arr[i][j][2]
    r = r / size
    g = g / size
    b  = b / size
    global red
    global green
    global blue
    #for individual frame processing
    red = int(round(r))
    green = int(round(g))
    blue = int(round(b))
    #returns an array of colors for video frames (need more processing)
    rgb = []
    rgb.append(red)
    rgb.append(green)
    rgb.append(blue)
    #print hex code for image
    print("Average color: ")
    print("RGB:", end = " ")
    print("(", end = "")
    print(rgb[0], end = ", ")
    print(rgb[1], end = ", ")
    print(rgb[2], end = ")\n")
    print("Hex Triplet:", end = " ")
    print('#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2]))
    return rgb

#calculates avg color row by row
def calc_avg_color_row(arr):
    rgb = []
    r = 0
    g = 0
    b = 0
    for i in range(width):
        for j in range(height):
            r = r + arr[i][j][0]
            g = g + arr[i][j][1]
            b = b + arr[i][j][2]
        r = r / width
        g = g / width
        b = b / width
        rgb.append(int(round(r)))
        rgb.append(int(round(g)))
        rgb.append(int(round(b)))
        r = 0
        g = 0
        b = 0
    temp = []
    start = 0
    end = 0
    for k in range(len(rgb)):
        if k % 3 == 0:
            start = k - 3
            end = k
            temp = rgb[start:end]
            global image_arr_row
            image_arr_row.append(temp)
            temp = []


#calculates avg color col by col
def calc_avg_color_col(arr):
    rgb = []
    arr_t = arr.T
    r = 0
    g = 0
    b = 0
    for i in range(len(arr_t)):
        for j in range(len(arr_t[0])):
            r = r + arr_t[i][j][0]
            g = g + arr_t[i][j][1]
            b = b + arr_t[i][j][2]
            r = r / height
            g = g / height
            b = b / height
            rgb.append(int(round(r)))
            rgb.append(int(round(g)))
            rgb.append(int(round(b)))
            r = 0
            g = 0
            b = 0
    temp = []
    start = 0
    end = 0
    for k in range(len(rgb)):
        if k % 3 == 0:
            start = k - 3
            end = k
            temp = rgb[start:end]
            global image_arr_col
            image_arr_col.append(temp)
            temp = []

#print representation of image based on colors
def create_images():

    #average color
    im_avg = Image.new('RGB', (500, 500))
    ld_avg = im_avg.load()
    for x in range(500):
        for y in range(500):
            ld_avg[x,y] = (red, green, blue)

    #bug fix for avg color by row
    sd = 0
    if width < height:
        sd = width
    else:
        sd = height

    #avg color by row
    im_row = Image.new('RGB', (300, sd))
    ld_row = im_row.load()
    for x in range(300):
        for y in range(1, sd):
            ld_row[x,y] = (image_arr_row[y][0], image_arr_row[y][1], image_arr_row[y][2])

    #avg color by col
    im_col = Image.new('RGB', (width, 300))
    ld_col = im_col.load()
    for x in range(1, width):
        for y in range(300):
            ld_col[x,y] =  (image_arr_row[x][0], image_arr_row[x][1], image_arr_row[x][2])

    #save images
    im_avg.save("average_color.jpg", "JPEG")
    im_row.save("average_row.jpg", "JPEG")
    im_col.save("average_col.jpg", "JPEG")

def run_prog():
    exit  = 'q'
    choice = input("Enter 'v' to analyze video, 'i' to analyze image, or 'q' to quit: ")
    while choice != exit:
        if choice == 'v':
            process_vid()
            v_create_images()
            choice = input("Enter 'v' to analyze video, 'i' to analyze image, or 'q' to quit: ")
        elif choice == 'i':
            open_image()
            calc_avg_color(image_arr)
            calc_avg_color_row(image_arr)
            calc_avg_color_col(image_arr)
            create_images()
            choice = input("Enter 'v' to analyze video, 'i' to analyze image, or 'q' to quit: ")
        else:
            choice = input("That is an invalid choice. Please try again: ")

#run program
run_prog()
