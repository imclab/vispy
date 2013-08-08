# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# This is a very minimal example that open a window and makes the background
# color to change from black to white to black ...
#
# The backend ('qt', 'glut', 'pyglet') should be chosen automatically depending
# on what is available on your machine.
# -----------------------------------------------------------------------------
import math
from vispy import app
from vispy import gl

class Canvas(app.Canvas):
    def __init__(self, *args, **kwargs):
        app.Canvas.__init__(self, *args, **kwargs)
        timer = app.Timer(1/60.0)
        timer.connect(self.on_timer)
        timer.start()
        self.tick = 0
        
    def on_paint(self, event):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        self.swap_buffers()
        
    def on_timer(self, event):
        self.tick += 1/60.0
        c = abs(math.sin(self.tick))
        gl.glClearColor(c,c,c,1)
        self.update()

if __name__ == '__main__':
    canvas = Canvas()
    canvas.show()
    app.run()
