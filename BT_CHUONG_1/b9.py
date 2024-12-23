class Da_Giac:
    def __init__(self,so_canh,do_dai_canh):
        self.so_canh = so_canh
        self.do_dai_canh = do_dai_canh
    def tinh_da_giac(self,so_canh,do_dai_canh):
        import math
        chu_vi_da_giac = 0
        chu_vi_da_giac += do_dai_canh
        dien_tich_da_giac = (1/4) * so_canh * (do_dai_canh**2) * (1/math.tan(math.pi / so_canh))
        print("Chu vi hình đa giác là: ",chu_vi_da_giac)
        print("Diện tích đa giác là: ", dien_tich_da_giac)

class hinh_binh_hanh(Da_Giac):
    def __init__(self,do_dai_canh,do_dai_ke_nhau,chieu_cao):
        super().__init__(so_canh,do_dai_canh)
        self.do_dai_ke_nhau = do_dai_ke_nhau
        self.chieu_cao = chieu_cao
    def tinh_hbh(self,do_dai_canh,do_dai_ke_nhau,chieu_cao):
        chu_vi_hbh = 2 * (do_dai_canh + do_dai_ke_nhau)
        dien_tich_hbh = do_dai_canh * chieu_cao
        print("Chu vi hbh là: ", chu_vi_hbh)
        print("Diện tích hbh là: ", dien_tich_hbh)

class hinh_chu_nhat(hinh_binh_hanh):
    def __init__(self,do_dai_canh,do_dai_ke_nhau):
        super().__init__(do_dai_canh,do_dai_ke_nhau,chieu_cao)
    def tinh_hcn(self,do_dai_canh,do_dai_ke_nhau):
        chu_vi_hcn = 2 * (do_dai_canh + do_dai_ke_nhau)
        dien_tich_hcn = do_dai_canh * do_dai_ke_nhau
        print("Chu vi hcn là: ", chu_vi_hcn)
        print("Diện tích hcn là: ", dien_tich_hcn)

class hinh_vuong(hinh_chu_nhat):
    def __init__(self,do_dai_canh):
        super().__init__(do_dai_canh,do_dai_ke_nhau)
    def tinh_hv(self,do_dai_canh):
        chu_vi_hv = 4 * do_dai_canh
        dien_tich_hv = do_dai_canh **2
        print("Chu vi hv là: ", chu_vi_hv)
        print("Diện tích hv là: ", dien_tich_hv)

so_canh = int(input("Nhập số cạnh hình đa giác: "))
do_dai_canh = float(input("Nhập độ dài cạnh cho các hình: "))
do_dai_ke_nhau = float(input("Nhập độ dài cạnh kề nhau/chiều rộng phục vụ cho các hình: "))
chieu_cao = float(input("Nhập chiều cao: "))
h1 = Da_Giac(so_canh,do_dai_canh)
h1.tinh_da_giac(so_canh,do_dai_canh)

h2 = hinh_binh_hanh(do_dai_canh,do_dai_ke_nhau,chieu_cao)
h2.tinh_hbh(do_dai_canh,do_dai_ke_nhau,chieu_cao)

h3 = hinh_chu_nhat(do_dai_canh,do_dai_ke_nhau)
h3.tinh_hcn(do_dai_canh,do_dai_ke_nhau)

h4 = hinh_vuong(do_dai_canh)
h4.tinh_hv(do_dai_canh)






