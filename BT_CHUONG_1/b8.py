class Employee:
    def __init__(self,ho_ten,ngay_sinh,ngay_vao_cong_ty):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.ngay_vao_cong_ty = ngay_vao_cong_ty
    def display(self):
        print(f"Họ tên nhân viên là {self.ho_ten}")
        print(f"Ngày sinh nhân viên là {self.ngay_sinh}")
        print(f"Ngày vào công ty của nhân viên là {self.ngay_vao_cong_ty}")

ho_ten = input("Nhập tên nhân viên: ")
ngay_sinh = int(input("Nhập ngày sinh nhân viên: "))
ngay_vao_cong_ty = int(input("Ngày nhân viên vào công ty: "))
thong_tin = Employee(ho_ten,ngay_sinh,ngay_vao_cong_ty)
thong_tin.display()
    

    