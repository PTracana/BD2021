--QUERY A
SELECT ean, descr
FROM replenishevent r
NATURAL JOIN planogram pl
NATURAL JOIN product p
NATURAL JOIN category cat
JOIN consists_of co ON cat.name = co.name_descendant
WHERE co.name_super = 'Milk' AND r.instant > '2021-03-25' AND r.unitsrep > 15;

-- QUERY B
SELECT s_name, nif FROM (
    SELECT nif, ean FROM supplies_prim as prim
    UNION ALL
    SELECT * FROM supplies_sec as sec
    ) as sup
NATURAL JOIN supplier
WHERE sup.ean = 7842651395888;

--QUERY C
SELECT count(*)
FROM consists_of
WHERE name_super= 'Milk';

--QUERY D
WITH res as (SELECT nif, COUNT(name) as catcount
    FROM  (
        SELECT nif, ean FROM supplies_prim as prim
        UNION ALL
        SELECT * FROM supplies_sec as sec
        ) as sup
    NATURAL JOIN product
    group by nif)
SELECT s_name,nif FROM (
SELECT  MAX(catcount) as max FROM res) as ab, res
NATURAL JOIN supplier
WHERE catcount = max;


--QUERY E

WITH res as (SELECT nif, COUNT(name) as catcount
    FROM  (
        SELECT nif, ean FROM supplies_prim as prim
        UNION ALL
        SELECT * FROM supplies_sec as sec
        ) as sup
    NATURAL JOIN product
    group by nif)
SELECT s_name, nif
FROM(SELECT count(name)  as counter
    FROM simplecategory ) as final
NATURAL JOIN res
NATURAL JOIN supplier
WHERE final.counter = res.catcount;



--Query F

SELECT nr , width , nif FROM(
    SELECT pr.ean
    FROM supplies_prim pr
    LEFT JOIN supplies_sec sec
    ON pr.nif = sec.nif
    WHERE sec.nif IS NULL) as ns
NATURAL JOIN product
NATURAL JOIN planogram
NATURAL JOIN corridor


