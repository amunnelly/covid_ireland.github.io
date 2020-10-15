#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:56:22 2020

@author: amunnelly
"""

import pandas as pd
import json

counties = pd.read_csv('counties.csv', index_col=0)
colors = pd.read_csv('colors.csv')

holder = []

palette = {}
for a, b in colors.iterrows():
    target = b['key']
    temp = (b['color'], b['dash'])
    if target in palette:
        palette[target].append(temp)
    else:
        palette[target] = []
        palette[target].append(temp)
        
for a, b in counties.iterrows():
    holder.append([a,
                   palette[b['firstColor']][0][0],
                   palette[b['firstColor']][0][1]])

    palette[b['firstColor']] = palette[b['firstColor']][1:]

df = pd.DataFrame(holder, columns=["CountyName", "color", "dash"])
df.index = df['CountyName']
del(df['CountyName'])

colors = df.to_dict('index')
with open('covid_ireland/colors.json', 'w') as f:
    json.dump(colors, f)