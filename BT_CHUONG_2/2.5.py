import xml.dom.minidom
def main():
    doc = xml.dom.minidom.parse("sample.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    name = doc.getElementsByTagName("name")
    salary = doc.getElementsByTagName("salary")

    for n in name:
        print(n.firstChild.nodeValue)
    for s in salary:
        print(s.firstChild.nodeValue)

if __name__ == "__main__":
    main()


