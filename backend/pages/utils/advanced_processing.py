import pandas as pd

BALANCE_SHEET_CONFIG = {
    "Brand Revenues":         {"type": "relative", "sign":  1},
    "Rebates":                {"type": "relative", "sign": -1},
    "Cost of Goods Sold":     {"type": "relative", "sign": -1},
    "Gross Profit":           {"ignore": True}, # This is a total, profit
    "Brand Design":           {"type": "relative", "sign": -1},
    "Ad Design":              {"type": "relative", "sign": -1},
    "Brand Advertising":      {"type": "relative", "sign": -1},
    "Point of Purchase Display": {"type": "relative", "sign": -1},
    "Expenses":               {"ignore": True}, # This is a total, based on the other expenses
    "Brand Profit":           {"type": "total",    "sign":  1},
    "% from Brand Revenues":  {'type': 'percentage', "reference": "Brand Profit"},
    "Profit per Unit":        {"type": "absolute",    "sign":  1}, # graph doesnt support multiple series on the same data
    
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
    "Total Expenses":                           {"ignore": True},
    "Miscellaneous Income and Expenses":        {"ignore": True},
    
    # Production costs    
    "Units Produced":   {"ignore": True, "sign": 1},
    "Direct Materials":   {"ignore": "relative", "sign": 1},
    "Direct Labor":       {"type": "relative", "sign": 1},
    "Total Overhead":     {"type": "relative", "sign": 1},
    "Changeover":         {"type": "relative", "sign": 1},
    "Production Average": {"type": "total",    "sign": 1},
    
    # Cashflow
    "Beginning Cash Balance":                   {"type": "relative", "sign": 1},
    "Production":                               {"type": "relative", "sign": -1},
    "Sales Force Expense":                      {"type": "relative", "sign": -1},
    "Net Operating Cash Flow":                  {"ignore":True},
    "Fixed Production Capacity":                {"type": "relative", "sign": -1},
    "Sinking Fund":                             {"type": "relative", "sign": -1},
    "Total Investing Activities":               {"ignore":True},
    "Increase in Common Stock":                 {"type": "relative", "sign": 1},
    "Borrow Conventional Loan":                 {"type": "relative", "sign": 1},
    "Repay Conventional Loan":                  {"type": "relative", "sign": -1},
    "Borrow Long-Term Loan":                    {"type": "relative", "sign": 1},
    "Borrow Emergency Loan":                    {"type": "relative", "sign": 1},
    "Repay Emergency Loan":                     {"type": "relative", "sign": -1},
    "Deposit 3 Month Certificate":              {"type": "relative", "sign": -1},
    "Withdraw 3 Month Certificate":             {"type": "relative", "sign": 1},
    "Dividends":                                {"type": "relative", "sign": -1},
    "Total Financing Activities":               {"ignore": True},
    "Cash Balance, End of Period":              {"type": "total",    "sign": 1},
    "Cash Balance, Beginning of Period":        {"type": "relative", "sign": 1},
    
    # Balance Sheet
    "Cash": {"type": "relative", "sign": 1},
    "3 Month Certificate of Deposit": {"type": "relative", "sign": 1},
    "Finished Goods Inventory": {"type": "relative", "sign": 1},
    "Skinking Fund": {"type": "relative", "sign": 1},
    "Net Fixed Assets": {"type": "relative", "sign": 1},
    "Total Assets": {"type": "total",    "sign": 1},

    "Conventional Bank Loan": {"type": "relative", "sign": 1},
    "Long Term Loan": {"type": "relative", "sign": 1},
    "Emergency Loan": {"type": "relative", "sign": 1},
    "Common Stock": {"type": "relative", "sign":1},
    "Retained Earnings": {"type": "relative", "sign": -1},
    "Total Debt and Equity": {"type": "total",    "sign": 1},

    
}


def parse_cell_production(label, value, column_name):
    original_label = label.strip()
    label_clean = original_label.lstrip("-+= ").strip()

    config = BALANCE_SHEET_CONFIG[label_clean]
    if config.get("ignore"):
        return None  # Skip ignored columns

    # Try to match after cleaning
    if label_clean not in BALANCE_SHEET_CONFIG:
        # If not found in mapping, we can skip or assume default logic
        # Here I'll assume it's relative if starts with "+", total if "="
        if original_label.startswith("="):
            measure = "total"
        else:
            measure = "relative"
        sign = 1
    else:
        measure = config["type"]
        sign = config["sign"]

    value = sign * abs(value)

    return {
        "Brand": column_name,
        "Label": label_clean,  # Cleaned label without +/= symbols
        "Measure": measure,
        "Value": value
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
def process_balance_sheet(df,quarter):
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

def process_detailed_brand_demand(df,quarter):
    parsed_df = df.melt(id_vars=["Brand", "Company", "City"], var_name="Segment", value_name="Demand")

    return parsed_df

def process_competitor_city(df,quarter):
    parsed_df = df.copy()

    for col in parsed_df.columns[1:]:
        parsed_df[col] = parsed_df[col].apply(lambda x: 1 if str(x).strip().upper() == "X" else 0)

    df_long = parsed_df.melt(id_vars="City", var_name="Competitor", value_name="Presence")

    df_long = df_long[df_long["Presence"] == 1]
    return parsed_df



def process_production_costs(df,quarter):
    # Clean and parse
    parsed_rows = []
    value_columns = df.columns.drop("Brand")

    # Remove commas and convert to float
    for col in value_columns:
        df[col] = df[col].astype(str).str.replace(",", "").astype(float)

    for _, row in df.iterrows():
        brand = row["Brand"]
        for col in value_columns:
            result = parse_cell_production(col, row[col], brand)
            if result:
                parsed_rows.append(result)

    parsed_df = pd.DataFrame(parsed_rows)
    return parsed_df


def process_cashflow(df,quarter):
    expected_column = f"Quarter {quarter.number}"
    quarter_columns = [col for col in df.columns if col.startswith("Quarter")]

    # Determine which column to use
    if expected_column in quarter_columns:
        selected_column = expected_column
    else:
        if quarter_columns:
            selected_column = quarter_columns[-1]  # fallback to the latest
            print(f"Warning: Column '{expected_column}' not found. Defaulting to '{selected_column}'.")
        else:
            raise ValueError("No 'Quarter' columns found in DataFrame.")

    # Extract and clean the data
    df = df[["Report Item", selected_column]].dropna()
    df[selected_column] = df[selected_column].astype(str).str.replace(",", "").astype(float)

    parsed_rows = []
    for _, row in df.iterrows():
        parsed = parse_cell(row["Report Item"], row[selected_column], selected_column, df[["Report Item", selected_column]])

        if parsed:
            parsed_rows.append(parsed)

    parsed_df = pd.DataFrame(parsed_rows)
    return parsed_df