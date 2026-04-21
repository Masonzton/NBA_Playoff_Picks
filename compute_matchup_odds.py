"""
A file for computing the matchup odds between different NBA teams based on ESPN's published odds and BPI ranking

https://www.espn.com/nba/bpi/_/view/playoffs
"""

import requests
from my_types import Team
from game import Matchup, BRACKET_MATCHUP
from config import MATCHUP_ODDS
from typing import Optional, Any, Tuple, List
import json

POWER_INDEX_URL = "http://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/seasons/2026/powerindex?lang=en&region=us&limit=100&page=1"
POWER_INDEX_DATA_JSON = "power_index_data.json"

TEAM_POWER_DATA : dict[str, dict[str, float]]= {}

def print_tabulate(header: Tuple[str,...], data: List[Tuple[Any,...]]):
    """
    Print a list of information in a nice tabulated form
    """
    assert len(header) == len(data[0])
    # First, calculate the maximum width for each column
    col_widths = [
        max(len(str(row[i])) for row in data + [header]) for i in range(len(header))
    ]

    # Print the header
    header_str_list = [f"{header[i]:<{col_widths[i]}}" for i in range(len(header))]
    header_str = "  ".join(header_str_list)
    print(header_str)
    print("-" * (sum(col_widths) + 6))

    # Print each row
    for row in data:
        assert len(row) == len(header)
        row_str_list = [f"{row[i]:<{col_widths[i]}}" for i in range(len(row))]
        row_str = "  ".join(row_str_list)
        print(row_str)

def get_odds_for_each_team():
    # First we need to grab the power indexes
    power_index_result = requests.get(POWER_INDEX_URL)
    power_index_result.raise_for_status()

    power_index_dict = power_index_result.json()

    data_to_grab = ["bpi", "probmakeplayoffs", "probmakeconfsemi", "probmakeconfchamp", "probmaketitlegame", "probwintitle"]
    headers = ["Team Name", "Season type"] + data_to_grab

    data : list[Tuple[Any]]= []

    for team_entry in power_index_dict["items"]:

        # TODO: wrap in try except block to avoid blowing up cause one team messed up

        if team_entry["seasonType"] != 3:
            continue

        # try: 
        team_ref_url = team_entry["team"]["$ref"]
        team_ref_result = requests.get(team_ref_url)
        team_ref_result.raise_for_status()
        team_ref_data = team_ref_result.json()
        team_name = team_ref_data["name"]


        name_to_stats : dict[str, float] = dict()
        for stat_entry in team_entry["stats"]:
            if "name" in stat_entry and "value" in stat_entry:
                name_to_stats[stat_entry["name"]] = stat_entry["value"]

        display_entry : list [Any]= [team_name, team_entry["seasonType"]]
        for header_field in data_to_grab:
            if header_field in name_to_stats:
                display_entry.append(name_to_stats[header_field])
            else:
                display_entry.append(None)
        data.append(tuple(display_entry))
    
    print_tabulate(header=tuple(headers), data=data)

    data_json = {row[0] : {header: row[idx] for idx, header in enumerate(headers)}  for row in data}
    with open(POWER_INDEX_DATA_JSON, 'w', encoding='utf-8') as f:
        json.dump(data_json, f)

def get_attribute(team: Team, attribute: str) -> float:
    return TEAM_POWER_DATA[team.team_name][attribute]
    pass

def compute_odds_sub(bracket: Matchup):
    if bracket.get_team() is not None:
        # nothing to fill out since the bracket has it's winners already
        return
    elif type(bracket.teamA) == Matchup:
        assert bracket.teamB == Matchup
        # fill out the left and right bracket's first if they are a matchup object
        if bracket.teamA.get_team() is None:
            compute_odds_sub(bracket=bracket.teamA)
        if bracket.teamB.get_team() is None:
            compute_odds_sub(bracket=bracket.teamB)
    # else:
    #     # this is an unfilled out team thing
    #     assert type(bracket.teamB) == Team
    #     assert type(bracket.teamA) == Team
    elif (type(bracket.teamA) == Team):
        bracket.teamA.name 
        pass


def compute_odds():
    global TEAM_POWER_DATA
    with open(POWER_INDEX_DATA_JSON, 'r') as file:
        TEAM_POWER_DATA = json.load(file)

    # go down to the lowest level of the tree
    assert type(BRACKET_MATCHUP.teamA) == Matchup
    compute_odds_sub(BRACKET_MATCHUP.teamA)



def main():
    get_odds_for_each_team()
    compute_odds()
    pass

if __name__ == "__main__":
    main()