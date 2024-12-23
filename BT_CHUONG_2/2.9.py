import json
du_lieu = {
    "Tên": "A",
    "Tuổi": 19,
    "Ngành": "Khoa học dữ liệu",
    "Trường đại học": "UNETI"
}

chuoi_json = json.dumps(du_lieu, ensure_ascii=False, indent=4, sort_keys=True)
print(chuoi_json)