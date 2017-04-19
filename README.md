# TableTalk
An interactive table that enhances your conversations.
A work-in-progress project developed through the DECO3850 course at the University of Queensland.

## Setup
1. Create a virtualenv
2. Put the Google Cloud Credentials json file (credentials.json) in the virtualenv directory
3. Add this line to the bottom of the `env/bin/activate` script

      ```export GOOGLE_APPLICATION_CREDENTIALS=$VIRTUAL_ENV/credentials.json```
      
      ```export GOOGLE_API_KEY="MY_API_KEY_HERE"```
 
4. Activate virtualenv: `source env/bin/activate`
5. Install dependencies for OSX (all required by Kivy & portaudio required by PyAudio): `brew install portaudio sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer`
6. Install requirements: `pip install -r requirements.txt`
7. Run using `python audio.py`
