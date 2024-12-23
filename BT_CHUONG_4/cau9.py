#Đầu tiên, chúng ta cần tạo một Series với 35 phần tử phần tử là một số nguyên ngẫu nhiên từ 1 đến 10. Sau đó, chúng ta sẽ chuyển đổi Series này thành DataFrame bằng cách sử dụng phương thức reshape để tạo ra một ma trận 7x5 (7 hàng và 5 cột).
import pandas as pd
import numpy as np
ser =pd.Series(np.random.randint(1,10,35))
df = pd.DataFrame(ser.values.reshape(7,5))
