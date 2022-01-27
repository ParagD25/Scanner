# PDF Scanner
An application where one can scan an object and save in it '.jpg' and '.pdf' format.


## Logic 🧠
- When we place an object under the webcam, edges are been detected using canny edge detection and further we can find the largest contours present in the image.

- After finding contours we use warp perspective to show case the scanned area. 

- Used img2pdf library, to convert the images into pdf. 

## Prerequisites 📋

You'll just need [Git](https://git-scm.com) and [Python](https://www.python.org/) installed on your computer.

[![](https://camo.githubusercontent.com/2fb0723ef80f8d87a51218680e209c66f213edf8/68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667)](https://python.org)


## Libraries Used 📁:
- <b><i> Open-CV </i></b>
- <b><i> Numpy </i></b>
- <b><i> img2pdf </i></b>

## How To Use 🔧:

From your command line, first clone this repo:

```bash
# Clone this repository
$ git clone https://github.com/ParagD25/Scanner/

# Go into the repository
$ cd Scanner

# Remove current origin repository
$ git remote remove origin

# Create new virtual python environment
$ python3 -m venv venv

# Activate virtual python environment
$ source venv/bin/activate

# Install all the libraries/frameworks mentioned above

# Run Python file
$ "python scanner.py"

```

## Working Example 📷:
[Scanned Images](https://github.com/ParagD25/Scanner/tree/master/Images)

[Scanned PDF](https://github.com/ParagD25/Scanner/tree/master/PDF)

Working of PDF Scanner - [Watch Demo](https://youtu.be/yfZKE19jc3w)

## Contributing ©️:

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
