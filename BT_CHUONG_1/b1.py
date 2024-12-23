class hcn:
    def __init__(self,dai,rong):
        self.dai = dai
        self.rong = rong 
    def tinh_toan(self,dai,rong):
        chu_vi = (dai + rong) *2
        dien_tich = dai * rong
        print("Chu vi HCN là: ", chu_vi)
        print("Diện tích HCN là: ", dien_tich)

chieu_dai = float(input("Nhập chiều dài: "))
chieu_rong = float(input("Nhập chiều rộng: "))
thong_tin_hcn = hcn(chieu_dai,chieu_rong)
thong_tin_hcn.tinh_toan(chieu_dai,chieu_rong)