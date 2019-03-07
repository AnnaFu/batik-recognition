import kivy
import os
import match #algorithm for image detection
kivy.require('1.10.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.carousel import Carousel
from kivy.factory import Factory
from kivy.uix.image import AsyncImage, Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty

# Declare both screens
class HomeScreen(Screen): 
	pass

class UploadScreen(Screen):
	mIndex = StringProperty(rebind=True)
	img_path = StringProperty(rebind=True)
	

	def show_select(self):
		self.ids['imgpath_label'].text = self.ids['icon_flc'].selection[0]

	def upload_image(self):
		self.img_path = self.ids['icon_flc'].selection[0]
		#print("upload image img_path = ", self.img_path)
		self.mIndex = match.doing([self.img_path])
		#print("upload image mIndex = ", self.mIndex)
		self.manager.current = 'DescScreen'

class StoryScreen(Screen):
	motif = StringProperty('')

	def k_click(self):
		self.motif = "kawung"
		self.manager.current = 'MotifScreen'

	def m_click(self):
		self.motif = "megaMendung"
		self.manager.current = 'MotifScreen'

	def p_click(self):
		self.motif = "parang"
		self.manager.current = 'MotifScreen'

	def sm_click(self):
		self.motif = "sidomuktiMagetan"
		self.manager.current = 'MotifScreen'
	

class DescScreen(Screen): #description screen
	mIndex = StringProperty(rebind=True)
	img_path = StringProperty(rebind=True)
	title = StringProperty('')
	intro = StringProperty('')
	history = StringProperty('')
	meaning = StringProperty('')

	def on_img_path(self, instance, value):
		print("masuk img path")
		print("desc screen img path : ", self.img_path, "\n mIndex", self.mIndex)
		self.ids['user_img'].source = self.img_path

	def on_mIndex(self, instance, value):
		desc_path = 'desc/' + value + '.txt'
		print(desc_path, self.img_path)
		carousel_folder = 'pic/' + value + '/'
		self.ids.carousel.clear_widgets()
		for i in range(1,11):
			img_src = carousel_folder + '%s.jpg' % str(i)
			image = Factory.AsyncImage(source=img_src, allow_stretch=True)
			self.ids.carousel.add_widget(image)
		with open('desc/' + value + '.txt', 'r') as content_file:
			self.title, self.intro, self.history, self.meaning = [line.rstrip() for line in content_file.read().split('/')]
		Clock.schedule_interval(self.ids.carousel.load_next, 3)

class MotifScreen(Screen):
	motif = StringProperty('')
	mtitle = StringProperty('')
	mintro = StringProperty('')
	mhistory = StringProperty('')
	mmeaning = StringProperty('')

	def on_motif(self, instance, value):
		print(value)
		self.ids.mcar.clear_widgets()
		desc_path = 'desc/' + value + '.txt'
		carousel_folder = 'pic/' + value + '/'
		for i in range(1,11):
			img_src = carousel_folder + '%s.jpg' % str(i)
			image = Factory.AsyncImage(source=img_src, allow_stretch=True)
			self.ids.mcar.add_widget(image)
		with open('desc/' + value + '.txt', 'r') as content_file:
			self.mtitle, self.mintro, self.mhistory, self.mmeaning = [line.rstrip() for line in content_file.read().split('/')]
		Clock.schedule_interval(self.ids.mcar.load_next, 3)
	
class ScreenManagement(ScreenManager):
	pass


class BatikApp(App):
	def build(self):
		presentation = Builder.load_file("Batik.kv")
		return presentation

if __name__ == "__main__":
    BatikApp().run()