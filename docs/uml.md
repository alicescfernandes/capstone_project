classDiagram
    direction LR

    class Quarter {
        UUID uuid
        PositiveInteger number
        DateTime created_at
        +__str__(): str
    }

    class ExcelFile {
        UUID uuid
        File file
        DateTime uploaded_at
        Boolean is_processed
        Char section_name
        +__str__(): str
        +process_and_store_csv()
    }

    class CSVData {
        UUID uuid
        Char sheet_name_pretty
        Char sheet_name_slug
        UUID quarter_uuid  %% weak reference to Quarter
        Boolean is_current
        DateTime created_at
        JSON data
        JSON column_order
        +__str__(): str
    }

    Quarter "1" --> "*" ExcelFile : files
    ExcelFile "1" --> "*" CSVData : csvs
    CSVData --> ExcelFile : quarter_file
    ExcelFile --> Quarter : quarter
