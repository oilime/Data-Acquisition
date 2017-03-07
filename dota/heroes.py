# -*- coding:utf-8 -*-
import dota2api
import cPickle as pickle

D2_API_KEY = '33EC3A24D17811D6EDD422A7D0DA5CB2'
api = dota2api.Initialise(D2_API_KEY)

hero_list = {}
heroes = api.get_heroes()['heroes']
for hero in heroes:
    hero_id = hero['id']
    name = hero['name']
    localized_name = hero['localized_name']
    hero_list[hero_id] = localized_name
with open('heroes.txt', 'w') as f:
    p = pickle.dump(hero_list, f)

