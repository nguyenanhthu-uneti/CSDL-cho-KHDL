import pandas as pd
import numpy as np

# Dữ liệu mẫu
df = pd.DataFrame({
    'value': [10, 12, 11, 13, 9, 100, 12, 11, 10, 13]
})

# Bước 1: Tính median
median = df['value'].median()

# Bước 2: Tính độ lệch tuyệt đối
df['abs_dev'] = abs(df['value'] - median)

# Bước 3: Tính MAD
mad = df['abs_dev'].median()

# Bước 4: Đặt ngưỡng (ví dụ: 1.5 * MAD)
threshold = 1.5 * mad

# Bước 5: Đánh dấu ngoại lệ
df['is_outlier'] = df['abs_dev'] > threshold

print(df)
