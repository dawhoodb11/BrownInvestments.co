import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

def render_dashboard():
    st.title('Market Dashboard')

    symbol = st.selectbox('Asset', ['BTC-USD','EURUSD=X','XAUUSD=X'])

    data = yf.download(symbol, period='1mo', interval='1h')

    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close']
    )])

    fig.update_layout(template='plotly_dark')

    st.plotly_chart(fig, use_container_width=True)

    st.metric('Market Bias','Bullish','+1.2%')
    st.metric('Risk Exposure','2.1%')
