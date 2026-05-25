raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 " 
menu = '''
===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====
1. Hiển thị chuỗi mã vạch gốc
2. Giải mã, làm sạch và in báo cáo kiểm kê
3. Tra cứu nhanh theo đuôi Serial
4. Thoát chương trình
'''

while True:
    print(menu)
    choice = int(input("Nhập lựa chọn của bạn (1-4): "))

    match choice:
        case 1:
            print("raw_batch")
        case 2:
            isvalid = 0
            list_item = raw_batch.split(";")
            for item in list_item:
                category = item.split("-")[0].strip().upper()
                nation = item.split("-")[1].strip().upper()
                year_of_manufacture = item.split("-")[2].strip()
                year_of_manufacture = "20" + year_of_manufacture
                serials = item.split("-")[3].strip()
                
                if serials.isdigit():
                    status = "Pass"
                    isvalid += 1
                else:
                    status = "Lỗi Serial - Reject"
                
                print(f"{category:<4}  | {nation:<7} | {year_of_manufacture:<6} | {serials:<6} | {status:<3} ")
                
            print()
            print(f"Đã giải mã thành công {isvalid} sản phẩm hợp lệ / Tổng số {len(list_item)} sản phẩm.")
            
        case 3:
            is_find = False 
            search_input = input("Nhập serial muốn tìm: ").strip()
            list_item = raw_batch.split(";")
            for item in list_item:
                category = item.split("-")[0].strip().upper()
                nation = item.split("-")[1].strip().upper()
                year_of_manufacture = item.split("-")[2].strip()
                year_of_manufacture = "20" + year_of_manufacture
                serials = item.split("-")[3].strip()
                
                if serials.isdigit():
                    status = "Pass"
                else:
                    status = "Lỗi Serial - Reject"
                if search_input == serials:
                    print(f"MÃ SP | XUẤT XỨ | NĂM SX | SERIAL | TRẠNG THÁI")
                    print(f"{category:<4}  | {nation:<7} | {year_of_manufacture:<6} | {serials:<6} | {status:<3} ")
                    is_find = True
                    break
                
            if is_find == False:
                print(f"Không tìm thấy {search_input} trong kho")
                
        case 4: 
            print("Cảm ơn vì đã sử dụng chương trình!!!")
            break
        case _:
            print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")
            
            
            
'''
- input:   
    + các lựa chọn
- output:
    + dữ liệu thô
    + dữ liệu đã qua sử lý
    + số lượng sp hợp lệ
    + mặt hàng đang tìm
    
- các phương thức cần dùng: upper(), len(), split(), strip(), isdigit()
-Pseudocode 
- khai báo raw_batch
- chạy vòng lặp while True đến khi nào nhập 4 để dừng lại
- quan sát lựa chọn người dùng để thực hiện chức năng 




'''
