t_n_c_t = float(input("nhập thâm niên (tháng):"))
luong_cb = 1.35
if t_n_c_t >= 60:
    luong = luong_cb * 3.99
elif 36 <= t_n_c_t < 60 :
    luong = luong_cb * 3.66
elif 12 <= t_n_c_t < 36 :
    luong = luong_cb *3.33
else :
    luong = luong_cb* 2.34
print(f"lương nhân viên đó nhận được là :{luong:.3f} " )