BASE_URL = "http://statsapi.mlb.com/api"
# double check the documentation Slater
# takes time to load, but paths /path = number, players is a little weird where u only write hte number
# querys usually ? and then same format, nust have to work thru it
# keep the functions i made i dont feel like fixing it and it really doesnt need to be put in
PATHS = {
    "attendance": {
        'url': BASE_URL + "/{ver}/attendance",
        "path_params": {
            "ver": {
                "required": True,
                "default": "v1"
            }

        },
        "query_params": ['teamId', 'leagueID', 'season', 'leagueListID', 'gameType', 'startDate', 'endDate', 'fields'],
        'required_params': [['teamID', 'leagueID', 'leagueListID']]




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
        'query_params': ['orgId', 'fields'],
        'required_params': [[]]


    },
    "config": {
                'url': BASE_URL + "/{ver}/{baseballStats}/{eventTypes}/{fielderDetailTypes}/{gameStatus}/{gameTypes}/{hitTrajectories}/{jobTypes}/\
{languages}/{leagueLeaderTypes}/{logicalEvents}/{metrics}/{pitchCodes}/{pitchTypes}/{platforms}/{playerStatusCodes}/{positions}/\
{reviewReasons}/{rosterTypes}/{runnerDetailTypes}/{scheduleEventTypes}/{situationCodes}/{sky}/{standingsTypes}/{statGroups}/{statTypes}/\
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
            "ver": {
                "required": True,
                "default": "v1"

            }

        },
        "query_params": ['divisionId', 'includeInactive', 'leagueID', 'sportId', 'fields'],
        'required_params': [[]]

    },
    "draft": {
        'url': BASE_URL + "/{ver}/draft/{year}",
        'path_params': {
            "ver": {
                "required": True,
                "default": "v1"

            },
            'year': {
                'required': True,
                'default': 2019

            },
            'query_params': ['limit', 'fields', 'order', 'round', 'name', 'position', 'team', 'teamId', 'state', 'country', 'playerId', 'bisPlayerId'],
            'required_params': [['year']]

        },

    },
    "prospects": {
        'url': BASE_URL + "/{ver}/draft/prospects/{year}",
        'path_params': {
            "ver": {
                "required": True,
                "default": "v1"

            },
            'year': {
                'required': True,
                'default': 2019

            },
            'query_params': ['limit', 'fields', 'order', 'round', 'name', 'position', 'team', 'teamId', 'state', 'country', 'playerId', 'bisPlayerId'],
            'required_params': [['year']]

        }

    },
    'stats':                        {
        'url': BASE_URL + '{ver}/stats',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            }
        },
        'query_params': ['stats', 'playerPool', 'position', 'teamId', 'leagueId', 'limit', 'offset', 'group', 'gameType', 'season', 'sportIds', 'sortStat', 'order',  'fields'],
        'required_params': [['stats', 'group']]
    },

<<<<<<< HEAD
    'stats_leaders':                {
                                                    'url': BASE_URL + '{ver}/stats/leaders',
                                                    'path_params':  {
                                                                        'ver':      {
                                                                                        'type': 'str',
                                                                                        'default': 'v1',
                                                                                        'leading_slash': False,
                                                                                        'trailing_slash': False,
=======
    'stats_leaders': {
                                                    'url': BASE_URL + '{ver}/stats/leaders',
                                                    'path_params':  {
                                                                        'ver':      {

                                                                                        'default': 'v1',

>>>>>>> bea26f18282da2b73a735c15e4c9576fb4a6a3c7
                                                                                        'required': True
                                                                                    }
                                                                    },
                                                    'query_params': ['leaderCategories','playerPool','leaderGameTypes','statGroup','season','leagueId','sportId','hydrate','limit','fields','statType'],
                                                    'required_params': [['leaderCategories']],
<<<<<<< HEAD
                                                    'note': 'If excluding season parameter to get all time leaders, include statType=statsSingleSeason or you will likely not get any results.'
                                                },
    'people':                       {
=======

                                                },
    'people':{
>>>>>>> bea26f18282da2b73a735c15e4c9576fb4a6a3c7
                                                    'url': BASE_URL + '/{ver}/people',
                                                    'path_params':  {
                                                                        'ver':      {

                                                                                        'default': 'v1',
                                                                                        'required': True
                                                                                    }
                                                                    },
                                                    'query_params': ['personIds','fields'],
                                                    'required_params': [['personIds']]
                                                },

    }
