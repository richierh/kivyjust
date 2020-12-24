from kivymd.app import MDApp
from kivy.lang import Builder
import kivy

from android.permissions import request_permissions, Permission

request_permissions([
    Permission.CAMERA,
    Permission.WRITE_EXTERNAL_STORAGE,
    Permission.READ_EXTERNAL_STORAGE
])

kv = """
#:import ZBarCam kivy_garden.zbarcam.ZBarCam
BoxLayout:
    orientation: 'vertical'
    ZBarCam:
        id: zbarcam
        # optional, by default checks all types
        code_types: 'QRCODE', 'EAN13'
    Label:
        size_hint: None, None
        size: self.texture_size[0], 50
        text: ', '.join([str(symbol.data) for symbol in zbarcam.symbols])
"""

class RunApp(MDApp):


    def build(self):

        return Builder.load_string(kv)


if __name__=="__main__":
    RunApp().run()