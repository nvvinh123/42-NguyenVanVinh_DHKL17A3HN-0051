def giao_dich(stk,chuyen_khoan,stk_nguoi_nhan):
    list_giao_dich = [stk, chuyen_khoan, stk_nguoi_nhan]
    print(list_giao_dich[0], "là số tài khoản của bạn")
    print(list_giao_dich[1], "là số tiền bạn chuyển khoản")
    print(list_giao_dich[2], "là số tài khoản người nhận")

def lua_chon(list_giao_dich):
    so = int(input("Bạn muốn ghi thông tin giao dịch không? (1/0)"))
    if so ==0:
        print("Kết thúc")
    elif so ==1:
        import datetime
        import json
        ten_file = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S.json")
        with open(ten_file, mode= 'w', encoding='UTF-8') as f:
            json.dump(list_giao_dich, f, ensure_ascii=False, indent=2)

stk = input("Nhập số tài khoản của bạn: ")
if stk.isnumeric() == False:
    print("Hãy nhập lại số tài khoản")
chuyen_khoan = int(input("Số tiền bạn muốn chuyển: "))
stk_nguoi_nhan = input("Nhập số tài khoản người nhận: ")
if stk_nguoi_nhan.isnumeric() == False:
    print("Hãy nhập lại số tài khoản")
list_giao_dich = [stk, chuyen_khoan, stk_nguoi_nhan]
print(giao_dich(stk, chuyen_khoan, stk_nguoi_nhan))
print(lua_chon(list_giao_dich))




