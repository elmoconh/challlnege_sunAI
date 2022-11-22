import os

class TextFile:

    def __init__(self):
        pass

    def generateFile(data, date):
        date = date.strftime("%d-%m-%Y")
        folder ='text_files/'+date
        TextFile.createFolder(folder)

        name =folder+ "/data_planta_"+str(data)+"_dia_"+date+".txt"
        file = open(name, "w")
        file.write("Datos de la planta: "+ str(data) + "\nFecha: "+ str(date))
        file.close()
        return name

    def total(value, file):
        file = open(file, "a")
        file.write("\ntotal: "+ str(value))
        file.close()
        

    def max_min(max, min, file) :
        file = open(file, "a")
        file.write("\nmax: "+ str(max) + " min: "+ str(min))
        file.close()
    
 
       
    def save_file(file, data):
        file = open(file, "a")
        file.write( "\nDireccion imagen: "+ data)
        file.close()
    
    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)