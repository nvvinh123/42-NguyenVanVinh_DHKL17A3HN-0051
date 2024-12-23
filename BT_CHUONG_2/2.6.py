import requests
import xml.etree.ElementTree as ET
url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
phan_hoi = requests.get(url)
if phan_hoi.status_code ==200:
    noi_dung = phan_hoi.content
    root = ET.ElementTree(ET.fromstring(noi_dung))
    with open('tin_tuc.xml', 'wb') as xml_file:
        root.write(xml_file)
else:
    print("Yêu cầu tải nguồn RSS thất bại. Mã trạng thái: ", phan_hoi.status_code)

