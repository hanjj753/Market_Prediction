import pandas as pd

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

# print(train.columns)
# print(test.columns)
# print(test[['is_scored']])

real_test = train.tail(181)
real_test[['is_scored']] = True
real_test[['lagged_forward_returns']] = real_test[['forward_returns']].shift(1)
real_test[['lagged_risk_free_rate']] = real_test[['risk_free_rate']].shift(1)
real_test[['lagged_market_forward_excess_returns']] = real_test[['market_forward_excess_returns']].shift(1)
real_test = real_test.drop(columns=['forward_returns', 'risk_free_rate', 'market_forward_excess_returns'])
real_test = real_test.tail(180)
print(real_test)

real_test.to_csv('data/real_test.csv', index=False)

# print(real_test.columns)