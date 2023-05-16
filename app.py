
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("this is the app title")
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
st.markdown("this is the markdown")
st.header("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r'''a+a r ^ 1 + a r^2 + a r^3 ''')

df = pd.DataFrame(np.random.randn(500,2)/[50,50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(df)

rand=np.random.normal(1,2,size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins = 15)
st.pyplot(fig)
