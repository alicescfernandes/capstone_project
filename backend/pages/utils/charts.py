import pandas as pd

def format_chart_trace(x,y, type, name=""):
    if(type == "pie"):        
        return {
            "values": y,
            "labels": x,
            "type": type
        }
    
    if(type == 'box'):
        return {
            "y":y,
            "type": type,
            "name": name,
        }
        
    # Return data as is
    return {
            "type": type,
            "x": x,
            "y": y
        }

def get_box_chart_all(df, chart_meta, csv_sheet_name, filter):

    indicator_col = df.columns[0]
    value_cols = df.columns[1:]

    df[value_cols] = df[value_cols].apply(pd.to_numeric, errors='coerce')

    available_filters = df[indicator_col].fillna("").tolist()

    traces = []
    for _, row in df.iterrows():
        trace = format_chart_trace(None,row[value_cols].dropna().tolist(), 'box',row[indicator_col] )       
        traces.append(trace)

    return {
        'chart_config': {
            "traces": traces,
            "layout": {
                "showlegend":False
            }
        },
        'title': csv_sheet_name,
        "options": available_filters,
        'selected_option': None
    }
        
def get_box_chart(df, chart_meta, csv_sheet_name, filter):
    chart_type = chart_meta["chart_type"]

    indicator_col = df.columns[0]
    value_cols = df.columns[1:]

    df[value_cols] = df[value_cols].apply(pd.to_numeric, errors='coerce')

    company = value_cols[::-1][0]
    # Lista de indicadores disponíveis
    available_filters = df[indicator_col].fillna("").tolist()
    selected_filter = filter if filter in available_filters else available_filters[0]

    # Obter a linha correspondente ao indicador filtrado
    row = df[df[indicator_col] == selected_filter].squeeze()

    company_value = row.get(company, None).round(3)
    
    # Criar um único trace com todos os valores do indicador selecionado
    trace = format_chart_trace(None, row[value_cols].dropna().tolist(), chart_type, selected_filter) 
    layout = {}

    # Se existir valor da empresa, adicionar linha vermelha e "legenda flutuante" estilo legenda de gráfico
    if company_value is not None:
        layout["shapes"] = [{
            "type": "line",
            "x0": -0.5,
            "x1": 0.5,  # ajusta à largura do gráfico
            "y0": company_value,
            "y1": company_value,
            "line": {
                "color": "red",
                "width": 2,
                "dash": "dash"
            }
        }]
        # Legenda flutuante: quadrado vermelho + nome da empresa
        layout["annotations"] = [{
            "x": 1,
            "y": max(row[value_cols].dropna().tolist()),
            "xref": "paper",
            "yref": "y",
            "text": f"<span style='font-size:22px;color:red;'>■</span> Company: {company}",
            "showarrow": False,
            "font": {
                "size": 14
            },
            "align": "left",
            "bgcolor": "white",
            "borderpad": 3,
            "borderwidth": 0,
            "opacity": 1
        }]

    return {
        'chart_config': {
            "traces": [trace],
            "layout": layout
        },
        'title': csv_sheet_name,
        "options": available_filters,
        'selected_option': selected_filter
    }

def get_simple_chart(df,chart_meta, csv_sheet_name, filter):
    chart_type = chart_meta["chart_type"]
    
    # Box charts use a whole different data structure, but is still "simple"
    if(chart_type == 'box'):
        return get_box_chart(df,chart_meta, csv_sheet_name, filter)

    first_column = df.columns[0]
    filter_cols = df.columns[1:]

    df[filter_cols] = df[filter_cols].apply(pd.to_numeric, errors='coerce')

    available_filters = filter_cols.tolist()
    selected_filter = filter if filter in available_filters else available_filters[0]

    first_column_values = df[first_column].fillna("").tolist()
    values = df[selected_filter].fillna(0).tolist()


    trace = format_chart_trace(first_column_values,values, chart_type)

    return {
    'chart_config':{
        "traces":[trace],
        "layout":{}
    },
    'title': csv_sheet_name,
    "options": available_filters,
    'selected_option': selected_filter
    }

