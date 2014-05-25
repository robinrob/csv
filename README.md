#Python App
Python App is a template Python application which contains an example of parsing input arguments.


# Installation on OS X

##Install Pythonbrew:
- sudo easy_install pythonbrew 
- pythonbrew_install

Instructions from: http://www.howopensource.com/2011/05/how-to-install-and-manage-different-versions-of-python-in-linux/

##Install Python2.7:
This is necessary purely to run the Fabric tool as it has not been ported to Python3 yet!

- pythonbrew install 2.7

## Install Fabric:
- pythonbrew use 2.7
- pip install fabric
						
##Setup the template project
- fab install