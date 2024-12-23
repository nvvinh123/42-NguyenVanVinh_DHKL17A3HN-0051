#Đoạn mã có chức năng tạo ra một series 30 phần tử ngẫu nhiên từ danh sách các ký tự 'abcdefgh'. 'np.random.randint(8, size=30)' tức là tạo ra một mảng có kích thước là 30 phần tử, mỗi phần tử mang giá trị ngẫu nhiên từ 0 đến 7. 'np.take(list('abcdefgh'), np.random.randint(8,size=30))' tức là chọn các phần tử của 'abcdefgh' tại vị trí các giá trị trong mảng được tạo ra, đây là một phương pháp tích hợp trong thư viện numpy, nó lấy ra các giá trị từ danh sách nơi mà cung cấp các indices (vị trí)
import numpy as np
import pandas as pd
ser=pd.Serieds(np.take(list('abcdefgh'), np.random.randint(8,size=30)))
ser.value_counts()
