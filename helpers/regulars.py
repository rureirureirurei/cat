import re
import numpy as np

# Some massive refactoring needed ...
# Shitty af 

def _integer(seq):
    res = np.array(list(map(lambda x: str(x).isnumeric(), seq))).mean()
    if res > threshold: 
        return ['numeric', 'integer'] 
    return []

def _float(seq):
    def is_float(x):
        x = str(x)
        return x.count('.') == 1 and x.replace('.','').isnumeric()
    res = np.array(list(map(is_float, seq))).mean()
    if res > threshold: 
        return ['numeric', 'float'] 
    return []

def _fixed(seq):
    return []

def _money(seq):
    return []

def _percentage(seq):
    return []


    
threshold = 0.9
max_len = 100
    
detectors = [
    _float, 
    _integer,
#    _fixed, 
#    _money,
#    _percentage
]

def set_to_csv(st):
    if len(st) == 0:
        return None
    return str(st)[1: -1]

def regulars(batch, header):
    tags = set()
     
    header = header.lower()
    
    #Special cases
    for detector in detectors:
        for t in detector(batch): tags.add(t)
  
    for reg in _regulars:
        # Check header
        for hdr in reg['header']:
            if hdr in header:
                for t in reg['tags']: tags.add(t)
        
        # Check regexes, count average
        res = 0
        for s in batch:
            s = str(s)
            if len(str(s)) > max_len:
                continue
            match = False
            for regx in reg['regex']:
                if re.match(regx, s):
                    match = True
            res += match
            
        if res / batch.shape[0] > threshold:
            for t in reg['tags']: tags.add(t)
    return set_to_csv(tags)
        
#TODO make it so each entry is a dict with 3 keys, not tuple
_regulars = [
    {
        'header' : ['id'], 
        'tags'   : ['id'],
        'regex'  : []
    },
    {    
        'header' : ['dt', 'date'],
        'tags'   : ['date, temporal'],
        'regex'  : [
            '^\d{4}-\d{2}-\d{2}([\+|\-]\d{2}:\d{2})?', 
            '^(0?[1-9]|1[0-2])[\/](0?[1-9]|[12]\d|3[01])[\/]\d{1,4}$',
            '^(0?[1-9]|1[0-2])[-](0?[1-9]|[12]\d|3[01])[-]\d{1,4}$',
            '^(0[1-9]|1[0-2])[\/](0[1-9]|[12]\d|3[01])[\/]\d{1,4}$',
            '^(0[1-9]|1[0-2])[-](0[1-9]|[12]\d|3[01])[-]\d{1,4}$',
            '^(0?[1-9]|[12]\d|3[01])[\/](0?[1-9]|1[0-2])[\/]\d{1,4}$',
            '^(0?[1-9]|[12]\d|3[01])[-](0?[1-9]|1[0-2])[-]\d{1,4}$',
            '^(0[1-9]|[12]\d|3[01])[\/](0[1-9]|1[0-2])[\/]\d{1,4}$',
            '^(0[1-9]|[12]\d|3[01])[-](0[1-9]|1[0-2])[-]\d{1,4}$' 
        ]
    },
    {
        'header' : ['datetime'],
        'tags'   : ['datetime, temporal'],
        'regex'  : [
            '^(?=\d)(?:(?:(?:(?:(?:0?[13578]|1[02])(\/|-|\.)31)\1|(?:(?:0?[1,3-9]|1[0-2])(\/|-|\.)(?:29|30)\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})|(?:0?2(\/|-|\.)29\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))|(?:(?:0?[1-9])|(?:1[0-2]))(\/|-|\.)(?:0?[1-9]|1\d|2[0-8])\4(?:(?:1[6-9]|[2-9]\d)?\d{2}))($|\ (?=\d)))?(((0?[1-9]|1[012])(:[0-5]\d){0,2}(\ [AP]M))|([01]\d|2[0-3])(:[0-5]\d){1,2})?$',
        ]
    },
    {
        'header' : ['time'],
        'tags'   : ['time, temporal'],
        'regex'  : [
            '^(0?[1-9]|1[0-2]):[0-5][0-9]$',
            '^((1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm]))$',
            '^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$',
            '^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$',
            '^(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$'
        ]
    }, 
    
    {
        'header' : ['description'],
        'tags'   : ['description'],
        'regex'  : []
    },
    
    {
        'header' : ['gender'],
        'tags'   : ['gender, personal'],
        'regex'  : []
    },
    
    
    {
        'header' : ['race'],
        'tags'   : ['race', 'personal'],
        'regex'  : []
    },
    
    {
        'header' : ['diag', 'diagnosis'],
        'tags'   : ['diagnosis, healthcare'],
        'regex'  : [
            '^(?i)[a-z]\\d{2}(\\.?[a-z0-9]{1,4})?$'
        ]
    },
    
    {
        'header' : ['height'],
        'tags'   : ['healthcare, numeric, weight'],
        'regex'  : []
    }, 
    
    {
        'header' : ['weight'],
        'tags'   : ['healthcare, numeric, weight'],
        'regex'  : []
    },
    
    {
        'header' : ['country', 'cntry'],
        'tags'   : ['geo, country'],
        'regex'  : []
    },
    
    
    {
        'header' : ['email', 'mail'],
        'tags'   : ['contact, email'],
        'regex'  : [
            """^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$""",
            "/@/"
        ]
    },
    
    {
        'header' : ['latitude', 'lat'],
        'tags'   : ['geo, float, latitude'],
        'regex'  : [
            """^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$"""
        ]
    },
       
    {
        'header' : ['longitude'],
        'tags'   : ['geo, float, longitude'],
        'regex'  : [
            """^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$"""
        ]
    }, 
       
    {
        'header' : ['phone'],
        'tags'   : ['contact, phone-number'],
        'regex'  : [
            """^\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})$"""
        ]
    }
]
