### Input and output types are onedim nparrays

import string
#Standart Python notebook imports

import itertools
import io
import os
import re
import json
from tqdm.auto import tqdm
import numpy as np
import pandas as pd

characters = string.printable

def stats(x):
    return np.array([x.min(), x.max(), x.mean(), x.std()])

def to_str(seq):
    return np.array(list(map(str, seq)))

def length(seq):
    res = list(map(len, seq))
    return stats(np.array(res))

# This function takes two arguments:
#
#   seq - sequence of elements being analized
#   
#   filter_func - function that takes a charater
#     and returns either 1 or 0 
#   
#   for each element in seq filter_func is applied to 
#   each symbol and then a sum is divided by element's length
#

def filtered_character(seq, filter_func):
    def len_(s):
        if len(s) == 0: 
            return 1 
        else: 
            return len(s)
    res = list(map(lambda s: sum([filter_func(c) for c in s]) / len_(s), seq))
    return stats(np.array(res))

def numeric(seq):
    res = filtered_character(seq, lambda c: c.isnumeric())
    return stats(np.array(res))

def alphabetic(seq):
    res = filtered_character(seq, lambda c: c.isalpha())
    return stats(np.array(res))

def uppercase(seq):
    res = filtered_character(seq, lambda c: ord(c) >= ord('A') and ord(c) <= ord('Z'))
    return stats(np.array(res))

def each_character(seq):
    res = np.array([])
    for ch in characters:
        res = np.append(filtered_character(seq, lambda c: c == ch), res)
    return res
    
def uniques(seq: np.ndarray) -> np.ndarray:
    return np.array([len(np.unique(seq)) / len(seq)])
    
def each_character_on_prefix(seq, pref_len=10):
    res = np.array([])
    for i in range(pref_len):
        for ch in characters:
            occs = 0
            for s in seq:
                if len(s) > i and s[i] == ch:
                    occs += 1
            res = np.append(res, np.array([occs / seq.shape[0]]))
    return res
        
def empties(seq):
    return np.array([(sum(list(map(lambda s: len(s) == 0, seq))) / len(seq))])
    
def features(seq):
    detectors = [
        length,
        numeric,
        alphabetic,
        uppercase,
        each_character,
        uniques,
        each_character_on_prefix,
    ]
    
    features = np.array([])
    for detector in detectors:
        features = np.append(detector(to_str(seq)), features)
    return features
    
