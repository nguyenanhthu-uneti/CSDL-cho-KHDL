import pandas as pd

# Dữ liệu mẫu
df = pd.DataFrame({
    'departure_time': [830, 1445, 5, 1230]
})

# Hàm chuyển đổi
def convert_to_time(val):
    val = f"{val:04}"  # Đảm bảo đủ 4 chữ số (ví dụ: 5 -> '0005')
    hour = int(val[:2])
    minute = int(val[2:])
    return f"{hour:02}:{minute:02}"

# Áp dụng
df['formatted_time'] = df['departure_time'].apply(convert_to_time)
print(df)
