DROP TRIGGER IF EXISTS supplier_sec_verify on supplies_sec ;

CREATE OR REPLACE FUNCTION supplier_sec_verify_proc()
    RETURNS TRIGGER AS $$
    BEGIN
        IF ((SELECT count(*) from supplies_sec as a WHERE a.ean = new.ean) >= 3) THEN
            RAISE EXCEPTION 'limite de suppliers ';
        END IF;
        RETURN new;
    END
    $$ LANGUAGE plpgsql;

CREATE TRIGGER supplier_sec_verify
    BEFORE UPDATE OR INSERT on supplies_sec
    EXECUTE PROCEDURE supplier_sec_verify_proc();

