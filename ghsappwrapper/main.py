import requests

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
        """Sets section to dbSection for use across all methods
        
        Arguments:
            section {[type]} -- [description]
        
        Raises:
            Exception: [description]
        """
        if "/" != list(section)[0] and "" != list(section)[0]:
            colored_warning = colored("Make sure path is exact", "red")
            raise Exception(colored_warning)
        else:
            self.dbSection = section

    #############################################################################
    #############################################################################

    def calendarEvents(self):
        """Gets a list of all the events that the app collects from the school calendar.
        We don't collect events that have to do with the following:
        1. Middle school events
        2. Practices
        3. Scrimmages
        4. Sports that isn't one of the following:
            1. Soccer
            2. Football
            3. Baseball
            4. Softball
            5. Field Hockey
            6. Volleyball
            7. Basketball
            8. Lacrosse
        If response comes back as {} then there are no events for today
        
        Returns:
            dict -- response from calendar events
        """
        return GET_SECTION("calendarEvents", self)

    #############################################################################
    #############################################################################

    def monitoringInfo(self):
        """Gets a list of all the monitoring information.
        The monitoring info section of the database is meta data set there
        by each micro service. The Server Monitor program then takes that data
        and uses it to monitor the other micro services. Each micro service has
        the following meta data set for it:
        1. If maintainers should be emailed if the micro service goes down
        2. The time that the server monitor micro service will send an email
        if the micro service isn't on until then.
        3. How often the micro service should update in the database
        
        Returns:
            dict -- response from monitoring information
        """
        return GET_SECTION("monitoringInfo", self)

    #############################################################################
    #############################################################################
    
    def statuses(self):
        """Get a list of the statuses for each micro service for the ghs app.
        Each micro service has the following information for it's status:
        1. Last time online
        2. Last time offline
        3. If online (bool)
        
        Returns:
            dict -- response from statuses section
        """
        return GET_SECTION("statuses", self)

    #############################################################################
    #############################################################################

    def fieldInfo(self):
        """Get the information for all the homefields supported
        The home fields that are supported are:
        1. Football Field
        2. Gym
        3. Softball Field
        
        For each field there is the following information:
        1. Current sport on that field (or last sport if vision program is off)
        2. Current away team name (or last away team name if vision program is off)
        3. Start time for current game (or last game if vision program is off)
        4. If the current game is varsity or jv (last game if vision program is off)
        5. Current home game score and away game score (last game scores if the vision program is off)
        
        Returns:
            dict -- response from field-information section
        """
        return GET_SECTION("fieldInfo", self)

    #############################################################################
    #############################################################################

    def footballFieldInfo(self):
        """Field information just for the football field
        
        Returns:
            dict -- response from field-information/football-field section
        """
        return GET_SECTION("footballFieldInfo", self)

    #############################################################################
    #############################################################################

    def gymInfo(self):
        """Field information just for the gym
        
        Returns:
            dict -- response from field-information/gym section
        """
        return GET_SECTION("gymInfo", self)

    #############################################################################
    #############################################################################

    def softballFieldInfo(self):
        """Field information just for the softball field
        
        Returns:
            dict -- response from field-information/softball-field section
        """
        return GET_SECTION("softballFieldInfo", self)
