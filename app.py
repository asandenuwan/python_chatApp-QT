from server import server 
from clint import client 
import sys,time
from gui import Ui_MainWindow 
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
##############################################################################################  thread

class msg_thraed(QThread):#clint msg box thread<<<<<<<<<<<<<<<<<<============ fix me
    msg=pyqtSignal(str)
    def run(self):
        self.t=""
        try:
            while (1):
                try:
                    self.t=myapp.clint.recive_message()
                    if not  self.t ==  False:
                        self.msg.emit(self.t)
                    time.sleep(0.5)
                except:
                    myapp.clint_stack.setCurrentWidget(myapp.userlogin_page)
                    myapp.clint.passme_flag=False
                    self.setTerminationEnabled(True)            
        except Exception as e:
            print("clint msg thread :>>>",e)
            
class userlist_thread(QThread):# id ckecing thread
    userlist_sin=pyqtSignal(str)
    
    def  run(self):
        try:
            while 1:
                text=""
                x=0
                print(myapp.server.ip_list)
                for i in myapp.server.ip_list:
                    text+=f"id  {x} -> "+i+"\n"
                    x+=1
                self.userlist_sin.emit(text)      
                time.sleep(1)
        except:pass

class live_chat(QThread):# server msg box thread
    chat_sin=pyqtSignal(str)
    def run(self):
        tmp=None
        try:
            while 1:
                try:
                    data=myapp.server.data
                    if tmp !=data[1]:
                        self.chat_sin.emit(data[0])
                        tmp=data[1]
                except:
                    pass
        except:
            pass
 
 ##############################################[------------------ application ---------------]##########################################################           
 

 
