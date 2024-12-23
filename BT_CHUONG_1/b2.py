class TS:
    def __init__(self,ho_ten,toan,ly,hoa):
        self.ho_ten = ho_ten
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
    def in_thong_tin(self,ho_ten,toan,ly,hoa):
        print(ho_ten,toan,ly,hoa)
    def tinh_diem(self,toan,ly,hoa,diem):
        diem = toan + ly + hoa
        print(diem, "là tổng điểm của thí sinh")
    def danh_sach(self,ho_ten,diem):
        ds = {"Họ tên": ho_ten, "Tổng điểm":diem}
        dao_nguoc_gtri = {key: value for key, value in sorted(ds.items(), key = lambda item: str(item[1]), reverse=True)}
        print(dao_nguoc_gtri)

n = int(input("Nhập số lượng thí sinh: "))
for i in range(n):
    ho_ten = input(f"Nhập tên thí sinh thứ {i+1}: ")
    toan = float(input(f"Nhập điểm toán của thí sinh thứ {i+1}: "))
    ly = float(input(f"Nhập điểm lý của thí sinh thứ {i+1}: "))
    hoa = float(input(f"Nhập điểm hóa của thí sinh thứ {i+1}: "))
    diem = toan + ly + hoa
    thi_sinh = TS(ho_ten,toan,ly,hoa)
    thi_sinh.in_thong_tin(ho_ten,toan,ly,hoa)
    thi_sinh.tinh_diem(toan,ly,hoa,diem)
    thi_sinh.danh_sach(ho_ten,diem)



