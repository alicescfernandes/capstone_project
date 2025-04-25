from .advanced_processing import process_balance_sheet, process_income_statement, process_detailed_brand_demand, process_compensation

CHART_CLASSIFICATION = {
    "industry-results-for": {
        "chart_type": "box",
        "type": "simple",
        'column_name':None
    },
    "competitors-prices-noram": {
        "chart_type": "bar",
        "type": "double",
        'column_name':"Company"
    },
    "competitors-prices-mea": {
        "chart_type": "bar",
        "type": "double",
        'column_name':"Company"
    },
    "competitors-prices-latam": {
        "chart_type": "bar",
        "type": "double",
        'column_name':"Company"
    },
    "competitors-prices-europe": {
        "chart_type": "bar",
        "type": "double",
        'column_name':"Company"
    },
    "competitors-prices-apac": {
        "chart_type": "bar",
        "type": "double",
        'column_name':"Company"
    },
    "sales-force-noram": {
        "chart_type": "bar",
        "type": "double",
        'column_name':"City"
    },
    "sales-force-mea": {
        "chart_type": "bar",
        "type": "double",
        'column_name':"City"
    },
    "sales-force-latam": {
        "chart_type": "bar",
        "type": "double",
        'column_name':"City"
    },
    "sales-force-europe": {
        "chart_type": "bar",
        "type": "double",
        'column_name':"City"
    },
    "sales-force-apac": {
        "chart_type": "bar",
        "type": "double",
        'column_name':"City"
    },
    "web-personnel-noram": {
        "chart_type": "bar",
        "type": "simple"
    },
    "web-personnel-mea": {
        "chart_type": "bar",
        "type": "simple"
    },
    "web-personnel-latam": {
        "chart_type": "bar",
        "type": "simple"
    },
    "web-personnel-europe": {
        "chart_type": "bar",
        "type": "simple"
    },
    "web-personnel-apac": {
        "chart_type": "bar",
        "type": "simple"
    },
    "web-traffic-budgets": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "commissions-to-web-partners": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "web-productivity-budgets": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "cost-of-production-estimate": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "cumulative-results-for-quarter": {
        "chart_type": "box",
        "type": "simple",
        'column_name':None
    },
    "customer-needs-and-wants": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "web-customer-needs-and-wants": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "market-demand": {
        "chart_type": "pie",
        "type": "simple",
        'column_name':None
    },
    "market-share": {
        "chart_type": "pie",
        "type": "simple",
        'column_name':None
    },
    "month-potential-demand": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "price-judgment-noram": {
        "chart_type": "bar",
        "type": "double",
        'column_name':"Company"
    },
    "price-judgment-mea": {
        "chart_type": "bar",
        "type": "double",
        'column_name':"Company"
    },
    "price-judgment-latam": {
        "chart_type": "bar",
        "type": "double",
        'column_name':"Company"
    },
    "price-judgment-europe": {
        "chart_type": "bar",
        "type": "double",
        'column_name':"Company"
    },
    "price-judgment-apac": {
        "chart_type": "bar",
        "type": "double",
        'column_name':"Company"
    },
    "price-willing-to-pay": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "sales-total": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "sales-sales-office-channel": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "sales-web-channel": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "sales-noram": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "sales-latam": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "sales-europe": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "sales-apac": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "sales-unwanted-inventory": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "segments-by-application": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },

    # phase 2
    "brand-profitability": {
        "chart_type": "waterfall",
        "type": "balance_sheet",
        'column_name':"Column"
    },
    "channel-profitability-noram": {
        "chart_type": "waterfall",
        "type": "balance_sheet",
        'column_name':"Column"
    },
    "channel-profitability-mea": {
        "chart_type": "waterfall",
        "type": "balance_sheet",
        'column_name':"Column"
    },
    "channel-profitability-latam": {
        "chart_type": "waterfall",
        "type": "balance_sheet",
        'column_name':"Column"
    },
    "channel-profitability-europe": {
        "chart_type": "waterfall",
        "type": "balance_sheet",
        'column_name':"Column"
    },
    "channel-profitability-apac": {
        "chart_type": "waterfall",
        "type": "balance_sheet",
        'column_name':"Column"
    },
    "local-media-inserts":{
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "advertising-mea": {
        "chart_type": "bar",
        "type": "grouped",
        'column_name':"Company",
        "group_by":['City', 'Ad'],
        "group_column_index":"City"
    },
    "advertising-noram": {
        "chart_type": "bar",
        "type": "grouped",
        'column_name':"Company",
        "group_by":['City', 'Ad'],
        "group_column_index":"City"
    },
    "advertising-latam": {
        "chart_type": "bar",
        "type": "grouped",
        'column_name':"Company",
        "group_by":['City', 'Ad'],
        "group_column_index":"City"
    },
    "advertising-europe": {
        "chart_type": "bar",
        "type": "grouped",
        'column_name':"Company",
        "group_by":['City', 'Ad'],
        "group_column_index":"City"
    },
    "advertising-apac": {
        "chart_type": "bar",
        "type": "grouped",
        'column_name':"Company",
        "group_by":['City', 'Ad'],
        "group_column_index":"City"
    },
    "regional-media-inserts":{
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "regional-advertising-mea": {
        "chart_type": "bar",
        "type": "grouped",
        'column_name':"Company",
        "group_by":['Media', 'Ad'],
        "group_column_index":"Media"

    },
    "regional-advertising-noram": {
        "chart_type": "bar",
        "type": "grouped",
        'column_name':"Company",
        "group_by":['Media', 'Ad'],
        "group_column_index":"Media"

    },
    "regional-advertising-latam": {
        "chart_type": "bar",
        "type": "grouped",
        'column_name':"Company",
        "group_by":['Media', 'Ad'],
        "group_column_index":"Media"

    },
    "regional-advertising-europe": {
        "chart_type": "bar",
        "type": "grouped",
        'column_name':"Company",
        "group_by":['Media', 'Ad'],
        "group_column_index":"Media"

    },
    "regional-advertising-apac": {
        "chart_type": "bar",
        "type": "grouped",
        'column_name':"Company",
        "group_by":['Media', 'Ad'],
        "group_column_index":"Media"
    },
    "demand-by-region":{
        "chart_type": "pie",
        "type": "simple",
        'column_name':None
    },
    "demand-by-city":{
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "demand-by-company":{
        "chart_type": "pie",
        "type": "simple",
        'column_name':None
    },
    "demand-by-brand":{
        "chart_type": "bar",
        "type": "double",
        'column_name':"Company"
    },
    "income-statement": {
        "chart_type": "waterfall",
        "type": "balance_sheet",
        'column_name':"Column"
    },
    "detailed-brand-demand-mea": {
        "chart_type": "skankey",
        "type": "skankey",
        'column_name':"Company",
        "group_by":['Media', 'Ad'],
        "group_column_index":"Media"

    },
    "detailed-brand-demand-noram": {
        "chart_type": "skankey",
        "type": "skankey",
        'column_name':"Company",
        "group_by":['Media', 'Ad'],
        "group_column_index":"Media"

    },
    "detailed-brand-demand-latam": {
        "chart_type": "skankey",
        "type": "skankey",
        'column_name':"Company",
        "group_by":['Media', 'Ad'],
        "group_column_index":"Media"

    },
    "detailed-brand-demand-europe": {
        "chart_type": "skankey",
        "type": "skankey",
        'column_name':"Company",
        "group_by":['Media', 'Ad'],
        "group_column_index":"Media"

    },
    "detailed-brand-demand-apac": {
        "chart_type": "skankey",
        "type": "skankey",
        'column_name':"Company",
        "group_by":['Media', 'Ad'],
        "group_column_index":"Media"
    },
    "competitors-compensation-for-sales-force-noram": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "competitors-compensation-for-sales-force-mea": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "competitors-compensation-for-sales-force-latam": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "competitors-compensation-for-sales-force-europe": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "competitors-compensation-for-sales-force-apac": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "competitors-compensation-for-production-workers-noram": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "competitors-compensation-for-production-workers-mea": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "competitors-compensation-for-production-workers-latam": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "competitors-compensation-for-production-workers-europe": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "competitors-compensation-for-production-workers-apac": {
        "chart_type": "bar",
        "type": "simple",
        'column_name':None
    },
    "changeover-costs": {
        "chart_type": "bar",
        "type": "simple",
        "column_name":None
    },
    "inventory-position-cost-unit": {
        "chart_type": "bar",
        "type": "simple",
        "column_name":None
    },
    "inventory-position": {
        "chart_type": "bar",
        "type": "simple",
        "column_name":None
    }
}

COLUMNS_TO_REMOVE = [
    "Priority",
    "Point of Purchase Display",
    "Total Sales People",
    "Total",
    "Importance of further improvements" #TODO: on API get the slug, and if the column is this, then return a whole different dataset

]

ROWS_TO_REMOVE = [
    "Total",
    "Importance of further improvements"
]

ADDITIONAL_PROCESSING_PIPELINE = {
    "brand-profitability": [process_balance_sheet],
    "channel-profitability-noram": [process_balance_sheet],
    "channel-profitability-mea": [process_balance_sheet],
    "channel-profitability-latam": [process_balance_sheet],
    "channel-profitability-europe": [process_balance_sheet],
    "channel-profitability-apac": [process_balance_sheet],
    "income-statement": [process_income_statement],
    "detailed-brand-demand-noram": [process_detailed_brand_demand],
    "detailed-brand-demand-latam": [process_detailed_brand_demand],
    "detailed-brand-demand-europe": [process_detailed_brand_demand],
    "detailed-brand-demand-apac": [process_detailed_brand_demand],
    "competitors-compensation-for-sales-force-noram": [process_compensation],
    "competitors-compensation-for-sales-force-mea": [process_compensation],
    "competitors-compensation-for-sales-force-latam": [process_compensation],
    "competitors-compensation-for-sales-force-europe": [process_compensation],
    "competitors-compensation-for-sales-force-apac": [process_compensation],
    "competitors-compensation-for-production-workers-noram": [process_compensation],
    "competitors-compensation-for-production-workers-mea": [process_compensation],
    "competitors-compensation-for-production-workers-latam": [process_compensation],
    "competitors-compensation-for-production-workers-europe": [process_compensation],
    "competitors-compensation-for-production-workers-apac": [process_compensation],
}