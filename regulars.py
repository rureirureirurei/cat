import re

def regulars(batch, header):
    header = header.lower()
    
    for reg in _regulars:
        tags = reg[1]
        
        # Check header
        for hdr in reg[0]['header']:
            if hdr in header:
                return tags
        
        # Check regexes, count average
        res = 0
        for s in batch:
            s = str(s)
            if len(str(s)) > 100:
                continue
            match = False
            for regx in reg[0]['regex']:
                if re.match(regx, s):
                    match = True
            res += match
            
        # TODO - make this configurable
        if res / batch.shape[0] > 0.8:
            return tags
        
#TODO make it so each entry is a dict with 3 keys, not tuple
_regulars = [
    ({'header': ['id'], 
        'regex': [      
        ]
    }, 'id'),
    
    ({'header': ['dt', 'date'],
        'regex': [
            '\d{4}-\d{2}-\d{2}([\+|\-]\d{2}:\d{2})?', 
            '(0?[1-9]|1[0-2])[\/](0?[1-9]|[12]\d|3[01])[\/]\d{1,4}',
            '(0?[1-9]|1[0-2])[-](0?[1-9]|[12]\d|3[01])[-]\d{1,4}',
            '(0[1-9]|1[0-2])[\/](0[1-9]|[12]\d|3[01])[\/]\d{1,4}',
            '(0[1-9]|1[0-2])[-](0[1-9]|[12]\d|3[01])[-]\d{1,4}',
            '(0?[1-9]|[12]\d|3[01])[\/](0?[1-9]|1[0-2])[\/]\d{1,4}',
            '(0?[1-9]|[12]\d|3[01])[-](0?[1-9]|1[0-2])[-]\d{1,4}',
            '(0[1-9]|[12]\d|3[01])[\/](0[1-9]|1[0-2])[\/]\d{1,4}',
            '(0[1-9]|[12]\d|3[01])[-](0[1-9]|1[0-2])[-]\d{1,4}' 
        ]
    }, 'date, temporal'),
    
    ({'header': ['datetime'],
        'regex': [
            '^(?=\d)(?:(?:(?:(?:(?:0?[13578]|1[02])(\/|-|\.)31)\1|(?:(?:0?[1,3-9]|1[0-2])(\/|-|\.)(?:29|30)\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})|(?:0?2(\/|-|\.)29\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))|(?:(?:0?[1-9])|(?:1[0-2]))(\/|-|\.)(?:0?[1-9]|1\d|2[0-8])\4(?:(?:1[6-9]|[2-9]\d)?\d{2}))($|\ (?=\d)))?(((0?[1-9]|1[012])(:[0-5]\d){0,2}(\ [AP]M))|([01]\d|2[0-3])(:[0-5]\d){1,2})?$',
        ]
    }, 'datetime, temporal'),
    
    ({'header': ['time'],
        'regex': [
            '(0?[1-9]|1[0-2]):[0-5][0-9]',
            '((1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm]))',
            '(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]',
            '([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]',
            '(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)'
        ]
    }, 'time, temporal'),
    
    ({'header': ['description'],
        'regex': []
    }, 'description'),
    
    ({'header': ['gender'],
        'regex': []
    }, 'gender, personal'),
    
    
    ({'header': ['race'],
        'regex': []
    }, 'race, personal'),
    
    ({'header': ['diag', 'diagnosis'],
        'regex': [
            '(?i)[a-z]\\d{2}(\\.?[a-z0-9]{1,4})?'
        ]
    }, 'diagnosis, healthcare'),
    
    
    ({'header': ['height'],
        'regex': []
    }, 'healthcare, numeric, weight'),
    
    
    ({'header': ['weight'],
        'regex': [
        ]
    }, 'healthcare, numeric, weight'),
    
    
    ({'header': ['country', 'cntry'],
        'regex': [
        ]
    }, 'geo, country'),
    
    
    ({'header': ['email', 'mail'],
        'regex': [
            """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""",
            "/@/"
        ]
    }, 'contact, email'),
    
    ({'header': ['latitude', 'lat'],
        'regex': [
            """^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$"""
        ]
    }, 'geo, float, latitude'),
       
    ({'header': ['longitude'],
        'regex': [
            """^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$"""
        ]
    }, 'geo, float, longitude'),
       
    ({'header': ['phone'],
        'regex': [
            """\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})"""
        ]
    }, 'contact, phone-number')
    
]