import plotly.express as px
import detention_data_dashboard

def display_aor_plot(us_loc):
    if us_loc == "West Coast":
        aor = ['LOS', 'SEA',  'SFR', 'SND']
    elif us_loc == "East Coast":
        aor = ['ATL', 'BAL', 'BOS', 'BUF', 'DET',  'MIA', 'NEW', 'NOL', 'NYC', 'PHI', 'WAS', 'HQ']
    elif us_loc == "Midwest":
        aor = ['CHI', 'SPM']
    elif us_loc == "Southwest":
        aor = ['DAL', 'DEN', 'ELP', 'HOU', 'PHO',  'SLC', 'SNA']
    elif us_loc == "All":
        aor = ['ATL', 'BAL', 'BOS', 'BUF', 'CHI', 'DAL', 'DEN', 'DET', 'ELP', 'HOU', 'HQ', 'LOS', 'MIA', 'NEW', 'NOL','NYC', 'PHI', 'PHO', 'SEA', 'SFR', 'SLC', 'SNA', 'SND', 'SPM', 'WAS']
    else:
        raise NameError('Please enter in a valid US region')

    df = detention_data_dashboard.data_download(us_loc)
    
    fig = px.line(df, x=df['date'], y=[df['encounters'], df['removals'], df['arrests']],
              title = "Encounters, Removals, and Arrests in Region per FY",
              labels=dict(x="Fiscal Year", y="Total"))
    fig.update_xaxes(title="Fiscal Year", nticks = 4)
    fig.update_yaxes(title="Total")
    fig.update_layout(legend_title_text=None)

    return fig