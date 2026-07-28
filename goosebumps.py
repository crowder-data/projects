import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



def load_data(filename):
  bins = [0,10,20,30,40,50,60,70,80,90,100,np.inf]
  labels = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100','100+']
  df_wide = pd.read_csv(filename).drop(columns = 'Total')
  df_long = df_wide.melt(id_vars=['First','Last'], var_name='Year',value_name='Miles')
  df_long['Range'] = pd.cut(df_long['Miles'],bins=bins,labels=labels)
  return df_long

def yearly_histogram(df, year):
  data = df.loc[df['Year']==year, "Miles"]

  fig, ax = plt.subplots(figsize = (8,4))

  ax.hist(
    data,
    bins=[0,10,20,30,40,50,60,70,80,90,100,np.inf],
    edgecolor='black'
  )

  ax.set_title(f'Runner Mileage Distribution - {year}')
  ax.set_xlabel('Total Miles')
  ax.set_ylabel('Runner Count')

  fig.tight_layout()

  return fig

def create_heatmap_data(df_long):
  heatmap_data = (
      df_long.groupby(['Year','Range'],observed=False)
      .size()
      .unstack(fill_value=0)
  )
  return heatmap_data

def create_heatmap_data_percents(heatmap_data):
  heatmap_data_percents = heatmap_data.apply(
      lambda row: row / row.sum(),
      axis=1
  )
  return heatmap_data_percents

def heatmap_raw(data):
  fig, ax = plt.subplots(figsize = (16,8))
    
  sns.heatmap(
    data,
    annot=True, 
    fmt='g',
    ax = ax
  )

  ax.tick_params(
    axis="both",
    labelsize=14
  )

  fig.tight_layout()

  return fig

def heatmap_pct(data):
  fig, ax = plt.subplots(figsize = (16,8))
  
  sns.heatmap(
      data,
      annot=True,
      fmt=".1%",
      ax = ax,
      annot_kws = {"fontsize":14}
  )

  
  ax.tick_params(
    axis="both",
    labelsize=14
  )

  fig.tight_layout()
  
  return fig


