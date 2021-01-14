# Backtesting

This is a simplified backtesting code to test out a 60 40 portfolio allocation that is split between sotcks and gold. The allocation changes dynamically between all stock to a split between stock and gold.

The allocation to gold increases once the CAPE ratio increases beyond a certain threshold, thereby indicating that the stocks are overvalued

Conversely, the gold position is liquidated and the proceeds invested into stocks once the CAPE ratio decreases beyond a certain threshold, thereby inducating that the stocks are valued fairly 

The goal of this back test is to prove or disporve the effectiveness of using a secondary asset that is negatively correlated with stocks to counterweigh exposure to stocks during times of high stock market price levels
