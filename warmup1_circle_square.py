"""
Warm-Up 1: Circle and Square

There's a bug in draw_circle_and_square() below: the circle is too
big for the square. Find and fix it.
"""
import dudraw


def draw_circle_and_square():
    """Draw a square with a circle inscribed exactly inside it.

    The circle should touch all four sides of the square, right in the
    middle, with no gap and no overlap. Run this once first and look
    at how far the circle pokes out past the square's edges.
    """
    center_x = 0.5
    center_y = 0.5
    half_side = 0.25

    dudraw.set_pen_color(dudraw.BLUE)
    dudraw.square(center_x, center_y, half_side)

    dudraw.set_pen_color(dudraw.RED)
    # BUG: this radius is too big, so the circle sticks out past the square.
    # What should the circle's radius be, in terms of half_side?
    radius = half_side * 1.5
    dudraw.circle(center_x, center_y, radius)


def main():
    dudraw.set_canvas_size(512, 512)
    dudraw.clear(dudraw.WHITE)
    dudraw.set_pen_width(0.01)
    draw_circle_and_square()
    dudraw.show(float("inf"))


if __name__ == "__main__":
    main()
