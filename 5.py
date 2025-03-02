#bai 5
ky_tu = input("Nhập một ký tự: ")
if ky_tu.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(f"Ký tự '{ky_tu}' là nguyên âm.")
else:
    print(f"Ký tự '{ky_tu}' là phụ âm.")
