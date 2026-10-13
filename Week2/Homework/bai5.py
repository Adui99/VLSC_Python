def xu_ly_bai_5(ten_file):
    # 1. Nhập nội dung từ bàn phím cho đến khi gặp "exit"
    print("Nhập nội dung (gõ 'exit' để dừng):")
    danh_sach_dong = []
    while True:
        dong = input()
        if dong == "exit":
            break
        # Dùng append() để thêm dòng kèm ký tự xuống dòng
        danh_sach_dong.append(dong + "\n")
        
    # 2. Mở file ở chế độ 'a' (append) để ghi thêm vào cuối
    f_ghi = open(ten_file, 'w' if False else 'a', encoding='utf-8')
    for d in danh_sach_dong:
        f_ghi.write(d)
    f_ghi.close()
    
    # 3. Đọc lại toàn bộ nội dung tập tin để xuất ra màn hình
    f_doc = open(ten_file, 'r', encoding='utf-8')
    noi_dung = f_doc.read()
    f_doc.close()
    
    print("\n--- NỘI DUNG SAU KHI GHI ---")
    print(noi_dung)


ten_file = input("Nhập tên tập tin: ")
xu_ly_bai_5(ten_file)