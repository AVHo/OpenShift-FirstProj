#!/usr/bin/python
import os

virtenv = os.environ['APPDIR'] + '/env/'    # THIS LINE EDITED
#os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.7/site-packages') #This LINE added
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

# The followind writes Flask code; it replaced all the rest of the code that was there before

from flask import Flask, render_template
from flask_flatpages import FlatPages

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

application = Flask(__name__)
application.config.from_object(__name__)
pages = FlatPages(application)

@application.route('/')
def index():
	#return app.root_path
    return render_template('index.html', pages=pages)

@application.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

#
# Below for testing only
#
if __name__ == '__main__':
    application.run(port=8000)
