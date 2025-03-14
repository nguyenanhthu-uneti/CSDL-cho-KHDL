import sqlite3


conn = sqlite3.connect('NHANVIEN.db')

cursor = conn.cursor()

# 1. create table
cursor.execute("DROP TABLE IF EXISTS NHANVIEN1")
cursor.execute('''
               CREATE TABLE IF NOT EXISTS NHANVIEN1 (
                         MANV INT PRIMARY KEY,
                         HOTEN VARCHAR(50) NOT NULL,
                         TUOI INT NOT NULL,
                         PHONGBAN VARCHAR(50) NOT NULL
               )
               ''')

conn.commit()

# 2. insert data
data = [  
          (1, 'Nguyen Van A', 30, 'Ke Toan'),
          (2, 'Tran Thi B', 25, 'Nhan Su'),
          (3, 'Le Van C', 28, 'IT'),
          (4, 'Pham Thi D', 32, 'Ke Toan'),
          (5, 'Vu Van E', 26, 'IT'),
          (6, 'Nguyen Thi F', 29, 'Marketing'),
          (7, 'Le Thi G', 27, 'Nhan Su'),
          (8, 'Hoang Van H', 35, 'Ke Toan'),
          (9, 'Pham Van I', 33, 'Marketing'),
          (10, 'Tran Van J', 24, 'IT'),
          (11, 'Dang Thi K', 31, 'Nhan Su'),
          (12, 'Nguyen Van L', 28, 'Ke Toan'),
          (13, 'Tran Thi M', 26, 'Marketing'),
          (14, 'Pham Van N', 30, 'Nhan Su'),
          (15, 'Hoang Thi O', 27, 'IT')
          ]
                    
cursor.executemany("INSERT INTO NHANVIEN1 (MANV, HOTEN, TUOI, PHONGBAN) VALUES (?, ?, ?, ?)", data)
conn.commit()

# 3. select data
cursor.execute("SELECT * FROM NHANVIEN1")
rows = cursor.fetchall()
for row in rows:
          print(row)
          
# 4. qerry Hoten, tuoi staff  in IT department
cursor.execute("SELECT HOTEN, TUOI FROM NHANVIEN1 WHERE PHONGBAN = 'IT'")
print(cursor.fetchall(), '\n')

# 5. find age staff bigger than 25
cursor.execute("SELECT * FROM NHANVIEN1 WHERE TUOI > 25")
than25 = cursor.fetchall()
print("STAFFS BIGGER THAN 25")
for row in than25:
    print(row)

# 6. the oldest staff in departments
print('\n')
cursor.execute("SELECT HOTEN,PHONGBAN, MAX(TUOI) FROM NHANVIEN1 GROUP BY PHONGBAN")
print("THE OLDEST STAFF IN DEPARTMENTS")
department_oldest = cursor.fetchall()
for row in department_oldest:
    print(row)      
print('\n')

# 7. convert info department 'Le Van C' to 'Marketing'
cursor.execute("UPDATE NHANVIEN1 SET PHONGBAN = 'Marketing' where HOTEN = 'Le Van C'")
conn.commit()
print('Le Van C move to Marketing department')
cursor.execute("SELECT * FROM NHANVIEN1")
rows = cursor.fetchall()
for row in rows:
          print(row)
print('\n')

# 8.delete staff MANV = 2
cursor.execute("DELETE FROM NHANVIEN1 WHERE MANV = 2")
conn.commit()
cursor.execute("SELECT PHONGBAN,COUNT(HOTEN) FROM NHANVIEN1 GROUP BY PHONGBAN")
print(cursor.fetchall(), '\n')