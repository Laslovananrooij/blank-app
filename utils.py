from PIL import Image

#Paste function with list of images
#Can probably convert this to work with a class object 
def flatten_images(save_filename, images):
    """
    Images: list with image locations in the order to flatten
    Dest: name and destination of flattened image
    """
    result = Image.open(images[0]).convert("RGBA")
    for i in range(1,len(images)):
        to_paste = Image.open(images[i]).convert("RGBA")
        result = paste(result,to_paste,(0,0))
    result.save(save_filename)

    return result

#Paste function (only 2 images)
def paste(first, second, pos):
    new_layer = Image.new("RGBA", first.size)
    new_layer.paste(second, pos)
    return Image.alpha_composite(first, new_layer)