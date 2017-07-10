# Rainbow Hearts
Using your Raspberry Pi and SenseHAT, make hearts appear on the LED matrix in a variety of colors! You can clone this repo to get the project up and running in a couple minutes (see below), or follow along with [the tutorial](https://allardbrain.github.io/sensehat-rainbow-hearts/) if you want to learn how all the parts of the code work together.

## What You Need
To make the file run and/or to complete the tutorial, you should have the following:

* A Raspberry Pi
* A SenseHAT, which is connected to the Pi's GPIO pins
* **Either** SSH access to your Pi
* **Or** an external monitor connected to your Pi with an HDMI cable, and a mouse & keyboard connected to your RPi
* The correct power adapter

Verify that everything is working properly:
* If the LEDs on your SenseHAT lit up in a rainbow when you connected the RPi to power, it's working!
* Boot up the RPi. If you are using a monitor, you should see either the Desktop or Bash, depending on whether you're using the GUI or not. 

## Clone This Repo
Open your Terminal or Command Prompt, and navigate to whichever directory you want this repo to be copied to (if you're not sure, you can save it in your Desktop directory).

For example: `cd ~/<your directory path here>` or `cd ~/Desktop`

Copy and paste the command below into your Terminal or Command Prompt and press enter:

`git clone https://github.com/allardbrain/sensehat-rainbow-hearts.git`

Navigate to the `sensehat-rainbow-hearts` directory that was created when you cloned the repo:

`cd sensehat-rainbow-hearts`

You can now access the `hearts.py` file and run it.
* If you're using the GUI, you can open the file with Python 3 (IDLE) and press the `F5` key to run it.
    * Raspbian logo in upper left corner  -->  Programming  -->  Python 3 (IDLE)
* If you're using Bash, you can run the file with this command: `python3 hearts.py`

## Make It Your Own!
* Change the RGB values (colors) of the hearts using [this guide](https://www.w3schools.com/colors/colors_picker.asp)
* Delete or add some hearts by following the structure you see in `hearts.py`
* Create other shapes, such as squares or triangles
* Change the length of time that the hearts are displayed
