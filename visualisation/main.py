'''
Basic Picture Viewer
====================

This simple image browser demonstrates the scatter widget. You should
see three framed photographs on a background. You can click and drag
the photos around, or multi-touch to drop a red dot to scale and rotate the
photos.

The photos are loaded from the local images directory, while the background
picture is from the data shipped with kivy in kivy/data/images/background.jpg.
The file pictures.kv describes the interface and the file shadow32.png is
the border to make the images look like framed photographs. Finally,
the file android.txt is used to package the application for use with the
Kivy Launcher Android application.

For Android devices, you can copy/paste this directory into
/sdcard/kivy/pictures on your Android device.

The images in the image directory are from the Internet Archive,
`https://archive.org/details/PublicDomainImages`, and are in the public
domain.

'''

import kivy
kivy.require('1.0.6')

from glob import glob
import os
from random import randint
from os.path import join, dirname
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock, mainthread
from kivy.uix.button import Button

from audio import AudioParser

# The list of mic names. These are the exact input names in System Preferences
# If you want to get the list of input names, run audio.py
MIC_NAMES = ["Built-in Microph"]
# MIC_NAMES = ["MOTU Mic 1", "MOTU Mic 2"]
# MIC_NAMES = ["MOTU Mic 1", "MOTU Mic 2", "MOTU Mic 3", "MOTU Mic 4"]

class Picture(Scatter):
    '''Picture is the class that will show the image with a white border and a
    shadow. They are nothing here because almost everything is inside the
    picture.kv. Check the rule named <Picture> inside the file, and you'll see
    how the Picture() is really constructed and used.

    The source property will be the filename to show.
    '''

    source = StringProperty(None)
    keyword = StringProperty(None)
    delete = ObjectProperty(None)	
    sentiment = StringProperty(None)
    mic = StringProperty(None)

    '''
    def __init__(self, **kwargs):
        super(Picture, self).__init__(**kwargs)
        sentiment = int(self.sentiment)
        if sentiment > 0:
            green = sentiment
            red = 0.0
        else: 
            red = sentiment
            green = 0.0
    '''

class PicturesApp(App):
    def build(self):
        # Create audio parser for each mic
        self.audioParsers = self.create_audio_parsers(MIC_NAMES)
        # Holds the Picture objects
        self.pictures = []
        self.load_pictures('test_data.txt')

    # The AudioParser calls this function once an image has been found for a keyword
    @mainthread
    def audio_completion(self, mic_name, keyword, sentiment, url):
        try:
            picture = Picture(source=url, keyword=keyword, sentiment=str(sentiment), mic=mic_name, rotation=randint(-15, 15), pos=(0,0), delete=self.remove_picture)
            self.pictures.append(picture)
            self.root.add_widget(picture)
        except Exception as e:
            Logger.exception('Pictures: Unable to load <%s>' % url)    
             
    # Removes a picture from the screen
    def remove_picture(self, widget):
        # TODO fix button visual
        root = self.root
        root.remove_widget(widget)
    
    def on_start(self):
        pass
                
    def on_pause(self):
        return True

    def on_stop(self):
        for parser in self.audioParsers:
            parser.stop_listening()
        os.remove(self.imgList)

    # Returns an array of audio parsers 
    def create_audio_parsers(self, deviceList):
        audioParsers = []

        # Iterates through list of device names we want to use
        for name in deviceList:
            parser = AudioParser(name, self.audio_completion)
            parser.start_listening()
            audioParsers.append(parser)
        return audioParsers

    # Adds a tonne of test pictures to the view. Used for testing purposes
    def load_pictures(self, filePath):
        with open(filePath) as f:
            for line in f:
                currentLine = line.split("|") # '|' is not used in URLs
                keyword = currentLine[0]
                sentiment = currentLine[1]
                mic = currentLine[2]
                url = currentLine[3]
                try:
                    picture = Picture(keyword=keyword, sentiment=sentiment, mic=mic, source=url, 
                            rotation=randint(-15, 15), pos=(0,0), delete=self.remove_picture)
                    self.root.add_widget(picture)
                except Exception as e:
                    Logger.exception('Pictures: Unable to load <%s>' % url)

    # Save the current pictures to a file
    def save_pictures(self, filePath):
        with open(filePath, 'a') as f:
            for picture in self.pictures:
                f.write(picture.keyword + '|' + picture.sentiment + '|' + picture.mic + '|' + picture.source + '\n')
         
if __name__ == '__main__':
    PicturesApp().run()
