import sqlite3

# Kết nối lại với cơ sở dữ liệu SQLite
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Tạo bảng và chèn dữ liệu cho câu hỏi 5 (so sánh người dựa trên last_name và weight)
cursor.execute('''
CREATE TABLE Patient (
    last_name TEXT,
    weight REAL
)
''')

patients_data = [
    ('Smith', 70),
    ('Johnson', 75),
    ('Smith', 72),
    ('Brown', 68),
]

cursor.executemany('INSERT INTO Patient (last_name, weight) VALUES (?, ?)', patients_data)
conn.commit()

# Câu lệnh SQL để so sánh các người dựa trên last_name và weight
query5 = '''
SELECT 
    p1.last_name,
    p1.weight,
    p2.last_name,
    p2.weight,
    CASE
        WHEN p1.last_name = p2.last_name AND ABS(p1.weight - p2.weight) < 5 THEN 'Same person'
        ELSE 'Different person'
    END AS person_comparison
FROM
    Patient p1
JOIN
    Patient p2
ON
    p1.rowid != p2.rowid;
'''

cursor.execute(query5)
person_comparison = cursor.fetchall()
print("Person Comparison Results:")
for comparison in person_comparison:
    print(f"{comparison[0]} ({comparison[1]}) and {comparison[2]} ({comparison[3]}) -> {comparison[4]}")

# Đóng kết nối
conn.close()
