def get_population(country_dict):
    population_dict={
        '2022':int(country_dict['2022 Population']),
        '2020':int(country_dict['2020 Population']),
        '2015':int(country_dict['2015 Population']),
        '2010':int(country_dict['2010 Population']),
        '2000':int(country_dict['2000 Population']),
        '1990':int(country_dict['1990 Population']),
        '1980':int(country_dict['1980 Population']),
        '1970':int(country_dict['1970 Population']),
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values


def get_countries_and_percentages(country_percentage_dict):
    countries = list(country_percentage_dict.keys())  # Lista de los países (las claves)
    percentages = list(country_percentage_dict.values())  # Lista de los porcentajes (los valores)
    return countries, percentages



def population_by_country(data, country):
    result = list(filter(lambda item: item.get('Country/Territory', '').lower() == country.lower(), data))
    return result


