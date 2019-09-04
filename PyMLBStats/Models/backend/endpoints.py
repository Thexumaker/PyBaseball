BASE_URL = "http://statsapi.mlb.com/api"
# double check the documentation Slater
# takes time to load, but paths /path = number, players is a little weird where u only write hte number
# querys usually ? and then same format, nust have to work thru it
# keep the functions i made i dont feel like fixing it and it really doesnt need to be put in
ENDPOINTS = {
    "attendance": {
        'url': BASE_URL + "/{ver}/attendance",
        "path_params": {
            "ver": {
                "required": True,
                "default": "v1"
            }

        },
        "query_params": ['teamId', 'leagueID', 'season', 'leagueListID', 'gameType', 'startDate', 'endDate', 'fields', 'hydrate'],
        'required_params': [['ver'], ['teamID', 'leagueID', 'leagueListID']]




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
                "default": 'awardId'
            },
            "recipients": {
                "required": False,
                "default": None
            }


        },
        'query_params': ['orgId', 'fields', 'hydrate'],
        'required_params': [['ver'], ['awardId'], ['recipients']]


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
        'required_params': [['ver']]

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
        'required_params': [['ver']]
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
            'query_params': ['limit', 'hydrate', 'fields', 'order', 'round', 'name', 'position', 'team', 'teamId', 'state', 'country', 'playerId', 'bisPlayerId'],
            'required_params': [['ver'], ['year']]

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
            'required_params': [['ver'], ['year']]

        }

    },
    'standings':                    {
        'url': BASE_URL + '/{ver}/standings',
        'path_params':  {
            'ver':      {

                'default': 'v1',
                'required': True
            }
        },
        'query_params': ['leagueId', 'season', 'standingsTypes', 'date', 'fields', 'hydrate'],
        'required_params': [['ver'], ['leagueId']]
    },

    'stats':                        {
        'url': BASE_URL + '/{ver}/stats',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            }
        },
        'query_params': ['stats', 'playerPool', 'position', 'teamId', 'leagueId', 'limit', 'offset', 'group', 'gameType', 'season', 'sportIds', 'sortStat', 'order',  'fields', 'hydrate'],
        'required_params': [['ver'], ['stats'], ['group']]
    },

    'stats_leaders':                {
        'url': BASE_URL + '/{ver}/stats/leaders',
        'path_params':  {
            'ver':      {

                'default': 'v1',
                'required': True
            }
        },
        'query_params': ['leaderCategories', 'playerPool', 'leaderGameTypes', 'statGroup', 'season', 'leagueId', 'sportId', 'hydrate', 'limit', 'fields', 'statType', 'hydrate'],
        'required_params': [['ver'], ['leaderCategories']],
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
        'required_params': [['streakType'], ['season'], ['streakSpan'], ['gameType']]
        # 'note': 'Valid streakType values: "hittingStreakOverall" "hittingStreakHome" "hittingStreakAway" "onBaseOverall" "onBaseHome" "onBaseAway". Valid streakSpan values: "career" "season" "currentStreak" "currentStreakInSeason" "notable" "notableInSeason".'
    },
    'people':                       {
        # Fix here
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
        'required_params': [['ver']]
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
        'required_params': [['ver']]
    },
    'teams_history':                {
        'url': BASE_URL + '/{ver}/teams/history',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            }
        },
        'query_params': ['teamIds', 'startSeason', 'endSeason', 'fields', 'hydrate'],
        'required_params': [['ver'], ['teamIds']]
    },
    'teams_stats':                  {
        'url': BASE_URL + '/{ver}/teams/stats',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            }
        },
        'query_params': ['season', 'sportIds', 'group', 'gameType', 'stats', 'order', 'sortStat', 'fields', 'hydrate'],
        'required_params': [['season', 'group', 'stats']],
        'note': 'Use meta(\'statGroups\') to look up valid values for group, and meta(\'statTypes\') for valid values for stats.'
    },
    'teams_affiliates':             {
        'url': BASE_URL + '/{ver}/teams/affiliates',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            }
        },
        'query_params': ['teamIds', 'sportId', 'season', 'hydrate', 'fields', 'hydrate'],
        'required_params': [['ver'], ['teamIds']]
    },
    'team_alumni':                  {
        'url': BASE_URL + '/{ver}/teams/{teamId}/alumni',
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
        'required_params': [['ver'], ['season', 'group']]
    },
    'team_coaches':                 {
        'url': BASE_URL + '/{ver}/teams/{teamId}/coaches',
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
        'required_params': [['ver']]
    },
    'team_personnel':               {
        'url': BASE_URL + '/{ver}/teams/{teamId}/personnel',
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
        'required_params': [['ver']]
    },
    'team_leaders':                  {
        'url': BASE_URL + '/{ver}/teams/{teamId}/leaders',
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
        'required_params': [['ver'], ['leaderCategories', 'season']]
    },
    'team_roster':                  {
        'url': BASE_URL + '/{ver}/teams/{teamId}/roster',
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
        'required_params': [['ver'], ['rosterType', 'season']]
    },

    'people_changes':               {
        'url': BASE_URL + '/{ver}/people/changes',
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
        'required_params': [['ver']]
    },
    'people_freeAgents':            {
        'url': BASE_URL + '/{ver}/people/freeAgents',
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
        'required_params': [['ver']]
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
        'required_params': [['ver'], ['personId']]
    },
    'person_stats':                 {
        'url': BASE_URL + '/{ver}/people/{personId}/stats/game/{gamePk}',
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
        'required_params': [['ver']],
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
        'query_params': ['scheduleType', 'eventTypes', 'hydrate', 'teamId', 'leagueId', 'sportId', 'gamePk', 'gamePks', 'venueIds', 'gameTypes', 'date', 'startDate', 'endDate', 'opponentId', 'fields', 'hydrate'],
        'required_params': [['ver'], ['sportId', 'gamePk', 'gamePks']]
    },
    'schedule_tied':                {
        'url': BASE_URL + '/{ver}/schedule/games/tied',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            }
        },
        'query_params': ['gameTypes', 'season', 'hydrate', 'fields'],
        'required_params': [['season']]
    },
    'schedule_postseason':          {
        'url': BASE_URL + '/{ver}/schedule/postseason',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            }
        },
        'query_params': ['gameTypes', 'seriesNumber', 'teamId', 'sportId', 'season', 'hydrate', 'fields'],
        'required_params': [[]]
    },
    'schedule_postseason_series':   {
        'url': BASE_URL + '/{ver}/schedule/postseason/series',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            }
        },
        'query_params': ['gameTypes', 'seriesNumber', 'teamId', 'sportId', 'season', 'fields'],
        'required_params': [[]]
    },
    'schedule_postseason_tuneIn':   {
        'url': BASE_URL + '/{ver}/schedule/postseason/tuneIn',
        'path_params':  {
            'ver':      {

                'default': 'v1',

                'required': True
            }
        },
        'query_params': ['teamId', 'sportId', 'season', 'hydrate', 'fields'],
        'required_params': [[]],
        'note': 'The schedule_postseason_tuneIn endpoint appears to return no data.'
    },


    'game':                         {
        'url': BASE_URL + '/{ver}/game/{gamePk}/feed/live',
        'path_params':  {
            'ver':  {

                'default': 'v1',

                'required': True
            },
            'gamePk': {

                'default': None,

                'required': True
            }
        },
        'query_params': ['timecode', 'hydrate', 'fields'],
        'required_params': [['ver']]
    },
    'game_diff':                    {
        'url': BASE_URL + '/{ver}/game/{gamePk}/feed/live/diffPatch',
        'path_params':  {
            'ver':  {

                'default': 'v1',

                'required': True
            },
            'gamePk': {

                'default': None,

                'required': True
            }
        },
        'query_params': ['startTimecode', 'endTimecode'],
        'required_params': [['ver'], ['startTimeCode', 'endTimeCode']]
    },
    'game_timestamps':              {
        'url': BASE_URL + '/{ver}/game/{gamePk}/feed/live/timestamps',
        'path_params':  {
            'ver':  {

                'default': 'v1',

                'required': True
            },
            'gamePk': {

                'default': None,

                'required': True
            }
        },
        'query_params': [],
        'required_params': [['ver']]
    },
    'game_changes':                 {
        'url': BASE_URL + '/{ver}/game/changes',
        'path_params':  {
            'ver':  {
                'type': 'str',
                'default': 'v1',
                'leading_slash': False,
                'trailing_slash': False,
                'required': True
            }
        },
        'query_params': ['updatedSince', 'sportId', 'gameType', 'season', 'fields'],
        'required_params': [['ver'], ['updatedSince']]
    },
    'game_contextMetrics':          {
        'url': BASE_URL + '/{ver}/game/{gamePk}/contextMetrics',
        'path_params':  {
            'ver':  {

                'default': 'v1',

                'required': True
            },
            'gamePk': {

                'default': None,

                'required': True
            }
        },
        'query_params': ['timecode', 'fields'],
        'required_params': [['ver']]
    },
    'game_winProbability':          {
        'url': BASE_URL + '/{ver}/game/{gamePk}/winProbability',
        'path_params':  {
            'ver':  {
                'default': 'v1',
                'required': True
            },
            'gamePk': {
                'default': None,
                'required': True
            }
        },
        'query_params': ['timecode', 'fields'],
        'required_params': [['ver']],
        'note': 'If you only want the current win probability for each team, try the game_contextMetrics endpoint instad.'
    },
    'game_boxscore':                {
        'url': BASE_URL + '/{ver}/game/{gamePk}/boxscore',
        'path_params':  {
            'ver':  {
                'default': 'v1',
                'required': True
            },
            'gamePk': {
                'default': '',
                'required': True
            }
        },
        'query_params': ['timecode', 'fields'],
        'required_params': [[]]
    },
    'game_content':                 {
        'url': BASE_URL + '/{ver}/game/{gamePk}/content',
        'path_params':  {
            'ver':  {

                'default': 'v1',

                'required': True
            },
            'gamePk': {

                'default': '',

                'required': True
            }
        },
        'query_params': ['highlightLimit'],
        'required_params': [[]]
    },
    'game_color':                   {
        'url': BASE_URL + '/{ver}/game/{gamePk}/feed/color',
        'path_params':  {
            'ver':  {

                'default': 'v1',

                'required': True
            },
            'gamePk': {

                'default': '',

                'required': True
            }
        },
        'query_params': ['timecode', 'fields'],
        'required_params': [[]]
    },
    'game_color_diff':              {
        'url': BASE_URL + '/{ver}/game/{gamePk}/feed/color/diffPatch',
        'path_params':  {
            'ver':  {

                'default': 'v1',

                'required': True
            },
            'gamePk': {

                'default': '',

                'required': True
            }
        },
        'query_params': ['startTimecode', 'endTimecode'],
        'required_params': [['startTimeCode', 'endTimeCode']]
    },
    'game_color_timestamps':        {
        'url': BASE_URL + '/{ver}/game/{gamePk}/feed/color/timestamps',
        'path_params':  {
            'ver':  {

                'default': 'v1',

                'required': True
            },
            'gamePk': {

                'default': '',

                'required': True
            }
        },
        'query_params': [],
        'required_params': [[]]
    },
    'game_linescore':               {
        'url': BASE_URL + '/{ver}/game/{gamePk}/linescore',
        'path_params':  {
            'ver':  {

                'default': 'v1',

                'required': True
            },
            'gamePk': {

                'default': '',

                'required': True
            }
        },
        'query_params': ['timecode', 'fields'],
        'required_params': [[]]
    },
    'game_playByPlay':              {
        'url': BASE_URL + '/{ver}/game/{gamePk}/playByPlay',
        'path_params':  {
            'ver':  {

                'default': 'v1',

                'required': True
            },
            'gamePk': {

                'default': '',

                'required': True
            }
        },
        'query_params': ['timecode', 'fields'],
        'required_params': [[]]
    },
    'gamePace':                     {
        'url': BASE_URL + '/{ver}/gamePace',
        'path_params':  {
            'ver':  {

                'default': 'v1',

                'required': True
            }
        },
        'query_params': ['season', 'teamIds', 'leagueIds', 'leagueListId', 'sportId', 'gameType', 'startDate', 'endDate', 'venueIds', 'orgType', 'includeChildren', 'fields'],
        'required_params': [['season']]
    },
    'highLow':                      {
        'url': BASE_URL + '/{ver}/highLow/{orgType}',
        'path_params':  {
            'ver':  {

                'default': 'v1',

                'required': True
            },
            'orgType':  {

                'default': '',

                'required': True
            }
        },
        'query_params': ['statGroup', 'sortStat', 'season', 'gameType', 'teamId', 'leagueId', 'sportIds', 'limit', 'fields'],
        'required_params': [['sortStat', 'season']],
        'note': 'Valid values for orgType parameter: player, team, division, league, sport, types.'
    },
    'homeRunDerby':                 {
        'url': BASE_URL + '/{ver}/honeRunDerby/{gamePk}{bracket}{pool}',
        'path_params':  {
            'ver':      {

                'default': 'v1',
                'required': True
            },
            'gamePk':   {
                'default': '',
                'required': True
            },
            'bracket':  {
                'default': False,

                'required': False
            },
            'pool':     {

                'default': False,
                'required': False
            }
        },
        'query_params': ['fields'],
        'required_params': [[]]
    },
    'league':                       {
        'url': BASE_URL + '/{ver}/league',
        'path_params':  {
            'ver':  {

                'default': 'v1',
                'required': True
            }
        },
        'query_params': ['sportId', 'leagueIds', 'seasons', 'fields'],
        'required_params': [['sportId'], ['leagueIds']]
    },
    'league_allStarBallot':         {
        'url': BASE_URL + '/{ver}/league/{leagueId}/allStarBallot',
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
        'query_params': ['season', 'fields'],
        'required_params': [['season']]
    },
    'league_allStarWriteIns':       {
        'url': BASE_URL + '/{ver}/league/{leagueId}/allStarWriteIns',
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
        'query_params': ['season', 'fields'],
        'required_params': [['season']]
    },
    'league_allStarFinalVote':      {
        'url': BASE_URL + '/{ver}/league/{leagueId}/allStarFinalVote',
        'path_params':  {
            'ver':      {

                'default': 'v1',
                'required': True
            },
            'leagueId': {
                'type': 'str',
                'default': '',
                'leading_slash': False,
                'trailing_slash': False,
                'required': True
            }
        },
        'query_params': ['season', 'fields'],
        'required_params': [['season']]
    },
    'sports':                       {
        'url': BASE_URL + '/{ver}/sports',
        'path_params':  {
            'ver':      {

                'default': 'v1',
                'required': True
            }
        },
        'query_params': ['sportId', 'fields'],
        'required_params': [[]]
    },
    'sports_players':               {
        'url': BASE_URL + '/{ver}/sports/{sportId}/players',
        'path_params':  {
            'ver':      {
                'default': 'v1',
                'required': True
            },
            'sportId': {
                'default': '1',
                'required': True
            }
        },
        'query_params': ['season', 'gameType', 'fields'],
        'required_params': [['season']]
    },
    'jobs':                         {
        'url': BASE_URL + '/{ver}/jobs',
        'path_params':  {
            'ver':      {
                'default': 'v1',
                'required': True
            }
        },
        'query_params': ['jobType', 'sportId', 'date', 'fields'],
        'required_params': [['jobType']]
    },
    'jobs_umpires':                 {
        'url': BASE_URL + '/{ver}/jobs/umpires',
        'path_params':  {
            'ver':      {
                'default': 'v1',
                'required': True
            }
        },
        'query_params': ['sportId', 'date', 'fields'],
        'required_params': [[]]
    },
    'jobs_umpire_games':            {
        'url': BASE_URL + '/{ver}/jobs/umpires/games/{umpireId}',
        'path_params':  {
            'ver':      {
                'type': 'str',
                'default': 'v1',
                'leading_slash': False,
                'trailing_slash': False,
                'required': True
            },
            'umpireId': {
                'type': 'str',
                'default': None,
                'leading_slash': False,
                'trailing_slash': False,
                'required': True
            }
        },
        'query_params': ['season', 'fields'],
        'required_params': [['season']]
    },
    'jobs_datacasters':             {
        'url': BASE_URL + '/{ver}/jobs/datacasters',
        'path_params':  {
            'ver':      {
                'default': 'v1',
                'required': True
            }
        },
        'query_params': ['sportId', 'date', 'fields'],
        'required_params': [[]]
    },
    'jobs_officialScorers':         {
        'url': BASE_URL + '/{ver}/jobs/officialScorers',
        'path_params':  {
            'ver':      {
                'default': 'v1',
                'required': True
            }
        },
        'query_params': ['timecode', 'fields'],
        'required_params': [[]]
    },
    'venue':                        {
        'url': BASE_URL + '{ver}/venues',
        'path_params':  {
            'ver':      {
                'default': 'v1',
                'required': True
            }
        },
        'query_params': ['venueIds', 'season', 'hydrate', 'fields'],
        'required_params': [['venueIds']]
    }


}
