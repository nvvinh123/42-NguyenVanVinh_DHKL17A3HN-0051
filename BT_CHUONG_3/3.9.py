import numpy as np
with open('euro2012.csv', 'r') as file:
    data = file.readlines()


euro12 = np.array(data[1:]).astype(str)


print(euro12[:, 3])


num_teams = np.count_nonzero(euro12[:, 0])
print("Số lượng đội tham gia Euro2012:", num_teams)


print("Thông tin của Euro2012:")
print(euro12)


discipline = euro12[:, [0, 5, 6]]


discipline = np.sort(discipline, axis=0, kind='descending')

avg_yellow_cards = np.mean(discipline[:, 1])
print("Trung bình Yellow Cards:", avg_yellow_cards)

top_teams = euro12[euro12[:, 3] > 6]
print("Các đội đã ghi hơn 6 bàn thắng:")
print(top_teams)

g_teams = euro12[euro12[:, 0].str.startswith('G')]
print("Các đội mà tên bắt đầu bằng 'G':")
print(g_teams)


print(euro12[:, :7])

print(euro12[:, :-3])


print(euro12[:, [0, 3, 4, 5, 6]])
england_italy_russia = euro12[euro12[:, 0].isin(['England', 'Italy', 'Russia'])][:, [0, 4]]
print("Các cột chỉ hiển thị 'Team', 'Shooting Accuracy' từ 'England', 'Italy', 'Russia':")
print(england_italy_russia)