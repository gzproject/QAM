import sys
sys.path.append(r'C:\Python24\Lib')

import clr
clr.AddReference("System.Windows.Forms")

from System.Windows.Forms import Application, Form
from gui import gui

form = gui()
Application.Run(form)
