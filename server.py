import socket
import threading
import time
class server:
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
        
        self.listen_flag=True
        self.recive_message_flag=True
        self.check_alive_flag=True
        
        self.data=[]
        self.sock_list=[]
        self.ip_list=[]
        self.main_port=port
        self.block_list=[]
        
        self.buffer_size=1024 #this is to buffer bit size when you recive msg 
                
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  

        self.sock.bind((ip,self.main_port))
        
        #set timeout
        self.sock.settimeout(1)
        
        #listen socket
        self.listen_thread=threading.Thread(target=self.listen).start()
        
        #resive message
        self.recive_thread=threading.Thread(target=self.recive_message).start()
        
        #check alive
        self.check_alive_thread=threading.Thread(target=self.check_alive).start()
        
    def listen(self):
        self.sock.listen(5)
        while self.listen_flag:
            try:
                conn,addr=self.sock.accept()
                if not addr[0] in self.block_list :
                    self.sock_list.append(conn)
                    self.ip_list.append(addr[0])
                    self.send_message(f"Connection from {addr[0]} as {len(self.sock_list)}","into server") # send a msg to people for notify new user add to chat
                else:
                    conn.close()
            except:
                pass
            
    def send_message(self,message:str,ip:str):
        message=ip+" : "+message
        for sock in self.sock_list:
            try:
                sock.send(message.encode("utf-8"))
            except Exception as errer:
                print("# error:",errer)
                sock.close()
                
    def recive_message(self):
        while self.recive_message_flag:
            for x in self.sock_list:
                try:
                    msg=x.recv(self.buffer_size).decode("utf-8")                    
                    l=msg.split("%>>>passme<<<%")
                    msg=""
                    for m in l:
                        if not(m=="" or m=="%>>>passme<<<%"):
                            msg+=m
                    if len(msg.split(" "))==len(msg)+1:
                        continue
                    #---------------------------------
                    #if you wont to pretend to be a name without ip use this formet
                    #$>2005command:<username>
                    #send a msg on is formet then is replace as your username
                    #---------------------------------
                    print("msg: ",msg)
                    if "$>2005command" in msg:
                        msg=msg.split(":")[1]
                        print("test un start")
                        self.ip_list[self.sock_list.index(x)]=msg
                        print("test un end")
                    elif not msg=="":
                        ip=self.ip_list[self.sock_list.index(x)]
                        self.data=[f"{ip} : {msg}",time.time()]
                        self.send_message(msg,ip)
                except:
                    continue
    
   
                
    def check_alive(self):#check users not in gruop
        while self.check_alive_flag:
            for x in self.sock_list:
                print("y ",self.sock_list.index(x))
                try:
                    print("test 1")
                    x.send(" ".encode())
                    print("z")
                except:
                    try:
                        print("test 2"*100)
                        self.remove(self.ip_list[self.sock_list.index(x)])
                        print("x")
                    except Exception as e:
                        print(e)
                        time.sleep(0.3)
                        
    def closeserver(self):
        for i in self.sock_list:
            i.close()
        self.sock.close()
        self.check_alive_flag=False
        self.listen_flag=False
        self.recive_message_flag=False
        
                    
    def remove(self,ip:str):
        index=self.ip_list.index(ip)
        print(index)
        print("test")
        self.sock_list[index].close()
        self.sock_list.pop(index)
        self.ip_list.pop(index)
        self.send_message(f"Connection from {ip} is lost","server")
                                  
if __name__=="__main__":
    s=server("127.0.0.1",1234)
    while(1):
        x=input(":>")
        s.remove(x)