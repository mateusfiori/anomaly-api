from luminol.anomaly_detector import AnomalyDetector
from datetime import datetime
import pandas as pd
import pprint
import dateutil.parser

def parseTs(dataArray): 
    dataDict = dict()
    for i in dataArray:
        dataDict[datetime.strptime(str(dateutil.parser.parse(i[0])), '%Y-%m-%d %H:%M:%S').strftime('%s')] = i[1]
    return dataDict 

def formatAnomalies(anomalies):
    return [[anomaly.exact_timestamp, anomaly.anomaly_score] for anomaly in anomalies]

def verboseResult(anomalies, timeseriesDict):
    print(f'Foram encontradas {len(anomalies)} anomalias na sua série temporal.\n')
    for anomaly in anomalies:
        print(f'No timestamp {datetime.fromtimestamp(anomaly[0])} com um score de {anomaly[1]} e valor {timeseriesDict[str(anomaly[0])]}')

def generateJsonResult(anomalies, timeseriesDict):
    result = {'anomalies': list()}
    for anomaly in anomalies:
        result['anomalies'].append({
            'timestamp': str(datetime.fromtimestamp(anomaly[0])),
            'value': timeseriesDict[str(anomaly[0])],
            'anomaly_score': anomaly[1]
        })
    pprint.PrettyPrinter(indent=3).pprint(result)
    return result

# verboseResult(formatAnomalies(AnomalyDetector(timeseriesDict).get_anomalies()), timeseriesDict)
# generateJsonResult(formatAnomalies(AnomalyDetector(timeseriesDict).get_anomalies()), timeseriesDict)