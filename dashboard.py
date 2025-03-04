import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("academic_performance_dataset_V2.csv")
df.head()
df_sorted = df.sort_values(by=['YoG', 'Prog Code'])
gender_counts = df.groupby(['YoG', 'Prog Code', 'Gender']).size().unstack(fill_value=0)
gender_counts['Female_Percentage'] = (gender_counts['Female'] / (gender_counts['Female'] + gender_counts['Male'])) * 100

year_dfs = {}

for year in gender_counts.index.get_level_values('YoG').unique():
    year_data = gender_counts.loc[year]
    
    sorted_year_data = year_data.sort_values(by='Female_Percentage', ascending=True)
    
    year_dfs[year] = sorted_year_data[['Female_Percentage']]

# [2010, 2011, 2012, 2013, 2014]
df_2010_p = year_dfs[2010].reset_index()
df_2011_p = year_dfs[2011].reset_index()
df_2012_p = year_dfs[2012].reset_index()
df_2013_p = year_dfs[2013].reset_index()
df_2014_p = year_dfs[2014].reset_index()
# Initialize Dash app
app = dash.Dash(__name__)

# Simulated dataset for gender counts over years
df_interactive = gender_counts.reset_index()
# Simulated datasets for treemap data
data = {
    2010: df_2010_p,
    2011: df_2011_p,
    2012: df_2012_p,
    2013: df_2013_p,
    2014: df_2014_p
}


topics = {
    'Biology': ['BCH', 'MCB'],
    'Computer Science': ['CEN', 'CIS', 'ICE'],
    'Tech': ['BLD', 'MIS'],
    'Math': ['MAT'],
    'Physics': ['PHYG', 'PHYR', 'PHYE'],
    'Chemistry': ['CHE', 'CHM', 'PET'],
    'Mechanics': ['CVE', 'MCE', 'BLD']
}

def map_topic(course):
    for topic, courses in topics.items():
        if course in courses:
            return topic

# Dashboard Layout
app.layout = html.Div([
    html.H1("Are there fewer women in Computer Science and Engineering? ", style={'textAlign': 'center', 'color': 'blue'}),
    
    html.Div([
        html.Div([
            html.H3("Number of Women and Men per Prog Code", style={ 'color': 'green'}),
            dcc.Dropdown(
                id='prog-code-dropdown',
                options=[{'label': prog_code, 'value': prog_code} for prog_code in df_interactive['Prog Code'].unique()],
                value='BCH',
                style={'width': '50%'}
            ),
            dcc.Graph(id='line-graph')
        ], style={'width': '48%', 'display': 'inline-block'}),
        
        html.Div([
            html.H3("Treemap of Percentage of Women by Topic over the years", style={'color': 'green'}),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': str(year), 'value': year} for year in data.keys()],
                value=2010,
                clearable=False
            ),
            dcc.Graph(id='treemap-graph')
        ], style={'width': '48%', 'display': 'inline-block'})
    ])
])

# Callback for line graph
@app.callback(
    Output('line-graph', 'figure'),
    Input('prog-code-dropdown', 'value')
)
def update_graph(selected_prog_code):
    filtered_data = df_interactive[df_interactive['Prog Code'] == selected_prog_code]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_data['YoG'], y=filtered_data['Female'], mode='lines+markers', name='Female', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=filtered_data['YoG'], y=filtered_data['Male'], mode='lines+markers', name='Male', line=dict(color='red')))
    
    fig.update_layout(title=f"Number of Women and Men - {selected_prog_code}", xaxis_title="Year", yaxis_title="Quantity")
    return fig

# Callback for treemap
@app.callback(
    Output('treemap-graph', 'figure'),
    Input('year-dropdown', 'value')
)
def update_treemap(selected_year):
    df_selected = data[selected_year].copy()
    df_selected['topic'] = df_selected['Prog Code'].apply(map_topic)
    df_grouped = df_selected.groupby('topic', as_index=False)['Female_Percentage'].sum()
    
    fig = go.Figure(go.Treemap(labels=df_grouped['topic'], parents=[''] * len(df_grouped), values=df_grouped['Female_Percentage'], textinfo="label+value+percent entry"))
    fig.update_layout(title=f"Treemap for {selected_year}")
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
