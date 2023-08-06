import threading
import socket
import motion
import time 
import cv2


class tello:
    
    def __init__(self):
        self.text='None'
        self.land=False
        self.socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(("0.0.0.0",8889))
        self.tello_address = ("192.168.10.1", 8889)
        self.local_video_port = 11111
        self.socket.sendto('command'.encode('utf-8'),self.tello_address)
        self.socket.sendto('streamon'.encode('utf-8'),self.tello_address)
        self.send_data_thread=threading.Thread(target=self.video_data)
        self.send_data_thread.daemon=True
        
        
    def video_data_start(self):
        self.send_data_thread.start()
        
           
    def video_data_stop(self):
        self.land=False       
           
           
    def vid(self):
        count = 0
        self.video = cv2.VideoCapture("udp://@0.0.0.0:11111")
        while 1:
            try:
                ret, frame = self.video.read()
                count= (count+1)%2
                if ret and count == 0:
                    self.text = motion.show(frame)
            except Exception as err:
                print(err)
          
            
    def send_data(self,msg):
        self.abort_flag = False
        self.socket.sendto(msg.encode('utf-8'), self.tello_address)
  
          
    def video_data(self):
        while 1:
            if self.land:
                if self.text=='COME':
                    time.sleep(0.3)
                    if self.text=='COME':
                        time.sleep(0.3)
                        if self.text=='COME':
                            self.send_data("rc 0 30 0 0")
                            time.sleep(1)
                            self.send_data("rc 0 0 0 0")
                if self.text=='AWAY':
                    time.sleep(0.3)
                    if self.text=='AWAY':
                        time.sleep(0.3)
                        if self.text=='AWAY':
                            self.send_data("land")
                            self.land=False
                            time.sleep(1)
                if self.text=='SPINL_LEFT':
                    time.sleep(0.3)
                    if self.text=='SPINL_LEFT':
                        time.sleep(0.3)
                        if self.text=='SPINL_LEFT':
                            self.send_data("curve 55 55 0 0 110 0 50")
                            time.sleep(3.5)
                            self.send_data("curve -55 -55 0 0 -110 0 50") 
                            time.sleep(4)
                if self.text=='SPIN_RIGHT':
                    time.sleep(0.3)
                    if self.text=='SPIN_RIGHT':
                        time.sleep(0.3)
                        if self.text=='SPIN_RIGHT':
                            self.send_data("curve 55 -55 0 0 -110 0 50")
                            time.sleep(3.5)
                            self.send_data("curve -55 55 0 0 110 0 50") 
                            time.sleep(4)          
                elif self.text=='?':
                    self.send_data("rc 0 0 0 0")
                    time.sleep(0.3)
                else:
                    time.sleep(0.3)
            elif self.text=='AWAY':
                    time.sleep(0.3)
                    if self.text=='AWAY':
                        time.sleep(0.3)
                        if self.text=='AWAY':
                            self.send_data("takeoff")
                            self.land=True
                            time.sleep(1)
            else:
                time.sleep(0.3)