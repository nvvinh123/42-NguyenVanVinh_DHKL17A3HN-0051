class Date:
    def __init__(self,ngay,thang,nam):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam
    def display(self):
        print(f"Hôm nay là ngày {self.ngay} tháng {self.thang} năm {self.nam}")
    def next(self,ngay,thang,nam):
        ngay_tiep_theo = ngay + 1
        print(f"Ngày tiếp theo là {ngay_tiep_theo} tháng {thang} năm {nam}")

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
xem_ngay = Date(ngay,thang,nam)
xem_ngay.display()
xem_ngay.next(ngay,thang,nam)