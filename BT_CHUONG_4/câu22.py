import pandas as pd


stocks1 = pd.read_csv('D:\CHUONG4_DHKL17A3\stocks1.csv')
print("Dữ liệu đầu và cuối của stocks1:")
print(stocks1.head(5))
print(stocks1.tail(5))
print("Kiểu dữ liệu của các cột của stocks1:")
print(stocks1.dtypes)
print("Thông tin của stocks1:")
print(stocks1.info())


stocks2 = pd.read_csv('D:\CHUONG4_DHKL17A3\stocks2.csv')
print("\nDữ liệu đầu và cuối của stocks2:")
print(stocks2.head(5))
print(stocks2.tail(5))
print("Kiểu dữ liệu của các cột của stocks2:")
print(stocks2.dtypes)
print("Thông tin của stocks2:")
print(stocks2.info())


companies = pd.read_csv('D:\CHUONG4_DHKL17A3\companies.csv')
print("\nDữ liệu của companies:")
print(companies)
print("Kiểu dữ liệu của các cột của companies:")
print(companies.dtypes)
print("Thông tin của companies:")
print(companies.info())


if stocks1.isnull().sum().any():
    print("\nCó dữ liệu Null trong stocks1.")

    stocks1['high'] = stocks1['high'].fillna(stocks1['high'].max())
    stocks1['low'] = stocks1['low'].fillna(stocks1['low'].min())
else:
    print("\nKhông có dữ liệu Null trong stocks1.")


stocks = pd.concat([stocks1, stocks2])
print("\nDữ liệu sau khi gộp:")
print(stocks.tail(15))


stocks_companies = pd.merge(stocks, companies, on='symbol')
print("\nDữ liệu sau khi gộp với companies:")
print(stocks_companies.head(5))


company_avg_price = stocks_companies.groupby('symbol')['open', 'high', 'low', 'close'].mean()
company_avg_volume = stocks_companies.groupby('symbol')['volume'].mean()
print("\nGiá trung bình và volume trung bình của mỗi công ty:")
print(company_avg_price)
print(company_avg_volume)


company_close_stats = stocks_companies.groupby('symbol')['close'].agg(['mean', 'ax', 'in'])
print("\nGiá đóng cửa trung bình, lớn nhất và nhỏ nhất ở mỗi công ty:")
print(company_close_stats)


stocks_companies['parsed_time'] = pd.to_datetime(stocks_companies['date'])
print("\nDữ liệu sau khi thêm cột parsed_time:")
print(stocks_companies.head(5))


stocks_companies['result'] = stocks_companies.apply(lambda row: 'up' if row['close'] > row['open'] else 'down', axis=1)
print("\nDữ liệu sau khi thêm cột result:")
print(stocks_companies.head(5))