"""
Matrix based Linear Transformation
------
https://github.com/campusx-official/matrix-linear-transformation-viz/blob/master/linear.py
"""

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

from src.utils import *

st.set_page_config('Matrix Transformation', 'random', 'wide')

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
# Some important variables
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
text_kwarg = {
    'fontsize': 14,
    'fontweight': 800,
    'color': 'k',
    'verticalalignment': 'bottom',
    'horizontalalignment': 'right',
}


def arrow_kwarg(color: str): return {
    'head_width': 0.1,
    'head_length': 0.1,
    'fc': color,
    'ec': color,
    'linewidth': 3,
    'zorder': 2,
}


def draw_grid(ax: plt.Axes, lines, line_color='blue', alpha=1.0):
    """ Draw grid lines. """
    for start, end in lines:
        ax.plot([start[0], end[0]], [start[1], end[1]],
                line_color, alpha=alpha, zorder=1)


def generate_grid(n_line: int = 10):
    """ Generate grid lines. """
    grid_lines = []
    for x in np.linspace(-n_line, n_line, 2 * n_line + 1):
        for _ in np.linspace(-n_line, n_line, 2 * n_line + 1):
            grid_lines.append((np.array([x, -n_line]), np.array([x, n_line])))
            grid_lines.append((np.array([-n_line, x]), np.array([n_line, x])))
    return grid_lines


def transform_grid(matrix, grid_lines):
    """ Apply matrix transformation on grid lines. """
    return [(matrix @ start, matrix @ end) for start, end in grid_lines]


with st.sidebar:
    st.title('Linear Transformation')
    matrix = np.zeros((2, 2), int)
    matrix[0, 0] = st.number_input('Element (0, 0)', value=1, format='%d')
    matrix[0, 1] = st.number_input('Element (0, 1)', value=0, format='%d')
    matrix[1, 0] = st.number_input('Element (1, 0)', value=0, format='%d')
    matrix[1, 1] = st.number_input('Element (1, 1)', value=1, format='%d')

    to_show = st.radio('To  Show:', [None, 'Unit Vector', 'Mera Vector'])

    vec = np.zeros(2, int)
    if to_show == 'Mera Vector':
        vec[0] = st.number_input('Vector X-coordinate', value=0, format='%d')
        vec[1] = st.number_input('Vector y-coordinate', value=0, format='%d')

    transform_button = st.button('**Transform**', use_container_width=True)


# Create the plot
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

ax.hlines([0], -100, 100, linestyles='dotted', color='r', zorder=3)
ax.vlines([0], -100, 100, linestyles='dotted', color='r', zorder=3)

# Generate the original grid lines
grid_lines = generate_grid()

# Draw the original grid lines
draw_grid(ax, grid_lines, 'lightblue')

trf_vec = np.zeros(2, int)
if transform_button:
    # Apply the transformation to the grid lines
    trf_lines = transform_grid(matrix, grid_lines)

    # Draw the transformed grid lines
    draw_grid(ax, trf_lines, 'orange')

    # Draw the origin as a big dot
    ax.plot(0, 0, marker='o', markersize=10, color='k', zorder=3)

    if to_show == 'Mera Vector':
        trf_vec = matrix @ vec
        ax.arrow(0, 0, vec[0], vec[1], **arrow_kwarg('green'))
        ax.arrow(0, 0, trf_vec[0], trf_vec[1], **arrow_kwarg('purple'))

        ax.text(vec[0], vec[1], f'({vec[0]}, {vec[1]})', **text_kwarg)
        ax.text(trf_vec[0], trf_vec[1],
                f'({trf_vec[0]}, {trf_vec[1]})', **text_kwarg)

    if to_show == 'Unit Vector':
        # Transform the unit vectors
        trf_i = matrix @ np.array([1, 0])
        trf_j = matrix @ np.array([0, 1])

        # Draw the original unit vectors
        ax.arrow(0, 0, 1, 0, **arrow_kwarg('black'))
        ax.arrow(0, 0, 0, 1, **arrow_kwarg('black'))

        # Draw the transformed unit vectors
        ax.arrow(0, 0, trf_i[0], trf_i[1], **arrow_kwarg('brown'))
        ax.arrow(0, 0, trf_j[0], trf_j[1], **arrow_kwarg('brown'))

        # Add labels for unit vectors
        ax.text(1, 0, 'i', **text_kwarg)
        ax.text(0, 1, 'j', **text_kwarg)
        ax.text(trf_i[0], trf_i[1], 'i^', **text_kwarg)
        ax.text(trf_j[0], trf_j[1], 'j^', **text_kwarg)

plt.text(0.02, 0.98, str(matrix), {'fontweight': 800},
         transform=ax.transAxes, verticalalignment='top')
plt.title('Matrix Transformation')

st.pyplot(fig, True, True)
