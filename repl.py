### Standart Python notebook imports

import itertools
import io
import os

import numpy as np
import pandas as pd
from modules.regulars import regulars
from modules.labeler import label

label(path='./data/small/', path_labels='./data/labels/', skip_exist=True)
