# app.py

import streamlit as st
import requests
import time

st.set_page_config(page_title="코인 시세 조회", layout="wide")

st.title("🪙 실시간 코인 시세 (Binance API)")
symbol = st.selectbox("조회할 코인 페어 선택", ["BTCUSDT", "ETHUSDT", "SOLUSDT"])

def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    res = requests.get(url)
    return float(res.json()["price"])

placeholder = st.empty()

refresh_sec = st.slider("업데이트 주기 (초)", 1, 30, 5)

while True:
    price = get_price(symbol)
    with placeholder.container():
        st.metric(label=f"{symbol} 현재가", value=f"{price:,.2f} USDT")
    time.sleep(refresh_sec)
