"""
Warm-Up 3: Random Colored Rectangles

draw_random_rectangles() below has two bugs. Both are examples of the
same mistake: something that should happen freshly EVERY time through
the loop is instead only happening once, outside of it.
"""
import random

import dudraw

RECT_HALF_WIDTH = 0.03
NUM_RECTANGLES = 3  # BUG: too few to cover the canvas
SPACING = 0.05  # BUG: too small -- rectangles end up overlapping


def new_random_color():
    """Return a randomly chosen dudraw color. (Nothing to fix here.)"""
    return random.choice(
        [dudraw.RED, dudraw.ORANGE, dudraw.YELLOW, dudraw.GREEN, dudraw.BLUE, dudraw.MAGENTA]
    )


def draw_random_rectangles():
    """Draw vertical rectangles of random colors, evenly spaced across the canvas.

    For everything in this function, ask: does this need to happen
    ONCE, or EVERY TIME through the loop?
    """
    # BUG: new_random_color() is only called once here, so every
    # rectangle ends up the same color. It needs to be called again
    # for each rectangle.
    color = new_random_color()

    for i in range(NUM_RECTANGLES):
        dudraw.set_pen_color(color)
        x = 0.2 + i * SPACING
        dudraw.filled_rectangle(x, 0.5, RECT_HALF_WIDTH, 0.5)

    # Once colors and spacing are fixed, try changing NUM_RECTANGLES
    # and SPACING and re-running -- your loop should still work.


def main():
    dudraw.set_canvas_size(512, 512)
    dudraw.clear(dudraw.WHITE)
    draw_random_rectangles()
    dudraw.show(float("inf"))


if __name__ == "__main__":
    main()
