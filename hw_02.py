import json
import pandas as pd
import matplotlib.pyplot as plt 

with open('rickandmorty.json','r') as rick_morty:
    text1 = rick_morty.read()

shows1 = json.loads(text1)

#scatter plot of rick and morty ratings
episodes_data=shows1['_embedded']

season_list=[]
number_list=[]
for i in range(len(shows1)):
    print('\n')
    season_num=shows1['_embedded']['episodes'][i]['season']
    episode_num=shows1['_embedded']['episodes'][i]['number']
    season_list.append(season_num)
    number_list.append(episode_num)
    
    #print(season_num,episode_num)
print(season_list)
print(number_list)

number_of_episodes=[0,0]
seasons=[0,1]
for index, val in enumerate(number_list):
    if season_list[index]==1:
        number_of_episodes[0]+=1
    if season_list[index]==2:
        number_of_episodes[1]+=1
print(number_of_episodes)


values=('Season 1','Season 2')
fig, ax = plt.subplots()
ax.set(
    xlabel='Rick and Morty Season',
    ylabel='Number of episodes',
    )
plt.bar(seasons,number_of_episodes)
plt.bar(seasons,number_of_episodes)

plt.xticks([0,1],values)
plt.show()

data1 = pd.read_csv('cereal.csv',delimiter=';', nrows=4, skiprows=[1])

x = data1['name']
y1 = data1['sugars']
y2 = data1['fiber']

fig,ax = plt.subplots()
# make a plot
ax.plot(x,y1)
# set x-axis label
ax.set_xlabel("Cereal")
# set y-axis label
ax.set_ylabel("Sugar", color="blue")

# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(x,y2, color="red")
ax2.set_ylabel("Fiber", color="red")
plt.show()

