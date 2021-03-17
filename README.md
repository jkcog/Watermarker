# Watermarker
GUI desktop application for applying custom image or text watermarks to multiple images with [Pillow](https://pillow.readthedocs.io/en/stable/).

* * *

# Setup
* `$ pip install -r requirements.txt`
* Run main.py


<br />

# Usage

<br />
<img src="/images/gui_screenshot.png" alt="GUI screenshot" align=right width=600px>

##### Select your watermark type: 
* Select "Text" to begin designing a custom text watermark
* Select "Image" to apply a pre-designed watermark image
##### If applying a pre-designed watermark image:
* Specify the file path to the watermark
##### If applying a text watermark:
* Specify the text
* Specify the colour by either typing the colour name or giving the hexadecimal color code
* Specify the opacity of the watermark
##### Select target image:
* Enter the file path for the target image
* Click "Select"
* Repeat until you have selected all your target images
* If you make a mistake you can click "Remove Image" to remove the most recent selection.
##### Apply watermark:
* Click "Add Watermark" to apply your watermark to the selected images
* You can find the new watermarked images in the project folder
