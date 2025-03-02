print("menu")
print("1.phim hành động")
print("2.phim ma")
print("3.phim tuổi học trò")
print("4.phim tình cảm")
print("5.phim tình cảm gia đình")
print("0.không chọn phim nào")
lua_chon = int(input("lựa chọn ở menu (1,2,3,4,5,0): "))
if lua_chon == 1:
    print("phim hành động")
if lua_chon == 2:
    print("phim ma")
if lua_chon == 3:
    print("phim tuổi học trò")
if lua_chon == 4:
    print("phim tình cảm")
if lua_chon == 5:
    print("phim tình cảm gia đình")
if lua_chon == 0:
    print("không chọn phim nào")
else:
    print("nhập lại đúng menu")