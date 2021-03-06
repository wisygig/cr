import json
import numpy as np
import os
import pandas as pd
import re
import requests

_stats = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom',
          'charisma']

_mechanics = ['challenge_rating', 'armor_class', 'hit_dice', 'hit_points',
              'condition_immunities', 'damage_immunities',
              'damage_resistances', 'damage_vulnerabilities', 'actions',
              'reactions', 'legendary_actions', 'special_abilities', 'size',
              'speed', 'senses']

_flavor = ['languages', 'subtype', 'type', 'alignment']

_stat_scores = ['strength', 'strength_mod', 'strength_save', 'dexterity',
                'dexterity_mod', 'dexterity_save', 'constitution',
                'constitution_mod', 'constitution_save', 'intelligence',
                'intelligence_mod', 'intelligence_save', 'wisdom',
                'wisdom_mod', 'wisdom_save', 'charisma', 'charisma_mod',
                'charisma_save']

_skills = ['acrobatics', 'arcana', 'athletics', 'deception', 'history',
           'insight', 'intimidation', 'investigation', 'medicine', 'nature',
           'perception', 'performance',  'persuasion', 'religion', 'stealth',
           'survival']

_column_order = _mechanics + _flavor + _stat_scores + _skills

_skills_stats = {'acrobatics': 'dexterity',
                 'arcana': 'intelligence',
                 'athletics': 'strength',
                 'deception': 'charisma',
                 'history': 'intelligence',
                 'insight': 'wisdom',
                 'intimidation': 'charisma',
                 'investigation': 'intelligence',
                 'medicine': 'wisdom',
                 'nature': 'intelligence',
                 'perception': 'wisdom',
                 'performance': 'charisma',
                 'persuasion': 'charisma',
                 'religion': 'intelligence',
                 'stealth': 'dexterity',
                 'survival': 'wisdom'}


def get_dfs():
    monsters, ogl = load_monsters()
    monster_df = get_monster_df(monsters)
    return monster_df, action_df


def load_monsters():
    filepath = 'data/5e-SRD-Monsters.json'

    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
    else:
        url = 'https://dl.dropboxusercontent.com/s/iwz112i0bxp2n4a/5e-SRD-Monsters.json'
        response = requests.get(url)
        data = json.loads(response.text)
        with open(filepath, 'w') as f:
            json.dump(data, f)
    monsters = data[:-1]
    ogl = data[-1]
    return monsters, ogl


def replace_nan(df, column, func):
    for x in df.loc[df[column].isnull(), column].index:
        df.at[x, column] = func()


def get_monster_df(monsters):
    df = pd.DataFrame(monsters)
    df = df.set_index(['name'])
    df = fix_saves(df)
    df = fix_skills(df)
    df.challenge_rating = df.challenge_rating.apply(fix_challenge_rating)
    df = df.reindex(columns=_column_order)
    columns_with_nan = df.columns[df.isnull().apply(any, axis=0)]
    for column in columns_with_nan:
        replace_nan(df, column, list)
    return df

def fix_saves(df):
    mods = [stat + '_mod' for stat in _stats]
    saves = [stat + '_save' for stat in _stats]
    for stat, mod in zip(_stats, mods):
        df[mod] = np.floor((df[stat] - 10) / 2)
    for mod, save in zip(mods, saves):
        df[save].fillna(df[mod], inplace=True)
    return df


def fix_skills(df):
    for skill, stat in _skills_stats.items():
        df[skill].fillna(df[stat+'_mod'], inplace=True)
    return df


def fix_challenge_rating(cr):
    pattern = re.compile(r'(?P<p>\d)/(?P<q>\d)$|(?P<n>\d+)')
    g = re.match(pattern, cr)
    try:
        x = int(g.group('p')) / int(g.group('q'))
    except:
        x = int(g.group('n'))
    return x

