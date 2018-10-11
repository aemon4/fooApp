# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:43:01 2018

@author: PC
"""

from flask_script import Manager
from fooApp.app import app

manager = Manager(app)
app.config['DEBUG'] = True # Ensure debugger will load.

if __name__ == '__main__':
  manager.run()