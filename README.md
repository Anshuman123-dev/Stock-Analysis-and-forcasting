# 📈 Stock Analysis and Forecasting Application

A powerful, interactive platform for stock market analysis and time series forecasting, built with Python and Streamlit. This application empowers traders and investors with advanced analytics, predictive modeling, and real-time market data visualization to make informed investment decisions.

## 🚀 Key Features

### Advanced Stock Analysis
- **Interactive Candlestick Charts**: Visualize price movements with configurable timeframes
- **Technical Indicators**: Over 20+ indicators including MACD, RSI, Bollinger Bands, and more
- **Volume Analysis**: Track trading volume patterns and their impact on price movements
- **Multiple Timeframe Analysis**: Switch between daily, weekly, and monthly views

### Predictive Analytics
- **Machine Learning Models**: ARIMA, LSTM, and Prophet models for price prediction
- **Sentiment Analysis**: Analyze market sentiment from news and social media
- **Volatility Forecasting**: Predict potential price movements and market volatility
- **Customizable Prediction Windows**: Forecast prices for different time horizons (1 day to 1 year)

### User Experience
- **Responsive Design**: Works seamlessly on desktop and tablet devices
- **Real-time Data**: Fetch and display the latest market data
- **Interactive Dashboards**: Customize your analysis with drag-and-drop components
- **Export Capabilities**: Download charts and data for further analysis

### Risk Management
- **Support & Resistance Levels**: Identify key price levels automatically
- **Risk/Reward Ratio Calculator**: Plan your trades effectively
- **Portfolio Simulation**: Test trading strategies with historical data
- **Performance Metrics**: Track and analyze your trading performance

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Time-Series-Project
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

   Note: For TA-Lib installation on Windows, you might need to download the appropriate wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib).

## Usage

1. Run the application:
   ```bash
   streamlit run Trading_App.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`

3. Use the sidebar to:
   - Enter a stock ticker symbol (e.g., AAPL, MSFT, GOOGL)
   - Select a date range for analysis
   - Choose different technical indicators
   - Toggle between different views and predictions

## Project Structure

```
Time-Series-Project/
├── Trading_App.py          # Main Streamlit application
├── pages/
│   ├── Stock_Analysis.py   # Stock analysis page
│   ├── Stock_Prediction.py # Stock prediction page
│   └── utils/              # Utility functions
│       ├── __init__.py
│       ├── model_train.py  # Model training utilities
│       └── plotly_figure.py# Plotting utilities
├── requirements.txt        # Project dependencies
└── README.md               # This file
```

## Dependencies

- Python 3.7+
- Streamlit
- yfinance
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- statsmodels
- TA-Lib
- plotly

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with ❤️ using Python and Streamlit
- Data provided by Yahoo Finance (yfinance)
- Special thanks to the open-source community for their valuable libraries and tools
