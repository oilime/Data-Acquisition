# -*- coding:utf-8 -*-
import dota2api
import time
import cPickle as pickle
import Constant
from prettytable import PrettyTable


x = PrettyTable(Constant.row_name)

api = dota2api.Initialise(Constant.D2_API_KEY)
hist = api.get_match_history(account_id=Constant.STEAM_ID)
matches = hist['matches']

with open('heroes.txt', 'r') as f:
    heroes_list = pickle.load(f)

for match in matches:
    match_id = match['match_id']
    start_time = time.strftime(Constant.time_format, time.localtime(match['start_time']))
    lobby_type = Constant.game_type[match['lobby_type']]
    players = match['players']
    p = [match_id, start_time, lobby_type]
    for player in players:
        hero_id = player['hero_id']
        account_id = player['account_id']
        team = player['player_slot']
        p.append(heroes_list[hero_id])
    while len(p) < 13:
        p.append('')
    x.add_row(p)
print x.get_string()
