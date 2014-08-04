sentence-relater
================

SuggestU's sentence-relater API

For Demo, [click here](http://suggestu.cloudapp.net/animal%20loves%20milk/a%20cat/)

***

###DEPLOYMENT NOTES

- For production server, ensure that:

  1. In config.py: ```PORT = 80``` OR whatever you want it to be.
  2. In config.py: ```DEBUG = False``` (to prevent 'restart with reloading')
  3. (Optionally) In ./start: ```COMMAND="sudo python run.py"``` is not commented out.
     (in case you decide to run it on port 80)
  
  Tip: Use ```$ nohup ./start``` for a quick deployment. And change your secret/CSRF keys.

- For Development server (Recommended: Skip step-2), ensure that:
  
  1. In config.py: ```PORT = 5000```
  2. (Optionally) In config.py: ```DEBUG = True```
     - setting ```DEBUG = True``` loads the app twice. And we're loading a huge vector space.

  3. In config.py: ```COMMAND="sudo python run.py"``` is commented
     (i.e., run app without sudo)