from .advanced_processing import process_balance_sheet

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
        "type": "advertising",
        'column_name':"Company",
        "group_by":['City', 'Ad'],
        "group_column_index":"City"
    },
    "advertising-noram": {
        "chart_type": "bar",
        "type": "advertising",
        'column_name':"Company",
        "group_by":['City', 'Ad'],
        "group_column_index":"City"
    },
    "advertising-latam": {
        "chart_type": "bar",
        "type": "advertising",
        'column_name':"Company",
        "group_by":['City', 'Ad'],
        "group_column_index":"City"
    },
    "advertising-europe": {
        "chart_type": "bar",
        "type": "advertising",
        'column_name':"Company",
        "group_by":['City', 'Ad'],
        "group_column_index":"City"
    },
    "advertising-apac": {
        "chart_type": "bar",
        "type": "advertising",
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
        "type": "advertising",
        'column_name':"Company",
        "group_by":['Media', 'Ad'],
        "group_column_index":"Media"

    },
    "regional-advertising-noram": {
        "chart_type": "bar",
        "type": "advertising",
        'column_name':"Company",
        "group_by":['Media', 'Ad'],
        "group_column_index":"Media"

    },
    "regional-advertising-latam": {
        "chart_type": "bar",
        "type": "advertising",
        'column_name':"Company",
        "group_by":['Media', 'Ad'],
        "group_column_index":"Media"

    },
    "regional-advertising-europe": {
        "chart_type": "bar",
        "type": "advertising",
        'column_name':"Company",
        "group_by":['Media', 'Ad'],
        "group_column_index":"Media"

    },
    "regional-advertising-apac": {
        "chart_type": "bar",
        "type": "advertising",
        'column_name':"Company",
        "group_by":['Media', 'Ad'],
        "group_column_index":"Media"

    }

}

COLUMNS_TO_REMOVE = [
    "Priority",
    "Point of Purchase Display",
    "Total Sales People",
    "Total"
]

ROWS_TO_REMOVE = [
    "Total"
]

ADDITIONAL_PROCESSING_PIPELINE = {
    "brand-profitability": [process_balance_sheet],
    "channel-profitability-noram": [process_balance_sheet],
    "channel-profitability-latam": [process_balance_sheet],
    "channel-profitability-europe": [process_balance_sheet],
    "channel-profitability-apac": [process_balance_sheet]
}