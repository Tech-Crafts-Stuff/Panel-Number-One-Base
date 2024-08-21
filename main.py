
# We need a few libraries for this script to work
import neopixel
from machine import Pin
import time, random

# A python class to configure the panel lights. You can change this as you see fit.
class PanelLights:

    # Set some constants containing RGB values for the addressable LEDS
    RED = (96,0,0)
    OFF = (0,0,0)
    BLUE = (0,0,128)
    GREEN = (0,128,0)
    BRIGHTWHITE = (190,75,15)
    WHITE = (143, 55, 11)

    # A couple of lists that mark the position of LEDs that have a red button
    # or mark the position of the small round lights on the panel
    REDLEDPOSITION = [1,6,11]
    SMALLROUNDLIGHTPOSITION = [7]

    # These are variables that are required for the LEDs to function
    # which are created when the class is created
    def __init__(self, numberOfPixels):
        # The number of pixels in the panel is passed to the class when it is created
        self.numberOfPixels = numberOfPixels
        # Set up the neopixels
        # There are 13 in total
        self.np = neopixel.NeoPixel(Pin(11), numberOfPixels)
        self.onOrOff = [1] * numberOfPixels # Set on/off state for all LEDs

    # This is the main function that sets the colour values of the LEDS
    # and decides whether they should display or not
    # This is called in a while loop later in the code so that the lights
    # will randomly turn on and off.
    def activatePanel(self):
        # This loop decides which of the LEDs will turn on and off
        for i in range(len(self.onOrOff)):
            self.onOrOff[i] = random.choice([0,1])
                    
        # This loop will iterate through the LEDs and set them on/off
        # and set their colour.
        for j in range(self.numberOfPixels):
            if self.onOrOff[j] == 0:
                self.np[j] = self.OFF
            else:
                if j == 0:
                    self.np[j] = self.WHITE
                elif j in self.REDLEDPOSITION:
                    self.np[j] = self.RED
                elif j in self.SMALLROUNDLIGHTPOSITION:
                    self.np[j] = random.choice([self.BLUE, self.GREEN, self.RED])
                else:
                    self.np[j] = self.WHITE

        # Once we have set up the LEDs we need to write them to the neopixel function
        # to get them to display (or not)
        self.np.write()

        # Sleep between 2–5 seconds
        time.sleep(random.choice([2,3,4,5]))
    
# Create the panel class, remembering to specify the number of LEDs
panel = PanelLights(12)

# Start a loop which calls the activatePanel() function
while True:
    panel.activatePanel()


    
    
  