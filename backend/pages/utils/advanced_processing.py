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
    
    # Income statement
    "Revenues":                                 {"type": "relative", "sign": 1},
    "Research and Development":                 {"type": "relative", "sign": -1},
    "Quality Costs":                            {"type": "relative", "sign": -1},
    "Advertising":                              {"type": "relative", "sign": -1},
    "Sales Office and Web Sales Center Expenses": {"type": "relative", "sign": -1},
    "Marketing Research":                       {"type": "relative", "sign": -1},
    "Shipping":                                 {"type": "relative", "sign": -1},
    "Inventory Holding Cost":                   {"type": "relative", "sign": -1},
    "Excess Capacity Cost":                     {"type": "relative", "sign": -1},
    "Depreciation":                             {"type": "relative", "sign": -1},
    "Operating Profit":                         {"type": "total",    "sign": 1},
    "Licensing Income":                         {"type": "relative", "sign": 1},
    "Licensing Fees":                           {"type": "relative", "sign": -1},
    "Other Income":                             {"type": "relative", "sign": 1},
    "Other Expenses":                           {"type": "relative", "sign": -1},
    "Earnings Before Interest and Taxes":       {"type": "total",    "sign": 1},
    "Interest Income":                          {"type": "relative", "sign": 1},
    "Interest Charges":                         {"type": "relative", "sign": -1},
    "Income Before Taxes":                      {"type": "total",    "sign": 1},
    "Loss Carry Forward":                       {"type": "relative", "sign": -1},
    "Taxable Income":                           {"ignore":True},
    "Income Taxes":                             {"type": "relative", "sign": -1},
    "Net Income":                               {"type": "total",    "sign": 1},
    "Earnings per Share":                       {"ignore": True},
    "Gross Profit":                             {"ignore": True},
    "Total Expenses":                           {"ignore": True},
    "Miscellaneous Income and Expenses":        {"ignore": True},
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


def process_income_statement(df):
    # extract last quarter from sheet (sheets have all the quarters, but we are only interested on the last)
    quarter_columns = [col for col in df.columns if col.startswith("Quarter")]
    latest_quarter = quarter_columns[-1] if quarter_columns else None

    # validate
    if latest_quarter is None:
        raise ValueError("Nenhuma coluna de trimestre encontrada no ficheiro CSV.")

    df = df[["Report Item", latest_quarter]].dropna()
    df[latest_quarter] = df[latest_quarter].astype(str).str.replace(",", "").astype(float)


    # parse sheets
    parsed_rows = []
    for _, row in df.iterrows():
        parsed = parse_cell(row["Report Item"], row[latest_quarter], latest_quarter, df[["Report Item", latest_quarter]])

        if parsed:
            parsed_rows.append(parsed)

    # Criar DataFrame
    parsed_df = pd.DataFrame(parsed_rows)
    return parsed_df


def process_detailed_brand_demand(df):
    parsed_df = df.melt(id_vars=["Brand", "Company", "City"], var_name="Segment", value_name="Demand")

    return parsed_df

# dropna is dropping all rows with nan values, and that is causing some rows to get removed
def process_compensation(df):
    last_two = df.tail(2)

    # Merges last two lines so that we have a single column
    merged = last_two.aggregate(lambda x: x.dropna().iloc[0] if x.dtype == object else x.sum())

    parsed_df = df.iloc[:-2]

    parsed_df = pd.concat([parsed_df, pd.DataFrame([merged])])
    
    print(parsed_df)
    return df