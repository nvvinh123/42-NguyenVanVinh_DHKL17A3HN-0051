import requests
yeu_cau = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
if yeu_cau.status_code ==200:
    du_lieu_json = yeu_cau.json()
    for post in du_lieu_json:
        print("Bài đăng nổi bật là: ", post['name'])
    for post in du_lieu_json[:3]:
        print("ID bài đăng: ", post['postId'])
        print("ID: ", post['id'])
        print("Tên bài đăng: ", post['name'])
        print("Email: ", post['email'])
        print("Nội dung bài đăng: ", post['body'])
        print("=================Kết thúc=====================")
else:
    print("Yêu cầu thất bại. Mã trạng thái: ", yeu_cau.status_code)
