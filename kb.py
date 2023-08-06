import keyboard

  
def getKey():
    while True:
        if keyboard.is_pressed("w"):
            return "rc 0 50 0 0"
        if keyboard.is_pressed("s"):
            return "rc 0 -50 0 0"
        if keyboard.is_pressed("a"):
            return "rc -50 0 0 0"
        if keyboard.is_pressed("d"):
            return "rc 50 0 0 0"
        if keyboard.is_pressed("8"):
            return "rc 0 0 50 0"
        if keyboard.is_pressed("5"):
            return "rc 0 0 -50 0"
        if keyboard.is_pressed("4"):
            return "rc 0 0 0 -50"
        if keyboard.is_pressed("6"):
            return "rc 0 0 0 50"
        if keyboard.is_pressed("z"):
            return "takeoff"
        if keyboard.is_pressed("x"):
            return "land"
        if keyboard.is_pressed("c"):
            return "stop"
            