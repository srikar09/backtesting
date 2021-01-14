# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 01:24:08 2021

@author: 14694
"""

# KEY ASSUMPTIONS: 
#  1) no capital gains tax
#  2) no transaction costs 
#  3) Prices used are real prices (inflation is accounted for )
#  4) There are only two possible assets to allocate to. No cash holdings 

import pandas as pd

capeindex_file_path = "C:/Users/14694/Documents/CAPEIndex.csv"
spindex_file_path = "C:/Users/14694/Documents/SP500.csv"
goldindex_file_path = "C:/Users/14694/Documents/GoldData.csv"


def load_csv_data(file_path):
    index_data = pd.read_csv(file_path)
    return index_data;

# these files contain monthly data that starts in 1927 and ends in 2020

sp_index = load_csv_data(spindex_file_path);
gold_index = load_csv_data(goldindex_file_path);
cape_index = load_csv_data(capeindex_file_path);


# upper limit & lower limit are ints 
# secondary asset allocation is a decmial from 0 to 1 
# inital capital is an int 

def backtest_strategy(cape_upper_limit, cape_lower_limit, secondary_asset_allocation, initial_capital):
    sp_index_real_values = sp_index["real"]
    gold_index_real_values = gold_index["real"]
    cape_index_metric_values = cape_index["CAPE"]
    
    portfolio_position = pd.DataFrame(index = range(sp_index_real_values.size), columns = ['S&P500', 'gold']) 
    portfolio_position = portfolio_position.fillna(0) 
    
    initial_stock_position = initial_capital/sp_index_real_values[0]
    portfolio_position.at['0', 'stocks']= initial_stock_position
    
    for trade_month in range (1, sp_index_real_values.size):
        
        if cape_index_metric_values[trade_month] > cape_upper_limit:    # overvalued
            current_stock_value = portfolio_position.iloc[trade_month]['stocks']* sp_index_real_values[trade_month]
            new_gold_allocation =  current_stock_value*secondary_asset_allocation / gold_index_real_values(trade_month)
            
        
        if cape_index_metric_values[trade_month] < cape_lower_limit:     # undervalued
                
        
            
    



# when CAPE ratio falls below 14 liqudate gold holdings and buy stocks (stocks are fairvalued)

# when CAPE ratio goes above 23 liquidate 40 percent of portfolio 
#    and buy gold (Stocks are overvalued), results in a 60/40 split

# starting with 100,000
