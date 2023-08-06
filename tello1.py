import threading
import socket
import single
import time 
import cv2


class tello:
    def __init__(self):
        self.text='None'
        self.socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(("0.0.0.0",8889))
        self.tello_address = ("192.168.10.1", 8889)
        self.local_video_port = 11111
        self.recive_video_thread = threading.Thread(target=self.recive_thread)
        self.data_thread=threading.Thread(target=self.video_data)
        self.recive_video_thread.daemon = True
        self._running=True
        #self.recive_video_thread.start()
        self.data_thread.start()
        self.socket.sendto('command'.encode('utf-8'),self.tello_address)
        self.socket.sendto('streamon'.encode('utf-8'),self.tello_address)
        
        
    def terminate(self):
        self._running=False
        cv2.destroyAllWindows()
     


    def recive_thread(self):
        while True:
            try:
                self.response, ip=self.socket.recvfrom(3000)
                print(self.response)
            except socket.error as e:
                print("err")

    def vid(self):
        self.video=cv2.VideoCapture("udp://@0.0.0.0:11111")
        while True:
            self.text=single.show(self.video)
    
                
    def recv(self):
        self.video=cv2.VideoCapture("udp://@0.0.0.0:11111")
        while self._running:
            self.text=single.show(self.video)
                

    def start(self):
        self.recv_videoThread=threading.Thread(target=self.recv)
        self.recv_videoThread.daemon=True
        self.recv_videoThread.start()


    def stop(self):
        print('stop')
        self.terminate()
        pass
        
        
    def data(self,msg):
        self.abort_flag = False
        self.socket.sendto(msg.encode('utf-8'), self.tello_address)
       

    def video_data(self):
        land=False
        while True:
            if self.text=='STOP':
                self.data("rc 0 0 0 0") 
            elif self.text=='GO':
                self.data("rc 0 30 0 0")
            elif self.text=='LEFT':
                self.data("rc 0 0 0 -50")
            elif self.text=='BACK':
                self.data("rc 0 -30 0 0")
            elif self.text=='RIGHT':
                self.data("rc 0 0 0 50")
            elif self.text=='TAKEOFF':
                if land:
                    self.data("land")
                    time.sleep(1)
                else:
                    self.data("takeoff")
                    time.sleep(1)
                    land=True
            else:
                self.data("rc 0 0 0 0") 
            time.sleep(0.5)
            
            
    
        