"""
Original Script of CampusX:

https://github.com/campusx-official/confidence-interval-viz/blob/master/app.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from scipy.stats import norm, t

from src import utils

# Page config
st.set_page_config('Confidence Interval Simulation', 'random', 'wide')

st.markdown(utils.H3C % 'Confidence Interval Simulation', True)
description = st.empty()

with st.sidebar:
    method = st.selectbox('Method', ['Z with sigma', 'Z with s', 'T with s'])
    sample_size = st.slider('Sample Size', 2, 100, 10, 2)
    pop_mean = st.slider('Population Mean', 0, 100, 50, 2)
    pop_std = st.slider('Population Standard Deviation', 5, 100, 15, 5)
    n_sim = st.slider('Number of Simulations', 10, 1000, 100, 10)
    conf_level = st.slider('Confidence Level (%)', 50, 99, 95, 5)

    if not st.button('**Show**', use_container_width=True):
        md = utils.get_readme_txt(Path('descriptions/confidence_interval.md'))
        description.markdown(md)
        st.stop()

# Run simulations
np.random.seed(42)
n_interval = 0
lower_bounds = []
upper_bounds = []

for _ in range(n_sim):
    # Generate random samples from the population
    sample = np.random.normal(loc=pop_mean, scale=pop_std, size=sample_size)

    # Compute confidence interval based on the selected method
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)

    if method == 'Z with sigma':
        critical_value = norm.ppf((1 + conf_level / 100) / 2)
        margin_of_error = critical_value * (pop_std / np.sqrt(sample_size))
    elif method == 'Z with s':
        critical_value = norm.ppf((1 + conf_level / 100) / 2)
        margin_of_error = critical_value * (sample_std / np.sqrt(sample_size))
    elif method == 'T with s':
        critical_value = t.ppf((1 + conf_level / 100) / 2, df=sample_size - 1)
        margin_of_error = critical_value * (sample_std / np.sqrt(sample_size))
    else:
        raise UnboundLocalError

    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error

    lower_bounds.append(lower_bound)
    upper_bounds.append(upper_bound)

    # Check if the confidence interval captured the population mean
    if lower_bound <= pop_mean <= upper_bound:
        n_interval += 1

# Plot results
plt.figure(figsize=(10, 5))

# Plot and connect the lower and upper bounds with a line
for i in range(n_sim):
    if lower_bounds[i] <= pop_mean <= upper_bounds[i]:
        color = 'blue'
    else:
        color = 'orange'
    plt.plot([i, i], [lower_bounds[i], upper_bounds[i]], color=color)

plt.hlines(pop_mean, 0, n_sim, colors=['r'], label='Population Mean')

plt.scatter(range(n_sim), lower_bounds, 100, label='Lower Bound', marker='_')
plt.scatter(range(n_sim), upper_bounds, 100, label='Upper Bound', marker='_')
plt.legend()

st.pyplot(plt.gcf())

st.write(
    utils.H2C % f'{n_interval} mean captured out of {n_sim} simulations',
    utils.H2C % f'About ({100*n_interval / n_sim:.2f}%)',
    unsafe_allow_html=True
)
