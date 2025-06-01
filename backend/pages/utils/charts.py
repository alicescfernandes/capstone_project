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
            "name": row[0],
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
    

def get_waterfall_chart(df, chart_meta, csv_sheet_name, filter):
    column_filter_name = chart_meta["column_name"]
    chart_type = chart_meta["chart_type"]
    available_column_filters = df[column_filter_name].unique()

    selected_column_filter = filter if filter in available_column_filters else available_column_filters[0]

    filtered_df = df[df[column_filter_name] == selected_column_filter]

    
    trace = {
        "type": "waterfall",
        "name": selected_column_filter,
        "x": filtered_df["Label"].tolist(),
        "y": filtered_df["Value"].tolist(),
        "measure": filtered_df["Measure"].tolist(),
        "textposition": "inside"
    }

    return {
        'title': csv_sheet_name,
        'type': chart_type,
        'chart_config': {
            "traces": [trace],
            "layout": {
                "showlegend": False,
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

def get_table_chart(df, chart_meta, csv_sheet_name, filter):
    data = [
        ['Tiger Nixon', 'System Architect', 'Edinburgh', '5421', '2011/04/25', '$320,800'],
        ['Garrett Winters', 'Accountant', 'Tokyo', '8422', '2011/07/25', '$170,750'],
        ['Ashton Cox', 'Junior Technical Author', 'San Francisco', '1562', '2009/01/12', '$86,000'],
        ['Cedric Kelly', 'Senior Javascript Developer', 'Edinburgh', '6224', '2012/03/29', '$433,060'],
        ['Airi Satou', 'Accountant', 'Tokyo', '5407', '2008/11/28', '$162,700'],
        ['Brielle Williamson', 'Integration Specialist', 'New York', '4804', '2012/12/02', '$372,000'],
        ['Herrod Chandler', 'Sales Assistant', 'San Francisco', '9608', '2012/08/06', '$137,500'],
        ['Rhona Davidson', 'Integration Specialist', 'Tokyo', '6200', '2010/10/14', '$327,900'],
        ['Colleen Hurst', 'Javascript Developer', 'San Francisco', '2360', '2009/09/15', '$205,500'],
        ['Sonya Frost', 'Software Engineer', 'Edinburgh', '1667', '2008/12/13', '$103,600'],
        ['Jena Gaines', 'Office Manager', 'London', '3814', '2008/12/19', '$90,560'],
        ['Quinn Flynn', 'Support Lead', 'Edinburgh', '9497', '2013/03/03', '$342,000'],
        ['Charde Marshall', 'Regional Director', 'San Francisco', '6741', '2008/10/16', '$470,600'],
        ['Haley Kennedy', 'Senior Marketing Designer', 'London', '3597', '2012/12/18', '$313,500'],
        ['Tatyana Fitzpatrick', 'Regional Director', 'London', '1965', '2010/03/17', '$385,750'],
        ['Michael Silva', 'Marketing Designer', 'London', '1581', '2012/11/27', '$198,500'],
        ['Paul Byrd', 'Chief Financial Officer (CFO)', 'New York', '3059', '2010/06/09', '$725,000'],
        ['Gloria Little', 'Systems Administrator', 'New York', '1721', '2009/04/10', '$237,500'],
        ['Bradley Greer', 'Software Engineer', 'London', '2558', '2012/10/13', '$132,000'],
        ['Dai Rios', 'Personnel Lead', 'Edinburgh', '2290', '2012/09/26', '$217,500'],
        ['Jenette Caldwell', 'Development Lead', 'New York', '1937', '2011/09/03', '$345,000'],
        ['Yuri Berry', 'Chief Marketing Officer (CMO)', 'New York', '6154', '2009/06/25', '$675,000'],
        ['Caesar Vance', 'Pre-Sales Support', 'New York', '8330', '2011/12/12', '$106,450'],
        ['Doris Wilder', 'Sales Assistant', 'Sydney', '3023', '2010/09/20', '$85,600'],
        ['Angelica Ramos', 'Chief Executive Officer (CEO)', 'London', '5797', '2009/10/09', '$1,200,000'],
        ['Gavin Joyce', 'Developer', 'Edinburgh', '8822', '2010/12/22', '$92,575'],
        ['Jennifer Chang', 'Regional Director', 'Singapore', '9239', '2010/11/14', '$357,650'],
        ['Brenden Wagner', 'Software Engineer', 'San Francisco', '1314', '2011/06/07', '$206,850'],
        ['Fiona Green', 'Chief Operating Officer (COO)', 'San Francisco', '2947', '2010/03/11', '$850,000'],
        ['Shou Itou', 'Regional Marketing', 'Tokyo', '8899', '2011/08/14', '$163,000'],
        ['Michelle House', 'Integration Specialist', 'Sydney', '2769', '2011/06/02', '$95,400'],
        ['Suki Burks', 'Developer', 'London', '6832', '2009/10/22', '$114,500'],
        ['Prescott Bartlett', 'Technical Author', 'London', '3606', '2011/05/07', '$145,000'],
        ['Gavin Cortez', 'Team Leader', 'San Francisco', '2860', '2008/10/26', '$235,500'],
        ['Martena Mccray', 'Post-Sales support', 'Edinburgh', '8240', '2011/03/09', '$324,050'],
        ['Unity Butler', 'Marketing Designer', 'San Francisco', '5384', '2009/12/09', '$85,675'],
    ]
    columns = [
        { "title": "Name" },
        { "title": "Position" },
        { "title": "Office" },
        { "title": "Extn." },
        { "title": "Start date" },
        { "title": "Salary" }
    ]
   
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


