import os
import pandas as pd
import plotly.express as px
from django.shortcuts import render
from abc import ABC, abstractmethod

class Section(ABC):
    def __init__(self, xlsx_dir):
        self.xlsx_dir = xlsx_dir
        self.file_path = self.find_file()
        if not self.file_path:
            raise FileNotFoundError(f"No matching XLSX file found in {xlsx_dir}")
        
        self.filename = os.path.basename(self.file_path)
        self.excel_file = pd.ExcelFile(self.file_path)
        self.sheets = {}
    
    @abstractmethod
    def find_file(self):
        """Find the appropriate XLSX file for this section"""
        pass
    
    def load_data(self):
        """Load and process data from all sheets"""
        for sheet_name in self.excel_file.sheet_names:
            try:
                df = pd.read_excel(self.file_path, sheet_name=sheet_name)
                if not df.empty:
                    self.sheets[sheet_name] = self.process_sheet(df)
            except Exception as e:
                print(f"Error processing sheet {sheet_name}: {str(e)}")
                continue
    
    @abstractmethod
    def process_sheet(self, df):
        """Process a single sheet and return the processed data"""
        pass
    
    @abstractmethod
    def create_visualizations(self):
        """Create visualizations from the processed data"""
        pass

class CustomerNeedsSection(Section):
    def find_file(self):
        """Find the Customer Needs XLSX file"""
        for file in os.listdir(self.xlsx_dir):
            if file.endswith('.xlsx') and 'customer' in file.lower() and 'needs' in file.lower():
                return os.path.join(self.xlsx_dir, file)
        return None
    
    def process_sheet(self, df):
        # Convert all columns except the first one to numeric
        for col in df.columns[1:]:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Set the first column as index and transpose
        return df.set_index(df.columns[0]).transpose()
    
    def create_visualizations(self):
        charts = []
        for sheet_name, df in self.sheets.items():
            fig = px.line(df, 
                         title=f"{sheet_name} - {self.filename.replace('.xlsx', '')}",
                         labels={"index": "Product Category", "value": "Score", "variable": "Customer Need"})
            
            # Update layout for better appearance
            fig.update_layout(
                height=600,
                width=1200,
                showlegend=True,
                legend=dict(
                    yanchor="top",
                    y=0.99,
                    xanchor="right",
                    x=0.99,
                    traceorder="normal"
                ),
                xaxis=dict(
                    tickangle=45,
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
            
            charts.append({
                'title': f"{sheet_name} - {self.filename.replace('.xlsx', '')}",
                'html': fig.to_html(
                    full_html=False,
                    config={
                        'displayModeBar': True,
                        'displaylogo': False,
                        'toImageButtonOptions': {'height': None, 'width': None}
                    }
                ),
                'sheet_name': sheet_name
            })
        
        return charts

def home(request):
    # Get the path to the xlsx directory
    current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    xlsx_dir = os.path.join(current_dir, 'xlsx')
    
    if not os.path.exists(xlsx_dir):
        return render(request, 'pages/home.html', {'sections': [], 'error': f'Directory not found: {xlsx_dir}'})
    
    sections = []
    
    # Create instances of each section type
    section_classes = [CustomerNeedsSection]
    
    for section_class in section_classes:
        try:
            section = section_class(xlsx_dir)
            
            # Load and process the data
            section.load_data()
            
            # Create visualizations
            charts = section.create_visualizations()
            
            if charts:
                sections.append({
                    'filename': section.filename,
                    'charts': charts,
                    'type': section_class.__name__.replace('Section', '')
                })
            
        except FileNotFoundError as e:
            print(f"Warning: {str(e)}")
            continue
        except Exception as e:
            print(f"Error processing section {section_class.__name__}: {str(e)}")
            import traceback
            print(traceback.format_exc())
            continue
    
    if not sections:
        return render(request, 'pages/home.html', {'sections': [], 'error': 'No valid XLSX files were processed'})
    
    return render(request, 'pages/home.html', {'sections': sections})