def get_double_chart(df, chart_meta,csv_sheet_name, filter):
    column_filter_name = chart_meta["column_name"]
    chart_type = chart_meta["chart_type"]

                
    available_column_filters = df[column_filter_name].unique()
    selected_column_filter = filter if filter in available_column_filters else available_column_filters[0]

    # Filtrar as linhas onde a coluna 'Company' == 'SWITCH'
    filtered_df = df[df[column_filter_name] == selected_column_filter]

    # Remover a coluna 'Company'
    filtered_df = filtered_df.drop(columns=[column_filter_name])

    traces = []
    x = filtered_df.columns[1:].to_list()
    for _, row in filtered_df.iterrows():
        trace = {
            "x": x,
            "y": [row[col] for col in x],
            "name":  row.iloc[0],
            "type": "bar"
        }
        traces.append(trace)

    return  {
        'title': csv_sheet_name,
        'type': chart_type,
        'chart_config':{
            "traces":traces,
            "layout":{
                "barmode": "group",
                "showlegend":True,
                "legend": {
                    "title": { "text": '' },     
                    "traceorder": 'normal'
                }
            }
        },
        "options": available_column_filters,
        'selected_option': selected_column_filter,
        'columns_filter':{
            'available': available_column_filters,
            'selected': selected_column_filter
        }
    }
    



def generate_multiple_waterfall_traces(quarter_df):
    if "Total Assets" not in quarter_df["Label"].values:
        raise ValueError("'Total Assets' row not found in DataFrame.")

    idx_total_assets = quarter_df[quarter_df["Label"] == "Total Assets"].index[0]

    assets_df = quarter_df.iloc[:idx_total_assets + 1]

    trace_assets = {
        "type": "waterfall",
        "name": "Assets",
        "x": assets_df["Label"].tolist(),
        "y": assets_df["Value"].tolist(),
        "measure": assets_df["Measure"].tolist(),
        "textposition": "inside"
    }

    liabilities_df = quarter_df.iloc[idx_total_assets + 1:]

    trace_liabilities = {
        "type": "waterfall",
        "name": "Debt & Equity",
        "x": liabilities_df["Label"].tolist(),
        "y": liabilities_df["Value"].tolist(),
        "measure": liabilities_df["Measure"].tolist(),
        "textposition": "inside"
    }

    return [trace_assets, trace_liabilities]

def get_waterfall_chart(df, chart_meta, csv_sheet_name, filter):
    column_filter_name = chart_meta["column_name"]
    chart_type = chart_meta["chart_type"]
    available_column_filters = df[column_filter_name].unique()

    selected_column_filter = filter if filter in available_column_filters else available_column_filters[0]

    filtered_df = df[df[column_filter_name] == selected_column_filter]

    traces = []

    if(csv_sheet_name == "Balance Sheet"):
        traces = generate_multiple_waterfall_traces(filtered_df) # creates multiple traces for each "section" of the waterfall
    else:
        traces.append({
            "type": "waterfall",
            "name": selected_column_filter,
            "x": filtered_df["Label"].tolist(),
            "y": filtered_df["Value"].tolist(),
            "measure": filtered_df["Measure"].tolist(),
            "textposition": "inside"
        })

    return {
        'title': csv_sheet_name,
        'type': chart_type,
        'chart_config': {
            "traces": traces,
            "layout": {
                "showlegend": True,
                "waterfallgap": 0.1,
            }
        },
        "options": available_column_filters.tolist(),
        'selected_option': selected_column_filter,
        'columns_filter': {
            'available': available_column_filters.tolist(),
            'selected': selected_column_filter
        }
    }
    
    
