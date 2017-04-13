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
from kivy.clock import Clock

class Picture(Scatter):
    '''Picture is the class that will show the image with a white border and a
    shadow. They are nothing here because almost everything is inside the
    picture.kv. Check the rule named <Picture> inside the file, and you'll see
    how the Picture() is really constructed and used.

    The source property will be the filename to show.
    '''

    source = StringProperty(None)


class PicturesApp(App):

    def build(self):

        # the root is created in pictures.kv
        root = self.root

        # get any files into images directory
        curdir = dirname(__file__)
        self.currentimages = {'foo','bar'}
        testpos = 0
        for filename in glob(join(curdir, 'images', '*')):
            try:
                self.currentimages.add(filename)
                # load the image
                picture = Picture(source=filename, pos=(100,testpos))
                # add to the main field
                root.add_widget(picture)
                testpos += 100
            except Exception as e:
                Logger.exception('Pictures: Unable to load <%s>' % filename)

    def fetch_images(self, *args):
        root = self.root

        curdir = dirname(__file__)
        for filename in glob(join(curdir, 'images', '*')):
            if filename not in self.currentimages:
                try:
                    self.currentimages.add(filename)
                    # load the image
                    picture = Picture(source=filename, rotation=randint(-100, 100), pos=(randint(0,1000),randint(0,1000)))
                    # add to the main field
                    root.add_widget(picture)
                except Exception as e:
                    Logger.exception('Pictures: Unable to load <%s>' % filename)

    def on_start(self):
        event = Clock.schedule_interval(self.fetch_images, 0.2)


    def on_pause(self):
        return True

    def on_stop(self):
        curdir = dirname(__file__)
        for filename in glob(join(curdir, 'images', '*')):
            os.remove(filename)



if __name__ == '__main__':
    PicturesApp().run()
