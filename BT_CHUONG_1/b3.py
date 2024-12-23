class PS:
    def __init__(self,tu_so,mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so
    def hop_le(self,mau_so):
        if mau_so ==0:
            print("Phân số không hợp lệ")
        else:
            print("Phân số hợp lệ")
    def in_phan_so(self,tu_so,mau_so):
        from fractions import Fraction
        print("Phân số là: ", Fraction(tu_so,mau_so))

tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))
phan_so = PS(tu_so,mau_so)
phan_so.hop_le(mau_so)
phan_so.in_phan_so(tu_so,mau_so)

