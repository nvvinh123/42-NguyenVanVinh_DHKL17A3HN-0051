class Stack:
    def __init__(self,kich_co):
        self.kich_co = kich_co
        self.cac_phan_tu = []
    def push(self,phan_tu):
        if not self.isFull(kich_co):
            self.cac_phan_tu.append(phan_tu)
        else:
            print("Stack đã đầy, không thể thêm phần tử")
    def isEmpty(self):
        if len(self.cac_phan_tu) ==0:
            print("Stack đã trống")
    def pop(self):
        if len(self.cac_phan_tu) !=0:
            return self.cac_phan_tu.pop()
        else:
            print("Không thể lấy thêm vì stack đã trống")
    def isFull(self,kich_co):
        if len(self.cac_phan_tu) ==kich_co:
            print("Stack đã đầy các phần tử")
    def __del__(self):
        print("Đã xóa stack")
    

kich_co = int(input("Nhập số phần tử bạn muốn thêm vào ngăn xếp: "))
ngan_xep = Stack(kich_co)
for i in range(kich_co):
    so = float(input("Nhập phần tử dưới dạng float: "))
    ngan_xep.push(so)
ngan_xep.isEmpty()
ngan_xep.isFull(kich_co)

