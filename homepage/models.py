from django.db import models
from PIL import Image
import re


class PixelCounter(models.Model):
    title = models.CharField(max_length=150, blank=True)
    hex_code = models.CharField(max_length=7, blank=True)
    cover = models.ImageField(upload_to='images/')

    def rgb_list(self):
        '''Creates a list with all pixels of the image (in rgb)'''
        im = Image.open(self.cover)
        pixels = im.load()
        width, height = im.size
        all_pixels = []
        for x in range(width):
            for y in range(height):
                cpixel = pixels[x, y]
                all_pixels.append(cpixel)
        return all_pixels

    def check_hex(self):
        '''Checks a string for a hex code using "re"'''
        if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', self):
            return True
        else:
            return False

    def hex_to_rgb(self):
        '''Converts hex code to rgb'''
        hex_str = self.lstrip('#')
        rgb_code = tuple(int(hex_str[i:i + 2], 16) for i in (0, 2, 4))
        return rgb_code

    def hex_counter(self, rgb_code):
        '''Counting and returning pixels by hex code '''
        colore = 0
        for pixel in self.rgb_list():
            if pixel == rgb_code:
                colore += 1
        return f'Количество пикселе по hex code: {colore}'

    def black_or_white(self):
        '''Counting black or white are more'''
        black = 0
        white = 0
        for pixel in self.rgb_list():
            if pixel == (0, 0, 0):  # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
                black += 1
            elif pixel == (255, 255, 255):
                white += 1

        if black > white:
            return f'Черных пикселей больше (Черных: {black}, Белых: {white}).'
        elif black < white:
            return f'Белых пикселей больше (Черных: {black}, Белых: {white}).'
        else:
            return f'Количество черных и белых пикселей равно Черных: ({black}, Белых: {white}).'

    def __str__(self):
        return self.title
