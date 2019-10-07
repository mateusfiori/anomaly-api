import pandas as pd
from fbprophet import Prophet
from datetime import datetime

def generateJsonResult(forecastDf):
    result = {'result': list()}
    for _, row in forecastDf.iterrows():
        result['result'].append({
            'timestamp': str(row['ds']),
            'yhat': row['yhat'],
            'yhat_lower': row['yhat_lower'],
            'yhat_upper': row['yhat_upper'],
        })
    return result

def formatDictToDataframe(timeserie):
    return {
        'ds': [str(datetime.fromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S')) for ts in list(timeserie.keys())],
        'y': list(timeserie.values())
    }

def forecastTimeserie(timeserie):
    model = Prophet().fit(pd.DataFrame.from_dict(formatDictToDataframe(timeserie['timeserie'])))
    return generateJsonResult(model.predict(model.make_future_dataframe(periods=timeserie['future_ahead'], freq=timeserie['frequency'])))