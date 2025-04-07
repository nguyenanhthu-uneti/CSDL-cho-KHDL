import sqlite3

# Kết nối lại với cơ sở dữ liệu SQLite
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Tạo bảng và chèn dữ liệu cho câu hỏi 4 (phát hiện ngoại lệ bằng MAD)
cursor.execute('''
CREATE TABLE data_table_for_outliers (
    value REAL
)
''')

outliers_data = [
    (8.1,),
    (7.5,),
    (6.0,),
    (7.0,),
    (8.0,),
]

cursor.executemany('INSERT INTO data_table_for_outliers (value) VALUES (?)', outliers_data)
conn.commit()

# Câu lệnh SQL để phát hiện các ngoại lệ sử dụng MAD
query4 = '''
WITH stats AS (
    SELECT
        AVG(value) AS mean_value,
        MEDIAN(ABS(value - AVG(value))) AS mad
    FROM
        data_table_for_outliers
),
outliers AS (
    SELECT
        value,
        ABS(value - (SELECT mean_value FROM stats)) AS deviation
    FROM
        data_table_for_outliers
)
SELECT
    value
FROM
    outliers
WHERE
    deviation > 1.5 * (SELECT mad FROM stats);
'''

cursor.execute(query4)
outliers = cursor.fetchall()
print("Outliers detected based on MAD:")
for outlier in outliers:
    print(outlier[0])

# Đóng kết nối
conn.close()
