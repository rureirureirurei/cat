# cat(egorical data analysis).

Raw tabular data semantical mapping using statistical features. 

Check the presentation and `overview.ipynb` notebook for more details

# Results 
Two best performing models - random forest and nn both gave accuracy ~0.84. The random classifier would give accuracy of ~0.02

Here is an example of model predictions:
```
Values    :  'Central Missouri', 'unattached', 'unattached', 'Kansas Sta . . .
Predicted :  {'affiliation': 0.3, 'country': 0.2, 'category': 0.2}
Truth     :  affiliation 

Values    :  95, 100, 95, 89, 84, 91, 88, 94, 75, 78, 90, 84, 90, 76, 93 . . .
Predicted :  {'rank': 0.3, 'plays': 0.3, 'education': 0.2}
Truth     :  weight 

Values    :  'Katie Crews', 'Christian Hiraldo', 'Alex Estrada', 'Fredy  . . .
Predicted :  {'jockey': 0.9, 'owner': 0.1, 'year': 0.0}
Truth     :  jockey 

Values    :  'Christian', 'Non-Christian', 'Unreported', 'Jewish', 'Athe . . .
Predicted :  {'type': 0.2, 'language': 0.1, 'name': 0.1}
Truth     :  religion 

Values    :  'AAF-McQuay Canada Inc.', 'AAF-McQuay Canada Inc.', 'Abilit . . .
Predicted :  {'company': 0.3, 'album': 0.2, 'description': 0.1}
Truth     :  company
```

Feel free to play with the model in the `overview.ipynb` notebook!

# Statistical features 
We extract min, mean, max, std statistical features from each sequence of values:
  - length
  - percentage of alphabetic characters
  - percentage of numeric characters
  - percentage of uppercase characters
  - each specific character on a fixed position occurence rate
  - uniqueness

Check the ```./modules/FeaturesExtractor.py``` for more details.
  

# Dataset used
Here I used dataset from this [research](https://arxiv.org/pdf/1905.10688.pdf).

Although there was initially an attempt to create the data from scratch, it ultimately failed due to the inability of humans to properly 

# Data structure
```
cat/
|
├─── modules/
|    |
│    ├─ regulars.py      # REGEX-based data typifiers
|    |
│    ├─ analyzer.py      # Statistical features
|    |
│    ├─ labeler.py       # Script for manual data labeling
|    |
│    ├─ cats.py          # Dictionary with all possible semantic types
|    |
│    ├─ formatter.ipynb  # Helper functions for parsing raw-raw data
|
|
├─── cached/             # Cached variables values (exracted features, model weights, etc)
|
├─── data/
|    |
|    ├─ unused           # 300+ GB of mostly unlabeled data
|    |
|    ├─ parquet          # data currently used for training and validating model
|    
|
├─ .gitignore
|
├─ overview.ipynb        # Notebook that demonstrates the project's core from A to Z
|
├─ README.md
|
├─ LABELING.md           # Guide for those who helped me with data labeling :D
```

Please note that the `cached` and `data` are not in the repository due to their large size.
identify the categories. The ```labeler``` can be used for labeling other, more human-like data though.

The project was in some degree inspired by this [research](https://arxiv.org/pdf/1905.10688.pdf).
