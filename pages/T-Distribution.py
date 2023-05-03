"""
Display thee difference between Normal Distribution and T-Distribution.

https://github.com/campusx-official/normal-distribution-vs-t-distribution/blob/master/app.py
"""

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from scipy.stats import norm, t

from src.utils import *

TITLE = 'Normal VS t-Distribution'

st.set_page_config(TITLE, 'random', 'wide', 'expanded')

st.markdown(H2C % TITLE, True)
description = st.empty()

# Input values
with st.sidebar:
    st.header('Input Parameters')
    deg_of_freedom = st.slider('Degrees of Freedom', 0, 100, 5, 2)

    if not st.button('**Show**', use_container_width=True):
        md = get_readme_txt(Path('descriptions/t_statistics.md'))
        description.markdown(md)
        st.stop()

# Generate data for normal distribution
x = np.linspace(-5, 5, 1000)
y_norm = norm.pdf(x)

# Generate data for t-distribution
y_t = t.pdf(x, df=deg_of_freedom)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, y_norm, label='Normal Distribution', color='b')
ax.plot(
    x, y_t, label=f"Student's t-Distribution (df={deg_of_freedom})", color='r'
)
ax.set_xlabel('x')
ax.set_ylabel('Probability Density')
ax.set_title('Normal VS t-Distribution Comparison')
ax.legend()

# Display the plot
st.pyplot(fig)
