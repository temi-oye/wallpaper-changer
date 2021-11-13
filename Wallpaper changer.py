import ctypes
import glob
import random

list_of_wallpapers = glob.glob("<Path to your wallpapers>/*")
new_wallpaper = random.choice(list_of_wallpapers)
SPI_SETDESKWALLPAPER = 20

def changeBG(path):
  ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)

changeBG(new_wallpaper)