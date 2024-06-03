import streamlit as st
import numpy as np
import plotly.graph_objects as go


st.markdown("<h1 style='text-align: center;'>Welcome Sir</h1>", unsafe_allow_html=True)
a=st.number_input("Enter the Fat you want",value=0.0)
b=st.number_input("Enter the Snf you want",value=0.0)
result = st.number_input("Enter total amount you want to make:", value=0, format="%d", key="result")
fat1 = st.number_input("Enter milk fat:", value=0.0, key="fat1")
fat2 = st.number_input("Enter Recon fat:", value=0.0, key="fat2")
snf1 = st.number_input("Enter milk snf:", value=0.0, key="snf1")
snf2 = st.number_input("Enter Recon snf:", value=0.0, key="snf2")


if st.button("Click Here"):
    x1 = np.linspace(10, result, 1000000)
    y1 = ((result * a) - (fat1 * x1)) / fat2
    x2 = np.linspace(10, result, 1000000)
    y2 = ((result * b) - (snf1 * x2)) / snf2

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x1, y=y1))
    fig.add_trace(go.Scatter(x=x2, y=y2))
    fig.update_layout(
        xaxis_title="Milk",
        yaxis_title="Recon",
        title="Milk and Recon Estimation"
    )

    st.plotly_chart(fig)

    
    for i in range(len(x2)):
        if abs(x2[i] - x1[i]) < 1 and abs(y2[i] - y1[i]) < 1:
            st.write(f"Milk: {int(x1[i])}")
            st.write(f"Recon: {int(y1[i])}")
            st.write(f"Water: {result - int(x1[i]) - int(y1[i])}")
            break
