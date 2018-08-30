# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:27:20 2018

@author: Rebecca
"""

def binpack(articles,bin_cap):
    """
    Intuitive Approach
    """
    
    my_team_number_or_name = "rswood"
    bin_contents = []  # list in sublist between bins
    
    item = articles.keys()
    vol = []
    for i in item:
        vol.append(articles.get(i))
    
    vol, item = zip(*sorted(zip(vol, item), reverse = True))

    for i in range(len(vol)):
        bin_contents.append([])
    
    used = []
    
    for j in range(len(bin_contents)):
        total = 0.0
        for i in range(len(vol)):
            if total + vol[i] <= bin_cap and item[i] not in used:
                bin_contents[j].append(item[i])
                used.append(item[i])
                total += vol[i]
    
    for z in range(len(bin_contents)-1, -1, -1):
        if bin_contents[z] == []:
            bin_contents.pop(z)

    return my_team_number_or_name, bin_contents