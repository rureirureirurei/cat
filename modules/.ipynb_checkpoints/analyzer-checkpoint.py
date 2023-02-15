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

def stats(x, keyname):
    return {
		keyname+'_min': x.min(),
		keyname+'_max': x.max(), 
		keyname+'_mean': x.mean(),
		keyname+'_std': x.std()
	}

def to_str(seq):
    return np.array(list(map(str, seq)))

def length(seq):
    res = list(map(len, seq))
    return stats(np.array(res), 'length')

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

def filtered_character(seq, filter_func, keyname):
    def len_(s):
        if len(s) == 0: 
            return 1 
        else: 
            return len(s)
    res = list(map(lambda s: sum([filter_func(c) for c in s]) / len_(s), seq))
    return stats(np.array(res), keyname)

def numeric(seq):
    return filtered_character(seq, lambda c: c.isnumeric(), 'numeric')

def alphabetic(seq):
    return filtered_character(seq, lambda c: c.isalpha(), 'alphabetic')

def uppercase(seq):
    return filtered_character(seq, lambda c: ord(c) >= ord('A') and ord(c) <= ord('Z'), 'uppercase')


def each_character(seq):
    res = {}
    for ch in characters:
        res.update(filtered_character(seq, lambda c: c == ch, ch+'_occurrence'))
    return res

    
def uniques(seq: np.ndarray) -> np.ndarray:
    return {"uniqueness": len(np.unique(seq)) / len(seq)}
    
def each_character_on_prefix(seq, pref_len=10):
    res = {}
    for i in range(pref_len):
        for ch in characters:
            occs = 0
            for s in seq:
                if len(s) > i and s[i] == ch:
                    occs += 1
            key = f"{ch}_occurence_on_position_{i}"
            res[key] = occs / seq.shape[0]
    return res
        
def empties(seq):
    return {"empties": (sum(list(map(lambda s: len(s) == 0, seq))) / len(seq))}
    
def extract_features(seq):
    detectors = [
        length,
        numeric,
        alphabetic,
        uppercase,
        each_character,
        uniques,
        each_character_on_prefix,
    ]
    
    features = {}
    for detector in detectors:
        features.update(detector(to_str(seq)))
	
    return np.array(list(features.values())), np.array(list(features.keys()))
    
