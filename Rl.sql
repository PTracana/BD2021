CREATE OR REPLACE FUNCTION supplier_sec_verify_proc(ean_g numeric(13))
    RETURNS TRIGGER AS
    $$
        DECLARE counter INTEGER;
    BEGIN
        SELECT count(*) from supplies_sec as a WHERE a.ean = ean_g into counter;
    IF counter = 3
    THEN
        RAISE EXCEPTION 'limite de suppliers ';
    END IF;

    END

    $$ LANGUAGE plpgsql;

CREATE TRIGGER supplier_sec_verify
    BEFORE UPDATE OR INSERT on supplies_sec
    EXECUTE PROCEDURE supplier_sec_verify_proc();