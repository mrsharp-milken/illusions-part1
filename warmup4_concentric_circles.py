"""
Warm-Up 4: Darkening Concentric Circles

draw_concentric_circles() below draws 4 circles, all hardcoded by
hand. Rewrite it as a loop that draws NUM_CIRCLES circles instead.
"""
import dudraw

CENTER_X = 0.5
CENTER_Y = 0.5
MAX_RADIUS = 0.45
NUM_CIRCLES = 6
RING_STEP = MAX_RADIUS / NUM_CIRCLES
BRIGHTNESS_STEP = 35


def draw_concentric_circles():
    """Draw NUM_CIRCLES concentric filled circles that get darker toward the center.

    Look closely at the 4 circles below before changing anything:
      - Each circle's radius is MAX_RADIUS minus some multiple of RING_STEP.
      - Each circle's brightness is 35 less than the one before it.
    Both of those "some multiple of ___" and "35 less each time" are
    exactly what a loop counter (i) is good for. Replace all four
    calls below with a single loop that works for any NUM_CIRCLES,
    using BRIGHTNESS_STEP instead of the hardcoded 35.
    """
    dudraw.set_pen_color_rgb(250, 250, 250)
    dudraw.filled_circle(CENTER_X, CENTER_Y, MAX_RADIUS - 0 * RING_STEP)

    dudraw.set_pen_color_rgb(215, 215, 215)
    dudraw.filled_circle(CENTER_X, CENTER_Y, MAX_RADIUS - 1 * RING_STEP)

    dudraw.set_pen_color_rgb(180, 180, 180)
    dudraw.filled_circle(CENTER_X, CENTER_Y, MAX_RADIUS - 2 * RING_STEP)

    dudraw.set_pen_color_rgb(145, 145, 145)
    dudraw.filled_circle(CENTER_X, CENTER_Y, MAX_RADIUS - 3 * RING_STEP)

    # TODO: delete the 4 pairs of calls above and replace them with a
    # loop that draws NUM_CIRCLES circles, largest (and lightest) first.


def main():
    dudraw.set_canvas_size(512, 512)
    dudraw.clear(dudraw.WHITE)
    draw_concentric_circles()
    dudraw.show(float("inf"))


if __name__ == "__main__":
    main()
