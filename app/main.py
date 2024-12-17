import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv('./data.csv') 
    country = input("Type country that you want to know their population")
    result = utils.population_by_country(data,country)
    country_percentage_dict = read_csv.read_csv_2('./data.csv')


    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        countries, percentages = utils.get_countries_and_percentages(country_percentage_dict)
        charts.generate_bar_chart(country['Country/Territory'],labels, values)
        charts.generate_pie_chart(countries, percentages)

    else:
        print('Country doesn´t exist')

if __name__ == '__main__':
    run()