import json
doi_tuong_python = {
    "Tên": "A",
    "Tuổi": 19,
    "Trường đại học": "UNETI"
}

chuoi_json = json.dumps(doi_tuong_python, ensure_ascii=False)
print(chuoi_json)