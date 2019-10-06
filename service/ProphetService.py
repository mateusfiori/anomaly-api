import pandas as pd
from fbprophet import Prophet
from datetime import datetime

def generateJsonResult():
    pass

def formatDictToDataframe(timeserie):
    return {
        'ds': [str(datetime.fromtimestamp(int(ts))) for ts in list(timeserie.keys())],
        'y': list(timeserie.values())
    }

def forecastTimeserie(timeserie):
    model = Prophet().fit(pd.DataFrame.from_dict(formatDictToDataframe(timeserie)))
    return model.predict(model.make_future_dataframe(periods=10))