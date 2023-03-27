# simple-image-tagger

## a simple (but performant!) little tkinter GUI to help you tag your dreambooth-style datasets

What it is:
-a simple graphical python script that helps you to easily tag image datasets

What it isn't:
-the perfect solution
-configurable
-pretty
-guaranteed to be bug free

Some Features/How it Works:

-run the script via: `python simple-image-tagger.py`
-loads/queues all images in folder chosen on load (optionally recursively)
-enter text in the provided text area as you please (ie: "a professional photograph of a snowy mountain, dynamic lighting, 8k, ...")
-content of text entry area is saved to a text file when you press next/prev (autosaving)
    -the text file's name matches image name (123.png -> 123.txt)
-text file is automatially read (if exists) into the text area when image is loaded (autoloading)

Dependencies:

-requires `PIL`

Enjoy! :)
