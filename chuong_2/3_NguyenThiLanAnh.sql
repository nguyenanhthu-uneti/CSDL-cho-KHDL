-- Tạo database 
CREATE DATABASE IF NOT EXISTS school;
USE school;

-- Tạo bảng course
CREATE TABLE IF NOT EXISTS course (
    id INT PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL
);

-- Tạo bảng student
CREATE TABLE IF NOT EXISTS student (
    student_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    class VARCHAR(255) NOT NULL,
    course_id INT, 
    score FLOAT
);

-- Thêm dữ liệu vào bảng course
INSERT INTO course (id, course_name) VALUES
(12, 'Giai tich'),
(34, 'Thong ke'),
(26, 'Tin hoc');

-- Thêm dữ liệu vào bảng student
INSERT INTO student (student_id, name, class, course_id, score) VALUES
(1, 'Nguyen Minh Hoang', 'May Tinh', 12, 6.7),
(2, 'Tran Thi Lan', 'Kinh Te', 34, 9.2),
(3, 'Pham Van Nam', 'Toan Tin', NULL, 7.9),
(4, 'Le Thanh Huyen', 'Toan Tin', 20, 7.2),
(5, 'Vu Quoc Anh', 'May Tinh', 24, 8.0),
(6, 'Dang Thuy Linh', 'May Tinh', 24, 5.5),
(7, 'Bui Tien Dung', 'Kinh Te', 34, 9.2),
(8, 'Ho Ngoc Mai', 'Toan Tin', 20, 8.8),
(9, 'Duong Huu Phuc', 'Kinh Te', NULL, 7.2),
(10, 'Cao Thi Hanh', 'May Tinh', NULL, 7.0);
SELECT * FROM student;
SELECT * FROM course;

--- INNERJOIN chỉ lấy những dòng có khóa học hợp lệ (course_id của student có trong id của course)
SELECT * FROM student  
JOIN course ON student.course_id = course.id;
--- LEFTJOIN lấy tất cả sinh viên từ student, kể cả sinh viên chưa có khóa học
SELECT * FROM student  
LEFT JOIN course ON student.course_id = course.id;
---- RIGHTJOIN lấy tất cả khóa học từ course, kể cả những khóa không có sinh viên nào
SELECT * FROM student  
RIGHT JOIN course ON student.course_id = course.id;
--- FULLOUTERJOIN lấy tất cả sinh viên + tất cả khóa học.
SELECT * FROM student  
LEFT JOIN course ON student.course_id = course.id
UNION
SELECT * FROM student  
RIGHT JOIN course ON student.course_id = course.id;
--- Cập nhật các course_id còn thiếu bằng giá trị hợp lệ
UPDATE student 
SET course_id = (SELECT id FROM course ORDER BY RAND() LIMIT 1)
WHERE course_id IS NULL;
-------------- ORDERBYRAND()LIMIT1: Chọn ngẫu nhiên một id từ bảng course.
-------------- WHEREcourse_idISNULL: Chỉ cập nhật các bản ghi course_id đang bị thiếu.
--- Xóa các bản ghi có course_id không tồn tại trong bảng course
DELETE FROM student
WHERE course_id NOT IN (SELECT id FROM course);
---- Tổng số sinh viên, điểm trung bình của từng lớp. 
SELECT 
    class, 
    COUNT(student_id) AS total_students, 
    AVG(score) AS avg_score
FROM student
GROUP BY class;
---- Tổng số sinh viên, điểm trung bình của từng môn học. 
SELECT course.course_name, 
       COUNT(student.student_id) AS total_students, 
       AVG(student.score) AS avg_score
FROM course
LEFT JOIN student ON student.course_id = course.id
GROUP BY course.course_name;
---- Danh sách môn học có điểm trung bình ≥ 9.0 (Xuất sắc)
SELECT course.course_name, 
       COUNT(student.student_id) AS total_students, 
       AVG(student.score) AS avg_score
FROM course
LEFT JOIN student ON student.course_id = course.id
GROUP BY course.course_name
HAVING AVG(student.score) >= 9.0;
--- Danh sách môn học có điểm trung bình từ 6.0 đến 8.9 (Tốt)
SELECT course.course_name, 
       COUNT(student.student_id) AS total_students, 
       AVG(student.score) AS avg_score
