def city_country(city_name, country_name, population=None):
    """
    Return a neatly formatted city and country name seperated by a comma.
    """
    final_name = f"{city_name}, {country_name}"
    final_name = final_name.title()
    if population:
        final_name += f" - population {population}"
    return final_name
