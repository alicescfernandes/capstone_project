import os
import pandas as pd
import plotly.express as px
from django.shortcuts import render

# Create your views here.

def home(request):
    # Get the path to the xlsx directory
    current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    xlsx_dir = os.path.join(current_dir, 'xlsx')
    
    if not os.path.exists(xlsx_dir):
        return render(request, 'pages/home.html', {'charts': [], 'error': f'Directory not found: {xlsx_dir}'})
    
    charts = []
    
    # Process each XLSX file in the directory
    files = os.listdir(xlsx_dir)
    
    for filename in files:
        if filename.endswith('.xlsx'):
            file_path = os.path.join(xlsx_dir, filename)
            try:
              
                # Read the first row to get the graph name
                title = pd.read_excel(file_path, nrows=0).columns[0]
                
                # Read the Excel file, skipping the first row (graph name)
                df = pd.read_excel(file_path, skiprows=1)
                
                # Convert all columns except the first one to numeric
                for col in df.columns[1:]:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
                
                # Set the first column as index and transpose
                df = df.set_index(df.columns[0]).transpose()
                
                # Create a line chart
                fig = px.line(df,title=title,
                                labels={"index": "Product Category", "value": "Score", "variable": "Customer Need"})
                
                # Update layout for better appearance
                fig.update_layout(
                    height=600,  # Taller graph
                    width=1200,  # Wider graph
                    showlegend=True,
                    legend=dict(
                        yanchor="top",
                        y=0.99,
                        xanchor="right",
                        x=0.99,
                        traceorder="normal"
                    ),
                    xaxis=dict(
                        tickangle=45,  # Rotate labels 45 degrees
                    ),
                    template="plotly_dark",
                    paper_bgcolor='rgba(0, 0, 0, 0)',
                    modebar={
                        'orientation': 'h',
                        'bgcolor': 'rgba(0,0,0,0)',
                        'color': 'white',
                        'activecolor': 'lightgray'
                    }
                )
                
                # Add gridlines
                fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
                fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
                
                # Convert the plot to HTML with proper modebar configuration
                chart_html = fig.to_html(
                    full_html=False,
                    config={
                        'displayModeBar': True,
                        'displaylogo': False,
                        'toImageButtonOptions': {'height': None, 'width': None}
                    }
                )
       
                charts.append({
                    'title': title,
                    'html': chart_html,
                    'filename': filename
                })
                
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
                import traceback
                print(traceback.format_exc())
    
    if not charts:
        return render(request, 'pages/home.html', {'charts': [], 'error': 'No valid XLSX files were processed'})
    
    return render(request, 'pages/home.html', {'charts': charts})
