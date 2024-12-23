import json
json_1 = '{"Tên":"A", "Tuổi": 18, "Trường đại học": "UNETI"}'
json_2 = '{"Tên":"B", "Tuổi": 19, "Trường đại học": "UNETI"}'

doi_tuong_python_1 = json.loads(json_1)
doi_tuong_python_2 = json.loads(json_2)

print(doi_tuong_python_1)
print(doi_tuong_python_2)
