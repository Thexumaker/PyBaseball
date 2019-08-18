BASE_URL = "http://statsapi.mlb.com/api"
#double check the documentation Slater
#takes time to load, but paths /path = number, players is a little weird where u only write hte number
#querys usually ? and then same format, nust have to work thru it
#keep the functions i made i dont feel like fixing it and it really doesnt need to be put in
PATHS = {
    "attendance": {
                    'url': BASE_URL + "/{ver}/attendance",
                    "path_params":{
                                    "ver": {
                                            "required": True,
                                            "default": "v1"
                                    }

                    },
                    "query_params":['teamId', 'leagueID', 'season', 'leagueListID', 'gameType', 'startDate', 'endDate', 'fields'],
                    'required_params':[['teamID', 'leagueID', 'leagueListID']]




    },
    "awards": {
                'url': BASE_URL + "/{ver}/awards/{awardId}/{recipients}",
                "path_params": {
                                "ver": {
                                        "required": True,
                                        "default": "v1"
                                },
                                "awardId": {
                                            "required": False,
                                            "default": None
                                },
                                "recipients": {
                                                "required:False"
                                                "default": None
                                }


                },
                'query_params':['orgId', 'fields'],
                'required_params':[[]]


    },
    "config": {
                'url': BASE_URL + "/{ver}/{baseballStats}/{eventTypes}/{fielderDetailTypes}/{gameStatus}/{gameTypes}/{hitTrajectories}/{jobTypes}/ \
                {languages}/{leagueLeaderTypes}/{logicalEvents}/{metrics}/{pitchCodes}/{pitchTypes}/{platforms}/{playerStatusCodes}/{positions}/ \
                {reviewReasons}/{rosterTypes}/{runnerDetailTypes}/{scheduleEventTypes}/{situationCodes}/{sky}/{standingsTypes}/{statGroups}/{statTypes}/ \
                {windDirection}",
                "path_params": {
                                "ver": {
                                        "required": True,
                                        "default": "v1"
                                },
                                "baseballStats": {
                                            "required": False,
                                            "default": None
                                },
                                "eventTypes": {
                                                "required:False"
                                                "default": None
                                },
                                "fielderDetailTypes": {
                                            "required": False,
                                            "default": None
                                },"gameStatus": {
                                            "required": False,
                                            "default": None
                                },"gameTypes": {
                                            "required": False,
                                            "default": None
                                },"hitTrajectories": {
                                            "required": False,
                                            "default": None
                                },"jobTypes": {
                                            "required": False,
                                            "default": None
                                },"languages": {
                                            "required": False,
                                            "default": None
                                },"leagueLeaderTypes": {
                                            "required": False,
                                            "default": None
                                },"logicalEvents": {
                                            "required": False,
                                            "default": None
                                },
                                "metrics": {
                                            "required": False,
                                            "default": None
                                },"pitchCodes": {
                                            "required": False,
                                            "default": None
                                },"platforms": {
                                            "required": False,
                                            "default": None
                                },"playerStatusCodes": {
                                            "required": False,
                                            "default": None
                                },"positions": {
                                            "required": False,
                                            "default": None
                                },"reviewReasons": {
                                            "required": False,
                                            "default": None
                                },"rosterTypes": {
                                            "required": False,
                                            "default": None
                                },"runnerDetailTypes": {
                                            "required": False,
                                            "default": None
                                },"scheduleEventTypes": {
                                            "required": False,
                                            "default": None
                                },"situationCodes": {
                                            "required": False,
                                            "default": None
                                },"sky": {
                                            "required": False,
                                            "default": None
                                },"standingsTypes": {
                                            "required": False,
                                            "default": None
                                },"statGroups": {
                                            "required": False,
                                            "default": None
                                },"statTypes": {
                                            "required": False,
                                            "default": None
                                },"windDirection": {
                                            "required": False,
                                            "default": None
                                }




                },
                'query_params':[],
                'required_params':[[]]



    },
    "divisions": {
                "url": BASE_URL + "/{ver}/divisions",
                'path_params': {
                                "ver" : {
                                        "required": True,
                                        "default": "v1"

                                }

                },
                "query_params": ['divisionId', 'includeInactive', 'leagueID', 'sportId', 'fields'],
                'required_params': [[]]

},



    "team": {
            'url': BASE_URL + "/{ver}/teams",
            "path_params":{
                            "ver" : {
                                    "required": True,
                                    "default": "v1"

                            }

            },
            "query_params": ['teamIds','startSeason','endSeason','fields'],
            "required_params": [['teamIds']]




            }
            #have to break

    }
