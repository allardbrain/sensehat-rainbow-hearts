from sense_hat import SenseHat
import time

# Create variables to hold each RGB color we want to use
r = (255, 0, 0)     # red 
p = (204, 0, 204)   # pink
o = (255, 128, 0)   # orange
y = (255, 255, 0)   # yellow
g = (0, 255, 0)     # green
a = (0, 255, 255)   # aqua
b = (0, 0, 255)     # blue
pr = (128, 0, 255)  # purple
e = (0, 0, 0)       # blank

# Create a list to hold the color of each pixel in our heart images
# Each image contains 8 rows of 8 pixels each
red_heart = [
     e, e, e, e, e, e, e, e,
     e, r, r, e, r, r, e, e,
     r, r, r, r, r, r, r, e,
     r, r, r, r, r, r, r, e,
     r, r, r, r, r, r, r, e,
     e, r, r, r, r, r, e, e,
     e, e, r, r, r, e, e, e,
     e, e, e, r, e, e, e, e
     ]

pink_heart = [
     e, e, e, e, e, e, e, e,
     e, p, p, e, p, p, e, e,
     p, p, p, p, p, p, p, e,
     p, p, p, p, p, p, p, e,
     p, p, p, p, p, p, p, e,
     e, p, p, p, p, p, e, e,
     e, e, p, p, p, e, e, e,
     e, e, e, p, e, e, e, e
     ]

orange_heart = [
     e, e, e, e, e, e, e, e,
     e, o, o, e, o, o, e, e,
     o, o, o, o, o, o, o, e,
     o, o, o, o, o, o, o, e,
     o, o, o, o, o, o, o, e,
     e, o, o, o, o, o, e, e,
     e, e, o, o, o, e, e, e,
     e, e, e, o, e, e, e, e
     ]

yellow_heart = [
     e, e, e, e, e, e, e, e,
     e, y, y, e, y, y, e, e,
     y, y, y, y, y, y, y, e,
     y, y, y, y, y, y, y, e,
     y, y, y, y, y, y, y, e,
     e, y, y, y, y, y, e, e,
     e, e, y, y, y, e, e, e,
     e, e, e, y, e, e, e, e
     ]

green_heart = [
     e, e, e, e, e, e, e, e,
     e, g, g, e, g, g, e, e,
     g, g, g, g, g, g, g, e,
     g, g, g, g, g, g, g, e,
     g, g, g, g, g, g, g, e,
     e, g, g, g, g, g, e, e,
     e, e, g, g, g, e, e, e,
     e, e, e, g, e, e, e, e
     ]

aqua_heart = [
     e, e, e, e, e, e, e, e,
     e, a, a, e, a, a, e, e,
     a, a, a, a, a, a, a, e,
     a, a, a, a, a, a, a, e,
     a, a, a, a, a, a, a, e,
     e, a, a, a, a, a, e, e,
     e, e, a, a, a, e, e, e,
     e, e, e, a, e, e, e, e
     ]

blue_heart = [
     e, e, e, e, e, e, e, e,
     e, b, b, e, b, b, e, e,
     b, b, b, b, b, b, b, e,
     b, b, b, b, b, b, b, e,
     b, b, b, b, b, b, b, e,
     e, b, b, b, b, b, e, e,
     e, e, b, b, b, e, e, e,
     e, e, e, b, e, e, e, e
     ]

purple_heart = [
     e, e, e, e, e, e, e, e,
     e, pr, pr, e, pr, pr, e, e,
     pr, pr, pr, pr, pr, pr, pr, e,
     pr, pr, pr, pr, pr, pr, pr, e,
     pr, pr, pr, pr, pr, pr, pr, e,
     e, pr, pr, pr, pr, pr, e, e,
     e, e, pr, pr, pr, e, e, e,
     e, e, e, pr, e, e, e, e
     ]

heart_colors = [red_heart, pink_heart, orange_heart, yellow_heart,
                green_heart, aqua_heart, blue_heart, purple_heart]

def rainbow_hearts():

    # Create a sense object
    sense = SenseHat()
        
    # Reduce the brightness of the LED display
    sense.low_light = True

    for color in heart_colors:
        sense.set_pixels(color)
        time.sleep(1)

    # Clear the LED display
    sense.clear()

rainbow_hearts()

