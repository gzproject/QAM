from System.Windows.Forms import Form, Button, AnchorStyles, Panel, DockStyle
from System.Drawing import Size, Point

WIDTH = 250
HEIGHT = 150
BUTTONS_SPACE = 15
PANEL_SPACE = 8
CLOSE_SPACE = 10


class window(Form):
    def __init__(self):
        self.Text = 'QAM'        
        self.Size = Size(WIDTH, HEIGHT)

        ok = Button()

        PANEL_HEIGHT = ok.Height + PANEL_SPACE

        panel = Panel()
        panel.Height = PANEL_HEIGHT
        panel.Dock = DockStyle.Bottom
        panel.Parent = self

        x = ok.Width * 2 + BUTTONS_SPACE
        y = (PANEL_HEIGHT - ok.Height) / 2

        ok.Text = "Ok"
        ok.Parent = panel
        ok.Location = Point(WIDTH-x, y)
        ok.Anchor = AnchorStyles.Right

        close = Button()
  
        x = close.Width

        close.Text = "Close"
        close.Parent = panel
        close.Location = Point(WIDTH-x-CLOSE_SPACE, y)
        close.Anchor = AnchorStyles.Right


        self.CenterToScreen()    