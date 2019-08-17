BASE_URL = "http://statsapi.mlb.com/api"
#double check the documentation Slater
#takes time to load, but paths /path = number, players is a little weird where u only write hte number
#querys usually ? and then same format, nust have to work thru it
#keep the functions i made i dont feel like fixing it and it really doesnt need to be put in
PATHS = {
    "team": {
            'url': BASE_URL + "/{ver}/teams",
            "path_params":{
                            "ver" : {
                                    "required": True,
                                    "default": "v1"

                            },

            },
            "query_params": ['teamIds','startSeason','endSeason','fields'],
            "required_params": [['teamIds']]




            }

    }
