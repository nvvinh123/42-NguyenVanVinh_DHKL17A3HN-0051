import tkinter as tk
from tkinter import messagebox
import sqlite3

db_path = r"D:\42-Nguyễn Văn Vinh-DHKL17A3HN-0051\Bài tập LAB_DHKL17A3\LAB4\DATA\product.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS product (
                Id INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Price REAL NOT NULL,
                Amount INTEGER NOT NULL)''')
conn.commit()

def display_products():
    cur.execute("SELECT * FROM product")
    rows = cur.fetchall()
    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, row)

def add_product():
    name = entry_name.get()
    price = entry_price.get()
    amount = entry_amount.get()
    if name and price and amount:
        cur.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (name, price, amount))
        conn.commit()
        display_products()
    else:
        messagebox.showwarning("Lỗi", "Vui lòng nhập đủ thông tin")

root = tk.Tk()
root.title("Quản lý sản phẩm")

tk.Label(root, text="Tên sản phẩm").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Giá").grid(row=1, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=1, column=1)

tk.Label(root, text="Số lượng").grid(row=2, column=0)
entry_amount = tk.Entry(root)
entry_amount.grid(row=2, column=1)

tk.Button(root, text="Thêm sản phẩm", command=add_product).grid(row=3, column=0, columnspan=2)

listbox = tk.Listbox(root, width=50)
listbox.grid(row=4, column=0, columnspan=2)

display_products()

root.mainloop()

conn.close()
