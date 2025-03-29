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
    print(f"Found files: {files}")
    
    for filename in files:
        if filename.endswith('.xlsx'):
            file_path = os.path.join(xlsx_dir, filename)
            try:
                # Read the Excel file
                df = pd.read_excel(file_path)
                
                # Get the title from the first row
                title = df.columns[0]
                
                # Convert all columns except the first one to numeric
                for col in df.columns[1:]:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
                
                # Set the first column as index and transpose
                df = df.set_index(df.columns[0]).transpose()
                
                # Create a line chart
                fig = px.line(df,
                            title=title,
                            labels={"index": "Product Category", "value": "Score", "variable": "Customer Need"})
                
                # Update layout for better appearance
                fig.update_layout(
                    height=600,  # Taller graph
                    width=1200,  # Wider graph
                    margin=dict(l=20, r=20, t=40, b=80),  # More bottom margin for labels
                    showlegend=True,
                    legend=dict(
                        yanchor="top",
                        y=0.99,
                        xanchor="right",
                        x=0.99,
                        bgcolor="rgba(255, 255, 255, 0.8)",  # Semi-transparent white background
                        traceorder="normal"
                    ),
                    xaxis=dict(
                        tickangle=45,  # Rotate labels 45 degrees
                    ),
                    plot_bgcolor='white',  # White background
                    paper_bgcolor='white'
                )
                
                # Add gridlines
                fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
                fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
                
                # Convert the plot to HTML
                chart_html = fig.to_html(full_html=False)
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
