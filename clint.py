import socket
import threading
import time
class client:
    
    #_______________________________________________________________________________________________________________________
    #                                       ----------READ ME IT IMPORTENT--------------
    ########################################################################################################################
    # THERE IS SOME RESERVED WORDS IN THERE
    #       $>2005command    <----THIS ONE FOR CHANGE USERNAME
    #       %>>>passme<<<%   <----THIS ONE USE as tag for pass user lising mod
    # DO NOT USE THESE WORD PLEASE, WHEN IT YOU COMMIUNICATE with ans programs it will not send to other users .
    # this word a use for use as like for tags
    #  _____________________________________________________________________________________________________________________
    
    def __init__(self,ip:str,port:int):
        
        self.passme_flag=True
        
        self.buffer_size=1024
        
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((ip,port))
        
        # passer
        self.passme=threading.Thread(target=self.passme).start()
        
    def send_message(self,message:str):
        try:
            self.sock.send(message.encode("utf-8"))
        except:
            self.sock.close()
            
            
            
    def recive_message(self):
        self.sock.settimeout(5)
        while (1):
            try:
                msg= self.sock.recv(self.buffer_size).decode("utf-8")#   baffur size <<<<<<<_____not a port____>>>>>>> :) becourse i allways  forget about it
                if len(msg.split(" "))==len(msg)+1:
                        continue
                return  msg
            except :
                return False #return noting when no msg yet
                            #if we do not have new msg  or we already it goted return will False
            
    def passme(self):#pass clint chance to other when do nothing 
        while self.passme_flag:
            try:
                self.send_message("%>>>passme<<<%")
                time.sleep(1)
            except:
                pass
                  

def temp():
    while (1):
        try:
            msg=c.recive_message()
            if not  msg ==  False:
                print(msg)
        except:
            print("temp error")
            pass

if __name__=="__main__":
    c=client("127.0.0.1",1234)
    thread=threading.Thread(target=temp)
    thread.start()
    while True:
        msg=input("")
        c.send_message(msg)