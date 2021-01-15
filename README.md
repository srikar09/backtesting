# Backtesting

This is a simplified code to backtest a dynamically changing 60/40 portfolio allocation that is split between sotcks and a secondary asset that is negatively correlated to stocks , which in this case is gold

The portfolio allocation changes from all stock to a 60/40 split between stocks and gold once the CAPE ratio increases beyond a certain threshold, indicating that the stocks are overvalued

Conversely, the gold position is liquidated and all the proceeds are invested into stocks (S&P 500) once the CAPE ratio decreases beyond a certain threshold, thereby indicating that the stocks are valued fairly 

The goal of this back test is to prove or disprove the effectiveness of using a secondary asset that is negatively correlated with stocks to counterweigh exposure to stocks during times when stocks could be highly overvalued with respect to their fundementals



Findings: 

without accounting for transaction costs , capital gains taxes and accrued dividends 100,000 dollars invested in S&P 500 in 1927  would equal 1,427,783 in 2020. On the other hand, 100,000 dollars invested in 1927 with this strategy would equal 2,295,093 dollars in 2020 




