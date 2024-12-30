import sqlite3
import os

db_path = r'D:\42-Nguyễn Văn Vinh-DHKL17A3HN-0051\Bài tập LAB_DHKL17A3\LAB4\DATA\product.db'

conn = sqlite3.connect(db_path)

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS product (
                Id INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Price REAL NOT NULL,
                Amount INTEGER NOT NULL)''')

conn.commit()
conn.close()

def display_products():
    conn = sqlite3.connect('product.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM product")
    products = cur.fetchall()
    for product in products:
        print(product)
    conn.close()

def add_product(name, price, amount):
    conn = sqlite3.connect('product.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (name, price, amount))
    conn.commit()
    conn.close()

def search_product(name):
    conn = sqlite3.connect('product.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM product WHERE Name = ?", (name,))
    products = cur.fetchall()
    for product in products:
        print(product)
    conn.close()

def delete_product(id):
    conn = sqlite3.connect('product.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM product WHERE Id = ?", (id,))
    conn.commit()
    conn.close()

def menu():
    while True:
        print("\n1. Hiển Thị Danh Sách Sản Phẩm")
        print("2. Thêm Sản Phẩm Mới")
        print("3. Tìm Kiếm Sản Phẩm Theo Tên")
        print("4. Cập Nhật Thông Tin Sản Phẩm")
        print("5. Xóa Sản Phẩm")
        print("6. Thoát")
        choice = input("Chọn chức năng: ")
        
        if choice == '1':
            display_products()
        elif choice == '2':
            name = input("Tên sản phẩm: ")
            price = float(input("Giá: "))
            amount = int(input("Số lượng: "))
            add_product(name, price, amount)
        elif choice == '3':
            name = input("Tên sản phẩm cần tìm: ")
            search_product(name)
        elif choice == '4':
            id = int(input("ID sản phẩm cần cập nhật: "))
            price = float(input("Giá mới: "))
            amount = int(input("Số lượng mới: "))
            update_product= float(id, price, amount)
        elif choice == '5':
            id = int(input("ID sản phẩm cần xóa: "))
            delete_product(id)
        elif choice == '6':
            break
        else:
            print("Lựa chọn không hợp lệ!")

menu()

