from server import server 
from clint import client 
import sys,time
from gui import Ui_MainWindow 
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtCore import QThread,pyqtSignal
##############################################################################################  thread

class msg_thraed(QThread):#clint msg box thread<<<<<<<<<<<<<<<<<<============ fix me
    msg=pyqtSignal(str)
    def run(self):
        self.t=""
        while (1):
            try:
                m=myapp.clint.recive_message()
                if not  m ==  False:
                    self.t+=m+"\n"
                    self.msg.emit(self.t)
                time.sleep(0.5)
            except:
                myapp.ui.clint_stack.setCurrentWidget(myapp.ui.userlogin_page)
                myapp.clint.passme_flag=False
                self.setTerminationEnabled(True)            
           
class userlist_thread(QThread):# id ckecing thread
    userlist_sin=pyqtSignal(str)
    
    def  run(self):
        while 1:
            text=""
            x=0
            for i in myapp.server.ip_list:
                text+=f"id  {x} -> "+i+"\n"
                x+=1
            self.userlist_sin.emit(text)      
            time.sleep(1)

class live_chat(QThread):# server msg box thread
    chat_sin=pyqtSignal(str)
    def run(self):
        tmp=None
        while 1:
            try:
                data=myapp.server.data
                if tmp !=data[1]:
                    self.chat_sin.emit(data[0])
                    tmp=data[1]
            except:
                pass
 
 
 ##############################################[------------------ application ---------------]##########################################################           
 

 
class app():
    
    def __init__(self):
        self.window=QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        
        self.ui.tabWidget.setCurrentWidget(self.ui.server_tab)
        self.ui.server_stack.setCurrentWidget(self.ui.serverlogin_page)
        self.ui.clint_stack.setCurrentWidget(self.ui.userlogin_page)
        
        self.ui.server_login_error_sheet.setVisible(False)
        
        self.window.show()
        
        self.server_login()
        self.clint_login()
        
####################################################################################################### event side    
    def close(self, event):
        print("run me")
        self.server.listen_flag=False
        self.server.recive_message_flag=False
        self.server.check_alive_flag=False
        
        self.clint.passme_flag=False
        
        self.chat_reader.setTerminationEnabled(True)
        self.chat.setTerminationEnabled(True)
        self.userlist_worker.setTerminationEnabled(True)
        
        del self.server
        del self.clint
        
        event.accept()
        return super().closeEvent(event)    
    
    
 
##################################################################################### clintside
    
    def clint_login(self):#client login begin
        self.ui.server_login_error_sheet_2.setVisible(False)
        
        self.ui.enterbtn_clint_page.clicked.connect(self.clint_login_enter)
    
        self.ui.clearbtn_clint_page.clicked.connect(self.clear_clint)
    
    def clint_login_enter(self):#when client enter press 
        try:
            ip=self.ui.serverip_clint_page.text()
            port=self.ui.port_clint_page.text()
            us=self.ui.username_clint_page.text()
            buf=self.ui.buffersize_clint_page.text()
            
            self.clint=client(ip,int(port))
            self.clint.buffer_size=int(buf)
            self.clint.send_message(f"$>2005command:{us}")
            
            
            self.ui.clint_stack.setCurrentWidget(self.ui.chatroom)#open client chat box
            
            self.ui.sendbtn_clint_page.clicked.connect(self.msg_sender)#msg send button
        
            
            self.chat_reader=msg_thraed()#thread for catch resive msg
            self.chat_reader.start()
            self.chat_reader.msg.connect(self.chatbox_writer)
            
            self.ui.clear_msg_btn_clint_page.clicked.connect(self.clearchat)
        except:
            self.ui.server_login_error_sheet_2.setVisible(True)
            self.ui.serverip_clint_page.setText("")
            self.ui.port_clint_page.setText("")
            self.ui.username_clint_page.setText("")
            self.ui.buffersize_clint_page.setText("")
            
    def clearchat(self):
        self.chat_reader.t=""
        self.ui.chat_pannel_clint_page.setPlainText("")
    
    def chatbox_writer(self,data):#write msg come form msg_tread
        self.ui.chat_pannel_clint_page.setPlainText(data)
        
    def msg_sender(self):
        msg=self.ui.msgbox_clint_page.text()
        self.clint.send_message(msg)
        self.ui.msgbox_clint_page.setText("")
         
    def clear_clint(self):#clear data in client pannel
        self.ui.serverip_clint_page.setText("")
        self.ui.username_clint_page.setText("")
        self.ui.port_clint_page.setText("")
        self.ui.buffersize_clint_page.setText("")
      
