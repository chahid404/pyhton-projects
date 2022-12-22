import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

rows = 2
cols = 3
specs = [[{'type': 'domain'}] * cols] * rows


class Sheet():          # leave this empty
    def __init__(self):   # constructor function using self
        self.values = None  # variable using self.
        self.names = None  # variable using self
        self.date = None
        self.sum = None
        self.excel_file = None


fig = make_subplots(rows=rows, cols=cols, specs=specs)


excel_files = []
excel_file = Sheet()

print(pd.ExcelFile("/home/chahid/Desktop/nov-2022.ods").sheet_names)
sheet_names = pd.ExcelFile("/home/chahid/Desktop/nov-2022.ods").sheet_names
for sheet_name in sheet_names:
    excel_file.excel_file(pd.read_excel(
        "/home/chahid/Desktop/nov-2022.ods", sheet_name=sheet_name))

    excel_file.names = excel_file.excel_file["9adeh srafet fih"]
    excel_file.values = excel_file.excel_file["chnawa srafet fih"]
    excel_file.date = excel_file.excel_file["date"]
    excel_file.sum = excel_file.excel_file["Spending by date"]
    excel_files.append(excel_file)


rows = len(sheet_names)
cols = 2
specs = [[{'type': 'domain'}] * cols] * rows
fig = make_subplots(rows=rows, cols=cols, specs=specs)


""" df = pd.read_excel("/home/chahid/Desktop/nov-2022.ods", sheet_name='December')
df1 = pd.read_excel("/home/chahid/Desktop/nov-2022.ods", sheet_name='November') """


""" values = df["chnawa srafet fih"]
names = df["9adeh srafet fih"]
values1 = df1["chnawa srafet fih"]
names1 = df1["9adeh srafet fih"]

values2 = df["Spending by date"]
names2 = df["date"] """


print(len(excel_files))
for sheet in excel_files:
    fig.add_trace(
        go.Pie(
            labels=names,
            values=values,
            name="Edible Mushroom",
            title="December"
        ),
        1,
        1,
    )

# crate traces to specify the various properties of the first pie chart subplot
fig.add_trace(
    go.Pie(
        labels=names,
        values=values,
        name="Edible Mushroom",
        title="December"
    ),
    1,
    1,
)
fig.add_trace(
    go.Pie(
        labels=names1,
        values=values1,
        name="Edible Mushroom",
        title="November"
    ),
    1,
    2,
)
fig.add_trace(
    go.Pie(
        labels=names2,
        values=values2,
        name="December by dates"
    ),
    2, 1,
)
fig.update_traces(textposition="inside", textinfo="percent+label")

fig.update_layout(
    title_font_size=42,
)
fig.update_layout(
    title_text="Mushroom Population by Edibility",
)
fig.show()

# Read data from excel
# print(pd.ExcelFile("/home/chahid/Desktop/nov-2022.ods").sheet_names)


# fig = px.pie(df, values=values, names=names, title="Spending PIE CHART")
#
# fig.update_traces(textposition="inside", textinfo="percent+label")
#
# fig.update_layout(
#     title_font_size=42,
# )
#
# # Export Piechart to HTML
# #fig.write_html("Piechart.html", auto_open=True)
# fig.show()
