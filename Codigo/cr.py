with open('./CSV/User_track_data.csv','r') as file: 
            for line in file:
                lista = line.split(sep=",")
                print(lista)