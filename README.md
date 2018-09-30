# fontbakery-desktop
An unofficial cross-platform desktop GUI for FontBakery. Made with python3 + wxPython. 

![screenshot](https://github.com/eliheuer/fontbakery-desktop/raw/master/docs/images/screenshot.png)

## Installation Instructions

1. Install a recent Python3 if you don't have it already.

2. Set up a new Python3 **virtual environment**. This is not
   required, but it's *highly recommended*. 

   -  To create a new virtual environment wherever you like 
      and call it whatever, something like ``WV-VENV``:

      ``python3 -m venv WX-VENV``

      This creates a new ``WX_VENV`` folder. The ``bin`` subfolder
      (or ``Scripts`` if you are on Windows) contains a new 
      ``python`` executable, and the ``pip`` installer linked to that.

   -  Activate the newly created environment:

      -  OS X or Linux: ``source WX-VENV/bin/activate``
      -  Windows: ``WX-VENV\Scripts\activate.bat``

      This temporarily adds the virtual environment's scripts folder to
      your console's `PATH`, so you can access the `python` and `pip` script from anywhere.

   -  Run ``deactivate`` when you wish to exit the virtual environment.
      This restores the default system `PATH`.
     
3. Install/update dependencies, from the root directory of this repo run:

   ``pip install -r requierments.txt``

4. Run the app from the root directory: 
   
   ``python3 src/fontbakery-desktop/__main__.py``
