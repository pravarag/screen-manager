import pyautogui
import time
# import keyboard
import os


def manage_screens():
    counter = 0
    screen_dir = ''
    while counter == 0:
        print("Inside counter")
        time.sleep(5)
        print("Sleep was executed")
        # if keyboard.is_pressed('i'):
        if os.getcwd() == screen_dir:
            take_screens()

        else:
            take_screens()
            os.chdir(os.getcwd()+'/screens')

        time.sleep(10)


def take_screens():
    image = pyautogui.screenshot()
    img_name = pyautogui.screenshot()
    img_name = "screen_"+str(time.time())+".png"
    image.save(img_name)


if __name__ == '__main__':

    manage_screens()
