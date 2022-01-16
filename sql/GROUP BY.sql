-- 고양이와 개는 몇마리 있을까? https://programmers.co.kr/learn/courses/30/lessons/59040
SELECT ANIMAL_TYPE, COUNT(*) AS count FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE;

-- 동명 동물 수 찾기 https://programmers.co.kr/learn/courses/30/lessons/59041
SELECT NAME, COUNT(*) as COUNT FROM ANIMAL_INS WHERE NAME is not NULL GROUP BY NAME HAVING COUNT >= 2 ORDER BY NAME;

-- 입양 시각 구하기(1) https://programmers.co.kr/learn/courses/30/lessons/59412
SELECT HOUR(DATETIME) AS 'HOUR', COUNT(*) AS COUNT 
FROM ANIMAL_OUTS 
WHERE HOUR(DATETIME) >= 9 and HOUR(DATETIME) < 20
GROUP BY HOUR
ORDER BY HOUR;

-- 입양 시각 구하기(2) https://programmers.co.kr/learn/courses/30/lessons/59413
SET @hour := -1; -- 변수 선언

SELECT (@hour := @hour + 1) as HOUR,
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23
