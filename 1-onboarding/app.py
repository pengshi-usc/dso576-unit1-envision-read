# Streamlit smoke test — confirms Streamlit runs and opens in your browser.
# Run it from the repo root with:   uv run streamlit run 1-onboarding/app.py
# Your browser should open showing a chart. Press Ctrl + C in the terminal to stop it.

import streamlit as st
import pandas as pd
import numpy as np

st.title("Setup works! 🎉")
st.write("If you can see this page and the chart below, your environment is ready.")

df = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(df)