def get_group_chart(df, chart_meta, csv_sheet_name, filter):
    column_filter_name = chart_meta["column_name"]  
    chart_type = chart_meta["chart_type"]
    group_by = chart_meta["group_by"]      
    group_column_index = chart_meta["group_column_index"]           

    available_column_filters = df[column_filter_name].unique()
    selected_column_filter = filter if filter in available_column_filters else available_column_filters[0]

    filtered_df = df[df[column_filter_name] == selected_column_filter].copy()

    grouped = (
        filtered_df
        .groupby(group_by)['Number of Inserts']
        .sum()
        .reset_index()
    )

    pivot_df = grouped.pivot(index='Ad', columns=group_column_index, values='Number of Inserts').fillna(0)

    traces = []
    x = pivot_df.columns.tolist() 
    for ad_name, row in pivot_df.iterrows():
        traces.append({
            "x": x,
            "y": row.tolist(),
            "name": ad_name,
            "type": "bar"
        })

    return {
        'title': csv_sheet_name,
        'type': chart_type,
        'chart_config': {
            "traces": traces,
            "layout": {
                "barmode": "group",
                "showlegend": True,
                "legend": {
                    "title": {"text": ''},
                    "traceorder": 'normal'
                },
                "xaxis": {"title": "City"},
                "yaxis": {"title": "Number of Inserts"}
            }
        },
        "options": available_column_filters.tolist(),
        'selected_option': selected_column_filter,
        'columns_filter': {
            'available': available_column_filters.tolist(),
            'selected': selected_column_filter
        }
    }
    
    
def get_sankey_chart(df, chart_meta, csv_sheet_name, filter):
    df_long = df.copy()
    chart_type = chart_meta["chart_type"]
    column_filter_name = chart_meta["column_name"]  

    available_column_filters = df[column_filter_name].unique()
    selected_column_filter = filter if filter in available_column_filters else available_column_filters[0]
    
    df_filtered = df_long[df_long[column_filter_name] == selected_column_filter]

    # Certificar que está em formato long com coluna Demand
    if "Demand" not in df_filtered.columns:
        df_filtered = df_filtered.melt(
            id_vars=["Brand", "Company", "City"],
            var_name="Segment",
            value_name="Demand"
        )

    # Gerar os nós únicos
    all_nodes = pd.unique(df_filtered[["Brand", "Segment", "City"]].values.ravel())
    node_indices = {name: i for i, name in enumerate(all_nodes)}

    # Brand → Segment
    bs = df_filtered.groupby(["Brand", "Segment"])["Demand"].sum().reset_index()
    source1 = bs["Brand"].map(node_indices).tolist()
    target1 = bs["Segment"].map(node_indices).tolist()
    value1 = bs["Demand"].tolist()

    # Segment → City
    sc = df_filtered.groupby(["Segment", "City"])["Demand"].sum().reset_index()
    source2 = sc["Segment"].map(node_indices).tolist()
    target2 = sc["City"].map(node_indices).tolist()
    value2 = sc["Demand"].tolist()

    # Combinar os fluxos
    source = source1 + source2
    target = target1 + target2
    value = value1 + value2

    # Plotly trace
    traces = [{
        "type": "sankey",
        "orientation": "h",
        "node": {
            "pad": 15,
            "thickness": 20,
            "line": {"color": "black", "width": 0.5},
            "label": all_nodes.tolist()
        },
        "link": {
            "source": source,
            "target": target,
            "value": value
        }
    }]
    
    return {
        'title': csv_sheet_name,
        'type': chart_type,
        'chart_config': {
            "traces": traces,
        },
        "options": available_column_filters.tolist(),
        'selected_option': selected_column_filter,
        'columns_filter': {
            'available': available_column_filters.tolist(),
            'selected': selected_column_filter
        }
    }

def get_table_chart(df, chart_meta, csv_sheet_name, selected_filter):
    # Convert DataFrame to list of lists for data
    data = df.values.tolist()
    
    # Create columns configuration from DataFrame columns
    columns = [{"title": col} for col in df.columns]
   
    return {
        'chart_config': {
        },
        "columns": columns,
        "data": data,
        'title': csv_sheet_name,
        'type': "table",
        "options": [],
        'selected_option': None
    }