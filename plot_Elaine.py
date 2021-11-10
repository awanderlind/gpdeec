import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.patches as patches

#PS = pd.read_excel(r'C:\Users\augus\Documents\Augusto ASUS\RESEARCH\Elaine - Dados Brutos.xlsx')
PS = pd.read_excel(r'C:\Users\I5-Coffee Lake\Documents\AW\PYTHON\PythonProjects\GPDEEC\Elaine - Dados Brutos.xlsx')
x = np.array(PS[0:432] ['MINUTOS'])
T = np.array(PS[0:432] ['T'])
U = np.array(PS[0:432] ['H'])
T2 = np.array(PS[0:432] ['T2'])
U2 = np.array(PS[0:432] ['H2'])

fig = plt.figure()

#ax2 = ax1.twinx()
gs = fig.add_gridspec(2, hspace=0)
ax1 = gs.subplots(sharex=True, sharey=False)
ax2 = gs.subplots(sharex=True, sharey=False)
Line1, = ax1[0].plot(x, T, 'b-', label='Temperature (°C)')
Line2, = ax2[0].plot(x, U, 'b--', label='Humidity (%)')
Line3, = ax1[1].plot(x, T2, 'r-', label='Temperature (°C)')
Line4, = ax2[1].plot(x, U2, 'r--', label='Humidity (%)')
ax1[1].set_xlabel('Time (min)', fontsize = 16)
ax1[0].yaxis.set_label_position("left")
#ax1[1].yaxis.set_label_position("left")
ax1[0].set_ylabel('Temperature (°C) & Humidity (%)                                                      ', fontsize = 16)
#ax1[1].set_ylabel('T (°C) & H (%)')
ax1[0].yaxis.grid()
ax1[1].yaxis.grid()

#### Retângulos ####
ax1[0].add_patch(
     patches.Rectangle(
        (0, 0),
        90,
        100,
        edgecolor = 'black',
        alpha = 0.4,
        facecolor = 'gray',
        fill=True     
     ) )
ax1[0].add_patch(
     patches.Rectangle(
        (180, 0),
        90,
        100,
        edgecolor = 'black',
        alpha = 0.4,
        facecolor = 'gray',
        fill=True     
     ) )
ax1[1].add_patch(
     patches.Rectangle(
        (0, 0),
        90,
        100,
        edgecolor = 'black',
        alpha = 0.10,
        facecolor = 'red',
        fill=True  
     ) )
ax1[1].add_patch(
     patches.Rectangle(
        (180, 0),
        90,
        100,
        edgecolor = 'black',
        alpha = 0.10,
        facecolor = 'red',
        fill=True   
     ) )

#### Legendas ####
Gray_rec = patches.Patch(color ='gray', alpha = 0.4, label='Water spraying with radiation')
Blank_rec = patches.Patch(color ='red', alpha = 0.10 , label='Radiation only')
ax1[0].legend(handles=[Gray_rec, Line1, Line2], loc='center left', bbox_to_anchor=(1, 0.5), fontsize = 16)
ax1[1].legend(handles=[Blank_rec, Line3, Line4], loc='center left', bbox_to_anchor=(1, 0.5), fontsize = 16)
#plt.xticks(fontsize = 16)
#plt.yticks(fontsize = 16)

plt.show()

fig.savefig('Gráfico_Elaine.png', format='png', dpi = 300)
