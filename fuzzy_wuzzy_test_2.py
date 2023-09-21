#pip install fuzzywuzzy
#pip install python-Levenshtein

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd
import itertools

names_list = ['3M Technical Ceramics Zweigniederlassung der 3M De GmbH',
'A PLAS GEN OTO MAM SAN TIC LTD STI','A RAYMOND GMBH & CO KG','A. KAYSER AUTOMOTIVE SYSTEMS GMBH',
'A.KAYSER AUTOMOTIVE IBERICA SL AUTOMOCION S.COM','ADHEX TECH TAPES SL',
'Adient Seating (UK) Ltd ( BPXSA)','AKWEL AUTOMOTIVE PORTUGAL, LTDA',
'AKWEL RUDNIK CZECH REPUBLIC a.s.','AKWEL RUDNIK CZECH REPUBLIC, a. s.',
'AKWEL Vannes France SAS','AKWEL, S.A',
'Aleaciones de Metales Sinterizados','ALPHA Vehicle Security Solutions Czech s.r.o.',
'ALUDEC IBERICA S.A.','ALUDEC S.A.','Andreas Schmid Kontrakt-Logistik GmbH & Co. KG',
'ANTOLIN SILESIA SP ZOO','A-PLAS GENEL OTOMOTIV MAMULLERI SAN VE TIC LTD STI','APTIV CONTRACT SERVICES- ocean']

results_list_score = []
results_list_name = []
results_list_query = []
output_list_score = []
output_list_name = []
output_list_query = []
for name2 in names_list:
    query = name2
    for x in names_list:
        output = fuzz.ratio(query, x)
        output_list_score.append(output)
        output_list_name.append(x)
        output_list_query.append(query)
results_list_score.append(output_list_score)
results_list_name.append(output_list_name)
results_list_query.append(output_list_query)
results_list_score = list(itertools.chain(*results_list_score))
results_list_name = list(itertools.chain(*results_list_name))
results_list_query = list(itertools.chain(*results_list_query))

df = pd.DataFrame({'score': results_list_score, 'name': results_list_name, 'query': results_list_query})
#df.to_csv('out.csv')