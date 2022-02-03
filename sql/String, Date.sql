-- 루시와 엘라 찾기 https://programmers.co.kr/learn/courses/30/lessons/59046
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')

-- 이름에 el이 들어가는 동물 찾기 https://programmers.co.kr/learn/courses/30/lessons/59047
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME

-- 중성화 여부 파악하기 https://programmers.co.kr/learn/courses/30/lessons/59409
SELECT ANIMAL_ID, NAME, 
IF(SEX_UPON_INTAKE LIKE '%NEUTERED%' OR SEX_UPON_INTAKE LIKE '%SPAYED%', 'O', 'X') AS 중성화
FROM ANIMAL_INS

-- 오랜 기간 보호한 동물(2) https://programmers.co.kr/learn/courses/30/lessons/59411
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS I
RIGHT JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY O.DATETIME - I.DATETIME DESC
LIMIT 2

-- DATETIME에서 DATE로 형 변환 https://programmers.co.kr/learn/courses/30/lessons/59414
SELECT ANIMAL_ID, NAME, DATE_FORMAT(datetime, '%Y-%m-%d')  AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
