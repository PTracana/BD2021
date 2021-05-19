DROP VIEW  IF EXISTS supplier_stats;

CREATE VIEW supplier_stats
AS SELECT * FROM (
        (SELECT ean, count(ean) AS pCount FROM supplies_prim GROUP BY ean) AS a
        NATURAL join
        (SELECT ean, count(ean) AS secCount FROM supplies_sec GROUP BY ean) as b
    );


