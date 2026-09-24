"""
Run this file first, before touching any of the warm-ups, to confirm
dudraw is installed and working.

    python3 test_dudraw.py

You should see a window pop up with a red circle in the middle. Close
the window when you're done -- it will stay open until you close it.
"""
import dudraw

dudraw.set_canvas_size(400, 400)
dudraw.set_pen_color(dudraw.RED)
dudraw.filled_circle(0.5, 0.5, 0.2)
dudraw.show(float("inf"))
