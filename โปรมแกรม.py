import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        morning = int(entry_morning.get())
        lunch = int(entry_lunch.get())
        evening = int(entry_evening.get())

        total = morning + lunch + evening

        result_label.config(
            text=f"สรุปแคลอรี่ที่ได้รับ\n"
                 f"มื้อเช้า: {morning} kcal\n"
                 f"มื้อกลางวัน: {lunch} kcal\n"
                 f"มื้อเย็น: {evening} kcal\n"
                 f"รวมทั้งหมด: {total} kcal"
        )
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกตัวเลขเท่านั้น")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมคำนวณแคลอรี่")
root.geometry("300x350")

# หัวข้อ
tk.Label(root, text="โปรแกรมคำนวณแคลอรี่", font=("TH Sarabun New", 16, "bold")).pack(pady=10)

# มื้อเช้า
tk.Label(root, text="แคลอรี่มื้อเช้า (kcal)").pack()
entry_morning = tk.Entry(root)
entry_morning.pack()

# มื้อกลางวัน
tk.Label(root, text="แคลอรี่มื้อกลางวัน (kcal)").pack()
entry_lunch = tk.Entry(root)
entry_lunch.pack()

# มื้อเย็น
tk.Label(root, text="แคลอรี่มื้อเย็น (kcal)").pack()
entry_evening = tk.Entry(root)
entry_evening.pack()
