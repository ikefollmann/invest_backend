import yahooquery as yq

def importa():
    data = yq.Ticker("aapl")
    df = data.history(period='1d', interval='1m')
    return df

importa()
