from django.db import models
from PIL import Image
import random


class PixelCounter(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='images/')

    def black_or_white(self):
        im = Image.open(self.cover)
        pixels = im.load()
        width, height = im.size
        all_pixels = []
        for x in range(width):
            for y in range(height):
                cpixel = pixels[x, y]
                all_pixels.append(cpixel)
        black = 0
        white = 0
        for pixel in all_pixels:
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
