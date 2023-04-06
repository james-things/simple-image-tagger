# simple-image-tagger

### a simple (but performant!) little tkinter GUI to help tag image datasets

**What it is:**

A simple graphical python script that helps you to easily tag image datasets.

**What it isn't:**

* The perfect solution.
* Configurable.
* Pretty.
* Guaranteed to be bug-free.

**Some Features/How it Works:**

* Run the script via: `python simple-image-tagger.py`.
* Loads/queues all images in folder chosen on load (optionally recursively).
* Enter text in the provided text area as you please (i.e., "a professional photograph of a snowy mountain, dynamic lighting, 8k, ...").
* Content of text entry area is saved to a text file when you press next/prev (autosaving).
* The text file's name matches image name (123.png -> 123.txt).
* Text file is automatically read (if exists) into the text area when image is loaded (autoloading).

**Dependencies:**

* Requires `PIL`.

Enjoy! :)
