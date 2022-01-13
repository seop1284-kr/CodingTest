-- 최댓값 구하기 https://programmers.co.kr/learn/courses/30/lessons/59415
SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME DESC LIMIT 1
SELECT MAX(DATETIME) FROM ANIMAL_INS

-- 최솟값 고르기 https://programmers.co.kr/learn/courses/30/lessons/59038
SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1
SELECT MIN(DATETIME) FROM ANIMAL_INS

-- 동물 수 구하기 https://programmers.co.kr/learn/courses/30/lessons/59406
SELECT COUNT(*) FROM ANIMAL_INS

-- 중복 제거하기 https://programmers.co.kr/learn/courses/30/lessons/59408
SELECT COUNT(distinct NAME) FROM ANIMAL_INS WHERE not NAME = "NULL"
SELECT COUNT(distinct NAME) FROM ANIMAL_INS WHERE not NAME is NULL
SELECT COUNT(distinct NAME) FROM ANIMAL_INS WHERE NAME is not NULL
