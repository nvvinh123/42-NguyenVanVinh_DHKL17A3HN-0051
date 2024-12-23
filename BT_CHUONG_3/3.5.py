import numpy as np

with open('heights_1.txt', 'r') as f:
    height = [float(line.strip()) for line in f]

with open('weights_1.txt', 'r') as f:
    weight = [float(line.strip()) for line in f]

# 1: Tạo numpy array arr_height từ list height
arr_height = np.array(height)
print("arr_height:", arr_height)

# 2: Tạo numpy array arr_weight từ list weight
arr_weight = np.array(weight)
print("arr_weight:", arr_weight)

# 3: Tạo arr_height_m bằng cách chuyển đổi chiều cao từ inch sang m
arr_height_m = arr_height * 0.0254
print("arr_height_m (m):", arr_height_m)

# 4: Tạo arr_weight_kg bằng cách chuyển đổi cân nặng từ pound sang kg
arr_weight_kg = arr_weight * 0.453592
print("arr_weight_kg (kg):", arr_weight_kg)

# 5: Tính BMI
arr_bmi = arr_weight_kg / (arr_height_m ** 2)
print("arr_bmi:", arr_bmi)

# 6: Cân nặng tại vị trí index = 50 trong arr_weight_kg
if len(arr_weight_kg) > 50:
    vi_tri_50 = arr_weight_kg[50]
    print("Cân nặng tại vị trí 50 là:", vi_tri_50)
else:
    print("Không có dữ liệu cho vị trí 50.")

# 7: Tạo arr_height_m_100 từ arr_height_m với các phần tử từ index 100 đến 110
if len(arr_height_m) > 110:
    arr_height_m_100 = arr_height_m[100:111]
    print("arr_height_m_100 (index 100-110):", arr_height_m_100)
else:
    print("Không có đủ dữ liệu để lấy các phần tử từ index 100 đến 110.")

# 8: Các cầu thủ có bmi < 21 trong arr_bmi
bmi_nho_hon_21 = arr_bmi[arr_bmi < 21]
print("Cầu thủ có BMI < 21:", bmi_nho_hon_21)

# 9: Chiều cao trung bình và cân nặng trung bình của các cầu thủ
chieu_cao_tb = np.mean(arr_height_m)
can_nang_tb = np.mean(arr_weight_kg)
print("Chiều cao trung bình của các cầu thủ là:", chieu_cao_tb)
print("Cân nặng trung bình của các cầu thủ là:", can_nang_tb)

# 10: Chiều cao và cân nặng lớn nhất của các cầu thủ
max_height = np.max(arr_height_m)
max_weight = np.max(arr_weight_kg)
print("Chiều cao lớn nhất của cầu thủ là:", max_height)
print("Cân nặng lớn nhất của cầu thủ là:", max_weight)

# 11: Chiều cao và cân nặng nhỏ nhất của các cầu thủ
min_height = np.min(arr_height_m)
min_weight = np.min(arr_weight_kg)
print("Chiều cao thấp nhất của cầu thủ là:", min_height)
print("Cân nặng nhỏ nhất của cầu thủ là:", min_weight)