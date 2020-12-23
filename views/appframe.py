from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.zbarcam import ZBarCam


class Screen2(Screen):

    def click(self):
        print("okay")
    

    def camera_on(self):
        self.ids.switchscreen.current = "Tampilkan Camera"
        pass



class ContentNavigationDrawer(BoxLayout):
    pass