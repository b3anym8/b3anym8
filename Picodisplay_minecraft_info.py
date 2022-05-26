import picodisplay as display
import utime
 
buf = bytearray(display.get_width() * display.get_height() * 2)
display.init(buf)
display.set_backlight(1)
 
 
def clear():
    display.set_pen(0, 0, 0)
    display.clear()
    display.update()
 
 
while True:
    if display.is_pressed(display.BUTTON_A):              
        clear()                                           
        display.set_pen(0, 0, 200)                    
        display.text("/effect @s speed 999 5 true makes you fast", 10, 10, 240, 4) 
        display.update()                                  # update the display
        utime.sleep(3)                                    # pause for a sec
        clear()                                           # clear to black again
    elif display.is_pressed(display.BUTTON_B):
        clear()
        display.set_pen(0, 255, 255)
        display.text("Call a mob grumm and it will flip over", 10, 10, 240, 4)
        display.update()
        utime.sleep(3)
        clear()
    elif display.is_pressed(display.BUTTON_X):
        clear()
        display.set_pen(255, 0, 200)
        display.text("Name a sheep jeb_ and it will go rainbow", 0, 10, 240, 4)
        display.update()
        utime.sleep(3)
        clear()
    elif display.is_pressed(display.BUTTON_Y):
        clear()
        display.set_pen(255, 255, 0)
        display.text("Jumping and hitting enemies will do 2x dmg", 0, 10, 240, 4)
        display.update()
        utime.sleep(3)
        clear()
    else:
        display.set_pen(255, 100, 255)
        display.text("Press buttons to discover", 10, 10, 240, 4)
        display.update()
    utime.sleep(0.1)