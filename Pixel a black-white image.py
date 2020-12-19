# -*- coding: utf-8 -*-
"""
@author: Xing
"""
from PIL import  Image

def mean(numberlist):
    """
    Parameters
    ----------
    numberlst : [int]
        List of int numbers
    
    Returns
    -------
    int
        Mean of the list
    
    Example
    -------
    >>> mean([1, 2, 3, 4]), mean([1, 2, 2, 3])
    ("2", "2")

    """
    sum_ = 0.0
    for t in numberlist:
        sum_ += t
    return int(sum_ / len(numberlist))


def pixelate(img, (pixel_width, pixel_height), mode):
    """
    This function create a new image, in black and white, calling "i",
    that correspond to the original image pixelated. It can pixelate 
    in three mode : "min", "mean" and "max" with any dimension integer.

    Parameters
    ----------
    img : a image in black and white.

    (pixel_width, pixel_height) : a tuple with two positive integers 
    indicating the resulting pixel size.

    mode : a string of characters indicating the mode to pixelate.

       "min" : the minimun value of the pixels in each pixel size.
       "mean": the average value of the pixels in each pixel size.
       "max" : the maximun value of the pixels in each pixel size.

    Returns
    -------
    A image, in black and white, pixelated in (pixel_width, pixel_height) 
    dimensions.

    Exemple
    -------
    >>> pixelate(i, (10, 10), "mean")
    get a new image pixelated in (10, 10) with the average value of each
    region.
    """
    
    i = Image.new("L", img.size, 0)
    width, height = img.size
    
    for x in xrange (0, width, pixel_width):
        for y in xrange (0, height, pixel_height):
            result = [] #a list where we keep the pixels values
            for a in xrange (x, min(x + pixel_width, width)):
                for b in xrange (y, min(y + pixel_height, height)):
                    pix_value = img.getpixel((a, b))
                    result.append(pix_value) #we keep the values obtained 
                        
            if mode == "min": 
                color = min(result)
                
            elif mode == "max": 
                color = max(result)
                
            elif mode == "mean":
                color = mean(result)
                
            for c in xrange (x, min(x + pixel_width, width)):
                for d in xrange (y, min(y + pixel_height, height)):
                    i.putpixel((c, d), color) #add the color in each region
    return i
