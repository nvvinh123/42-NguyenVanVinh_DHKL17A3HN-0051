import pandas as pd


drink = pd.read_csv('drinks.csv', index_col=0)

print("Kiểu dữ liệu:", drink.dtype)
print("Kích thước:", drink.shape)
print("Tên các cột:", drink.columns)


print("5 dòng đầu tiên:")
print(drink.head())
print("5 dòng cuối cùng:")
print(drink.tail())


print("Số lượng bia tiêu thụ trung bình ở mỗi châu lục:")
print(drink.mean(axis=1))


print("Thông tin thống kê tổng quát về số lượng rượu vang được tiêu thụ ở mỗi châu lục:")
print(drink.describe())


print("Số lượng các loại bia và rượu tiêu thụ trung bình ở mỗi châu lục:")
print(drink.mean(axis=0))


print("Giá trị trung vị cho các loại bia và rượu tiêu thụ ở mỗi châu lục:")
print(drink.median(axis=0))


print("Số lượng rượu mạnh (spirit servings) tiêu thụ trung bình, lớn nhất và nhỏ nhất ở mỗi châu lục:")
print(drink['spirit servings'].mean(axis=0))
print(drink['spirit servings'].max(axis=0))
print(drink['spirit servings'].min(axis=0))


sorted_by_beer_consumption = drink.sort_values(by='beer servings', ascending=True)


print("5 quốc gia có lượng tiêu thụ bia nhiều nhất:")
print(sorted_by_beer_consumption.index[:5])


print("5 quốc gia có lượng tiêu thụ bia ít nhất:")
print(sorted_by_beer_consumption.index[-5:])