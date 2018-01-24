import sys
sys.path.append(r'C:\Python24\Lib')

import clr
clr.AddReference("System.Windows.Forms")

from System.Windows.Forms import Application, Form
from gui.window import window

form = window()
Application.Run(form)
