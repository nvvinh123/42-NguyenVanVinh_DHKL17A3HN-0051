class Diem:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def toa_do(self):
        return self.x, self.y
    
class elip(Diem):
    def __init__(self,x,y,a,b):
        super().__init__(x,y)
        self.a = a
        self.b = b
    def dien_tich_elip(self):
        import math
        print(math.pi * self.a * self.b, "là diện tích hình elip")

class Duong_tron(elip):
    def __init__(self,x,y,r):
        super().__init__(x,y,r,r)
        self.r = r
    def display2(self):
        print(f"Đường tròn tại {super().toa_do()} với bán trục lớn {self.a} và bán trục nhỏ {self.b} ")

x = float(input("Nhập tọa độ x tâm elip: "))
y = float(input("Nhập tọa độ y tâm elip: "))
a = float(input("Nhập bán trục lớn  của elip: "))
b = float(input("Nhập bán trục nhỏ của elip: "))
hinh_elip = elip(x,y,a,b)
hinh_elip.dien_tich_elip()



