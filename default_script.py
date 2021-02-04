import pandas as pd
import numpy as np
import streamlit as st

df = pd.DataFrame({f"col_{i+1}": np.random.random(size=5) for i in range(30)})
expander = st.beta_expander("Look at the bug", True)
expander.table(df)

