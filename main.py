from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def search_image(self):
        # Get User Query from text input
        query = self.manager.current.screen.ids.user_query.text
        # Get wikipedia page and list of image urls
        page = wikipedia.page(query)
        image_link = page.images[0]
        return image_link

    def download_image(self):
        req = requests.get(self.get_image_link())
        imagepath = 'file/the_beach.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
            return imagepath

    def set_image(self):
        self.manager.current.screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
