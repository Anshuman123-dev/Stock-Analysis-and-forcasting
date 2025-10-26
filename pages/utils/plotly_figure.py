import plotly.graph_objects as go
import dateutil
import pandas as pd
import ta
import datetime

def plotly_table(dataframe):
    headerColor = 'grey'
    rowEvenColor = '#f0fafd'
    rowOddColor = '#e1efff'

    # Format column headers - handle datetime columns properly
    header_values = ['<b>Date</b>'] + ['<b>' + str(col) + '</b>' for col in dataframe.columns]
    
    # Format cell values - transpose data for proper display
    cell_values = [['<b>' + str(idx).split()[0] + '</b>' for idx in dataframe.index]]
    for col in dataframe.columns:
        cell_values.append(dataframe[col].values)

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=header_values,
            line_color='#0078ff', fill_color='#0078ff',
            align='center', font=dict(color='white', size=15), height=35,
        ),
        cells=dict(
            values=cell_values, 
            fill_color = [[rowOddColor if i % 2 == 0 else rowEvenColor for i in range(len(dataframe))]],
            align='left', line_color='white', font=dict(color='black', size=13), height=30
        )
    )])
    
    fig.update_layout(height=400, margin=dict(l=0, r=0, t=0, b=0))
    return fig

def filter_data(dataframe, num_period):
    if num_period == '1mo':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(months=-1)
    elif num_period == '5d':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(days=-5)
    elif num_period == '6mo':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(months=-6)
    elif num_period == '1y':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(years=-1)
    elif num_period == '5y':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(years=-5)
    elif num_period == 'ytd':
        date = datetime.datetime(dataframe.index[-1].year, 1,1).strftime('%Y-%m-%d')
    else:
        date = dataframe.index[0]
    
    return dataframe.reset_index()[dataframe.reset_index()['Date']>date]

# From images 8ea782.png and 8ea7ff.png
def close_chart(dataframe, num_period = False):
    if num_period:
        dataframe = filter_data(dataframe,num_period)
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Open'],
        mode='lines',
        name='Open', line = dict(width=2, color = '#5ab7ff')))
    
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Close'],
        mode='lines',
        name='Close', line = dict(width=2,color = 'black')))
    
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['High'],
        mode='lines', name='High', line = dict(width=2,color = '#0078ff')))
    
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Low'],
        mode='lines', name='Low', line = dict(width=2,color = 'red')))
    
    fig.update_xaxes(
        title_text='Date',
        showgrid=True,
        gridcolor='#E5E5E5',
        rangeslider_visible=True
    )
    fig.update_yaxes(
        title_text='Price ($)',
        showgrid=True,
        gridcolor='#E5E5E5'
    )
    fig.update_layout(
        title=dict(text='Stock Price Chart', font=dict(size=16, color='#333'), x=0.5, xanchor='center'),
        height=500,
        margin=dict(l=60, r=40, t=60, b=40),
        plot_bgcolor='white',
        paper_bgcolor='#F8F9FA',
        hovermode='x unified',
        legend=dict(
            yanchor="top",
            xanchor="right",
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#CCC',
            borderwidth=1
        )
    )
    return fig

# From images 8eaac5.png and 8ea7ff.png
def candlestick(dataframe, num_period):
    dataframe = filter_data(dataframe,num_period)
    fig = go.Figure()
    
    fig.add_trace(go.Candlestick(x=dataframe['Date'],
        open=dataframe['Open'], high=dataframe['High'],
        low=dataframe['Low'], close=dataframe['Close']))
    
    fig.update_xaxes(
        title_text='Date',
        showgrid=True,
        gridcolor='#E5E5E5'
    )
    fig.update_yaxes(
        title_text='Price ($)',
        showgrid=True,
        gridcolor='#E5E5E5'
    )
    fig.update_layout(
        title=dict(text='Candlestick Chart', font=dict(size=16, color='#333'), x=0.5, xanchor='center'),
        showlegend=False,
        height=500,
        margin=dict(l=60, r=40, t=60, b=40),
        plot_bgcolor='white',
        paper_bgcolor='#F8F9FA',
        hovermode='x'
    )
    return fig

# From images 8eaac5.png and 8eab00.png
def RSI(dataframe, num_period):
    dataframe['RSI'] = ta.momentum.RSIIndicator(dataframe['Close']).rsi()
    dataframe = filter_data(dataframe,num_period)
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe.RSI, name = 'RSI', marker_color='orange', line = dict(width=2,color = 'orange'),
    ))
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=[70]*(len(dataframe)), name = 'Overbought', marker_color='red', line = dict(width=2,color = 'red',dash='dash'),
    ))
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=[30]*(len(dataframe)), fill='tonexty', name = 'Oversold', marker_color='#79da84', line = dict(width=2,color = '#79da84',dash='dash'),
    ))
    
    fig.update_xaxes(
        title_text='Date',
        showgrid=True,
        gridcolor='#E5E5E5'
    )
    fig.update_yaxes(
        title_text='RSI',
        showgrid=True,
        gridcolor='#E5E5E5',
        range=[0, 100]
    )
    fig.update_layout(
        title=dict(text='Relative Strength Index (RSI)', font=dict(size=14, color='#333'), x=0.5, xanchor='center'),
        height=250,
        plot_bgcolor='white',
        paper_bgcolor='#F8F9FA',
        margin=dict(l=60, r=40, t=50, b=40),
        hovermode='x unified',
        legend=dict(
            orientation="h",
            yanchor="top",
            y=1.15,
            xanchor="right",
            x=1,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#CCC',
            borderwidth=1
        )
    )
    return fig

