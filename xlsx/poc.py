import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def read_xlsx_file(file_path):
    # Read the first row to get the graph name
    graph_name = pd.read_excel(file_path, nrows=0).columns[0]
    
    # Read the Excel file, skipping the first row (graph name)
    df = pd.read_excel(file_path, skiprows=1)
    
    # Get the x-axis column (first column)
    x_axis_column = df.columns[0]
    
    # Get the data columns (all columns except the first one)
    data_columns = df.columns[1:]
    
    print(f"\nGraph Name: {graph_name}")
    print(f"\nX-axis Column: {x_axis_column}")
    print(f"\nData Columns: {list(data_columns)}")
    
    # Display the first few rows
    print("\nFirst few rows of the data:")
    print(df.head())
    
    # Display basic information about the dataset
    print("\nDataset Info:")
    print(df.info())
    
    return df, graph_name, x_axis_column, data_columns

def create_bar_chart(df, graph_name, x_axis_column, data_columns):
    # Create figure
    fig = go.Figure()
    
    # Add bars for each segment
    for column in data_columns:
        fig.add_trace(go.Bar(
            name=column,
            x=df[x_axis_column],
            y=df[column],
            text=df[column],  # Add value labels
            textposition='auto',
        ))
    
    # Update layout
    fig.update_layout(
        title=graph_name,
        xaxis_title="Applications",
        yaxis_title="Value",
        barmode='group',  # Group bars side by side
        showlegend=True,
        legend_title="Segments",
        # Rotate x-axis labels for better readability
        xaxis={'tickangle': -45},
        # Adjust margins to accommodate rotated labels
        margin=dict(b=150),
        # Make the plot higher to accommodate all labels
        height=800
    )
    
    # Show the plot
    fig.show()
    
    # Save the plot as HTML
    fig.write_html(f"{graph_name.replace(' ', '_')}.html")

def create_interactive_pie_chart(df, graph_name, x_axis_column, data_columns):
    # Create figure
    fig = go.Figure()
    
    # Add a dropdown menu
    buttons = []
    for idx, application in enumerate(df[x_axis_column]):
        # Create a pie chart trace for each application
        values = df.iloc[idx, 1:]  # Get values for this application across all segments
        trace = go.Pie(
            labels=data_columns,
            values=values,
            name=application,
            visible=False,
            hole=0.4,  # Creates a donut chart
            textinfo='label+percent+value',
            textposition='outside'
        )
        fig.add_trace(trace)
        
        # Create a button for this application
        button = dict(
            args=[{"visible": [i == len(buttons) for i in range(len(df[x_axis_column]))]},
                  {"annotations": [{"text": application, "x": 0.5, "y": 0.5, "font_size": 20, "showarrow": False}]}],
            label=application,
            method="update"
        )
        buttons.append(button)
    
    # Make the first trace visible
    fig.data[0].visible = True
    
    # Update layout
    fig.update_layout(
        title=f"{graph_name} - By Segment",
        showlegend=True,
        updatemenus=[{
            'buttons': buttons,
            'direction': 'down',
            'showactive': True,
            'x': 0.7,
            'y': 1.15,
            'xanchor': 'left',
            'yanchor': 'top'
        }],
        annotations=[
            dict(text=df[x_axis_column][0], x=0.5, y=0.5, font_size=20, showarrow=False),
            dict(text="Select Application:", x=0.6, y=1.12, showarrow=False, yref="paper", xref="paper")
        ],
        height=800  # Make the plot higher to accommodate the dropdown
    )
    
    # Show the plot
    fig.show()
    
    # Save the plot as HTML
    fig.write_html(f"{graph_name.replace(' ', '_')}_pie.html")

if __name__ == "__main__":
    # Example usage
    df, graph_name, x_axis_column, data_columns = read_xlsx_file('UsePattern-Q2.xlsx')
    
    # Create and display both charts
    create_bar_chart(df, graph_name, x_axis_column, data_columns)
    create_interactive_pie_chart(df, graph_name, x_axis_column, data_columns) 