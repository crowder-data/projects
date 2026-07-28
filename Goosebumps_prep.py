import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

bins = [0,10,20,30,40,50,60,70,80,90,100,np.inf]
labels = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100','100+']

df_wide = pd.read_csv('/data/Goosebumps.csv').drop(columns = 'Total')
df_long = df_wide.melt(id_vars=['First','Last'], var_name='Year',value_name='Miles')
df_long['Range'] = pd.cut(df_long['Miles'],bins=bins,labels=labels)

def yearly_histogram(df, year, bins):
  data = df.loc[df['Year']==year, "Miles"]

  fig, ax = plt.subplots(figsize = (8,4))

  ax.hist(
    data,
    bins=bins,
    edgecolor='black'
  )

  ax.set_title(f'Runner Mileage Distribution - {year}')
  ax.set_xlabel('Total Miles')
  ax.set_ylabel('Runner Count')

  fig.tight_layout()

  return fig


heatmap_data = (
    df_long.groupby(['Year','Range'],observed=False)
    .size()
    .unstack(fill_value=0)
)

heatmap_data_percents = heatmap_data.apply(
    lambda row: row / row.sum(),
    axis=1
)

def heatmap_raw(data = heatmap_data):
  fig, ax = plt.subplots(figsize = (8,4))
    
  sns.heatmap(
    data,
    annot=True, 
    fmt='g',
    ax = ax
  )

  fig.tight_layout()

  return fig

def heatmap_pct(data = heatmap_data_percents):
  fig, ax = plt.subplots(figsize = (8,4))
  
  sns.heatmap(
      data,
      annot=True,
      fmt=".1%",
      ax = ax,
      annot_kws = {"fontsize":6}
  )

  fig.tight_layout()
  
  return fig


