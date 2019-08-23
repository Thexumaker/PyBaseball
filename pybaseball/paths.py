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
        "query_params": ['teamId', 'leagueID', 'season', 'leagueListID', 'gameType', 'startDate', 'endDate', 'fields', 'hydrate'],
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
        'query_params': ['orgId', 'fields', 'hydrate'],
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
            }, "gameStatus": {
                "required": False,
                "default": None
            }, "gameTypes": {
                "required": False,
                "default": None
            }, "hitTrajectories": {
                "required": False,
                "default": None
            }, "jobTypes": {
                "required": False,
                "default": None
            }, "languages": {
                "required": False,
                "default": None
            }, "leagueLeaderTypes": {
                "required": False,
                "default": None
            }, "logicalEvents": {
                "required": False,
                "default": None
            },
            "metrics": {
                "required": False,
                "default": None
            }, "pitchCodes": {
                "required": False,
                "default": None
            }, "platforms": {
                "required": False,
                "default": None
            }, "playerStatusCodes": {
                "required": False,
                "default": None
            }, "positions": {
                "required": False,
                "default": None
            }, "reviewReasons": {
                "required": False,
                "default": None
            }, "rosterTypes": {
                "required": False,
                "default": None
            }, "runnerDetailTypes": {
                "required": False,
                "default": None
            }, "scheduleEventTypes": {
                "required": False,
                "default": None
            }, "situationCodes": {
                "required": False,
                "default": None
            }, "sky": {
                "required": False,
                "default": None
            }, "standingsTypes": {
                "required": False,
                "default": None
            }, "statGroups": {
                "required": False,
                "default": None
            }, "statTypes": {
                "required": False,
                "default": None
            }, "windDirection": {
                "required": False,
                "default": None
            }




        },
        'query_params': [],
        'required_params': [[]]



    },
    "divisions": {
        "url": BASE_URL + "/{ver}/divisions",
        'path_params': {
            "ver": {
                "required": True,
                "default": "v1"

            }

        },
        "query_params": ['divisionId', 'includeInactive', 'leagueID', 'sportId', 'fields', 'hydrate'],
        'required_params': [[]]

    },
    'conferences':                   {
        'url': BASE_URL + '/{ver}/conferences',
        'path_params':  {
            'ver':  {
                'default': 'v1',
                'required': True
            }
        },
        'query_params': ['conferenceId', 'season', 'fields', 'hydrate'],
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
            'query_params': ['limit','hydrate', 'fields', 'order', 'round', 'name', 'position', 'team', 'teamId', 'state', 'country', 'playerId', 'bisPlayerId'],
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
            'query_params': ['hydrate', 'limit', 'fields', 'order', 'round', 'name', 'position', 'team', 'teamId', 'state', 'country', 'playerId', 'bisPlayerId'],
            'required_params': [['year']]

        }

    },
    'standings':                    {
        'url': BASE_URL + '{ver}/standings',
        'path_params':  {
            'ver':      {

                'default': 'v1',
                'required': True
            }
        },
        'query_params': ['leagueId', 'season', 'standingsTypes', 'date', 'fields', 'hydrate'],
        'required_params': [['leagueId']]
    },

    'stats':                        {
        'url': BASE_URL + '{ver}/stats',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            }
        },
        'query_params': ['stats', 'playerPool', 'position', 'teamId', 'leagueId', 'limit', 'offset', 'group', 'gameType', 'season', 'sportIds', 'sortStat', 'order',  'fields', 'hydrate'],
        'required_params': [['stats', 'group']]
    },

    'stats_leaders':                {
        'url': BASE_URL + '{ver}/stats/leaders',
        'path_params':  {
            'ver':      {
                'type': 'str',
                'default': 'v1',
                'leading_slash': False,
                'trailing_slash': False,
                'required': True
            }
        },
        'query_params': ['leaderCategories', 'playerPool', 'leaderGameTypes', 'statGroup', 'season', 'leagueId', 'sportId', 'hydrate', 'limit', 'fields', 'statType', 'hydrate'],
        'required_params': [['leaderCategories']],
        'note': 'If excluding season parameter to get all time leaders, include statType=statsSingleSeason or you will likely not get any results.'
    },
    'stats_streaks':                {
        'url': BASE_URL + '/{ver}/stats/streaks',
        'path_params':  {
            'ver':      {

                'default': 'v1',
                'required': True
            }
        },
        'query_params': ['streakType', 'streakSpan', 'gameType', 'season', 'sportId', 'limit', 'fields', 'hydrate'],
        'required_params': [['streakType', 'streakSpan', 'season']],
        # 'note': 'Valid streakType values: "hittingStreakOverall" "hittingStreakHome" "hittingStreakAway" "onBaseOverall" "onBaseHome" "onBaseAway". Valid streakSpan values: "career" "season" "currentStreak" "currentStreakInSeason" "notable" "notableInSeason".'
    },
    'people':                       {
    #Fix here
        'url': BASE_URL + '/{ver}/people/{personId}',
        'path_params':  {
            'ver':      {

                'default': 'v1',
                'required': True
            },
            'personId' : {
                'default': None,
                'required': True

            }
        },
        'query_params': [ 'fields', 'hydrate'],
        'required_params': [[]]
    },
    'teams':                        {
        'url': BASE_URL + '/{ver}/teams',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            }
        },
        'query_params': ['season', 'activeStatus', 'leagueIds', 'sportIds', 'gameType', 'fields', 'hydrate'],
        'required_params': [[]]
    },
    'teams_history':                {
        'url': BASE_URL + '{ver}/teams/history',
        'path_params':  {
            'ver':      {
                'type': 'str',
                'default': 'v1',
                'leading_slash': False,
                'trailing_slash': False,
                'required': True
            }
        },
        'query_params': ['teamIds', 'startSeason', 'endSeason', 'fields', 'hydrate'],
        'required_params': [['teamIds']]
    },
    'teams_stats':                  {
        'url': BASE_URL + '{ver}/teams/stats',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            }
        },
        'query_params': ['season', 'sportIds', 'group', 'gameType', 'stats', 'order', 'sortStat', 'fields' , 'hydrate'],
        'required_params': [['season', 'group', 'stats']],
        'note': 'Use meta(\'statGroups\') to look up valid values for group, and meta(\'statTypes\') for valid values for stats.'
    },
    'teams_affiliates':             {
        'url': BASE_URL + '{ver}/teams/affiliates',
        'path_params':  {
            'ver':      {
                'type': 'str',
                'default': 'v1',
                'leading_slash': False,
                'trailing_slash': False,
                'required': True
            }
        },
        'query_params': ['teamIds', 'sportId', 'season', 'hydrate', 'fields', 'hydrate'],
        'required_params': [['teamIds']]
    },
    'team_alumni':                  {
        'url': BASE_URL + '{ver}/teams/{teamId}/alumni',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            },
            'teamId':   {

                'default': None,

                'required': True
            }
        },
        'query_params': ['season', 'group', 'hydrate', 'fields', 'hydrate'],
        'required_params': [['season', 'group']]
    },
    'team_coaches':                 {
        'url': BASE_URL + '{ver}/teams/{teamId}/coaches',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            },
            'teamId':   {

                'default': None,

                'required': True
            }
        },
        'query_params': ['season', 'date', 'fields', 'hydrate'],
        'required_params': [[]]
    },
    'team_personnel':               {
        'url': BASE_URL + '{ver}/teams/{teamId}/personnel',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            },
            'teamId':   {

                'default': None,

                'required': True
            }
        },
        'query_params': ['date', 'fields', 'hydrate'],
        'required_params': [[]]
    },
    'team_leaders':                  {
        'url': BASE_URL + '{ver}/teams/{teamId}/leaders',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            },
            'teamId':   {

                'default': None,

                'required': True
            }
        },
        'query_params': ['leaderCategories', 'season', 'leaderGameTypes', 'hydrate', 'limit', 'fields', 'hydrate'],
        'required_params': [['leaderCategories', 'season']]
    },
    'team_roster':                  {
        'url': BASE_URL + '{ver}/teams/{teamId}/roster',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            },
            'teamId':   {

                'default': None,

                'required': True
            }
        },
        'query_params': ['rosterType', 'season', 'date', 'hydrate', 'fields'],
        'required_params': [['rosterType', 'season']]
    },

    'people_changes':               {
        'url': BASE_URL + '{ver}/people/changes',
        'path_params':  {
            'ver':      {
                'type': 'str',
                'default': 'v1',
                'leading_slash': False,
                'trailing_slash': False,
                'required': True
            }
        },
        'query_params': ['updatedSince', 'fields', 'hydrate'],
        'required_params': [[]]
    },
    'people_freeAgents':            {
        'url': BASE_URL + '{ver}/people/freeAgents',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            },
            'leagueId': {

                'default': '',

                'required': True
            }
        },
        'query_params': ['order', 'hydrate', 'fields'],
        'required_params': [[]]
    },
    'person':                       {
        'url': BASE_URL + '/{ver}/people/{personId}',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            },
            'personId': {

                'default': None,

                'required': True
            }
        },
        'query_params': ['fields', 'hydrate'],
        'required_params': [['personId']]
    },
    'person_stats':                 {
        'url': BASE_URL + '{ver}/people/{personId}/stats/game/{gamePk}',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            },
            'personId': {
                'default': None,
                'required': True
            },
            'gamePk': {

                'default': None,

                'required': True
            }
        },
        'query_params': ['fields', 'hydrate'],
        'required_params': [[]],
        'note': 'Specify "current" instead of a gamePk for a player\'s current game stats.'
    },
    'schedule':                     {
                                                    'url': BASE_URL + '/{ver}/schedule',
                                                    'path_params':  {
                                                                        'ver':      {

                                                                                        'default': 'v1',

                                                                                        'required': True
                                                                                    }
                                                                    },
                                                    'query_params': ['scheduleType','eventTypes','hydrate','teamId','leagueId','sportId','gamePk','gamePks','venueIds','gameTypes','date','startDate','endDate','opponentId','fields', 'hydrate'],
                                                    'required_params': [['sportId', 'gamePk', 'gamePks']]
                                                },
                'schedule_tied':                {
                                                    'url': BASE_URL + '{ver}/schedule/games/tied',
                                                    'path_params':  {
                                                                        'ver':      {

                                                                                        'default': 'v1',

                                                                                        'required': True
                                                                                    }
                                                                    },
                                                    'query_params': ['gameTypes','season','hydrate','fields'],
                                                    'required_params': [['season']]
                                                },
                'schedule_postseason':          {
                                                    'url': BASE_URL + '{ver}/schedule/postseason',
                                                    'path_params':  {
                                                                        'ver':      {

                                                                                        'default': 'v1',

                                                                                        'required': True
                                                                                    }
                                                                    },
                                                    'query_params': ['gameTypes','seriesNumber','teamId','sportId','season','hydrate','fields'],
                                                    'required_params': [[]]
                                                },
                'schedule_postseason_series':   {
                                                    'url': BASE_URL + '{ver}/schedule/postseason/series',
                                                    'path_params':  {
                                                                        'ver':      {

                                                                                        'default': 'v1',

                                                                                        'required': True
                                                                                    }
                                                                    },
                                                    'query_params': ['gameTypes','seriesNumber','teamId','sportId','season','fields'],
                                                    'required_params': [[]]
                                                },
                'schedule_postseason_tuneIn':   {
                                                    'url': BASE_URL + '{ver}/schedule/postseason/tuneIn',
                                                    'path_params':  {
                                                                        'ver':      {

                                                                                        'default': 'v1',

                                                                                        'required': True
                                                                                    }
},
                                                    'query_params': ['teamId','sportId','season','hydrate','fields'],
                                                    'required_params': [[]],
                                                    'note': 'The schedule_postseason_tuneIn endpoint appears to return no data.'
                                                },


}
