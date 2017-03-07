# -*- coding:utf-8 -*-
import dota2api
import cPickle as pickle

D2_API_KEY = '33EC3A24D17811D6EDD422A7D0DA5CB2'
api = dota2api.Initialise(D2_API_KEY)

item_list = {}
items = api.get_game_items()['items']
for item in items:
    item_id = item['id']
    name = item['name']
    price = item['cost']
    localized_name = item['localized_name']
    item_list[item_id] = localized_name
with open('items.txt', 'w') as f:
    p = pickle.dump(item_list, f)
