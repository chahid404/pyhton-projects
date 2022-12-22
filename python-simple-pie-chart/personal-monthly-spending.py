import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from datetime import datetime


class Sheet():
    def __init__(self):
        self.values = None
        self.names = None
        self.date = None
        self.sum = None
        self.sheet_name = None
        self.excel_file = None
        self.total_Spending = None


def custom_date_parser(x): return datetime.strptime(x, "%Y-%d-%m")


FILE_URL = "/home/chahid/Desktop/personal expense tracker.ods"
TEMPLATE = "TEMPLATE"
sheet_names = pd.ExcelFile(FILE_URL).sheet_names
excel_files = []
excel_file = Sheet()
rows = len(sheet_names)
cols = 2
specs = [[{'type': 'domain'}] * cols] * rows
fig = make_subplots(rows=rows, cols=cols, specs=specs)

for sheet_name in sheet_names:
    if sheet_name != TEMPLATE:
        excel_file.excel_file = pd.read_excel(
            FILE_URL, skiprows=3,
            sheet_name=sheet_name,
            date_parser=custom_date_parser)
        excel_file.names = excel_file.excel_file["NAME"]
        excel_file.values = excel_file.excel_file["AMOUNT"]
        excel_file.date = excel_file.excel_file["EXPENSE DATE"].dt.strftime(
            '%m/%d/%Y')
        excel_file.sum = excel_file.excel_file["SPENDING BY DATE"]
        excel_file.sheet_name = sheet_name
        excel_file.total_Spending = excel_file.values.sum()
        excel_files.append(excel_file)
        excel_file = Sheet()

for index, sheet in enumerate(excel_files):
    fig.add_trace(
        go.Pie(
            labels=sheet.names,
            values=sheet.values,
            title=sheet.sheet_name + " : The Total is : ( " +
            str(round(sheet.total_Spending, 0))+" dt )",
            textinfo="label+percent",
            name="NAME"
        ), index+1, 1
    )

    fig.add_trace(
        go.Pie(
            labels=sheet.date,
            values=sheet.sum,
            title=sheet.sheet_name + " : Spending per date",
            textinfo="label",
            name="DATE"
        ), index+1, 2)

fig.update_traces(textposition="inside", textinfo="percent+label")

fig.update_layout(
    autosize=True,
    width=2200,
    height=2200,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    title_font_size=42,
    title_text="MY MONTHLY SPENDING MADE WITH ❤ keep the good work CHAHDA",
)

# fig.show()
fig.write_html("personal expense tracker.html")
