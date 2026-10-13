def thong_ke_tap_tin(ten_file):
    # Mở tập tin để đọc nội dung
    f = open(ten_file, 'r', encoding='utf-8')
    noi_dung = f.read()
    f.close()
    
    so_dong = 0
    so_tu = 0
    so_ky_tu = 0
    
    # Nếu file không rỗng thì bắt đầu tính từ dòng 1
    if len(noi_dung) > 0:
        so_dong = 1
        
    dang_o_trong_tu = False # Biến cờ để theo dõi trạng thái từ
    
    # Duyệt qua từng ký tự trong nội dung
    for i in range(len(noi_dung)):
        c = noi_dung[i]
        
        # Đếm số dòng dựa trên ký tự xuống dòng
        if c == '\n':
            so_dong += 1
            
        # Đếm ký tự (không tính khoảng trắng, tab, xuống dòng)
        if c != ' ' and c != '\t' and c != '\n' and c != '\r':
            so_ky_tu += 1
            
        # Đếm số từ dựa vào việc chuyển đổi trạng thái khoảng trắng và chữ cái
        if c == ' ' or c == '\t' or c == '\n' or c == '\r':
            dang_o_trong_tu = False
        else:
            if not dang_o_trong_tu:
                so_tu += 1
                dang_o_trong_tu = True
                
    print(f"Kết quả: {so_dong} dòng . {so_tu} từ . {so_ky_tu} ký tự")

thong_ke_tap_tin(input("Nhập tên tập tin văn bản: "))