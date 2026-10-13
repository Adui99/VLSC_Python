def chuyen_doi_chu_hoa(file_nguon, file_dich):
    # Mở tập tin nguồn để đọc và tập tin đích để ghi
    f_in = open(file_nguon, 'r', encoding='utf-8')
    f_out = open(file_dich, 'w', encoding='utf-8')
    
    # Đọc nội dung, chuyển thành chữ in hoa và ghi sang file đích
    f_out.write(f_in.read().upper())
    
    # Đóng các tập tin
    f_in.close()
    f_out.close()
    print(f"Đã chuyển đổi thành công sang '{file_dich}'.")

chuyen_doi_chu_hoa(input("Nhập tên tập tin nguồn: "), input("Nhập tên tập tin đích: "))