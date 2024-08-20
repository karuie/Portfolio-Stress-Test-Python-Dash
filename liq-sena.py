# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the Dash app
app.layout = html.Div([
    html.H1("Yimin' Frist Liquidity Stress Test Dashboard"),

    html.H2("Redemption Scenario Table"),
    dash_table.DataTable(
        id='metrics_table',
        columns=[
            {"name": 'Fund ID', "id": 'fund_id'},
            {"name": 'Value1 Scenario 1', "id": 'value1_scenario1'},
            {"name": 'Value2 Scenario 1', "id": 'value2_scenario1'},
            {"name": 'Numerator Class 1 Scenario 1', "id": 'numerator_class1_scenario1'},
            {"name": 'Numerator Class 2 Scenario 1', "id": 'numerator_class2_scenario1'},
            {"name": 'Denominator Scenario 1 Class 1', "id": 'denominator_scenario1_class1'},
            {"name": 'Denominator Scenario 1 Class 2', "id": 'denominator_scenario1_class2'},

            {"name": 'Value1 Scenario 2', "id": 'value1_scenario2'},
            {"name": 'Value2 Scenario 2', "id": 'value2_scenario2'},
            {"name": 'Numerator Class 1 Scenario 2', "id": 'numerator_class1_scenario2'},
            {"name": 'Numerator Class 2 Scenario 2', "id": 'numerator_class2_scenario2'},
            {"name": 'Denominator Scenario 2 Class 1', "id": 'denominator_scenario2_class1'},
            {"name": 'Denominator Scenario 2 Class 2', "id": 'denominator_scenario2_class2'},


            {"name": 'Value1 Scenario 3', "id": 'value1_scenario3'},
            {"name": 'Value2 Scenario 3', "id": 'value2_scenario3'},
            {"name": 'Numerator Class 1 Scenario 3', "id": 'numerator_class1_scenario3'},
            {"name": 'Numerator Class 2 Scenario 3', "id": 'numerator_class2_scenario3'},
            {"name": 'Denominator Scenario 3 Class 1', "id": 'denominator_scenario3_class1'},
            {"name": 'Denominator Scenario 3 Class 2', "id": 'denominator_scenario3_class2'},

            {"name": 'Metric Scenario 1 Class 1', "id": 'metric_scenario1_class1'},
            {"name": 'Metric Scenario 1 Class 2', "id": 'metric_scenario1_class2'},
            {"name": 'Metric Scenario 2 Class 1', "id": 'metric_scenario2_class1'},
            {"name": 'Metric Scenario 2 Class 2', "id": 'metric_scenario2_class2'},
            {"name": 'Metric Scenario 3 Class 1', "id": 'metric_scenario3_class1'},
            {"name": 'Metric Scenario 3 Class 2', "id": 'metric_scenario3_class2'}
        ],
        data=merged_df.to_dict('records'),
        style_table={'overflowX': 'auto'},
        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data={
            'backgroundColor': 'rgb(50, 50, 50)',
            'color': 'white'
        },
        style_data_conditional=[
                                   {
                                       'if': {
                                           'filter_query': f'{{metric_scenario{i}_class{j}_class}} = "Red"',
                                           'column_id': f'metric_scenario{i}_class{j}'
                                       },
                                       'backgroundColor': 'red',
                                       'color': 'white'
                                   } for i in range(1, 4) for j in range(1, 3)
                               ] + [
                                   {
                                       'if': {
                                           'filter_query': f'{{metric_scenario{i}_class{j}_class}} = "Amber"',
                                           'column_id': f'metric_scenario{i}_class{j}'
                                       },
                                       'backgroundColor': 'orange',
                                       'color': 'white'
                                   } for i in range(1, 4) for j in range(1, 3)
                               ] + [
                                   {
                                       'if': {
                                           'filter_query': f'{{metric_scenario{i}_class{j}_class}} = "Green"',
                                           'column_id': f'metric_scenario{i}_class{j}'
                                       },
                                       'backgroundColor': 'green',
                                       'color': 'white'
                                   } for i in range(1, 4) for j in range(1, 3)
                               ],
    page_size = 25,  # Show 10 rows per page
                row_deletable = False,  # Prevent deletion of rows
                                editable = True,  # Allow editing of cells
                                           row_selectable = 'multi',  # Allow selection of multiple rows
                                                            selected_rows = [],  # Initialize selected rows to empty list
                                                                            export_format = 'xlsx',  # Allow export to Excel format
                                                                                            export_headers = 'display'  # Use display headers for exported file
# Show 10 rows per page
    ),

    html.A(
        'Download Data',
        id='download-link',
        download="metrics_data.csv",
        href="",
        target="_blank"
    )
])


# Callback to update download link href
@app.callback(
    Output('download-link', 'href'),
    [Input('metrics_table', 'data')]
)
def update_download_link(data):
    df = pd.DataFrame(data)
    csv_string = df.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
    return csv_string


if __name__ == '__main__':
    app.run_server(debug=True)
