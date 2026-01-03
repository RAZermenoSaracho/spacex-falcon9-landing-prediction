ROCKET_ID_MAP = {
    "5e9d0d95eda69955f709d1eb": "Falcon 1",
    "5e9d0d95eda69973a809d1ec": "Falcon 9 v1.0",
    "5e9d0d95eda69974db09d1ed": "Falcon 9 v1.1",
    "5e9d0d95eda69975f709d1ee": "Falcon 9 Full Thrust",
    "5e9d0d95eda69955f709d1ef": "Falcon Heavy",
    "5e9e4501f509094ba4566f84": "Falcon 9 Block 5"
}


def map_rocket_name(rocket_id):
    return ROCKET_ID_MAP.get(rocket_id, "Unknown Rocket")