class app(QMainWindow):

        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 835)
        MainWindow.setStyleSheet("font: 20pt \"Jokerman\";\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(30, 69, 94);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Jokerman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setStyleSheet("color: rgb(0, 0, 127);\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.server_tab = QtWidgets.QWidget()
        self.server_tab.setStyleSheet("")
        self.server_tab.setObjectName("server_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.server_tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.server_stack = QtWidgets.QStackedWidget(self.server_tab)
        self.server_stack.setStyleSheet("font: 20pt \"Jokerman\";\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(30, 69, 94);")
        self.server_stack.setObjectName("server_stack")
        self.serverlogin_page = QtWidgets.QWidget()
        self.serverlogin_page.setObjectName("serverlogin_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.serverlogin_page)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.serverlogin_page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.serverip_server_page = QtWidgets.QLineEdit(self.frame_2)
        self.serverip_server_page.setObjectName("serverip_server_page")
        self.verticalLayout_2.addWidget(self.serverip_server_page)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.port_server_page = QtWidgets.QLineEdit(self.frame_2)
        self.port_server_page.setObjectName("port_server_page")
        self.verticalLayout_2.addWidget(self.port_server_page)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.buffersize_server_page = QtWidgets.QLineEdit(self.frame_2)
        self.buffersize_server_page.setObjectName("buffersize_server_page")
        self.verticalLayout_2.addWidget(self.buffersize_server_page)
        self.frame_12 = QtWidgets.QFrame(self.frame_2)
        self.frame_12.setStyleSheet("")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.server_login_error_sheet = QtWidgets.QLabel(self.frame_12)
        self.server_login_error_sheet.setEnabled(True)
        self.server_login_error_sheet.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.server_login_error_sheet.setObjectName("server_login_error_sheet")
        self.verticalLayout_13.addWidget(self.server_login_error_sheet)
        self.verticalLayout_2.addWidget(self.frame_12)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.serverlogin_page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.enterbtn_server_page = QtWidgets.QPushButton(self.frame)
        self.enterbtn_server_page.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enterbtn_server_page.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(156, 156, 117,255), stop:1 rgba(255, 255, 255, 25));")
        self.enterbtn_server_page.setAutoRepeatDelay(700)
        self.enterbtn_server_page.setObjectName("enterbtn_server_page")
        self.horizontalLayout_2.addWidget(self.enterbtn_server_page)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.clearbtn_server_page = QtWidgets.QPushButton(self.frame)
        self.clearbtn_server_page.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.clearbtn_server_page.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(200, 0, 0, 255), stop:1 rgba(255, 255, 255, 25));")
        self.clearbtn_server_page.setObjectName("clearbtn_server_page")
        self.horizontalLayout_2.addWidget(self.clearbtn_server_page)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 2)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout_3.setStretch(0, 5)
        self.verticalLayout_3.setStretch(1, 1)
        self.server_stack.addWidget(self.serverlogin_page)
        self.server_cpannel = QtWidgets.QWidget()
        self.server_cpannel.setObjectName("server_cpannel")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.server_cpannel)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.server_cpannel)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.user_list = QtWidgets.QPlainTextEdit(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.user_list.setFont(font)
        self.user_list.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.user_list.setStyleSheet("background-color: rgba(104, 104, 0,0.7);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Rockwell\";")
        self.user_list.setReadOnly(True)
        self.user_list.setTabStopWidth(1000)
        self.user_list.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.user_list.setCenterOnScroll(True)
        self.user_list.setObjectName("user_list")
        self.verticalLayout_5.addWidget(self.user_list)
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.Server_chat = QtWidgets.QPlainTextEdit(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Server_chat.setFont(font)
        self.Server_chat.setStyleSheet("background-color: rgba(104, 104, 0,0.7);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Rockwell\";")
        self.Server_chat.setReadOnly(True)
        self.Server_chat.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.Server_chat.setCenterOnScroll(True)
        self.Server_chat.setObjectName("Server_chat")
        self.verticalLayout_6.addWidget(self.Server_chat)
        self.horizontalLayout_4.addWidget(self.frame_7)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.server_cpannel)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.exit_server = QtWidgets.QPushButton(self.frame_4)
        self.exit_server.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.exit_server.setStyleSheet("background-color: rgb(217, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.exit_server.setObjectName("exit_server")
        self.verticalLayout_4.addWidget(self.exit_server)
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.terminal_log = QtWidgets.QPlainTextEdit(self.frame_4)
        self.terminal_log.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(150, 0, 112,0.7);\n"
"color: rgb(255, 255, 127);")
        self.terminal_log.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.terminal_log.setFrameShadow(QtWidgets.QFrame.Plain)
        self.terminal_log.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.terminal_log.setReadOnly(True)
        self.terminal_log.setPlainText("")
        self.terminal_log.setOverwriteMode(False)
        self.terminal_log.setTabStopWidth(199)
        self.terminal_log.setCursorWidth(1)
        self.terminal_log.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.terminal_log.setCenterOnScroll(True)
        self.terminal_log.setObjectName("terminal_log")
        self.verticalLayout_4.addWidget(self.terminal_log)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.command = QtWidgets.QLineEdit(self.frame_5)
        self.command.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.command.setObjectName("command")
        self.horizontalLayout_3.addWidget(self.command)
        self.command_btn = QtWidgets.QPushButton(self.frame_5)
        self.command_btn.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
"")
        self.command_btn.setObjectName("command_btn")
        self.horizontalLayout_3.addWidget(self.command_btn)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.server_stack.addWidget(self.server_cpannel)
        self.verticalLayout.addWidget(self.server_stack)
        self.tabWidget.addTab(self.server_tab, "")
        self.clint_tab = QtWidgets.QWidget()
        self.clint_tab.setStyleSheet("font: 20pt \"Jokerman\";\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(30, 69, 94);")
        self.clint_tab.setObjectName("clint_tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.clint_tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.clint_stack = QtWidgets.QStackedWidget(self.clint_tab)
        self.clint_stack.setStyleSheet("font: 20pt \"Jokerman\";\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(30, 69, 94);")
        self.clint_stack.setObjectName("clint_stack")
        self.userlogin_page = QtWidgets.QWidget()
        self.userlogin_page.setObjectName("userlogin_page")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.userlogin_page)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_8 = QtWidgets.QFrame(self.userlogin_page)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.frame_8)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.serverip_clint_page = QtWidgets.QLineEdit(self.frame_8)
        self.serverip_clint_page.setObjectName("serverip_clint_page")
        self.verticalLayout_9.addWidget(self.serverip_clint_page)
        self.label_11 = QtWidgets.QLabel(self.frame_8)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_9.addWidget(self.label_11)
        self.port_clint_page = QtWidgets.QLineEdit(self.frame_8)
        self.port_clint_page.setObjectName("port_clint_page")
        self.verticalLayout_9.addWidget(self.port_clint_page)
        self.label_9 = QtWidgets.QLabel(self.frame_8)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.buffersize_clint_page = QtWidgets.QLineEdit(self.frame_8)
        self.buffersize_clint_page.setObjectName("buffersize_clint_page")
        self.verticalLayout_9.addWidget(self.buffersize_clint_page)
        self.label_10 = QtWidgets.QLabel(self.frame_8)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.username_clint_page = QtWidgets.QLineEdit(self.frame_8)
        self.username_clint_page.setObjectName("username_clint_page")
        self.verticalLayout_9.addWidget(self.username_clint_page)
        self.verticalLayout_10.addWidget(self.frame_8)
        self.frame_13 = QtWidgets.QFrame(self.userlogin_page)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.server_login_error_sheet_2 = QtWidgets.QLabel(self.frame_13)
        self.server_login_error_sheet_2.setEnabled(True)
        self.server_login_error_sheet_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.server_login_error_sheet_2.setObjectName("server_login_error_sheet_2")
        self.verticalLayout_14.addWidget(self.server_login_error_sheet_2)
        self.verticalLayout_10.addWidget(self.frame_13)
        self.frame_9 = QtWidgets.QFrame(self.userlogin_page)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.enterbtn_clint_page = QtWidgets.QPushButton(self.frame_9)
        self.enterbtn_clint_page.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enterbtn_clint_page.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(156, 156, 117,255), stop:1 rgba(255, 255, 255, 25));")
        self.enterbtn_clint_page.setAutoRepeatDelay(700)
        self.enterbtn_clint_page.setObjectName("enterbtn_clint_page")
        self.horizontalLayout_5.addWidget(self.enterbtn_clint_page)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.clearbtn_clint_page = QtWidgets.QPushButton(self.frame_9)
        self.clearbtn_clint_page.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.clearbtn_clint_page.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(200, 0, 0, 255), stop:1 rgba(255, 255, 255, 25));")
        self.clearbtn_clint_page.setObjectName("clearbtn_clint_page")
        self.horizontalLayout_5.addWidget(self.clearbtn_clint_page)
        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 3)
        self.verticalLayout_10.addWidget(self.frame_9)
        self.verticalLayout_10.setStretch(0, 4)
        self.verticalLayout_10.setStretch(1, 1)
        self.verticalLayout_10.setStretch(2, 1)
        self.clint_stack.addWidget(self.userlogin_page)
        self.chatroom = QtWidgets.QWidget()
        self.chatroom.setObjectName("chatroom")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.chatroom)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_10 = QtWidgets.QFrame(self.chatroom)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.frame_10)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_11.addWidget(self.label_13)
        self.chat_pannel_clint_page = QtWidgets.QPlainTextEdit(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.chat_pannel_clint_page.setFont(font)
        self.chat_pannel_clint_page.setStyleSheet("background-color: rgba(150, 0, 112,0.7);\n"
"font: 75 12pt \"Segoe Print\";\n"
"color: rgb(255, 255, 127);")
        self.chat_pannel_clint_page.setReadOnly(True)
        self.chat_pannel_clint_page.setObjectName("chat_pannel_clint_page")
        self.verticalLayout_11.addWidget(self.chat_pannel_clint_page)
        self.verticalLayout_12.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.chatroom)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.frame_11)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.msgbox_clint_page = QtWidgets.QLineEdit(self.frame_11)
        self.msgbox_clint_page.setObjectName("msgbox_clint_page")
        self.horizontalLayout_6.addWidget(self.msgbox_clint_page)
        self.sendbtn_clint_page = QtWidgets.QPushButton(self.frame_11)
        self.sendbtn_clint_page.setStyleSheet("background-color: rgb(0, 227, 0);")
        self.sendbtn_clint_page.setObjectName("sendbtn_clint_page")
        self.horizontalLayout_6.addWidget(self.sendbtn_clint_page)
        self.clear_msg_btn_clint_page = QtWidgets.QPushButton(self.frame_11)
        self.clear_msg_btn_clint_page.setStyleSheet("background-color:rgb(0, 0, 112)")
        self.clear_msg_btn_clint_page.setObjectName("clear_msg_btn_clint_page")
        self.horizontalLayout_6.addWidget(self.clear_msg_btn_clint_page)
        self.verticalLayout_12.addWidget(self.frame_11)
        self.exit_chat = QtWidgets.QPushButton(self.chatroom)
        self.exit_chat.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.exit_chat.setStyleSheet("background-color: rgb(217, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.exit_chat.setObjectName("exit_chat")
        self.verticalLayout_12.addWidget(self.exit_chat)
        self.clint_stack.addWidget(self.chatroom)
        self.verticalLayout_8.addWidget(self.clint_stack)
        self.tabWidget.addTab(self.clint_tab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.server_stack.setCurrentIndex(0)
        self.clint_stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">SERVER IP</p></body></html>"))
        self.serverip_server_page.setText(_translate("MainWindow", "127.0.0.1"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">PORT</p></body></html>"))
        self.port_server_page.setText(_translate("MainWindow", "1234"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">BUFFEER SIZE[RECIVE]]</p></body></html>"))
        self.buffersize_server_page.setText(_translate("MainWindow", "1024"))
        self.server_login_error_sheet.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">ERROR</span></p></body></html>"))
        self.enterbtn_server_page.setText(_translate("MainWindow", "ENTER"))
        self.clearbtn_server_page.setText(_translate("MainWindow", "CLEAR"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">users</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">chat</p></body></html>"))
        self.exit_server.setText(_translate("MainWindow", "stop server"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">-----&lt;&lt;&lt;Terminal&gt;&gt;&gt;-----</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">command</span></p></body></html>"))
        self.command_btn.setText(_translate("MainWindow", "enter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.server_tab), _translate("MainWindow", "server"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">SERVER IP</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">PORT</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">BUFFER SIZE</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">USERNAME</p></body></html>"))
        self.server_login_error_sheet_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">ERROR</span></p></body></html>"))
        self.enterbtn_clint_page.setText(_translate("MainWindow", "ENTER"))
        self.clearbtn_clint_page.setText(_translate("MainWindow", "CLEAR"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">chat box</p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "messege: "))
        self.sendbtn_clint_page.setText(_translate("MainWindow", "send"))
        self.clear_msg_btn_clint_page.setText(_translate("MainWindow", "clear"))
        self.exit_chat.setText(_translate("MainWindow", "exit from chat"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.clint_tab), _translate("MainWindow", "client"))
  
    
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
                
        self.tabWidget.setCurrentWidget(self.server_tab)
        self.server_stack.setCurrentWidget(self.serverlogin_page)
        self.clint_stack.setCurrentWidget(self.userlogin_page)
        
        self.server_login_error_sheet.setVisible(False)
        
        self.show()
        
        self.server_login()
        self.clint_login()
        
####################################################################################################### close connet  side    
    
    def closeEvent(self, event):
        print("run me")
        try:self.closeclint()
        except:print("error clint close")
        try:self.closeserver()
        except:print("error server close")
        event.accept()
        
    def closeserver(self):
        self.server.closeserver()
         
        self.chat.setTerminationEnabled(True)
        self.userlist_worker.setTerminationEnabled(True)
        
        self.server_stack.setCurrentWidget(self.serverlogin_page)
        
        print("server closed")
    
    def closeclint(self):
        self.clint.sock.close()
        self.chat_reader.t=""
        self.clint.passme_flag=False
        self.chat_reader.setTerminationEnabled(True)
    
        self.clint_stack.setCurrentWidget(self.userlogin_page)    

        print("clint closed")
 
##################################################################################### clintside
    
    def clint_login(self):#client login begin
        self.server_login_error_sheet_2.setVisible(False)
        
        self.serverip_clint_page.setText("127.0.0.1")
        self.port_clint_page.setText("1234")
        self.username_clint_page.setText("myname")
        self.buffersize_clint_page.setText("1024")
        
        self.enterbtn_clint_page.clicked.connect(self.clint_login_enter)
    
        self.clearbtn_clint_page.clicked.connect(self.clear_clint)
    
    def clint_login_enter(self):#when client enter press 
        try:
            ip=self.serverip_clint_page.text()
            port=self.port_clint_page.text()
            us=self.username_clint_page.text()
            buf=self.buffersize_clint_page.text()
            
            self.clint=client(ip,int(port))
            self.clint.buffer_size=int(buf)
            self.msgbox_clint_page.setText("")
            self.chat_pannel_clint_page.setPlainText("")
            self.clint.send_message(f"$>2005command:{us}")
            
            
            self.clint_stack.setCurrentWidget(self.chatroom)#open client chat box
            try:self.sendbtn_clint_page.clicked.connect(self.msg_sender)#msg send button
            except Exception as e:print("send error ",e)
            self.exit_chat.clicked.connect(self.closeclint)# close server
            
            self.chat_reader=msg_thraed()#thread for catch resive msg
            self.chat_reader.start()
            self.chat_reader.msg.connect(self.chatbox_writer)
            
            self.clear_msg_btn_clint_page.clicked.connect(self.clearchat)
        except Exception as e:
            print("error log in ",e)
            self.server_login_error_sheet_2.setVisible(True)
            self.serverip_clint_page.setText("")
            self.port_clint_page.setText("")
            self.username_clint_page.setText("")
            self.buffersize_clint_page.setText("")
            
    def clearchat(self):
        self.chat_reader.t=""
        self.chat_pannel_clint_page.setPlainText("")
    
    def chatbox_writer(self,data):#write msg come form msg_tread
        x=self.chat_pannel_clint_page.toPlainText()
        self.chat_pannel_clint_page.setPlainText(data+"\n"+x)
        
    def msg_sender(self):
        msg=self.msgbox_clint_page.text()
        self.clint.send_message(msg)
        self.msgbox_clint_page.setText("")
         
    def clear_clint(self):#clear data in client pannel
        self.serverip_clint_page.setText("")
        self.username_clint_page.setText("")
        self.port_clint_page.setText("")
        self.buffersize_clint_page.setText("")
      
#####################################################################################server side  

    def server_login(self):
        self.enterbtn_server_page.clicked.connect(self.enter_server)
        self.clearbtn_server_page.clicked.connect(self.clear_server)
        
    def clear_server(self):
        self.serverip_server_page.setText("")
        self.port_server_page.setText("")
        self.buffersize_server_page.setText("")
        
    def enter_server(self):  
        try:
            ip=self.serverip_server_page.text()
            port=int(self.port_server_page.text())
            buf=int(self.buffersize_server_page.text())
            
            self.server=server(ip,port)
            self.server.buffer_size=buf
            
            self.server_stack.setCurrentWidget(self.server_cpannel)
            self.cpannel()
            
        except:
            self.clear_server()
            self.server_login_error_sheet.setVisible(True)   
    
    def cpannel(self):
        self.userlist_worker=userlist_thread()# thread of showing current users
        self.userlist_worker.start()
        self.userlist_worker.userlist_sin.connect(self.userlist)
        
        self.chat=live_chat()# thread of showing current chat
        self.chat.start()
        self.chat.chat_sin.connect(self.chatbox)
        
        self.command_btn.clicked.connect(self.commander)
        self.exit_server.clicked.connect(self.closeserver)
        
        
        
    def chatbox(self,data):# return  chat list range max 10000
        data=data+"\n"+self.Server_chat.toPlainText()
        self.Server_chat.setPlainText(data)
        
    
    def userlist(self,test):# update user list in server tab per second 
            self.user_list.setPlainText(test)
    
    def commander(self):
        c=self.command.text()
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
                print(e,"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-------")
            
                self.add_to_terminal(f"ID *ERROR\nCKECK [ID] ==> {c[1]}  {e}")
            
        elif c[0]=="send":
           
            tmp=self.Server_chat.toPlainText()
            msg=""
            for i in range(1,len(c)):
                msg+=c[i]+" "
            self.server.send_message(msg,"admin")
            data=f"*you : {msg}"
            tmp=self.Server_chat.toPlainText()
            self.add_to_terminal(f"sended : {msg}")
            self.Server_chat.setPlainText(data+"\n"+tmp)
            
        elif c[0]=="block":
            # try:
                id=int(c[1])
                
                b=self.server.sock_list[id]
                self.server.block_list.append(b)
                self.add_to_terminal(f"{id} is blocked")
                self.server.sock_list[int(c[1])].send("server : admin was block you in this chat".encode("utf-8"))
                name=self.server.ip_list[int(c[1])]
                print("block running")
                self.server.remove(name)
                
            # except Exception as e:
            #     self.add_to_terminal(f"ID *ERROR\nCKECK [ID] ==> {c[1]} {e} ")
                   
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
                    t+=str(x)+" :==> "+i+"\n"
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
        elif c[0]=="clear":
            self.terminal_log.setPlainText("")
        else:
            self.add_to_terminal(f" *ERROR '{c[0]}' is not found...")
        self.command.setText("")
        
    def add_to_terminal(self,data):
        tmp=self.terminal_log.toPlainText()
        data=tmp+"\n"+data
        self.terminal_log.setPlainText(data)
          
    
if __name__=="__main__":
    application=QApplication(sys.argv)
    myapp=app()
    sys.exit(application.exec_())