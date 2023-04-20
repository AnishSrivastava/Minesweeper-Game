import settings

#creating default functions to generate heigh and width of required panels accoding to the overall layout
def height_percent(percentage):
    return (settings.HEIGHT / 100) * percentage

def width_percent(percentage):
    return (settings.WIDTH / 100) * percentage