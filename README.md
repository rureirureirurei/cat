# cat(egorical data analysis).

Raw tabular data semantical mapping using statistical features. Check the presentation and `overview.ipynb` notebook for more details

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

# Statistical features 
We extract min, mean, max, std statistical features from each sequence of values:
  - length
  - percentage of alphabetic values
  - percentage of numeric values
  - etc (you can check it in the ```./modules/FeaturesExtractor.py```)
  

# Dataset used
Here I used dataset from this [research](https://arxiv.org/pdf/1905.10688.pdf).

Although there was initially an attempt to create the data from scratch, it ultimately failed due to the inability of humans to properly identify the categories. The ```labeler``` can be used for labeling other, more human-like data though.

The project was in some degree inspired by this [research](https://arxiv.org/pdf/1905.10688.pdf).
