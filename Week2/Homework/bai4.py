def xu_ly_bai_4(ten_file):
    # 1. Đọc file
    f = open(ten_file, 'r', encoding='utf-8')
    noi_dung = f.read()
    f.close()
    
    # 2. Tách chuỗi bằng split() và chuyển đổi bằng append()
    cac_chuoi = noi_dung.split()
    danh_sach_so = []
    for x in cac_chuoi:
        danh_sach_so.append(int(x))
        
    # 3. Phân loại chẵn lẻ và tính tổng
    chan = []
    le = []
    tong_chan = 0
    tong_le = 0
    
    for so in danh_sach_so:
        if so % 2 == 0:
            chan.append(so)
            tong_chan += so
        else:
            le.append(so)
            tong_le += so
            
    # 4. Ghi file chan.txt
    f_chan = open("chan.txt", 'w', encoding='utf-8')
    chuoi_chan = ""
    for i in range(len(chan)):
        chuoi_chan += str(chan[i])
        if i < len(chan) - 1:
            chuoi_chan += " "
    f_chan.write(chuoi_chan)
    f_chan.close()
    
    # 5. Ghi file le.txt
    f_le = open("le.txt", 'w', encoding='utf-8')
    chuoi_le = ""
    for i in range(len(le)):
        chuoi_le += str(le[i])
        if i < len(le) - 1:
            chuoi_le += " "
    f_le.write(chuoi_le)
    f_le.close()
    
    # 6. Xuất kết quả
    print(f"chan.txt: {chuoi_chan} (Tổng: {tong_chan})")
    print(f"le.txt: {chuoi_le} (Tổng: {tong_le})")


ten_file = input("Nhập tên tập tin chứa dãy số: ")
xu_ly_bai_4(ten_file)

