import os
import pandas as pd
#test
teams = ["MIA", "WAS", "TOR", "PHI", "ORL", 
         "NYK", "MIL", "ATL", "IND", "CLE", 
         "BOS", "NJN", "CHI", "CHA", "DET", 
         "MEM", "DEN", "DAL", "MIN", "NOH", 
         "GSW", "OKC", "LAL", "LAC", "PHO", 
         "POR", "SAC", "SAS", "UTA", "HOU"]
os.mkdir("data")
for team in teams:
    url = f"https://www.basketball-reference.com/teams/{team}/stats_basic_totals.html#stats"
    nba = pd.read_html(url)
    data = pd.DataFrame(nba[0]).to_csv(f"data/{team}.csv")
