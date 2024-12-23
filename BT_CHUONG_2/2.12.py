import requests
yeu_cau = requests.get('https://jsonplaceholder.typicode.com/posts')
if yeu_cau.status_code ==200:
    du_lieu_json = yeu_cau.json()

    so_bai_dang = 0
    for post in du_lieu_json:
        so_bai_dang += 1
        print("Số bài đăng: ", so_bai_dang)
        print("User ID từ bài đăng là: ", post['userId'])
        print("ID bài đăng là: ", post['id'])
        print("Tiêu đề: ", post['title'])
        print("Nội dung: ", post['body'])
        print("========================Kết thúc=============================")
else:
    print("Yêu cầu thất bại. Mã trạng thái: ", yeu_cau.status_code)