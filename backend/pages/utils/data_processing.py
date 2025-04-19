import pandas as pd
import os
import re
from .chart_classification import COLUMNS_TO_REMOVE, ROWS_TO_REMOVE
import inflection

def extract_section_name(file_name):
    # Remove a extensão
    name = os.path.splitext(file_name)[0]

    # Substituir underscores e hífens por espaços
    name = re.sub(r'[_\-]', ' ', name)

    # Remover padrões tipo "Q2", "2023", "v1", etc.
    name = re.sub(r'\b(Q\d+|[12][0-9]{3}|v\d+)\b', '', name, flags=re.IGNORECASE)

    # Normalizar múltiplos espaços
    name = re.sub(r'\s+', ' ', name).strip()

    # Detetar se está em camelCase ou snake_case e transformar
    name = inflection.titleize(name)

    return name

def clean_title(text):
    return re.sub(r"(the\s*)?for Quarter \d+", "", text, flags=re.IGNORECASE).strip()

def remove_line_breaks_from_data(df):
    """
    Remove all line breaks from every value in the DataFrame.

    Parameters:
        df (pd.DataFrame): DataFrame whose content may include line breaks.

    Returns:
        pd.DataFrame: DataFrame with all line breaks removed from every cell.
    """
    return df.map(
        lambda x: str(x).replace('\n', ' ').replace('\r', ' ') if pd.notna(x) else x
    )

def normalize_column_names(df):
    """
    Normalize column names by removing line breaks, extra spaces and trimming.

    Parameters:
        df (pd.DataFrame): The DataFrame whose column names are to be cleaned.

    Returns:
        pd.DataFrame: The same DataFrame with normalized column names.
    """
    df.columns = [
        str(col).replace('\n', ' ').replace('\r', '').strip()
        for col in df.columns
    ]
    return df

def remove_rows(df):
    """
    Remove rows where any cell contains any of the specified keywords (case-insensitive).

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        keywords (list of str): List of keywords to look for. Rows containing them will be removed.

    Returns:
        pd.DataFrame: A DataFrame with the matching rows removed.
    """
    lower_keywords = [kw.lower() for kw in ROWS_TO_REMOVE]

    def row_should_be_removed(row):
        return any(
            str(cell).lower().strip() in lower_keywords
            for cell in row
        )

    mask = df.apply(row_should_be_removed, axis=1)
    return df[~mask]  # Keeps only the lines that must not be removed

def remove_columns(df):
    """
    Remove specific columns from the DataFrame by name, case-insensitively.

    Parameters:
        df (pd.DataFrame): The input DataFrame with potentially unwanted columns.

    Returns:
        pd.DataFrame: A DataFrame with specified columns removed.
    """

    normalized_cols = {str(col).lower(): col for col in df.columns}
    to_remove = [normalized_cols[col.lower()] for col in COLUMNS_TO_REMOVE if col.lower() in normalized_cols]
    return df.drop(columns=to_remove, errors='ignore')

def sanitize_sheet_name(sheet_name):
    """
    Sanitize an Excel sheet name to produce a safe, lowercase, hyphenated file name.

    Parameters:
        sheet_name (str): The original sheet name.

    Returns:
        str: A sanitized and normalized version of the sheet name.
    """
    name = re.sub(r"\b(q\d+|quarter\s*\d+)\b", "", sheet_name, flags=re.IGNORECASE)
    name = re.sub(r"\b\d+\b", "", name)
    name = "".join(c if c.isalnum() or c in " _-" else " " for c in name)
    name = re.sub(r"[\s_-]+", "-", name)
    return name.strip("-").lower()

def parse_sheet(xls, sheet_name):
    """
    Parse a sheet from an Excel file with no headers.

    Parameters:
        xls (pd.ExcelFile): A loaded Excel file via pd.ExcelFile.
        sheet_name (str): Name of the sheet to parse.

    Returns:
        pd.DataFrame: Raw data from the sheet without headers.
    """
    return xls.parse(sheet_name, header=None)

def extract_sheet_title(df_raw):
    """
    Extract the title of the sheet, assuming it is in the first cell.

    Parameters:
        df_raw (pd.DataFrame): Raw sheet data.

    Returns:
        str: The title extracted from cell (0, 0).
    """
    return clean_title(str(df_raw.iloc[0, 0]).strip())

def extract_column_names(df_raw,sheet_title):
    """
    Extract column names from the second row of the sheet, replacing line breaks
    and filling first column with sheet title if missing.

    Parameters:
        df_raw (pd.DataFrame): Raw sheet data.
        sheet_title (str): The title extracted from the first cell (0, 0).

    Returns:
        list[str]: A list of cleaned column names.
    """
    columns = [
        str(c).strip() if pd.notna(c) else ''
        for c in df_raw.iloc[1]
    ]
    if not columns[0].strip():  # First column is empty or blank
        columns[0] = sheet_title
    return columns

def extract_clean_data(df_raw, column_names):
    """
    Extract the main dataset, skipping the title and column name rows.

    Parameters:
        df_raw (pd.DataFrame): Raw sheet data.
        column_names (list[str]): Column names extracted previously.

    Returns:
        pd.DataFrame: Cleaned DataFrame with correct headers.
    """
    df = df_raw.iloc[2:-1].copy()
    df.columns = column_names
    return df

def export_csv_with_title(df, title, output_dir, sheet_name):
    """
    Export a DataFrame to CSV using a sanitized filename.

    Parameters:
        df (pd.DataFrame): The cleaned dataset to export.
        title (str): The title extracted from the sheet (not used in filename).
        output_dir (str): Path to the directory where the CSV should be saved.
        sheet_name (str): Original sheet name, used for filename generation.

    Returns:
        str: The generated CSV filename.
    """
    filename = f"{sanitize_sheet_name(sheet_name)}.csv"
    path = os.path.join(output_dir, filename)
    with open(path, mode='w', encoding='utf-8', newline='') as f:
        df.to_csv(f, index=False)
    return filename

def run_pipeline_for_sheet(xls, sheet_name, output_dir):
    """
    Full processing pipeline for a single Excel sheet.

    Parameters:
        xls (pd.ExcelFile): Loaded Excel file.
        sheet_name (str): Name of the sheet to process.
        output_dir (str): Directory to save the resulting CSV.

    Returns:
        tuple[str, str]: A tuple containing the CSV filename and sheet title.
    """
    df_raw = parse_sheet(xls, sheet_name)
    df_raw = remove_line_breaks_from_data(df_raw)
    title = extract_sheet_title(df_raw)
    columns = extract_column_names(df_raw, title)
    df_clean = extract_clean_data(df_raw, columns)
    df_clean = normalize_column_names(df_clean)
    df_clean = remove_columns(df_clean)
    df_clean = remove_rows(df_clean)
    clean_sheet_name = sanitize_sheet_name(sheet_name)
    return (df_clean,  clean_sheet_name, title)
