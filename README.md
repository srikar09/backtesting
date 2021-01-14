# Backtesting

This is a simplified backtesting code to test out a 60 40 portfolio allocation that is split between sotcks and gold. The allocation changes dynamically between a portfolio of all stock to a portfolio that is split between stock and gold.

The portfolio allocation of gold increases once the CAPE ratio increases beyond a certain threshold, thereby indicating that the stocks are overvalued

Conversely, the gold position is liquidated and all the proceeds invested into stocks once the CAPE ratio decreases beyond a certain threshold, thereby indicating that the stocks are valued fairly 

The goal of this back test is to prove or disporve the effectiveness of using a secondary asset that is negatively correlated with stocks to counterweigh exposure to stocks during times of high stocks could be overvalued with respect to their fundementals
