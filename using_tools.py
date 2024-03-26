import  random
feet_in_mile = 5200
metters_in_kilomitters = 100
beats = ["shakil","mira","tuni","rakim khan"]

def get_file_ext(filename):
    return filename[filename.index(".")+1:]

def roll_dice(num):
    return random.randint(1,num)
