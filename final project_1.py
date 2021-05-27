
import pandas as pd

df_mine= pd.read_csv('Topic_Survey_Assignment.csv')
print(df_mine)
# df_mine.set_index(df_mine[''], inplace=True)
#df_mine['Total'] = df_mine.sum(axis=1)
#print(df_mine)
df_mine.sort_values(['Very interested'], ascending=False, axis=0, inplace=True)
df_mine.rename( columns={'Unnamed: 0':'Subjects'}, inplace=True )
print(df_mine)
ax1 = df_mine.plot(kind='bar', 
                   figsize=(20, 8),
                   width = 0.8,
                   color = ('#5cb85c', '#5bc0de', '#d9534f'),
                   fontsize = 14) 
ax1.set_title("Percentage of Respondents' Interest in Data Science Areas", fontsize = 16)
ax1.legend(fontsize = 14)
ax1.set_xticklabels(df_mine['Subjects'], fontsize = 14)
ax1.set_yticklabels('')


# # create a list to collect the plt.patches data
# totals = []

# # find the values and append to list
# for i in ax1.patches:
#     totals.append(i.get_height())

# print(totals)

# # set individual bar lables using above list
# total = sum(totals)
# print(total)

total = 2233

# set individual bar lables using above list
for i in ax1.patches:
    print(i)
    # get_x pulls left or right; get_height pushes up or down
    ax1.text(i.get_x()+0.009, i.get_height()+15,
             str(round((i.get_height()/total)*100, 2))+'%', fontsize=14,
             color='dimgrey')    
    
for spine in ax1.spines:
    print(spine)
    if spine == 'bottom':
        continue
    ax1.spines[spine].set_visible(False)