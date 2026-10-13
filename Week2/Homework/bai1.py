import os
from datetime import datetime

def xem_tap_tin(ten_file):
    # Kiểm tra tập tin có tồn tại hay không
    if not os.path.exists(ten_file):
        print("Không tồn tại tập tin này")
        return
    
    # Nếu tồn tại, xuất thông tin và nội dung
    f = open(ten_file, 'r', encoding='utf-8')
    print(f"Kích thước: {os.path.getsize(ten_file)} bytes")
    print(f"Ngày tạo: {datetime.fromtimestamp(os.path.getctime(ten_file))}")
    print(f"Ngày sửa đổi: {datetime.fromtimestamp(os.path.getmtime(ten_file))}")
    print("Nội dung:\n" + f.read())
    f.close()

xem_tap_tin(input("Nhập tên tập tin: "))