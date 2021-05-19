DROP TRIGGER IF EXISTS supplier_sec_verify on supplies_sec ;

CREATE OR REPLACE FUNCTION supplier_sec_verify_proc()
    RETURNS TRIGGER AS $$
    DECLARE counter INTEGER;
    BEGIN
        SELECT count(ean) into counter
            from supplies_sec as a
            WHERE new.ean = a.ean;
        IF (counter >= 3) THEN
            RAISE EXCEPTION 'limite de suppliers para produto %', new.ean;
        END IF;
    RETURN new;
    END
    $$ LANGUAGE plpgsql;

CREATE TRIGGER supplier_sec_verify
    BEFORE INSERT OR UPDATE on supplies_sec
    EXECUTE PROCEDURE supplier_sec_verify_proc();

