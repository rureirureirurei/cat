### Standart Python notebook imports

import itertools
import io
import os

import numpy as np
import pandas as pd
from tqdm.auto import tqdm
from helpers.regulars import regulars

def _sources(path):
    result = [i for i in os.listdir(path) if i.endswith(".csv")]
    return result

def _is_csv(s):
    if not isinstance(s, str):
        return False
    if len(s) < 5:    # ?.csv
        return False
    if s[-4:] != '.csv':
        return False
    return True

def label(path='./data/', path_labeled='./labels/'):

    if (os.getcwd().split('/')[-1] == 'repl'):
        path = '.' + path
        path_labeled = '.' + path_labeled
        
    for source in tqdm(_sources(path)):
        if not _is_csv(source):
            continue

        if os.path.exists(path_labeled + source):
            print("SKIP\nfound labels file" + source)
            continue

        try:
            data = pd.read_csv(path + source, encoding='utf-8')
        except:
            f = open("logs", "a")
            f.write(source + "\n")
            f.close()
            continue
        labels = []

        print('\n\n'+source+'\n'+str(data.columns.shape[0])+'\n')

        for column in data.columns:

            batch = data[column][:100].to_numpy()
            tags = regulars(batch, column)

            print(data[column][:5])
            if tags:
                print("\nSKIP\ndetected types " + tags + "\n")
                labels.append(tags)
                continue

            label = input()

            if label == '???':
                labels = labels + ['?'] * (data.columns.shape[0] - len(labels))
                break

            labels.append(label)

        print("Labels: ", str(labels) + '\n\n')
        namepath = path_labeled + source
        pd.DataFrame(labels).to_csv(namepath, index=False, header=False)
        print("Saved labels ✅\n")

    
