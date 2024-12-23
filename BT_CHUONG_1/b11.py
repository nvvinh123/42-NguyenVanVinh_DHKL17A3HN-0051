class TamGiac:
    def __init__(self,a,b,c,h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    def tinh_tg_thuong(self,a,b,c,h):
        chu_vi_tg_thuong = a + b + c
        dien_tich_tg_thuong = 1/2 * a * h
        print(chu_vi_tg_thuong, "là chu vi tam giác thường")
        print(dien_tich_tg_thuong, "là diện tích tam giác thường")
    
class TamGiacVuong(TamGiac):
    def __init__(self,a,b):
        import math
        super().__init__(a,b,math.sqrt(a**2 + b**2),None)
    def tinh_tg_vuong(self,a,b):
        import math
        c2 = math.sqrt((a**2) + (b**2))    # ở đây c2 là độ dài cạnh huyền
        chu_vi_tg_vuong = a + b + c2
        dien_tich_tg_vuong = 1/2 * a * b
        print(chu_vi_tg_vuong, "là chu vi tam giác vuông")
        print(dien_tich_tg_vuong, "là diện tích tam giác vuông")

class TamGiacCan(TamGiac):
    def __init__(self,a,b,h):
        super().__init__(a,b,c,h)
        self.h = h
    def tinh_tg_can(self,a,b,h):
        chu_vi_tg_can = 2*a + b
        dien_tich_tg_can = 1/2 * b * h
        print(chu_vi_tg_can, "là chu vi tam giác cân")
        print(dien_tich_tg_can, "là diện tích tam giác cân")

class TamGiacDeu(TamGiacCan):
    def __init__(self,a):
        super().__init__(a,b,h)
    def tinh_tg_deu(self,a):
        import math
        chu_vi_tg_deu = 3*a
        dien_tich_tg_deu = (math.sqrt(3) / 4) * (a**2)
        print(chu_vi_tg_deu, "là chu vi tam giác đều")
        print(dien_tich_tg_deu, "là diện tích tam giác đều")

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
h = float(input("Nhập h: "))
h1 = TamGiac(a,b,c,h)
h1.tinh_tg_thuong(a,b,c,h)

h2 = TamGiacVuong(a,b)
h2.tinh_tg_vuong(a,b)

h3 = TamGiacCan(a,b,h)
h3.tinh_tg_can(a,b,h)

h4 = TamGiacDeu(a)
h4.tinh_tg_deu(a)
