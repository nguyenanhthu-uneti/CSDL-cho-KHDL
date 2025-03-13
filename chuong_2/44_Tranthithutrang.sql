CREATE DATABASE IF NOT EXISTS StudentDB;
USE StudentDB;

CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    class VARCHAR(20),
    course_id INT,
    score FLOAT
);

INSERT INTO Student (student_id, name, class, course_id, score) VALUES
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
SELECT * FROM Student;

CREATE TABLE Course (
    id INT PRIMARY KEY,
    course_name VARCHAR(50)
);

INSERT INTO Course (id, course_name) VALUES
(12, 'Giai tich'),
(34, 'Thong ke'),
(26, 'Tin hoc');
SELECT * FROM Course;

# Kết nối 2 bảng
# Sử dụng Decartes
SELECT *
FROM Student,
	 Course;
# Sử dụng join
# INNER JOIN
SELECT Student.student_id, Student.name, Student.class, Student.score, Course.course_name
FROM Student
INNER JOIN Course ON Student.course_id = Course.id;
# LEFT JOIN
SELECT Student.student_id, Student.name, Student.class, Student.score, Course.course_name
FROM Student
LEFT JOIN Course ON Student.course_id = Course.id;
# RIGHT JOIN
SELECT Student.student_id, Student.name, Student.class, Student.score, Course.course_name
FROM Student
RIGHT JOIN Course ON Student.course_id = Course.id;
# FULL OUTER JOIN
SELECT Student.student_id, Student.name, Student.class, Student.score, Course.id, Course.course_name
FROM Student
LEFT JOIN Course ON Student.course_id = Course.id
UNION
SELECT Student.student_id, Student.name, Student.class, Student.score, Course.id, Course.course_name
FROM Student
RIGHT JOIN Course ON Student.course_id = Course.id;

#2
UPDATE Student 
SET course_id = (SELECT id FROM Course ORDER BY RANDOM() LIMIT 1)
WHERE course_id IS NULL;
DELETE FROM Student 
WHERE course_id NOT IN (SELECT id FROM Course);
#2a. Tổng số sinh viên, điểm trung bình của từng lớp.
SELECT class, COUNT(student_id) AS total_students, AVG(score) AS avg_score
FROM Student 
GROUP BY class;
#2b. Tổng số sinh viên, điểm trung bình của từng môn học.
SELECT Course.course_name, COUNT(Student.student_id) AS total_students, AVG(Student.score) AS avg_score
FROM Student
JOIN Course ON Student.course_id = Course.id
GROUP BY Course.course_name;
#2c. Phân loại thi đua
SELECT Course.course_name, 
       AVG(Student.score) AS avg_score,
       CASE 
           WHEN AVG(Student.score) >= 9.0 THEN 'Xuất sắc'
           WHEN AVG(Student.score) BETWEEN 6.0 AND 8.9 THEN 'Tốt'
           ELSE 'Kém'
       END rank_category
FROM Student
JOIN Course ON Student.course_id = Course.id
GROUP BY Course.course_name;

#3. Xếp hạng sinh viên
# Điểm số
SELECT student_id, name, class, course_id, score,
       RANK() OVER (ORDER BY score DESC) AS rank_overall
FROM Student;
# Top3 cao nhất và thấp nhất
-- Top 3 sinh viên có điểm cao nhất theo điểm số chung
SELECT student_id, name, class, course_id, score, 'Top 3 Overall' AS category
FROM (
    SELECT student_id, name, class, course_id, score,
           RANK() OVER (ORDER BY score DESC) AS rank_overall
    FROM Student
) AS Ranked_Overall
WHERE rank_overall <= 3;

-- Top 3 sinh viên có điểm thấp nhất theo điểm số chung
SELECT student_id, name, class, course_id, score, 'Bottom 3 Overall' AS category
FROM (
    SELECT student_id, name, class, course_id, score,
           RANK() OVER (ORDER BY score ASC) AS rank_lowest_overall
    FROM Student
) AS Ranked_Overall
WHERE rank_lowest_overall <= 3;

# Điểm số theo lớp
SELECT student_id, name, class, course_id, score,
       RANK() OVER (PARTITION BY class ORDER BY score DESC) AS rank_by_class
FROM Student;
# Top3
-- Top 3 sinh viên có điểm cao nhất theo từng lớp
SELECT student_id, name, class, course_id, score, 'Top 3 by Class' AS category
FROM (
    SELECT student_id, name, class, course_id, score,
           RANK() OVER (PARTITION BY class ORDER BY score DESC) AS rank_by_class
    FROM Student
) AS Ranked_By_Class
WHERE rank_by_class <= 3;

-- Top 3 sinh viên có điểm thấp nhất theo từng lớp
SELECT student_id, name, class, course_id, score, 'Bottom 3 by Class' AS category
FROM (
    SELECT student_id, name, class, course_id, score,
           RANK() OVER (PARTITION BY class ORDER BY score ASC) AS rank_lowest_by_class
    FROM Student
) AS Ranked_By_Class
WHERE rank_lowest_by_class <= 3;

# Điểm số theo mã môn học
SELECT student_id, name, class, course_id, score,
       RANK() OVER (PARTITION BY course_id ORDER BY score DESC) AS rank_by_course
FROM Student;
#Top3
-- Top 3 sinh viên có điểm cao nhất theo từng môn học
SELECT student_id, name, class, course_id, score, 'Top 3 by Course' AS category
FROM (
    SELECT student_id, name, class, course_id, score,
           RANK() OVER (PARTITION BY course_id ORDER BY score DESC) AS rank_by_course
    FROM Student
) AS Ranked_By_Course
WHERE rank_by_course <= 3;

-- Top 3 sinh viên có điểm thấp nhất theo từng môn học
SELECT student_id, name, class, course_id, score, 'Bottom 3 by Course' AS category
FROM (
    SELECT student_id, name, class, course_id, score,
           RANK() OVER (PARTITION BY course_id ORDER BY score ASC) AS rank_lowest_by_course
    FROM Student
) AS Ranked_By_Course
WHERE rank_lowest_by_course <= 3;

#4. 
-- Thêm cột graduation_date vào bảng Student nếu chưa có
ALTER TABLE Student ADD COLUMN graduation_date DATETIME;

-- Cập nhật graduation_date theo thứ hạng của sinh viên
UPDATE Student AS S
JOIN (
    -- Tạo bảng tạm với rank của từng sinh viên theo điểm số
    SELECT student_id, 
           RANK() OVER (ORDER BY score DESC) AS rank_position
    FROM Student
) AS Ranked ON S.student_id = Ranked.student_id
SET S.graduation_date = DATE_ADD(NOW(), INTERVAL Ranked.rank_position MONTH);

-- Kiểm tra lại dữ liệu sau khi cập nhật
SELECT student_id, name, score, graduation_date FROM Student ORDER BY graduation_date;