#####################################################################################server side  

    def server_login(self):
        self.ui.enterbtn_server_page.clicked.connect(self.enter_server)
        self.ui.clearbtn_server_page.clicked.connect(self.clear_server)
        
    def clear_server(self):
        self.ui.serverip_server_page.setText("")
        self.ui.port_server_page.setText("")
        self.ui.buffersize_server_page.setText("")
        
    def enter_server(self):  
        try:
            ip=self.ui.serverip_server_page.text()
            port=int(self.ui.port_server_page.text())
            buf=int(self.ui.buffersize_server_page.text())
            
            self.server=server(ip,port)
            self.server.buffer_size=buf
            
            self.ui.server_stack.setCurrentWidget(self.ui.server_cpannel)
            self.cpannel()
            
        except:
            self.clear_server()
            self.ui.server_login_error_sheet.setVisible(True)   
    
    def cpannel(self):
        self.userlist_worker=userlist_thread()# thread of showing current users
        self.userlist_worker.start()
        self.userlist_worker.userlist_sin.connect(self.userlist)
        
        self.chat=live_chat()# thread of showing current chat
        self.chat.start()
        self.chat.chat_sin.connect(self.chatbox)
        
        self.ui.command_btn.clicked.connect(self.command)
        
        
    def chatbox(self,data):# return  chat list range max 10000
        data=self.ui.Server_chat.toPlainText()+"\n"+data
        self.ui.Server_chat.setPlainText(data)
        
    
    def userlist(self,test):# update user list in server tab per second 
            self.ui.user_list.setPlainText(test)
    
    def command(self):
        c=self.ui.command.text()
        c=c.split(" ")
        
        if c[0]=="kick":
            try:
                self.server.sock_list[int(c[1])].send("server : admin was kicked you form this chat".encode("utf-8"))
                name=self.server.ip_list[int(c[1])]
                print("kick running")
                self.server.remove(name)
                print("kick done")
                self.add_to_terminal(f"kicked => {name}")
                
            except Exception as e:
                self.add_to_terminal(f"ID *ERROR\nCKECK [ID] ==> {c[1]}  {e}")
            
        elif c[0]=="send":
           
            tmp=self.ui.Server_chat.toPlainText()
            msg=""
            for i in range(1,len(c)):
                msg+=c[i]+" "
            self.server.send_message(msg,"admin")
            data=f"*you : {msg}"
            tmp=self.ui.Server_chat.toPlainText()
            self.add_to_terminal(f"sended : {msg}")
            self.ui.Server_chat.setPlainText(tmp+"\n "+data)
            
        elif c[0]=="block":
            try:
                id=int(c[1])
                s=self.server.ip_list[id]
                self.server.block_list.append(s)
                self.add_to_terminal(f"{s} is blocked")
                self.server.sock_list[int(c[1])].send("server : admin was block you in this chat".encode("utf-8"))
                name=self.server.ip_list[int(c[1])]
                print("block running")
                self.server.remove(name)
                
            except Exception as e:
                self.add_to_terminal(f"ID *ERROR\nCKECK [ID] ==> {c[1]} {e} ")
                   
        elif c[0]=="unblock":
            try:
                id=int(c[1])
                self.server.block_list.pop(id)
                self.add_to_terminal(f"id {id} is unblocked...")
            except Exception as e:
                self.add_to_terminal(f"ID *ERROR\nCKECK [ID] ==> {c[1]} {e}")
                    
        elif c[0]=="block_list":
            t="====== blocked sockets======\n"
            x=0
            if len(self.server.block_list) !=0:
                for i in self.server.block_list:
                    t+=x+" :==> "+i+"\n"
                    x+=1
            else:
                t="NO BLOCKED sockets"
            
            self.add_to_terminal(t)     
        
        elif c[0]=="help":
            t="""
           [#] kick            : remove users form chat
           [#] block           : block users in chat
           [#] unblock         : unblock users in block list
           [#] block_list      : show list for block sockects
           [#] send            : send message to users as admin 
            
            """
            self.add_to_terminal(t)
                   
        else:
            self.add_to_terminal(f" *ERROR '{c[0]}' is not found...")
        self.ui.command.setText("")
        
    def add_to_terminal(self,data):
        tmp=self.ui.terminal_log.toPlainText()
        data=tmp+"\n"+data
        self.ui.terminal_log.setPlainText(data)
          
    
if __name__=="__main__":
    application=QApplication(sys.argv)
    myapp=app()
    sys.exit(application.exec_())