FROM course
LEFT JOIN student ON student.course_id = course.id
GROUP BY course.course_name
HAVING AVG(student.score) BETWEEN 6.0 AND 8.9;
---- Danh sách môn học có điểm trung bình < 6.0 (Kém)
SELECT course.course_name, 
       COUNT(student.student_id) AS total_students, 
       AVG(student.score) AS avg_score
FROM course
LEFT JOIN student ON student.course_id = course.id
GROUP BY course.course_name
HAVING AVG(student.score) < 6.0;
------ Xếp hạng sinh viên theo điểm số chung
SELECT 
    student_id, 
    name, 
    class, 
    course_id, 
    score,
    RANK() OVER (ORDER BY score DESC) AS overall_rank
FROM student;
---- Xếp hạng sinh viên theo điểm số trong từng lớp
SELECT 
    student_id, 
    name, 
    class, 
    course_id, 
    score,
    DENSE_RANK() OVER (PARTITION BY class ORDER BY score DESC) AS class_rank
FROM student;
--- Xếp hạng sinh viên theo điểm số trong từng môn học
SELECT 
    student_id, 
    name, 
    class, 
    course_name, 
    score,
    DENSE_RANK() OVER (
        PARTITION BY course_name 
        ORDER BY score DESC
    ) AS course_rank
FROM student 
LEFT JOIN course ON student.course_id = course.id;
-- Top 3 sinh viên có điểm cao nhất
SELECT student_id, name, class, course_id, score
FROM student
ORDER BY score DESC
LIMIT 3;

-- Top 3 sinh viên có điểm thấp nhất
SELECT student_id, name, class, course_id, score
FROM student
ORDER BY score DESC
LIMIT 3;
-- Top 3 sinh viên có điểm cao nhất theo từng lớp
SELECT student_id, name, class, course_id, score, rnk AS ranktop
FROM (
    SELECT *, 
           DENSE_RANK() OVER (PARTITION BY class ORDER BY score DESC) AS rnk
    FROM student
) AS ranked
WHERE rnk <= 3
ORDER BY class, score DESC;

-- Top 3 sinh viên có điểm thấp nhất theo từng lớp
SELECT student_id, name, class, course_id, score, rnk AS rankshort
FROM (
    SELECT *, 
           DENSE_RANK() OVER (PARTITION BY class ORDER BY score ASC) AS rnk
    FROM student
) AS ranked
WHERE rnk <= 3
ORDER BY class, score ASC;
---- Top 3 sinh viên có điểm cao nhất theo từng môn học
SELECT student_id, name, class, course_name, score, course_rank AS ranking
FROM (
    SELECT 
        student_id, 
        name, 
        class, 
        course_name, 
        score,
        DENSE_RANK() OVER (
            PARTITION BY course_name 
            ORDER BY score DESC
        ) AS course_rank
    FROM student 
    LEFT JOIN course ON student.course_id = course.id
) AS ranked
WHERE course_rank <= 3;
--- Top 3 sinh viên có điểm thấp nhất theo từng môn học
SELECT student_id, name, class, course_name, score, course_rank AS ranking
FROM (
    SELECT 
        student_id, 
        name, 
        class, 
        course_name, 
        score,
        DENSE_RANK() OVER (
            PARTITION BY course_name 
            ORDER BY score ASC
        ) AS course_rank
    FROM student 
    LEFT JOIN course ON student.course_id = course.id
) AS ranked
WHERE course_rank <= 3;

-- Thêm cột graduation_date vào bảng student
ALTER TABLE student ADD COLUMN graduation_date DATETIME;

-- Cập nhật graduation_date dựa trên thứ hạng của sinh viên theo điểm số
UPDATE student s
JOIN (
    SELECT student_id, 
           DENSE_RANK() OVER (ORDER BY score DESC) AS ranking
    FROM student
) AS ranked ON s.student_id = ranked.student_id
SET s.graduation_date = NOW() + INTERVAL ranked.ranking MONTH;
---- Kiểm tra kết quả
SELECT student_id, name, score, graduation_date 
FROM student
ORDER BY graduation_date;












