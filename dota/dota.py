# -*- coding:utf-8 -*-
import dota2api
import time
import Constant
from prettytable import PrettyTable

api = dota2api.Initialise(Constant.D2_API_KEY)


def get_match_history(account_id=Constant.STEAM_ID):
    hist = api.get_match_history(account_id=account_id)
    matches = hist['matches']
    for match in matches:
        match_id = match['match_id']
        start_time = time.strftime(Constant.time_format, time.localtime(match['start_time']))
        lobby_type = Constant.lobby_type[match['lobby_type']]
        players = match['players']
        p = [match_id, start_time, lobby_type]
        for player in players:
            hero_id = player['hero_id']
            account_id = player['account_id']
            team = player['player_slot']
            p.append(Constant.heroes_list[hero_id])
        while len(p) < 13:
            p.append('')
    return matches


def get_match_details(match_id):
    details = api.get_match_details(match_id)
    radiant_win = details['radiant_win']
    duration = details['duration']
    start_time = details['start_time']
    tower_status_radiant = details['tower_status_radiant']
    tower_status_dire = details['tower_status_dire']
    barracks_status_radiant = details['barracks_status_radiant']
    barracks_status_dire = details['barracks_status_radiant']
    # cluster_name = details['cluster_name']
    print radiant_win, duration, start_time, tower_status_dire, tower_status_radiant, barracks_status_dire, \
        barracks_status_radiant


if __name__ == '__main__':
    x = PrettyTable(Constant.row_name)
    matches = get_match_history(Constant.STEAM_ID)
    for match in matches:
        match_id = match['match_id']
        get_match_details(match_id)

