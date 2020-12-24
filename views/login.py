from kivymd.app import MDApp
import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.button import MDRoundFlatButton
from kivy.properties import ObjectProperty
import sqlite3
from views.appframe import Screen2
# from android.permissions import request_permissions, Permission

# request_permissions([
#     Permission.CAMERA,
#     Permission.WRITE_EXTERNAL_STORAGE,
#     Permission.READ_EXTERNAL_STORAGE
# ])


class Connect():
    
    def __init__(self,parent=None):
        self.parent = parent
        # self.connect = sqlite3.connect("models/app.db")
        self.connect = "models/app.db"
    
        # self.conn = self.connect.cursor()
    
    def connect_now(self):
        return self.connect

        
class ScreenUtama(ScreenManager):

    def sign_in(self,username,password):
        print("helllo")
        self.get_db = Connect()
        self.conn = self.get_db.connect_now()
        self.username = username
        self.password = password
        self.db = sqlite3.connect(self.conn)
        self.cursor = self.db.cursor()
        self.cursor.execute("""SELECT * FROM Login WHERE username=? AND password =?;""",[self.username.text,self.password.text,])
        self.data = self.cursor.fetchall()
        # import pdb
        # pdb.set_trace()
        # print(self.data)
        if not self.data:
            print("Tidak ada data")
            self.username.text = ""
            self.password.text = ""
        else :
            print (self.data)
            self.screenmanager.current="screen2"
        self.screenmanager.current="screen2"

    
    def text_change(self,username):
        self.username = username
        # self.username.text =""

    def sign_up(self,*args):
        print("isinya data ")

class RunApp(MDApp):
    kv_directory="views/kv"


# class RunApp(MDApp):
#     kv_directory = "views/kv"
#     def build(self):
#         return Builder.load_file("views/kv/apaaja.kv")

