import pandas as pd
import plotly.express as px


# Read data from excel
print(pd.ExcelFile("/home/chahid/Desktop/nov-2022.ods").sheet_names)
df = pd.read_excel("/home/chahid/Desktop/nov-2022.ods")
values = df["chnawa srafet fih"]
names = df["9adeh srafet fih"]

fig = px.pie(df, values=values, names=names, title="Spending PIE CHART")

fig.update_traces(textposition="inside", textinfo="percent+label")

fig.update_layout(
    title_font_size=42,
)

# Export Piechart to HTML
#fig.write_html("Piechart.html", auto_open=True)
fig.show()
