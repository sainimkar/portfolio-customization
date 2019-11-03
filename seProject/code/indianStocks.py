#!/usr/bin/env python
# coding: utf-8

# In[125]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web


# In[126]:


data = pd.read_excel (r'C:\Users\nawan\Desktop\seProject\db\portfolio.xlsx') 
df = pd.DataFrame(data)
print(df)


# In[127]:


daily_returns = df['RELIANCE'].pct_change(1)


# In[128]:


daily_returns


# In[129]:


fig = plt.figure()
ax1 = fig.add_axes([0.5,0.5,2,2])
ax1.plot(daily_returns)
ax1.set_xlabel("Date")
ax1.set_ylabel("Percent")
ax1.set_title("daily returns data of RELIANCE")
plt.show()


# In[130]:


cum_returns = (daily_returns + 1).cumprod()


# In[131]:


fig = plt.figure()
ax1 = fig.add_axes([0.2,0.2,1,1])
cum_returns.plot()
ax1.set_xlabel("Date")
ax1.set_ylabel("Growth of $1 investment")
ax1.set_title("daily cumulative returns data of RELIANCE")
plt.show()


# In[132]:


tickers=["RELIANCE","ACC","AMBUJACEM","ASHOKLEY","AUROPHARMA","BAJAJHLDNG","BANKBARODA","BERGEPAINT","BIOCON","BOSCHLTD","CADILAHC","COLPAL","CONCOR","ADANIPORTS","ASIANPAINTS","AXISBANK","BAJAJAUTO","BAJAJFINSV","BAJAJFINANCE","BPCL","BHARTIARTL","INFRATEL","CIPLA","COALINDIA","EICHER","GAIL","GRASIM","HCLTECH","HDFCBANK","HDFC","HEROMOTOCO","HINDALCO","HINDUINILVR","ICICIBANK","ITC","IOC","INUSINDBK","INFOSYS","JSWSTEEL","KOTAKBANK","MAHINDRA","MARUTI","TCS","SUNPHARMA","SBIN","POWERGRID","ONGC","NESTLE","NTPC","ZEEL","YESBANK","WIPRO","VEDL","ULTACEMCO","TITAN","TECHM","TATASTEEL","TATAMOTORS","DRREDDY"]


# In[133]:


multi_stocks = df[tickers]


# In[134]:


multi_stocks


# In[135]:


multi_stock_daily_returns = multi_stocks.pct_change(1)


# In[136]:


multi_stock_daily_returns


# In[137]:


fig = plt.figure()
(multi_stock_daily_returns + 1).cumprod().plot()
plt.show()


# In[138]:


multi_stock_quarterly_returns = multi_stocks.pct_change(21*3)
multi_stock_quarterly_returns_mean = multi_stock_quarterly_returns.mean()
multi_stock_quarterly_returns_mean


# In[139]:


print(multi_stock_quarterly_returns.std())


# In[140]:


print(multi_stock_quarterly_returns.corr())


# In[141]:


cov_mat = multi_stock_quarterly_returns.cov()
print(cov_mat)


# In[142]:


returns_stocks = pd.DataFrame(multi_stock_quarterly_returns_mean)
returns_stocks


# In[ ]:





# In[143]:


for cols in returns_stocks.columns:
    port_stocks = returns_stocks.loc[returns_stocks[cols] > 0]


# In[144]:


port_stocks = multi_stocks


# In[145]:


log_ret = np.log(port_stocks/port_stocks.shift(1))
cov_mat = log_ret.cov() * 252
print(cov_mat)


# In[146]:


# Simulating 10000 portfolios
num_port = 5000
# Creating an empty array to store portfolio weights
all_wts = np.zeros((num_port, len(port_stocks.columns)))
# Creating an empty array to store portfolio returns
port_returns = np.zeros((num_port))
# Creating an empty array to store portfolio risks
port_risk = np.zeros((num_port))
# Creating an empty array to store portfolio sharpe ratio
sharpe_ratio = np.zeros((num_port))


# In[147]:


for i in range(num_port):
    wts = np.random.uniform(size = len(port_stocks.columns))
    wts = wts/np.sum(wts)
    # saving weights in the array
    all_wts[i,:] = wts
    # Portfolio Returns
    port_ret = np.sum(log_ret.mean() * wts)
    port_ret = (port_ret + 1) ** 252 - 1
    # Saving Portfolio returns
    port_returns[i] = port_ret
    # Portfolio Risk
    port_sd = np.sqrt(np.dot(wts.T, np.dot(cov_mat, wts)))
    port_risk[i] = port_sd
    # Portfolio Sharpe Ratio
    # Assuming 0% Risk Free Rate
    sr = port_ret / port_sd
    sharpe_ratio[i] = sr


# In[148]:


names = port_stocks.columns
min_var = all_wts[port_risk.argmin()]
print(min_var)


# In[149]:


max_sr = all_wts[sharpe_ratio.argmax()]
print(max_sr)


# In[150]:


print(sharpe_ratio.max())


# In[151]:


print(port_risk.min())


# In[152]:


print(port_risk.max())


# In[ ]:





# In[153]:


max_sr = pd.Series(max_sr, index=names)
max_sr = max_sr.sort_values()
fig = plt.figure()
ax1 = fig.add_axes([1,1,2,2])
ax1.set_xlabel('Asset')
ax1.set_ylabel("Weights")
ax1.set_title("Tangency Portfolio weights")
max_sr.plot(kind = 'bar')
plt.show();


# In[154]:


fig = plt.figure()
ax1 = fig.add_axes([1,1,2,2])
ax1.set_xlabel('Risk')
ax1.set_ylabel("Returns")
ax1.set_title("Portfolio optimization and Efficient Frontier")
plt.scatter(port_risk, port_returns)
plt.show();


# In[155]:


min_var = pd.Series(min_var, index=names)
min_var = min_var.sort_values()
fig = plt.figure()
ax1 = fig.add_axes([1,1,2,2])
ax1.set_xlabel('Asset')
ax1.set_ylabel("Weights")
ax1.set_title("Minimum Variance Portfolio weights")
min_var.plot(kind ='bar')
plt.show();


# In[ ]:





# In[ ]:




