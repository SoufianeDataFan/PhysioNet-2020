import pandas as pd
import os

unscored_labels = pd.read_csv('https://raw.githubusercontent.com/physionetchallenges/evaluation-2020/master/dx_mapping_unscored.csv')
scored_labels = pd.read_csv('https://raw.githubusercontent.com/physionetchallenges/evaluation-2020/master/dx_mapping_scored.csv')
# scored_labels.head()
# fix similar labels
mask_simil = lambda x:[int(val) for i, val in enumerate(x.split()) if i in [2,4] ]
ls_lab_simil = scored_labels['Notes'][~scored_labels['Notes'].isnull()].apply(mask_simil)

ls_lab_simil = [list(x) for x in set(tuple(x) for x in ls_lab_simil.values)]

for lab in ls_lab_simil:
    lab_1 = scored_labels[scored_labels['SNOMED CT Code'].isin([lab[0]])].Abbreviation.values[0]
    lab_2 = scored_labels[scored_labels['SNOMED CT Code'].isin([lab[1]])].Abbreviation.values[0]
    ls_temp = scored_labels[scored_labels['SNOMED CT Code'].isin(lab)].Abbreviation.values
    scored_labels.Abbreviation.loc[scored_labels['SNOMED CT Code'].isin(lab)] = ['_'.join([lab_1,lab_2])]*len(ls_temp)

del scored_labels['Notes']
# scored_labels.head(28)

unscored_labels['scored']=0
scored_labels['scored']=1
all_dx = pd.concat([scored_labels, unscored_labels], axis=0)
# all_dx.to_csv('dx_mapping_curated.csv', index= False)
all_dx.head()
