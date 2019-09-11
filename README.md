# anomaly-api

API para detecção de anomalias em séries temporais

Available routes:
  POST "/detect"
  
Expected request body:
    `{
      "<timestamp>": "<value>"
    }`
