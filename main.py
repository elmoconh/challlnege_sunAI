# Import pandas library
import pandas as pd
import os 
import glob
import numpy as np
import matplotlib.pyplot as plt
import datetime 
from scripts import generate_txt 


def readExcelFiles(path):
    text_file = generate_txt.TextFile

    excel_files = glob.glob(os.path.join(path, "*.xlsx"))
    sum = 0
    for file in excel_files:
        df = pd.read_excel(file)
        folder ='images/'+ df['fecha_im'][0].strftime("%d-%m-%Y")
        createFolder(folder)

        img_file =folder+'/grafico_planta_'+str(df['id_p'][0])+'.png'
        df.loc[df['active_power_im'] == 'data_faltante', 'active_power_im'] = 0    
        sum = sum + df['active_power_im'].sum()

        fig, ax = plt.subplots()
        for key, grp in df.groupby(['id_i']):
            ax = grp.plot(ax=ax, kind='line', x='fecha_im', y='active_power_im', label=key)
        plt.title('Planta '+str(df['id_p'][0]))
        plt.show()
        fig.savefig(img_file, dpi=100)
        plt.close(fig)


        try:
            file_name = text_file.generateFile(df['id_p'][0], df['fecha_im'][0])
            text_file.total(df['active_power_im'].sum(), file_name)
            text_file.max_min(df['active_energy_im'].max(), df['active_energy_im'].min(), file_name)
            text_file.save_file(file_name, img_file)
            
            print("Archivo generado con exito")

        except:
            print("Error al generar el archivo de texto")
    total_active_energy(sum)

def total_active_energy(value):
    os.system('cls' if os.name=='nt' else 'clear')
    print('Total Active Power: ',int(value))


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


if __name__ == '__main__':
    path = os.getcwd() 
    readExcelFiles(path)