cmd = ''
engine = False
while cmd != "quit":
    cmd = input(print('enter the value 1.start 2.stop 3.quit')).lower()
    if cmd == "start":
        if engine == False:
            print("Car has started Let's go!!! ")
            engine = True
        else:
            print("Car is already running idiot")
    elif cmd == "stop":
        if engine == True:
            print("Car has stopped!!! ")
            engine = False
        else:
            print("Car is already Stopped idiot")
    elif cmd == "quit":
        print("Okay bye Fuck off")
        break
    else:
        print("Error bad input")
