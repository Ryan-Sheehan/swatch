# Swatch
Swatch is a quick project idea I came up with while reading about color theory and film. It has two main features; image and video processing. By inputting an image, the user can find the average color for that image, as well as the average color by row or average color by column (rows and columns in reference to the rows and columns of pixels that make up the image). By inputting a video file, the program parses through the frames of a video and generates the average color for each frame. Then, it creates a color palette using all of those average colors. This repo comes with sample images and videos to use swatch on.

### Image Demo
Example of Swatch on Vermeer's <i>View of Delft</i>:

<em>Source Image:</em>

![alt text](https://github.com/shaikat9000/swatch/blob/master/examples/viewofdelft.jpg)

<em>Average Color</em>:

![alt text](https://github.com/shaikat9000/swatch/blob/master/examples/average_color.jpg)

<em>Average Color by Row</em>:

![alt text](https://github.com/shaikat9000/swatch/blob/master/examples/average_row.jpg)

<em>Average Color by Column</em>:

![alt text](https://github.com/shaikat9000/swatch/blob/master/examples/average_col.jpg)

### Video/Movie Demos
Example of Swatch on Christopher Nolan's <i>Inception</i> (2010):

![alt text](https://github.com/shaikat9000/swatch/blob/master/examples/inception.jpg)


Example of Swatch on Pixar's <i>Inside Out</i> (2015):

![alt text](https://github.com/shaikat9000/swatch/blob/master/examples/insideout.jpg)


## Getting Started
Swatch runs on Python 3.x. 
You can download Python [here.](https://www.python.org/downloads/ "Python Download")

### Prerequisites
Swatch uses a few libraries:

```
pillow
numpy
opencv
imageio
```

You can install these libraries using <b>pip</b>.
Here is a [guide.](https://packaging.python.org/tutorials/installing-packages/ "pip guide")

### Installing
To install swatch after all the prerequisites have been installed, follow these steps:

1) Clone this repo:
```
git clone git@github.com:shaikat9000/swatch.git
```

2) Go into the /swatch directory:
```
cd swatch
```

3) Run swatch:
```
python swatch.py
```

## Built With
* [Python](https://www.python.org/downloads/) 
* [OpenCV](https://opencv.org/) 


## Authors
* **Shaikat Islam** - [Github](https://github.com/shaikat9000/)


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
- **Artists and coders everywhere.**
- **Great teachers and professors!**
- **Codacken** - for the name

