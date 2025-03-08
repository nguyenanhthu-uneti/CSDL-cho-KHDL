# Nhập lương 
luong = float(input("Nhập lương của nhân viên (triệu): "))
# Tính 
if luong >= 15:
    thue_thu_nhap = luong * 0.30
elif luong >= 7:
    thue_thu_nhap = luong * 0.20
else:
    thue_thu_nhap = luong * 0.10
# Tính lương ròng
luong_rong = luong - thue_thu_nhap
# kết quả
print("Thuế thu nhập:", thue_thu_nhap, "triệu VND")
print("Lương ròng:", luong_rong, "triệu VND")
