import numpy as np

# Đọc dữ liệu từ file baseball_2D.txt
try:
    with open('baseball_2D.txt', 'r') as f:
        baseball = [list(map(float, line.strip().split())) for line in f]

    # Tạo 2D numpy array từ danh sách baseball
    np_baseball = np.array(baseball)
    print("Kiểu dữ liệu của np_baseball:", np_baseball.dtype)
    print("Kích thước của np_baseball:", np_baseball.shape)

    # 2: In các giá trị của dòng thứ 50 trong np_baseball
    if np_baseball.shape[0] > 49:  # Kiểm tra số dòng trong np_baseball
        print("\nGiá trị của dòng thứ 50 trong np_baseball:", np_baseball[49])  # Chỉ số bắt đầu từ 0
    else:
        print("Không có đủ dòng để in giá trị của dòng thứ 50.")

    # 3: Tạo numpy array np_weight với dữ liệu từ cột hai của np_baseball
    np_weight = np_baseball[:, 1]
    print("\nGiá trị của cột cân nặng trong np_baseball:", np_weight)

    # 4: Chiều cao của vận động viên thứ 124
    if np_baseball.shape[0] > 123:  # Kiểm tra số dòng trong np_baseball
        height_of_player_124 = np_baseball[123, 0]  # Chỉ số bắt đầu từ 0
        print("\nChiều cao của vận động viên thứ 124 (inch):", height_of_player_124)
    else:
        print("Không có đủ dữ liệu cho vận động viên thứ 124.")

    # 5: Chiều cao trung bình và cân nặng trung bình
    mean_height = np.mean(np_baseball[:, 0])
    mean_weight = np.mean(np_baseball[:, 1])
    print("\nChiều cao trung bình (inch):", mean_height)
    print("Cân nặng trung bình (pounds):", mean_weight)

    # 6: Mối tương quan giữa chiều cao và cân nặng
    correlation = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])[0, 1]
    print("\nMối tương quan giữa chiều cao và cân nặng:", correlation)

    if correlation > 0:
        print("Có tương quan thuận giữa chiều cao và cân nặng.")
    elif correlation < 0:
        print("Có tương quan nghịch giữa chiều cao và cân nặng.")
    else:
        print("Không có tương quan giữa chiều cao và cân nặng.")

except FileNotFoundError:
    print("Không tìm thấy file baseball_2D.txt.")