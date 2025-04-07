import sqlite3
import math

# Kết nối với cơ sở dữ liệu SQLite (ở đây sử dụng :memory: để tạo cơ sở dữ liệu trong bộ nhớ)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Tạo bảng và chèn dữ liệu mẫu cho câu hỏi 1 (hệ số tương quan giữa A và B)
cursor.execute('''
CREATE TABLE data_table (
    A REAL,
    B REAL
)
''')

data = [
    (8, 9),
    (7.5, 8.5),
    (6, 7),
    (7, 6),
]

cursor.executemany('INSERT INTO data_table (A, B) VALUES (?, ?)', data)
conn.commit()

# Tính số lượng các cặp giá trị (n)
query_n = 'SELECT COUNT(*) FROM data_table'
cursor.execute(query_n)
n = cursor.fetchone()[0]

# Tính toán hệ số tương quan Pearson sử dụng công thức
query1 = '''
SELECT
    ({} * SUM(A * B) - SUM(A) * SUM(B)) / 
    (SQRT(({} * SUM(A * A) - SUM(A) * SUM(A)) * ({} * SUM(B * B) - SUM(B) * SUM(B)))) AS correlation
FROM
    data_table;
'''.format(n, n, n)

cursor.execute(query1)
correlation = cursor.fetchone()[0]
print(f"Correlation between A and B: {correlation}")

# Đóng kết nối
conn.close()
