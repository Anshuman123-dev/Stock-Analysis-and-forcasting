import streamlit as st
# Assuming 'model_train' is a custom module name
from pages.utils.model_train import get_data, get_rolling_mean, get_differencing_order, scaling, evaluate_model, get_forecast, inverse_scaling 
import pandas as pd
# Assuming 'plotly_figure' is a custom module with these functions
from pages.utils.plotly_figure import plotly_table, Moving_average_forecast

st.set_page_config(
    page_title="Stock Prediction",
    page_icon=":chart_with_downwards_trend:",
    layout="wide",
)

st.title("Stock Prediction")

col1, col2, col3 = st.columns(3)

# Popular stock tickers
popular_stocks = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Google': 'GOOGL',
    'Amazon': 'AMZN',
    'Tesla': 'TSLA',
    'Meta (Facebook)': 'META',
    'NVIDIA': 'NVDA',
    'Netflix': 'NFLX',
    'AMD': 'AMD',
    'Intel': 'INTC',
    'Coca-Cola': 'KO',
    'Disney': 'DIS',
    'Nike': 'NKE',
    'Visa': 'V',
    'Mastercard': 'MA',
    'JPMorgan': 'JPM',
    'Bank of America': 'BAC',
    'Walmart': 'WMT',
    'Pfizer': 'PFE',
    'Johnson & Johnson': 'JNJ'
}

with col1:
    stock_name = st.selectbox("Select Stock", list(popular_stocks.keys()), index=0)
    ticker = popular_stocks[stock_name]

rmse = 0 # This line is from image 8f08f7.png, though it's immediately recalculated

st.subheader('Predicting Next 30 days Close Price for: ' + stock_name + ' (' + ticker + ')')

close_price = get_data(ticker)
rolling_price = get_rolling_mean(close_price)
differencing_order = get_differencing_order(rolling_price)
scaled_data, scaler = scaling(rolling_price)
rmse = evaluate_model(scaled_data, differencing_order)

st.write("**Model RMSE Score:**", rmse)

forecast = get_forecast(scaled_data, differencing_order)

forecast['Close'] = inverse_scaling(scaler, forecast['Close'])
st.write('#### Forecast Data (Next 30 days)')
fig_tail = plotly_table(forecast.sort_index(ascending = True).round(3))
fig_tail.update_layout(height = 220)
st.plotly_chart(fig_tail, use_container_width=True)

forecast = pd.concat([rolling_price, forecast])

# Show recent data - last 180 days of historical + 30 forecast days
total_length = len(forecast)
show_length = min(total_length, 210)  # Max 210 days (180 historical + 30 forecast)
if show_length < total_length:
    forecast_to_show = forecast.iloc[-show_length:]
else:
    forecast_to_show = forecast

st.plotly_chart(Moving_average_forecast(forecast_to_show), use_container_width=True)