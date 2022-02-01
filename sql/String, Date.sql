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
