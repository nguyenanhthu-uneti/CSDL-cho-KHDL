import sqlite3

# Kết nối lại với cơ sở dữ liệu SQLite
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Tạo bảng và chèn dữ liệu cho câu hỏi 3 (chuyển đổi thời gian)
cursor.execute('''
CREATE TABLE flights (
    departure_time INTEGER
)
''')

flights_data = [
    (830,),
    (1445,),
    (1230,),
    (500,)
]

cursor.executemany('INSERT INTO flights (departure_time) VALUES (?)', flights_data)
conn.commit()

# Chuyển đổi thời gian từ số nguyên thành định dạng thời gian (HH:MM)
query3 = '''
SELECT
    departure_time,
    CAST(CAST(departure_time / 100 AS INTEGER) AS TEXT) || ':' || 
    CAST(departure_time % 100 AS TEXT) AS departure_time_formatted
FROM
    flights;
'''

cursor.execute(query3)
time_formats = cursor.fetchall()
print("Converted Departure Times:")
for time in time_formats:
    print(f"{time[0]} => {time[1]}")

# Đóng kết nối
conn.close()
