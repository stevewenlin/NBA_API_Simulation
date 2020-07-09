## PER is per-minute performance measurement that considers both positive & negative attributes of a player.

def PER_function(alldata_df): 
    
    columns_df = alldata_df[['player', 'Player_ID', 'Game_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'MIN', 'FGM',
                                  'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
                                  'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS','PLUS_MINUS']]
    
    columns_df['PER']= ((columns_df['FGM'] * 85.910)
    + (columns_df['STL'] * 53.897)
    + (columns_df['FG3M'] * 51.757)
    + (columns_df['FTM'] * 46.845)
    + (columns_df['BLK'] * 39.190)
    + (columns_df['OREB'] * 39.190)
    + (columns_df['AST'] * 34.677)
    + (columns_df['DREB'] * 14.707)
    - (columns_df['PF'] * 17.174)
    - ((columns_df['FTA']- columns_df['FTM']) * 20.091)
    - ((columns_df['FGA'] - columns_df['FGM']) * 39.190)
    - (columns_df['TOV'] * 53.897))*(1 /columns_df['MIN'])
    
    columns_df.to_csv('PER_calculation.csv', index=False)
    


    
    
    
                                    
    
