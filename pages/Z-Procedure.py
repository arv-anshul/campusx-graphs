"""
Calculate Confidence Interval using Z-Procedure.

https://github.com/campusx-official/z-distribution-confidence-interval/blob/master/confidence-interval.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from scipy.stats import norm

from src import utils
from src.utils import H2C, NBSP

# Page config
st.set_page_config('CI using Z-Procedure', 'random', 'wide', 'expanded')

st.markdown(
    H2C % 'Confidence interval for a population mean using Z-procedure', True
)
description = st.empty()

with st.sidebar:
    conf_level = st.slider('Confidence Level (%)', 0, 99, 95, 5)
    sample_mean = st.number_input('Sample Mean', value=30, format='%d')
    pop_std = st.number_input('Population Standard Dev', value=10, format='%d')
    sample_size = st.number_input('Sample Size', 1, value=30, format='%d')

    if not st.button('**Show**', use_container_width=True):
        md = utils.get_readme_txt(Path('descriptions/z_procedure.md'))
        description.markdown(md)
        st.stop()

# Calculate the critical value (z-score) and margin of error
z_score = norm.ppf(1 - (1 - conf_level / 100) / 2)
margin_of_error = z_score * (pop_std / np.sqrt(sample_size))

# Calculate the confidence interval
lower_limit = sample_mean - margin_of_error
upper_limit = sample_mean + margin_of_error

# Display results
values_txt = (
    f':red[Critical Value (z-score):] {z_score:.2f}'
    f'{NBSP * 8}'
    f':red[Margin of Error:] {margin_of_error:.2f}'
    f'{NBSP * 8}'
    f':red[Confidence Interval:] ({lower_limit:.2f}, {upper_limit:.2f})'
)
st.subheader(values_txt)

# Plot the confidence interval
fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(['Lower Limit', 'Upper Limit'], [lower_limit, upper_limit], color='lightblue')
ax.plot(['Lower Limit', 'Upper Limit'], [lower_limit, upper_limit], color='red', linewidth=2)
ax.axhline(sample_mean, color='green', linestyle='--', label='Sample Mean')

ax.set_ylabel('Value')
ax.set_title('Confidence Interval')
ax.legend()

st.pyplot(fig)