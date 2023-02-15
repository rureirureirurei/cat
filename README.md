# cat(egorical data analysis).

Raw tabular data semantical mapping using statistical features.

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
We extract following statistical features from each sequence of values:
  - min, mean, max, standart deviation of length
  - min, mean, max, standart deviation of fractions of alphabetic values
  - min, mean, max, standart deviation of fractions of numeric values
  

# Dataset used
TODO

The project was in some degree inspired by this [research](https://arxiv.org/pdf/1905.10688.pdf).
