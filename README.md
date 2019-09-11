# anomaly-api

API para detecção de anomalias em séries temporais

Available routes:
  POST "/detect"
  
Expected request body:
    {
     "1388906821": 9.18,
     "1388906823": 10.76,
     "1388906825": 0.0,
     "1388906827": 7.06,
     "1388906829": 57.77,
     "1388906831": 7.2,
     "1388906833": 31.98,
     "1388906835": 0.0,
     "1388906837": 9.6,
     "1388906839": 27.46,
     "1388906841": 9.8
    }
    
    {
      "<timestamp>": "<value>"
    }
