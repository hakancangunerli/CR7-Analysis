# %%
from datasets import load_dataset

dataset = load_dataset("azminetoushikwasi/cristiano-ronaldo-all-club-goals-stats", use_auth_token=True)

# %%
dataset

# %%
df = dataset['train'].to_pandas()

# %%
df

# %%
# replace Ã§ with ç 
df['Competition'] = df['Competition'].str.replace('Ã§', 'ç')

df['Competition'] = df['Competition'].str.replace('Italy Cup', 'Coppa Italia')

df['Competition'] = df['Competition'].str.replace('Liga Portugal', 'Primeira Liga')


df['Competition'] = df['Competition'].str.replace('Taça de Portugal Placard', 'Taça de Portugal')

# %%
df

# %%
df.describe()
df = df.drop('Unnamed: 0', axis=1)




# %%
df

# %%
# cluster the goals based on the competition 
df['Competition'].value_counts()

# %%


# if there's a + sign in the minutes, replace it with 90 + the number after the + sign
for i in range(len(df['Minute'])):
    if '+' in df['Minute'][i]:
        if ('90+') in df['Minute'][i]:
            df['Minute'][i] = df['Minute'][i].replace('+', '')
            df['Minute'][i] = 90 +int(df['Minute'][i])
            df['Minute'][i] = df['Minute'][i] - 900
        elif ('45+') in df['Minute'][i]:
            df['Minute'][i] = df['Minute'][i].replace('+', '')
            df['Minute'][i] = 45 +int(df['Minute'][i])
            df['Minute'][i] = df['Minute'][i] - 450
            
    
df['Minute'] = df['Minute'].astype(int)


# %%
df

# %%
# plot the goals based on the competition using plotly

import plotly.express as px
fig = px.scatter(df, x="Minute", y="Competition", color="Competition", size='Minute')


# cut competitions based on what country they're in

countries_ronaldo_played = ['Portugal', 'England', 'Spain', 'Italy']
competitions_pt = ['Primeira Liga', 'Taça de Portugal', 'Supertaça Cândido de Oliveira', 'Taça da Liga', 'Supertaça de Portugal', ]
competitions_eng = ['Premier League', 'FA Cup', 'League Cup', 'Community Shield', 'EFL Cup']
competitions_ita = ['Serie A', 'Coppa Italia', 'Supercoppa Italiana', 'Coppa Italia']
competition_esp = ['LaLiga', 'Copa del Rey', 'Supercopa de España', 'Supercopa de España', 'Supercopa']
competition_european = ['UEFA Super Cup', 'UEFA Champions League', 'UEFA Europa League', 'UEFA Champions League Qualifying', 'UEFA Europa League Qualifying']
df['Country'] = df['Competition'].apply(lambda x: 'Portugal' if x in competitions_pt else ('England' if x in competitions_eng else ('Italy' if x in competitions_ita else ('Spain' if x in competition_esp else ('Europe' if x in competition_european else 'Other')))))

# the other in this case is the FIFA Club World Cup
print(df['Country'].value_counts())

# export the dataframe to a csv file for checking
# df.to_csv('ronaldo_goals.csv')

# %%
# plot the goals based on country using mathplotlib


df['Country'].value_counts().plot(kind='bar')

# %%
# fig.show()

# %%
# calculate the number of goals based on the type of goal
df['Type_of_goal'].value_counts().plot(kind='bar')

# %%
df['Minute'].value_counts()

# %%
#
df['Minute'].astype(int)

df['number_scored_at_that_minute'] = df.groupby('Minute')['Minute'].transform('count')


# %%
df


# %%

fig = px.scatter(df, x="Minute", y="Competition", color="Competition", size='number_scored_at_that_minute')


fig.show()

# %%



