import numpy as np
with open('heights.txt', 'r') as file:
    heights = file.readlines()

with open('positions.txt', 'r') as file:
    positions = file.readlines()

# Tạo numpy array từ list
np_positions = np.array(positions)
print("Kiểu dữ liệu của np_positions:", np_positions.dtype)

np_heights = np.array(heights)
print("Kiểu dữ liệu của np_heights:", np_heights.dtype)

# Tính chiều cao trung bình của các GK
gk_positions = np_positions[np_positions == 'GK']
gk_heights = np_heights[gk_positions]
avg_gk_height = np.mean(gk_heights)
print("Chiều cao trung bình của các GK:", avg_gk_height)

# Tính chiều cao trung bình của các vị trí khác (không phải GK)
other_positions = np_positions[np_positions!= 'GK']
other_heights = np_heights[other_positions]
avg_other_height = np.mean(other_heights)
print("Chiều cao trung bình của các vị trí khác (không phải GK):", avg_other_height)

# Tạo mảng dữ liệu có cấu trúc tự định nghĩa
player_data = np.array([
    {'position': pos, 'height': height} for pos, height in zip(positions, heights)
])
print("Mảng player_data:", player_data)
sorted_player_data = sorted(player_data, key=lambda x: x['height'])
print("Mảng players sắp xếp theo chiều cao:")
for player in sorted_player_data:
    print(f"Position: {player['position']}, Height: {player['height']}")