import streamlit as st
from core.risk_manager import RiskManager

def render_risk():
    st.title('Risk Manager')

    rm = RiskManager()

    bal = st.number_input('Balance',1000)
    risk = st.slider('Risk %',0.5,5.0,1.0)
    sl = st.number_input('Stop Loss',10)

    if st.button('Calculate'):
        st.success(rm.position_size(bal,risk,sl))