# From images 8eab80.png and 8eabc1.png
def MACD(dataframe, num_period):
    macd_indicator = ta.trend.MACD(dataframe['Close'])
    macd = macd_indicator.macd()
    macd_signal = macd_indicator.macd_signal()
    macd_hist = macd_indicator.macd_diff()
    dataframe['MACD'] = macd
    dataframe['MACD Signal'] = macd_signal
    dataframe['MACD Hist'] = macd_hist
    dataframe = filter_data(dataframe,num_period)
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        # Note: name = 'RSI' appears to be a typo in the original image, but transcribed as-is.
        y=dataframe['MACD'], name = 'RSI', marker_color='orange', line = dict(width=2,color = 'orange'),
    ))
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
         # Note: name = 'Overbought' appears to be a typo, but transcribed as-is.
        y=dataframe['MACD Signal'], name = 'Overbought', marker_color='red', line = dict(width=2,color = 'red',dash='dash'),
    ))
    
    # Note: The 'c' variable is defined but not used in the traces. Transcribed as-is.
    c = ['red' if cl <0 else "green" for cl in macd_hist]
    
    fig.update_xaxes(
        title_text='Date',
        showgrid=True,
        gridcolor='#E5E5E5'
    )
    fig.update_yaxes(
        title_text='MACD',
        showgrid=True,
        gridcolor='#E5E5E5'
    )
    fig.update_layout(
        title=dict(text='MACD Indicator', font=dict(size=14, color='#333'), x=0.5, xanchor='center'),
        height=250,
        plot_bgcolor='white',
        paper_bgcolor='#F8F9FA',
        margin=dict(l=60, r=40, t=50, b=40),
        hovermode='x unified',
        legend=dict(
            orientation="h",
            yanchor="top",
            y=1.15,
            xanchor="right",
            x=1,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#CCC',
            borderwidth=1
        )
    )
    return fig

# From image 8eab43.png
def Moving_average(dataframe, num_period):
    dataframe['SMA_50'] = ta.trend.SMAIndicator(dataframe['Close'], window=50).sma_indicator()
    dataframe = filter_data(dataframe,num_period)
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Open'],
        mode='lines',
        name='Open', line = dict(width=2, color = '#5ab7ff')))
    
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Close'],
        mode='lines',
        name='Close', line = dict(width=2,color = 'black')))
    
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['High'],
        mode='lines', name='High', line = dict(width=2,color = '#0078ff')))
    
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Low'],
        mode='lines', name='Low', line = dict(width=2,color = 'red')))
    
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['SMA_50'],
        mode='lines', name='SMA 50', line = dict(width=2,color = 'purple')))
    
    fig.update_xaxes(
        title_text='Date',
        showgrid=True,
        gridcolor='#E5E5E5',
        rangeslider_visible=True
    )
    fig.update_yaxes(
        title_text='Price ($)',
        showgrid=True,
        gridcolor='#E5E5E5'
    )
    fig.update_layout(
        title=dict(text='Moving Average (SMA 50)', font=dict(size=16, color='#333'), x=0.5, xanchor='center'),
        height=500,
        margin=dict(l=60, r=40, t=60, b=40),
        plot_bgcolor='white',
        paper_bgcolor='#F8F9FA',
        hovermode='x unified',
        legend=dict(
            xanchor="right",
            yanchor="top",
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#CCC',
            borderwidth=1
        )
    )
    return fig

# import plotly.graph_objects as go # Inferred import

def Moving_average_forecast(forecast):
    fig = go.Figure()

    # Historical data
    fig.add_trace(go.Scatter(
        x=forecast.index[:-30], 
        y=forecast['Close'].iloc[:-30],
        mode='lines',
        name='Historical Price', 
        line=dict(width=2.5, color='#2E86AB'),
        hovertemplate='<b>Date</b>: %{x}<br><b>Price</b>: $%{y:.2f}<extra></extra>'
    ))

    # Forecasted data
    fig.add_trace(go.Scatter(
        x=forecast.index[-31:], 
        y=forecast['Close'].iloc[-31:],
        mode='lines', 
        name='Forecasted Price', 
        line=dict(width=2.5, color='#E63946', dash='dash'),
        hovertemplate='<b>Date</b>: %{x}<br><b>Forecast</b>: $%{y:.2f}<extra></extra>'
    ))

    fig.update_xaxes(
        title_text='Date',
        title_font=dict(size=14, color='#333'),
        showgrid=True,
        gridcolor='#E5E5E5',
        rangeslider_visible=True,
        rangeslider=dict(bgcolor='#F0F0F0')
    )
    
    fig.update_yaxes(
        title_text='Stock Price ($)',
        title_font=dict(size=14, color='#333'),
        showgrid=True,
        gridcolor='#E5E5E5'
    )
    
    fig.update_layout(
        title=dict(
            text='Stock Price Forecast (Next 30 Days)',
            font=dict(size=18, color='#333', family='Arial Black'),
            x=0.5,
            xanchor='center'
        ),
        height=550,
        margin=dict(l=60, r=40, t=60, b=40),
        plot_bgcolor='white',
        paper_bgcolor='#F8F9FA',
        hovermode='x unified',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#CCC',
            borderwidth=1
        )
    )

    return fig