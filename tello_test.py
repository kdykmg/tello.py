from tello_data import tello
import kb 
import time
import keyboard
import threading


def key_data():
    while 1:
        val=kb.getKey()
        if val=='takeoff':
            tello.send_data(val)
            tello.video_data_start()
        elif val=='land':
            tello.send_data(val)
            tello.video_data_stop()
        elif val=='stop':
            tello.video_data_stop()
            exit()
        else:
            tello.send_data(val)
        keyboard.on_release(handle_event)
        time.sleep(1)
   
    
def handle_event(e):
    tello.data("rc 0 0 0 0")
    
    
tello=tello()
#key=threading.Thread(target=key_data)
#key.daemon=True
#key.start()
tello.video_data_start()
tello.vid()




