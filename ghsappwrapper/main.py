import requests
from termcolor import colored

def GET_SECTION(section_name, section):
    """Make response to database and clean it
    
    Arguments:
        section_name {string} -- name of the section to select from locations dict
        section {sting} -- specific section to get from inside section. If root of section than just put ""
    
    Returns:
        object -- response from request to section
    """
    
    locations = {
        "calendarEvents": "/calendar/tday-section",
        "monitoringInfo": "/db-info/monitoring",
        "statuses": "/db-info/statuses",
        "fieldInfo": "/field-information",
        "scores": "/scores",
        "footballFieldInfo": "/field-information/field-status/football-field",
        "gymInfo": "/field-information/field-status/gym"
    }
    
    full_url = "https://ghs-app-5a0ba.firebaseio.com" + \
        locations[section_name] + section + ".json"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(full_url, headers=headers)
    json_response = response.json()
    if json_response == None:
        return {}
    else:
        return json_response


class ghsApp():

    def __init__(self, section):
        if "/" != list(section)[0] and "" != list(section)[0]:
            colored_warning = colored("Make sure path is exact", "red")
            raise Exception(colored_warning)
        else:
            self.dbSection = section

    def calendarEvents(self):
        return GET_SECTION("calendarEvents", self)

    def monitoringInfo(self):
        return GET_SECTION("monitoringInfo", self)

    def statuses(self):
        return GET_SECTION("statuses", self)

    def fieldInfo(self):
        return GET_SECTION("fieldInfo", self)

    def scores(self):
        return GET_SECTION("scores", self)

    def footballFieldInfo(self):
        return GET_SECTION("footballFieldInfo", self)
    
    def gymInfo(self):
        return GET_SECTION("gymInfo", self)
    
    def softballFieldInfo(self):
        return GET_SECTION("softballFieldInfo", self)
