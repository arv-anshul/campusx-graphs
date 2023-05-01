""" All graphs provided by CampusX in DSMP Course """

import streamlit as st

st.set_page_config('CampusX Graphs.md', '🗒️', 'wide')

with open('README.md') as md:
    st.markdown(md.read())
