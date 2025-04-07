import sqlite3

# Kết nối lại với cơ sở dữ liệu SQLite
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Tạo bảng và chèn dữ liệu mẫu cho câu hỏi 2 (kiểm tra sự khác biệt giữa các mẫu)
cursor.execute('''
CREATE TABLE samples (
    Day INTEGER,
    A REAL,
    B REAL,
    C REAL
)
''')

samples_data = [
    (1, 8, 9, 7),
    (2, 7.5, 8.5, 7),
    (3, 6, 7, 8),
    (4, 7, 6, 5),
]

cursor.executemany('INSERT INTO samples (Day, A, B, C) VALUES (?, ?, ?, ?)', samples_data)
conn.commit()

# Tính tổng của từng mẫu qua các ngày (A, B, C)
query2 = '''
SELECT 
    SUM(A) AS total_A,
    SUM(B) AS total_B,
    SUM(C) AS total_C
FROM
    samples;
'''

cursor.execute(query2)
total_samples = cursor.fetchall()
print(f"Total A: {total_samples[0][0]}, Total B: {total_samples[0][1]}, Total C: {total_samples[0][2]}")

# Đóng kết nối
conn.close()
