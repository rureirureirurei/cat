### Standart Python notebook imports

import itertools
import io
import os

import numpy as np
import pandas as pd
from tqdm.auto import tqdm
from helpers.regulars import regulars


def _sources(path):
  return [i for i in os.listdir(path) if i.endswith(".csv")]

def _file_exists(pathname):
    return os.path.exists(pathname) 

def _write_to_logs(source, file='logs'):
    f = open("logs", "a")
    f.write(source + "\n")
    f.close()

def _print_info(source, columns):
    print('filename: ' + source + ' cols: ' + str(columns.shape[0]))

def _print_sample(seq, n=5):
    print(seq[:n])

def _save_labels(labels, namepath):
    pd.DataFrame(labels).to_csv(namepath, index=False, header=False)


def label(path='./data/', path_labels='./labels/', skip_exist=False):
    for source in tqdm(_sources(path)):
        print( _file_exists(path_labels + source))
        print(path_labels + source)
        if skip_exist and _file_exists(path_labels + source):
            continue

        try: data = pd.read_csv(path + source, encoding='utf-8')
        except:
            _write_to_logs(source)
            continue

        labels = []
        columns = data.columns

        for column in columns:
            batch = data[column][:100].to_numpy()
            tags = regulars(batch, column)

            if tags:
                labels.append(tags)
                continue


            _print_info(source, columns)
            _print_sample(data[column], n=10)

            label = input()
  
            if label == '':
                labels.append('?')
                continue

            if label == '???':
                labels = labels + ['?'] * (data.columns.shape[0] - len(labels))
                break

            labels.append(label)
        _save_labels(labels, path_labels + source)
        print("saved"+source)
