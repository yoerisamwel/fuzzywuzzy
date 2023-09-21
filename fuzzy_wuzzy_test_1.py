#pip install fuzzywuzzy
#pip install python-Levenshtein

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

data = {'Name':['To1mDSV', 'DSV1nick', 'DSVkri4sh', 'ja2ckDSV','TDSVo4m', 'nick3DSV', 'kD3SVr3ish', 'jacDS3Vk',
                'T2omDSV', 'DSVni2ck', 'DSVkr2ish', 'ja4ckDSV','TDSVom', 'nick2DSV', 'kDSV3rish', 'ja3cDS3Vk',
                'TomD3SV', 'DSV2nick', 'DSVkr3ish', 'j3ackDSV','TDSVo4m', 'nickD2SV', 'kDSVr3ish', 'ja3c3DSVk',
                'Tom4DSV', 'DSVni3ck', 'DSVkri4sh', 'jack2DSV','TDSVo4m', 'nic2kDSV', 'kD3SVri3sh', 'jacD3SVk'],

        'Age':[20, 21, 19, 18,20, 21, 19, 18,20, 21, 19, 18,20, 21, 19, 18,20, 21, 19, 18,20, 21, 19, 18,
               20, 21, 19, 18,20, 21, 19, 18]}
df = pd.DataFrame(data)
names = []
names = [name for name in df['Name']]

query = 'DSV'

# Get a list of matches ordered by score, default limit to 5
output = process.extract(query, names)
print(output)