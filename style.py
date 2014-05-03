import numpy as np
import pandas as pd
from bokeh.plotting import *
from bokeh.objects import Range1d

# Define some categories
categories = [
    'ousia', 'poson', 'poion', 'pros ti', 'pou',
    'pote', 'keisthai', 'echein', 'poiein', 'paschein',
]

# Create data
N = 10
data = { cat : np.random.randint(10, 100, size=N) for cat in categories }

# Define a little function to stack series together to make polygons. Soon
# this will be built into Bokeh.
def stacked(data, categories):
    ys = []
    last = np.zeros(len(data.values()[0]))
    for cat in categories:
        next = last + data[cat]
        ys.append(np.hstack((last[::-1], next)))
        last = next
    return ys

# Get the y coordinates of the stacked data
ys = stacked(data, categories)

# The x coordinates for each polygon are simply the series concatenated
# with its reverse.
xs = [np.hstack((categories[::-1], categories))] * len(ys)

# Pick out a color palette
colors = brewer["Spectral"][len(ys)]

# EXERCISE: output static HTML file
output_file("style.html")

# EXERCISE: play around with parameters like:
#   - line_color
#   - line_alpha
#   - line_width
#   - line_dash   (e.g., [2,4])
#   - fill_color
#   - fill_alpha
#   - background_fill
patches(
    xs,
    ys,
    x_range=categories,
    y_range=Range1d(start=0, end=800),
    color=colors,
    alpha=0.8,
    line_color="blue",
    line_alpha=.5,
    line_width=3,
    line_dash=[2,3],
    fill_color="purple",
    background_fill="lightgrey",
    title="Categories of Brewering"
)

# EXERCISE: configure all of the following plot properties
ygrid().grid_line_color = "blue"           # color, or None, to suppress the line
ygrid().grid_line_width = "red"           # line width for grid lines
axis().major_label_text_font_size = "10pt" # "12pt", "1.5em", "10px", etc
axis().major_label_text_font_style = "bold" # "bold", "normal", "italic"
axis().major_label_standoff =  1      # distance of tick labels from ticks
axis().axis_line_color =   "brown"          # color, or None, to suppress the line
xaxis().major_label_orientation = "horizontal"   # radians, "horizontal", "vertical", "normal"
xaxis().major_tick_in =   2           # distance ticks extends into the plot
xaxis().major_tick_out =   3          # and distance they extend out
xaxis().major_tick_line_color = "black"     # color, or None, to suppress the line

show()