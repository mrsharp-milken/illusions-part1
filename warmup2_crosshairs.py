"""
Warm-Up 2: Crosshairs

draw_crosshairs() below only draws part of a "+". Finish it.
"""
import dudraw


def draw_crosshairs():
    """Draw a red '+' through the center of the canvas.

    Right now this only draws a line from the center to the right
    edge. Two things are missing:
      1. That line should span the FULL canvas, left edge to right edge.
      2. There should also be a vertical line spanning the full canvas.
    """
    center_x = 0.5
    center_y = 0.5

    dudraw.set_pen_color(dudraw.RED)
    # BUG: this only reaches from the center to the right edge.
    dudraw.line(center_x, center_y, 1, center_y)

    # TODO: add a vertical line through center_x, spanning the full
    # canvas from bottom (y=0) to top (y=1).


def main():
    dudraw.set_canvas_size(512, 512)
    dudraw.clear(dudraw.WHITE)
    dudraw.set_pen_width(0.02)
    draw_crosshairs()
    dudraw.show(float("inf"))


if __name__ == "__main__":
    main()
