import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots


class Sheet():
    def __init__(self):
        self.values = None
        self.names = None
        self.date = None
        self.sum = None
        self.sheet_name = None
        self.excel_file = None
        self.total_Spending = None


FILE_URL = "/home/chahid/Desktop/nov-2022.ods"
sheet_names = pd.ExcelFile(FILE_URL).sheet_names
excel_files = []
excel_file = Sheet()
rows = len(sheet_names)
cols = 2
specs = [[{'type': 'domain'}] * cols] * rows
fig = make_subplots(rows=rows, cols=cols, specs=specs)

for sheet_name in sheet_names:

    excel_file.excel_file = pd.read_excel(FILE_URL, sheet_name=sheet_name)
    excel_file.names = excel_file.excel_file["9adeh srafet fih"]
    excel_file.values = excel_file.excel_file["chnawa srafet fih"]
    excel_file.date = excel_file.excel_file["date"]
    excel_file.sum = excel_file.excel_file["Spending by date"]
    excel_file.sheet_name = sheet_name
    excel_file.total_Spending = excel_file.values.sum()
    excel_files.append(excel_file)
    excel_file = Sheet()

for index, sheet in enumerate(excel_files):
    print(sheet.values[0])
    fig.add_trace(
        go.Pie(
            labels=sheet.names,
            values=sheet.values,
            title=sheet.sheet_name + " : The Total is : ( " +
            str(sheet.total_Spending)+" dt )",
            textinfo="label+percent",
            name="item"
        ), index+1, 1
    )

    fig.add_trace(
        go.Pie(
            labels=sheet.date,
            values=sheet.sum,
            title=sheet.sheet_name + " : Spending per date",
            textinfo="label+percent",
            name="date"
        ), index+1, 2)

fig.update_traces(textposition="inside", textinfo="percent+label")

fig.update_layout(
    title_font_size=42,
    title_text="MY MONTHLY SPENDING MADE WITH ❤ keep the good work CHAHDA",
)

# fig.show()
fig.write_html("Piechart.html", auto_open=True)
