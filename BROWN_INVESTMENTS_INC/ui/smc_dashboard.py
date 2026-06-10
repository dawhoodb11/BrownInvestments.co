import streamlit as st
from core.smc_engine import SMC
import yfinance as yf

def render_smc():
    st.title('SMC Engine')

    smc = SMC()
    data = yf.download('BTC-USD', period='5d', interval='1h')

    st.write(smc.detect_bos(data))
    st.write(smc.detect_choch(data))
    st.write(smc.detect_fvg(data))
    st.write(smc.detect_liquidity_sweep(data))
    st.write(smc.detect_order_blocks(data))
