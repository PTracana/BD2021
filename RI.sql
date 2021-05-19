DROP TRIGGER IF EXISTS supplier_sec_verify on supplies_sec ;

CREATE OR REPLACE FUNCTION supplier_sec_verify_proc()
    RETURNS TRIGGER AS $$
    DECLARE counter INTEGER;
    BEGIN
        SELECT COUNT(*) into counter FROM supplies_sec WHERE ean = NEW.ean;
        IF (counter >= 3) THEN
            RAISE EXCEPTION 'limite de suppliers para produto %', NEW.ean;
        END IF;
    RETURN new;
    END
    $$ LANGUAGE plpgsql;

CREATE TRIGGER supplier_sec_verify
    BEFORE INSERT OR UPDATE on supplies_sec
    FOR EACH ROW EXECUTE PROCEDURE supplier_sec_verify_proc();

DROP TRIGGER IF EXISTS Supplier_repeat_verify on supplies_sec ;

CREATE OR REPLACE FUNCTION supplier_repeat_verify_proc()
    RETURNS TRIGGER AS $$
    DECLARE t_num INTEGER;
    BEGIN
        SELECT count(*) into t_num FROM supplies_prim as a
            WHERE NEW.ean = a.ean AND NEW.nif = a.nif;
        IF(t_num = 1 ) THEN
            RAISE EXCEPTION 'For a given product, a supplier cannot be simultaneously a primary and secondary supplier';
        END IF;
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER Supplier_repeat_verify
    BEFORE INSERT OR UPDATE on supplies_sec
    FOR EACH ROW EXECUTE PROCEDURE supplier_repeat_verify_proc();