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

def backtest_strategy(cape_upper_limit, cape_lower_limit, gold_allocation_percent, initial_capital):
    sp_index_real_values = sp_index["real"]
    gold_index_real_values = gold_index["real"]
    cape_index_metric_values = cape_index["CAPE"]
    
    portfolio_position = pd.DataFrame(index = range(sp_index_real_values.size), columns = ['S&P500', 'gold', 'portfolio_value', 'sp_benchmark']) 
    portfolio_position = portfolio_position.fillna(0) 
    
    initial_stock_position = initial_capital/sp_index_real_values[0]
    initial_gold_position = 0;
    
    portfolio_position.at[0, 'stocks']= initial_stock_position
    portfolio_position.at[0, 'gold']= initial_gold_position
    portfolio_position.at[0, 'portfolio_value']= initial_capital  
    portfolio_position.at[0, 'sp_benchmark']= initial_capital
    
    for trade_month in range (1, sp_index_real_values.size):
        
        # if stocks are overvalued and portfolio has no gold , rebalance towards an allocation of stock and gold
        if (cape_index_metric_values[trade_month] > cape_upper_limit and portfolio_position.iloc[trade_month-1]['gold']==0):  
            current_portfolio_value = portfolio_position.iloc[trade_month-1]['stocks']* sp_index_real_values[trade_month]
            new_gold_allocation = (current_portfolio_value*gold_allocation_percent) / gold_index_real_values[trade_month]
            new_stock_allocation =  (current_portfolio_value * (1-gold_allocation_percent))/(sp_index_real_values[trade_month])
            current_sp_value = calculate_sp_benchmark(portfolio_position.iloc[trade_month-1]['sp_benchmark'],sp_index_real_values[trade_month-1], sp_index_real_values[trade_month] )
            portfolio_position.at[trade_month,'stocks'] = new_stock_allocation
            portfolio_position.at[trade_month,'gold'] = new_gold_allocation
            portfolio_position.at[trade_month,'portfolio_value'] = current_portfolio_value
            portfolio_position.at[trade_month,'sp_benchmark'] = current_sp_value
         
            # if stocks are undervalued and portfolio has gold , rebalance towards an allocation of all stock
        elif (cape_index_metric_values[trade_month] < cape_lower_limit and portfolio_position.iloc[trade_month-1]['gold']>0):     
            current_stock_value = portfolio_position.iloc[trade_month-1]['stocks']* sp_index_real_values[trade_month] 
            current_gold_value = portfolio_position.iloc[trade_month-1]['gold']* gold_index_real_values[trade_month]
            current_portfolio_value = current_stock_value +  current_gold_value
            new_gold_allocation = 0
            new_stock_allocation =  (current_portfolio_value)/(sp_index_real_values[trade_month])
            current_sp_value = calculate_sp_benchmark(portfolio_position.iloc[trade_month-1]['sp_benchmark'],sp_index_real_values[trade_month-1], sp_index_real_values[trade_month] )
            portfolio_position.at[trade_month, 'stocks'] = new_stock_allocation
            portfolio_position.at[trade_month, 'gold'] = new_gold_allocation
            portfolio_position.at[trade_month, 'portfolio_value'] = current_portfolio_value
            portfolio_position.at[trade_month, 'sp_benchmark'] = current_sp_value

        # updating portfolio and sp benchmark value
        else:
            current_stock_value = portfolio_position.iloc[trade_month-1]['stocks']* sp_index_real_values[trade_month] 
            current_gold_value = portfolio_position.iloc[trade_month-1]['gold']* gold_index_real_values[trade_month]
            current_portfolio_value = current_stock_value +  current_gold_value
            current_sp_value = calculate_sp_benchmark(portfolio_position.iloc[trade_month-1]['sp_benchmark'],sp_index_real_values[trade_month-1], sp_index_real_values[trade_month] )
            portfolio_position.at[trade_month, 'portfolio_value'] = current_portfolio_value
            portfolio_position.at[trade_month, 'sp_benchmark'] = current_sp_value
            portfolio_position.at[trade_month, 'stocks'] = portfolio_position.at[trade_month-1, 'stocks']
            portfolio_position.at[trade_month, 'gold'] = portfolio_position.at[trade_month-1, 'gold']

    
    return portfolio_position
    

    


def calculate_sp_benchmark(previous_month_sp_benchmark_value, previous_month_sp_benchmark_price, current_month_sp_benchmark_price):
    current_sp_amount = previous_month_sp_benchmark_value/previous_month_sp_benchmark_price
    current_sp_value = current_sp_amount *  current_month_sp_benchmark_price
    return current_sp_value
        
# when CAPE ratio falls below 14 liqudate gold holdings and buy stocks (stocks are fairvalued)
# when CAPE ratio goes above 23 liquidate 40 percent of portfolio 
#    and buy gold (Stocks are overvalued), results in a 60/40 split
# starting with 100,000

portfolio_performance =  backtest_strategy(23, 14, 0.4, 100000)
portfolio_performance.plot()
