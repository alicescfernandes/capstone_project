import pandas as pd

BALANCE_SHEET_CONFIG = {
    "Brand Revenues":         {"type": "relative", "sign":  1},
    "Rebates":                {"type": "relative", "sign": -1},
    "Cost of Goods Sold":     {"type": "relative", "sign": -1},
    "Gross Profit":           {"ignore": True},
    "Brand Design":           {"type": "relative", "sign": -1},
    "Ad Design":              {"type": "relative", "sign": -1},
    "Brand Advertising":      {"type": "relative", "sign": -1},
    "Point of Purchase Display": {"type": "relative", "sign": -1},
    "Expenses":               {"ignore": True},
    "Brand Profit":           {"type": "total",    "sign":  1},
    "Profit per Unit":        {"ignore": True},
    "% from Brand Revenues":  {'type': 'percentage', "reference": "Brand Revenues"},
    # Regional Profitability
    "Sales Revenue":         {"type": "relative", "sign":  1},
    "Gross Margin":           {"ignore": True},
    "Sales Office Leases":    {"type": "relative", "sign": -1},
    "Sales Force Expenses":   {"type": "relative", "sign": -1},
    "Web Marketing Expenses": {"type": "relative", "sign": -1},
    "Channel Expenses":       {"ignore": True},
    "Channel Profit":         {"type": "total",    "sign":  1},
    "% from Sales Revenue":  {'type': 'percentage', "reference": "Sales Revenue"},
}

# Helper function for each cell
def parse_cell(label, value, column_name, df_col):
    label = label.strip().lstrip("-+= ").strip()
    if label not in BALANCE_SHEET_CONFIG or BALANCE_SHEET_CONFIG[label].get("ignore"):
        return None

    config = BALANCE_SHEET_CONFIG[label]
    measure = config["type"]

    if measure == "percentage":
        ref_label = config["reference"]
        ref_row = df_col[df_col["Report Item"].str.contains(ref_label, case=False, na=False)]
        if not ref_row.empty:
            ref_value = ref_row.iloc[0][column_name]
            value = (int(value) / 100) * abs(ref_value)
        else:
            value = 0
        measure = "absolute"
    elif measure == "relative":
        sign = config["sign"]
        value = sign * abs(value)

    return {
        "Column": column_name,
        "Label": label,
        "Measure": measure,
        "Value": value
    }

# Clean and parse all numeric columns
def process_balance_sheet(df,):
    parsed_rows = []
    value_columns = df.columns.drop("Report Item")

    # Remove commas and convert to float
    for col in value_columns:
        df[col] = df[col].astype(str).str.replace(",", "").astype(float)

    for col in value_columns:
        for _, row in df.iterrows():
            result = parse_cell(row["Report Item"], row[col], col, df[["Report Item", col]])
            if result:
                parsed_rows.append(result)

    # Final parsed DataFrame
    parsed_df = pd.DataFrame(parsed_rows)
    return parsed_df