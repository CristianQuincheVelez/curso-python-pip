import csv

def read_csv(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []   
        for row in reader:
            iterable =zip(header,row)
            country_dict = {key:value for key, value in iterable}
            data.append(country_dict)

        return data

def read_csv_2(path):
    with open(path, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        
        # Crear un diccionario vacío para almacenar los países y sus porcentajes
        country_percentage_dict = {}

        # Recorrer cada fila del archivo CSV
        for row in reader:
          

            country = row['Country/Territory']
            percentage = row['World Population Percentage']
            
            # Convertir el porcentaje a tipo float y agregarlo al diccionario
            country_percentage_dict[country] = float(percentage)

    return country_percentage_dict


if __name__ =='__main__':
    data = read_csv('./data.csv')
    print(data[0])
    
    
    