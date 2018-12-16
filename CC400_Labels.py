#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:03:28 2018
@author: xinyang
This program is to find out the top five correlatd and anti-correlated ROIs of ASD and TD
"""

from nilearn.datasets import fetch_abide_pcp
import pandas as pd
import numpy as np

labels = pd.read_csv('CC400_ROI_labels.csv')
atlas_filename = 'cc400_roi_atlas.nii.gz'

abide = fetch_abide_pcp(derivatives = ['rois_cc400'], pipeline = 'cpac', quality_checked = False)
y = abide.phenotypic['DX_GROUP']
names = ['DX_GROUP','rois_cc400']
data = pd.DataFrame([y,abide.rois_cc400]).transpose()
data.columns = names

ASD =  data[data['DX_GROUP']==1]['rois_cc400'] #505
TD = data[data['DX_GROUP']==2]['rois_cc400'] #530

##############################################################################
# Compute and display a correlation matrix
# -----------------------------------------
# Plot the correlation matrix
from nilearn import plotting
from nilearn.connectome import ConnectivityMeasure
correlation_measure = ConnectivityMeasure(kind='correlation')
correlation_matrix_asd = correlation_measure.fit_transform(ASD)
correlation_matrix_asd_mean =correlation_measure.mean_

# Make a large figure
# Mask the main diagonal for visualization:
np.fill_diagonal(correlation_measure.mean_, 0)
# The labels we have start with the background (0), hence we skip the
# first label
# matrices are ordered for block-like representation
plotting.plot_matrix(correlation_measure.mean_, figure=(10,5),
                     vmax=0.8, vmin=-0.8, reorder=False)


##############################################################################
correlation_measure = ConnectivityMeasure(kind='correlation')
correlation_matrix_td = correlation_measure.fit_transform(TD)

correlation_matrix_td_mean = correlation_measure.mean_
# Make a large figure
# Mask the main diagonal for visualization:
np.fill_diagonal(correlation_measure.mean_, 0)
# The labels we have start with the background (0), hence we skip the
# first label
# matrices are ordered for block-like representation

plotting.plot_matrix(correlation_measure.mean_, figure=(10,5),
                     vmax=0.8, vmin=-0.8, reorder=False)

##############################################################################



##############################################################################
#ASD top 5 correlation and anti-correlation
##############################################################################

correlation_matrix_asd_mean[correlation_matrix_asd_mean==1]=0
correlation_matrix_asd_mean.max()
np.where(correlation_matrix_asd_mean == correlation_matrix_asd_mean.max())

#1.correlation
#[118, 159],[159, 118] 0.7369703736448466
correlation_matrix_asd_mean[118][159]
labels.iloc[118]
labels.iloc[159]

'''
labels.iloc[118]
Out[73]: 
ROI number                                                          122
 volume                                                             162
 center of mass                                        (-7.2;-77.3;7.7)
Dosenbach                        ["None": 0.88]["post occipital": 0.12]
AAL                            ["Calcarine_L": 0.59]["Lingual_L": 0.39]
Eickhoff-Zilles       ["Left Lingual Gyrus": 0.51]["Left Calcarine G...
Talairach-Tournoux    ["Left Cuneus": 0.48]["Left Lingual Gyrus": 0.45]
Harvard-Oxford        ["Left Intracalcarine Cortex": 0.62]["Left Lin...
Name: 118, dtype: object


labels.iloc[159]
Out[74]: 
ROI number                                                          163
 volume                                                             170
 center of mass                                        (11.6;-76.7;8.5)
Dosenbach                                                ["None": 0.89]
AAL                            ["Calcarine_R": 0.69]["Lingual_R": 0.25]
Eickhoff-Zilles       ["Right Calcarine Gyrus": 0.51]["Right Lingual...
Talairach-Tournoux    ["Right Cuneus": 0.55]["Right Lingual Gyrus": ...
Harvard-Oxford        ["Right Intracalcarine Cortex": 0.69]["Right L...
Name: 159, dtype: object

'''


#2.correlation
correlation_matrix_asd_mean[118][159] = 0
correlation_matrix_asd_mean[159][118] = 0
np.where(correlation_matrix_asd_mean == correlation_matrix_asd_mean.max())
#[172, 319], [319, 172] 0.6992675563395099
labels.iloc[172]
labels.iloc[319]

'''

labels.iloc[172]
Out[78]: 
ROI number                                                          176
 volume                                                             168
 center of mass                                        (-7.0;-95.3;1.3)
Dosenbach                                                ["None": 0.98]
AAL                      ["Calcarine_L": 0.79]["Occipital_Sup_L": 0.11]
Eickhoff-Zilles                          ["Left Calcarine Gyrus": 0.68]
Talairach-Tournoux    ["Left Lingual Gyrus": 0.50]["Left Cuneus": 0.42]
Harvard-Oxford        ["Left Occipital Pole": 0.70]["Left Intracalca...
Name: 172, dtype: object


labels.iloc[319]
Out[79]: 
ROI number                                                          324
 volume                                                             133
 center of mass                                         (9.7;-91.6;2.9)
Dosenbach                        ["None": 0.86]["post occipital": 0.14]
AAL                          ["Calcarine_R": 0.53]["Calcarine_L": 0.35]
Eickhoff-Zilles       ["Left Calcarine Gyrus": 0.43]["Right Calcarin...
Talairach-Tournoux    ["Right Lingual Gyrus": 0.59]["Right Cuneus": ...
Harvard-Oxford        ["Right Occipital Pole": 0.59]["Right Intracal...
Name: 319, dtype: object

'''



#3.correlation
correlation_matrix_asd_mean[172][319] = 0
correlation_matrix_asd_mean[319][172] = 0
np.where(correlation_matrix_asd_mean == correlation_matrix_asd_mean.max())
# [104, 265], [265, 104] 0.6946156489140184
labels.iloc[104]
labels.iloc[265]

'''

labels.iloc[104]
Out[82]: 
ROI number                                                          108
 volume                                                             126
 center of mass                                       (-7.5;-86.3;29.7)
Dosenbach                                                ["None": 0.97]
AAL                         ["Cuneus_L": 0.83]["Occipital_Sup_L": 0.17]
Eickhoff-Zilles       ["Left Cuneus": 0.71]["Left Superior Occipital...
Talairach-Tournoux                                ["Left Cuneus": 0.99]
Harvard-Oxford        ["Left Cuneal Cortex": 0.59]["Left Occipital P...
Name: 104, dtype: object



labels.iloc[265]
Out[83]: 
ROI number                                                          269
 volume                                                             147
 center of mass                                        (8.2;-83.0;28.1)
Dosenbach                                                ["None": 0.96]
AAL                                ["Cuneus_R": 0.78]["Cuneus_L": 0.18]
Eickhoff-Zilles             ["Right Cuneus": 0.60]["Left Cuneus": 0.39]
Talairach-Tournoux                               ["Right Cuneus": 0.99]
Harvard-Oxford        ["Right Cuneal Cortex": 0.75]["Right Occipital...
Name: 265, dtype: object

'''


#4.correlation
correlation_matrix_asd_mean[104][265] = 0
correlation_matrix_asd_mean[265][104] = 0
np.where(correlation_matrix_asd_mean == correlation_matrix_asd_mean.max())
# [189, 244], [244, 189] 0.6851492618977734
labels.iloc[189]
labels.iloc[244]

'''

labels.iloc[189]
Out[86]: 
ROI number                                                          193
 volume                                                             145
 center of mass                                       (-2.3;-63.7;35.5)
Dosenbach                                                ["None": 0.93]
AAL                          ["Precuneus_L": 0.74]["Precuneus_R": 0.22]
Eickhoff-Zilles       ["Left Precuneus": 0.67]["Right Precuneus": 0....
Talairach-Tournoux    ["Left Precuneus": 0.51]["Right Precuneus": 0.31]
Harvard-Oxford        ["Left Precuneous Cortex": 0.54]["Right Precun...
Name: 189, dtype: object


labels.iloc[244]
Out[87]: 
ROI number                                                          248
 volume                                                             122
 center of mass                                        (7.7;-53.0;34.5)
Dosenbach                             ["None": 0.84]["precuneus": 0.16]
AAL                       ["Precuneus_R": 0.72]["Cingulum_Mid_R": 0.20]
Eickhoff-Zilles       ["Right Precuneus": 0.77]["Right Posterior Cin...
Talairach-Tournoux    ["Right Precuneus": 0.65]["Right Cingulate Gyr...
Harvard-Oxford        ["Right Precuneous Cortex": 0.59]["Right Cingu...
Name: 244, dtype: object

'''


#5.correlation
correlation_matrix_asd_mean[189][244] = 0
correlation_matrix_asd_mean[244][189] = 0
np.where(correlation_matrix_asd_mean == correlation_matrix_asd_mean.max())
# [227, 327], [327, 227] 0.6730819248355813
labels.iloc[227]
labels.iloc[327]

'''

labels.iloc[227]
Out[90]: 
ROI number                                                          231
 volume                                                             198
 center of mass                                     (-24.8;-70.7;-11.7)
Dosenbach                                                ["None": 0.97]
AAL                   ["Fusiform_L": 0.42]["Lingual_L": 0.30]["Cereb...
Eickhoff-Zilles       ["Left Fusiform Gyrus": 0.44]["Left Cerebellum...
Talairach-Tournoux    ["Left Declive": 0.56]["Left Fusiform Gyrus": ...
Harvard-Oxford        ["Left Occipital Fusiform Gyrus": 0.75]["Left ...
Name: 227, dtype: object


labels.iloc[327]
Out[91]: 
ROI number                                                          332
 volume                                                             156
 center of mass                                      (-11.1;-77.5;-9.3)
Dosenbach                                                ["None": 0.94]
AAL                          ["Lingual_L": 0.59]["Cerebelum_6_L": 0.29]
Eickhoff-Zilles       ["Left Lingual Gyrus": 0.46]["Left Cerebellum"...
Talairach-Tournoux    ["Left Declive": 0.45]["Left Lingual Gyrus": 0...
Harvard-Oxford        ["Left Lingual Gyrus": 0.73]["Left Occipital F...
Name: 327, dtype: object

'''


#1. Anti-correlation
correlation_matrix_asd_mean.min()
np.where(correlation_matrix_asd_mean == correlation_matrix_asd_mean.min())
correlation_matrix_asd_mean[185][342]
#[185, 342],[342, 185] -0.055487721528736655
labels.iloc[185]
labels.iloc[342]

'''

labels.iloc[185]
Out[94]: 
ROI number                                                          189
 volume                                                             112
 center of mass                                      (-46.8;-67.4;30.2)
Dosenbach                         ["None": 0.86]["angular gyrus": 0.11]
AAL                                                 ["Angular_L": 0.92]
Eickhoff-Zilles       ["Left Angular Gyrus": 0.62]["Left Middle Temp...
Talairach-Tournoux    ["Left Middle Temporal Gyrus": 0.58]["Left Ang...
Harvard-Oxford        ["Left Lateral Occipital Cortex; superior divi...
Name: 185, dtype: object



labels.iloc[342]
Out[95]: 
ROI number                                                          347
 volume                                                             100
 center of mass                                         (37.7;13.7;7.4)
Dosenbach                                                ["None": 1.00]
AAL                   ["Insula_R": 0.57]["Putamen_R": 0.19]["Frontal...
Eickhoff-Zilles       ["Right Insula Lobe": 0.64]["Right Putamen": 0...
Talairach-Tournoux    ["Right Insula": 0.71]["Right Inferior Frontal...
Harvard-Oxford        ["Right Frontal Operculum Cortex": 0.43]["Righ...
Name: 342, dtype: object


'''


#2. Anti-correlation

correlation_matrix_asd_mean[185][342] = 0
correlation_matrix_asd_mean[342][185] = 0
np.where(correlation_matrix_asd_mean == correlation_matrix_asd_mean.min())
correlation_matrix_asd_mean[342][145]
#[145, 342],[342, 145] -0.044731721774396264
labels.iloc[145]
labels.iloc[342]

'''
labels.iloc[145]
Out[103]: 
ROI number                                                          149
 volume                                                             113
 center of mass                                        (0.7;41.5;-15.5)
Dosenbach                                                ["None": 1.00]
AAL                   ["Rectus_L": 0.37]["Rectus_R": 0.31]["Frontal_...
Eickhoff-Zilles       ["Left Rectal Gyrus": 0.37]["Right Rectal Gyru...
Talairach-Tournoux    ["Left Medial Frontal Gyrus": 0.36]["Right Med...
Harvard-Oxford        ["Right Frontal Medial Cortex": 0.60]["Left Fr...
Name: 145, dtype: object


labels.iloc[342]
Out[104]: 
ROI number                                                          347
 volume                                                             100
 center of mass                                         (37.7;13.7;7.4)
Dosenbach                                                ["None": 1.00]
AAL                   ["Insula_R": 0.57]["Putamen_R": 0.19]["Frontal...
Eickhoff-Zilles       ["Right Insula Lobe": 0.64]["Right Putamen": 0...
Talairach-Tournoux    ["Right Insula": 0.71]["Right Inferior Frontal...
Harvard-Oxford        ["Right Frontal Operculum Cortex": 0.43]["Righ...
Name: 342, dtype: object
'''


#3. Anti-correlation
correlation_matrix_asd_mean[342][145] = 0
correlation_matrix_asd_mean[145][342] = 0
np.where(correlation_matrix_asd_mean == correlation_matrix_asd_mean.min())
#[342, 367] [367, 342] -0.040665119989683515
correlation_matrix_asd_mean[342][367]
labels.iloc[342]
labels.iloc[367]


'''
labels.iloc[342]
Out[109]: 
ROI number                                                          347
 volume                                                             100
 center of mass                                         (37.7;13.7;7.4)
Dosenbach                                                ["None": 1.00]
AAL                   ["Insula_R": 0.57]["Putamen_R": 0.19]["Frontal...
Eickhoff-Zilles       ["Right Insula Lobe": 0.64]["Right Putamen": 0...
Talairach-Tournoux    ["Right Insula": 0.71]["Right Inferior Frontal...
Harvard-Oxford        ["Right Frontal Operculum Cortex": 0.43]["Righ...
Name: 342, dtype: object


labels.iloc[367]
Out[110]: 
ROI number                                                          374
 volume                                                              91
 center of mass                                     (-57.0;-16.0;-20.5)
Dosenbach                                                ["None": 0.97]
AAL                    ["Temporal_Mid_L": 0.76]["Temporal_Inf_L": 0.24]
Eickhoff-Zilles       ["Left Inferior Temporal Gyrus": 0.53]["Left M...
Talairach-Tournoux    ["Left Inferior Temporal Gyrus": 0.58]["Left F...
Harvard-Oxford        ["Left Middle Temporal Gyrus; posterior divisi...
Name: 367, dtype: object
'''



#4. Anti-correlation
correlation_matrix_asd_mean[342][367] = 0
correlation_matrix_asd_mean[367][342] = 0
np.where(correlation_matrix_asd_mean == correlation_matrix_asd_mean.min())
#[244, 342] [342, 244] -0.03729060429844615
correlation_matrix_asd_mean[244][342] 
labels.iloc[244]
labels.iloc[342]

'''

labels.iloc[244]
Out[114]: 
ROI number                                                          248
 volume                                                             122
 center of mass                                        (7.7;-53.0;34.5)
Dosenbach                             ["None": 0.84]["precuneus": 0.16]
AAL                       ["Precuneus_R": 0.72]["Cingulum_Mid_R": 0.20]
Eickhoff-Zilles       ["Right Precuneus": 0.77]["Right Posterior Cin...
Talairach-Tournoux    ["Right Precuneus": 0.65]["Right Cingulate Gyr...
Harvard-Oxford        ["Right Precuneous Cortex": 0.59]["Right Cingu...
Name: 244, dtype: object

labels.iloc[342]
Out[115]: 
ROI number                                                          347
 volume                                                             100
 center of mass                                         (37.7;13.7;7.4)
Dosenbach                                                ["None": 1.00]
AAL                   ["Insula_R": 0.57]["Putamen_R": 0.19]["Frontal...
Eickhoff-Zilles       ["Right Insula Lobe": 0.64]["Right Putamen": 0...
Talairach-Tournoux    ["Right Insula": 0.71]["Right Inferior Frontal...
Harvard-Oxford        ["Right Frontal Operculum Cortex": 0.43]["Righ...
Name: 342, dtype: object

'''


#5. Anti-correlation
correlation_matrix_asd_mean[244][342] = 0
correlation_matrix_asd_mean[342][244] = 0
np.where(correlation_matrix_asd_mean == correlation_matrix_asd_mean.min())
#[189, 342] [342, 189] -0.036017166248113665
correlation_matrix_asd_mean[189][342]

labels.iloc[189]
labels.iloc[342]


'''
labels.iloc[189]
Out[118]: 
ROI number                                                          193
 volume                                                             145
 center of mass                                       (-2.3;-63.7;35.5)
Dosenbach                                                ["None": 0.93]
AAL                          ["Precuneus_L": 0.74]["Precuneus_R": 0.22]
Eickhoff-Zilles       ["Left Precuneus": 0.67]["Right Precuneus": 0....
Talairach-Tournoux    ["Left Precuneus": 0.51]["Right Precuneus": 0.31]
Harvard-Oxford        ["Left Precuneous Cortex": 0.54]["Right Precun...
Name: 189, dtype: object


labels.iloc[342]
Out[119]: 
ROI number                                                          347
 volume                                                             100
 center of mass                                         (37.7;13.7;7.4)
Dosenbach                                                ["None": 1.00]
AAL                   ["Insula_R": 0.57]["Putamen_R": 0.19]["Frontal...
Eickhoff-Zilles       ["Right Insula Lobe": 0.64]["Right Putamen": 0...
Talairach-Tournoux    ["Right Insula": 0.71]["Right Inferior Frontal...
Harvard-Oxford        ["Right Frontal Operculum Cortex": 0.43]["Righ...
Name: 342, dtype: object
'''


##############################################################################
#TD top 5 correlation and anti-correlation
##############################################################################

correlation_matrix_td_mean[correlation_matrix_td_mean==1]=0
correlation_matrix_td_mean.max()
np.where(correlation_matrix_td_mean == correlation_matrix_td_mean.max())

#1.correlation
#[118, 159],[159, 118] 0.745200471939508
correlation_matrix_td_mean[118][159]
labels.iloc[118]
labels.iloc[159]

'''
labels.iloc[118]
Out[73]: 
ROI number                                                          122
 volume                                                             162
 center of mass                                        (-7.2;-77.3;7.7)
Dosenbach                        ["None": 0.88]["post occipital": 0.12]
AAL                            ["Calcarine_L": 0.59]["Lingual_L": 0.39]
Eickhoff-Zilles       ["Left Lingual Gyrus": 0.51]["Left Calcarine G...
Talairach-Tournoux    ["Left Cuneus": 0.48]["Left Lingual Gyrus": 0.45]
Harvard-Oxford        ["Left Intracalcarine Cortex": 0.62]["Left Lin...
Name: 118, dtype: object


labels.iloc[159]
Out[74]: 
ROI number                                                          163
 volume                                                             170
 center of mass                                        (11.6;-76.7;8.5)
Dosenbach                                                ["None": 0.89]
AAL                            ["Calcarine_R": 0.69]["Lingual_R": 0.25]
Eickhoff-Zilles       ["Right Calcarine Gyrus": 0.51]["Right Lingual...
Talairach-Tournoux    ["Right Cuneus": 0.55]["Right Lingual Gyrus": ...
Harvard-Oxford        ["Right Intracalcarine Cortex": 0.69]["Right L...
Name: 159, dtype: object

'''


#2.correlation
correlation_matrix_td_mean[118][159] = 0
correlation_matrix_td_mean[159][118] = 0
np.where(correlation_matrix_td_mean == correlation_matrix_td_mean.max())
#[189, 244], [244, 18] 0.7070816070367121
labels.iloc[189]
labels.iloc[244]

'''

labels.iloc[189]
Out[133]: 
ROI number                                                          193
 volume                                                             145
 center of mass                                       (-2.3;-63.7;35.5)
Dosenbach                                                ["None": 0.93]
AAL                          ["Precuneus_L": 0.74]["Precuneus_R": 0.22]
Eickhoff-Zilles       ["Left Precuneus": 0.67]["Right Precuneus": 0....
Talairach-Tournoux    ["Left Precuneus": 0.51]["Right Precuneus": 0.31]
Harvard-Oxford        ["Left Precuneous Cortex": 0.54]["Right Precun...
Name: 189, dtype: object


labels.iloc[244]
Out[134]: 
ROI number                                                          248
 volume                                                             122
 center of mass                                        (7.7;-53.0;34.5)
Dosenbach                             ["None": 0.84]["precuneus": 0.16]
AAL                       ["Precuneus_R": 0.72]["Cingulum_Mid_R": 0.20]
Eickhoff-Zilles       ["Right Precuneus": 0.77]["Right Posterior Cin...
Talairach-Tournoux    ["Right Precuneus": 0.65]["Right Cingulate Gyr...
Harvard-Oxford        ["Right Precuneous Cortex": 0.59]["Right Cingu...
Name: 244, dtype: object
'''


#3.correlation
correlation_matrix_td_mean[189][244] = 0
correlation_matrix_td_mean[244][189] = 0
np.where(correlation_matrix_td_mean == correlation_matrix_td_mean.max())
# [244, 362], [362, 244] 0.699028873827817
labels.iloc[244]
labels.iloc[362]

'''

labels.iloc[244]
Out[138]: 
ROI number                                                          248
 volume                                                             122
 center of mass                                        (7.7;-53.0;34.5)
Dosenbach                             ["None": 0.84]["precuneus": 0.16]
AAL                       ["Precuneus_R": 0.72]["Cingulum_Mid_R": 0.20]
Eickhoff-Zilles       ["Right Precuneus": 0.77]["Right Posterior Cin...
Talairach-Tournoux    ["Right Precuneus": 0.65]["Right Cingulate Gyr...
Harvard-Oxford        ["Right Precuneous Cortex": 0.59]["Right Cingu...
Name: 244, dtype: object



labels.iloc[362]
Out[139]: 
ROI number                                                          368
 volume                                                             143
 center of mass                                       (-6.6;-49.8;35.5)
Dosenbach                                                ["None": 0.90]
AAL                   ["Precuneus_L": 0.49]["Cingulum_Mid_L": 0.29][...
Eickhoff-Zilles       ["Left Precuneus": 0.62]["Left Posterior Cingu...
Talairach-Tournoux    ["Left Precuneus": 0.56]["Left Cingulate Gyrus...
Harvard-Oxford        ["Left Cingulate Gyrus; posterior division": 0...
Name: 362, dtype: object

'''


#4.correlation
correlation_matrix_td_mean[244][362] = 0
correlation_matrix_td_mean[362][244] = 0
np.where(correlation_matrix_td_mean == correlation_matrix_td_mean.max())
# [172, 319], [319, 172] 0.6977990957796967
labels.iloc[172]
labels.iloc[319]

'''
labels.iloc[172]
Out[151]: 
ROI number                                                          176
 volume                                                             168
 center of mass                                        (-7.0;-95.3;1.3)
Dosenbach                                                ["None": 0.98]
AAL                      ["Calcarine_L": 0.79]["Occipital_Sup_L": 0.11]
Eickhoff-Zilles                          ["Left Calcarine Gyrus": 0.68]
Talairach-Tournoux    ["Left Lingual Gyrus": 0.50]["Left Cuneus": 0.42]
Harvard-Oxford        ["Left Occipital Pole": 0.70]["Left Intracalca...
Name: 172, dtype: object


labels.iloc[319]
Out[152]: 
ROI number                                                          324
 volume                                                             133
 center of mass                                         (9.7;-91.6;2.9)
Dosenbach                        ["None": 0.86]["post occipital": 0.14]
AAL                          ["Calcarine_R": 0.53]["Calcarine_L": 0.35]
Eickhoff-Zilles       ["Left Calcarine Gyrus": 0.43]["Right Calcarin...
Talairach-Tournoux    ["Right Lingual Gyrus": 0.59]["Right Cuneus": ...
Harvard-Oxford        ["Right Occipital Pole": 0.59]["Right Intracal...
Name: 319, dtype: object

'''


#5.correlation
correlation_matrix_td_mean[172][319] = 0
correlation_matrix_td_mean[319][172] = 0
np.where(correlation_matrix_td_mean == correlation_matrix_td_mean.max())
# [104, 265], [265, 104] 0.6967884407740069
labels.iloc[104]
labels.iloc[265]

'''

labels.iloc[104]
Out[156]: 
ROI number                                                          108
 volume                                                             126
 center of mass                                       (-7.5;-86.3;29.7)
Dosenbach                                                ["None": 0.97]
AAL                         ["Cuneus_L": 0.83]["Occipital_Sup_L": 0.17]
Eickhoff-Zilles       ["Left Cuneus": 0.71]["Left Superior Occipital...
Talairach-Tournoux                                ["Left Cuneus": 0.99]
Harvard-Oxford        ["Left Cuneal Cortex": 0.59]["Left Occipital P...
Name: 104, dtype: object


labels.iloc[265]
Out[157]: 
ROI number                                                          269
 volume                                                             147
 center of mass                                        (8.2;-83.0;28.1)
Dosenbach                                                ["None": 0.96]
AAL                                ["Cuneus_R": 0.78]["Cuneus_L": 0.18]
Eickhoff-Zilles             ["Right Cuneus": 0.60]["Left Cuneus": 0.39]
Talairach-Tournoux                               ["Right Cuneus": 0.99]
Harvard-Oxford        ["Right Cuneal Cortex": 0.75]["Right Occipital...
Name: 265, dtype: object

'''



#1. Anti-correlation
correlation_matrix_td_mean.min()
np.where(correlation_matrix_td_mean == correlation_matrix_td_mean.min())
correlation_matrix_td_mean[185][342]
#[185, 342],[342, 185] -0.07837479045403875
labels.iloc[185]
labels.iloc[342]

'''

labels.iloc[185]
Out[94]: 
ROI number                                                          189
 volume                                                             112
 center of mass                                      (-46.8;-67.4;30.2)
Dosenbach                         ["None": 0.86]["angular gyrus": 0.11]
AAL                                                 ["Angular_L": 0.92]
Eickhoff-Zilles       ["Left Angular Gyrus": 0.62]["Left Middle Temp...
Talairach-Tournoux    ["Left Middle Temporal Gyrus": 0.58]["Left Ang...
Harvard-Oxford        ["Left Lateral Occipital Cortex; superior divi...
Name: 185, dtype: object



labels.iloc[342]
Out[95]: 
ROI number                                                          347
 volume                                                             100
 center of mass                                         (37.7;13.7;7.4)
Dosenbach                                                ["None": 1.00]
AAL                   ["Insula_R": 0.57]["Putamen_R": 0.19]["Frontal...
Eickhoff-Zilles       ["Right Insula Lobe": 0.64]["Right Putamen": 0...
Talairach-Tournoux    ["Right Insula": 0.71]["Right Inferior Frontal...
Harvard-Oxford        ["Right Frontal Operculum Cortex": 0.43]["Righ...
Name: 342, dtype: object


'''


#2. Anti-correlation

correlation_matrix_td_mean[185][342] = 0
correlation_matrix_td_mean[342][185] = 0
np.where(correlation_matrix_td_mean == correlation_matrix_td_mean.min())
correlation_matrix_td_mean[189][342]
#[189, 342],[342, 189] -0.06564722082216376
labels.iloc[189]
labels.iloc[342]

'''
labels.iloc[189]
Out[164]: 
ROI number                                                          193
 volume                                                             145
 center of mass                                       (-2.3;-63.7;35.5)
Dosenbach                                                ["None": 0.93]
AAL                          ["Precuneus_L": 0.74]["Precuneus_R": 0.22]
Eickhoff-Zilles       ["Left Precuneus": 0.67]["Right Precuneus": 0....
Talairach-Tournoux    ["Left Precuneus": 0.51]["Right Precuneus": 0.31]
Harvard-Oxford        ["Left Precuneous Cortex": 0.54]["Right Precun...
Name: 189, dtype: object


labels.iloc[342]
Out[104]: 
ROI number                                                          347
 volume                                                             100
 center of mass                                         (37.7;13.7;7.4)
Dosenbach                                                ["None": 1.00]
AAL                   ["Insula_R": 0.57]["Putamen_R": 0.19]["Frontal...
Eickhoff-Zilles       ["Right Insula Lobe": 0.64]["Right Putamen": 0...
Talairach-Tournoux    ["Right Insula": 0.71]["Right Inferior Frontal...
Harvard-Oxford        ["Right Frontal Operculum Cortex": 0.43]["Righ...
Name: 342, dtype: object
'''


#3. Anti-correlation
correlation_matrix_td_mean[342][189] = 0
correlation_matrix_td_mean[189][342] = 0
np.where(correlation_matrix_td_mean == correlation_matrix_td_mean.min())
#[342, 145] [145, 342]  -0.060037386459578096
correlation_matrix_td_mean[145][342]
labels.iloc[342]
labels.iloc[145]


'''
labels.iloc[342]
Out[109]: 
ROI number                                                          347
 volume                                                             100
 center of mass                                         (37.7;13.7;7.4)
Dosenbach                                                ["None": 1.00]
AAL                   ["Insula_R": 0.57]["Putamen_R": 0.19]["Frontal...
Eickhoff-Zilles       ["Right Insula Lobe": 0.64]["Right Putamen": 0...
Talairach-Tournoux    ["Right Insula": 0.71]["Right Inferior Frontal...
Harvard-Oxford        ["Right Frontal Operculum Cortex": 0.43]["Righ...
Name: 342, dtype: object


labels.iloc[145]
Out[212]: 
ROI number                                                          149
 volume                                                             113
 center of mass                                        (0.7;41.5;-15.5)
Dosenbach                                                ["None": 1.00]
AAL                   ["Rectus_L": 0.37]["Rectus_R": 0.31]["Frontal_...
Eickhoff-Zilles       ["Left Rectal Gyrus": 0.37]["Right Rectal Gyru...
Talairach-Tournoux    ["Left Medial Frontal Gyrus": 0.36]["Right Med...
Harvard-Oxford        ["Right Frontal Medial Cortex": 0.60]["Left Fr...
Name: 145, dtype: object
'''


#4. Anti-correlation
correlation_matrix_td_mean[342][145] = 0
correlation_matrix_td_mean[145][342] = 0
np.where(correlation_matrix_td_mean == correlation_matrix_td_mean.min())
#[248, 342] [342, 248] -0.05769888647662072
correlation_matrix_td_mean[248][342] 
labels.iloc[248]
labels.iloc[342]

'''

labels.iloc[248]
Out[216]: 
ROI number                                                          252
 volume                                                             109
 center of mass                                       (50.5;-62.6;33.6)
Dosenbach                         ["None": 0.83]["angular gyrus": 0.17]
AAL                                                 ["Angular_R": 0.96]
Eickhoff-Zilles       ["Right Angular Gyrus": 0.72]["Right Middle Te...
Talairach-Tournoux    ["Right Angular Gyrus": 0.49]["Right Middle Te...
Harvard-Oxford        ["Right Lateral Occipital Cortex; superior div...
Name: 248, dtype: object

labels.iloc[342]
Out[115]: 
ROI number                                                          347
 volume                                                             100
 center of mass                                         (37.7;13.7;7.4)
Dosenbach                                                ["None": 1.00]
AAL                   ["Insula_R": 0.57]["Putamen_R": 0.19]["Frontal...
Eickhoff-Zilles       ["Right Insula Lobe": 0.64]["Right Putamen": 0...
Talairach-Tournoux    ["Right Insula": 0.71]["Right Inferior Frontal...
Harvard-Oxford        ["Right Frontal Operculum Cortex": 0.43]["Righ...
Name: 342, dtype: object

'''


#5. Anti-correlation
correlation_matrix_td_mean[248][342] = 0
correlation_matrix_td_mean[342][248] = 0
np.where(correlation_matrix_td_mean == correlation_matrix_td_mean.min())
#[158, 248] [248, 158] -0.05654264413379059
correlation_matrix_td_mean[248][158]

labels.iloc[248]
labels.iloc[158]


'''
labels.iloc[248]
Out[181]: 
ROI number                                                          252
 volume                                                             109
 center of mass                                       (50.5;-62.6;33.6)
Dosenbach                         ["None": 0.83]["angular gyrus": 0.17]
AAL                                                 ["Angular_R": 0.96]
Eickhoff-Zilles       ["Right Angular Gyrus": 0.72]["Right Middle Te...
Talairach-Tournoux    ["Right Angular Gyrus": 0.49]["Right Middle Te...
Harvard-Oxford        ["Right Lateral Occipital Cortex; superior div...
Name: 248, dtype: object


labels.iloc[158]
Out[220]: 
ROI number                                                          162
 volume                                                             120
 center of mass                                          (42.6;2.0;6.7)
Dosenbach                                   ["None": 0.88]["vFC": 0.12]
AAL                         ["Insula_R": 0.75]["Rolandic_Oper_R": 0.13]
Eickhoff-Zilles       ["Right Insula Lobe": 0.78]["Right Inferior Fr...
Talairach-Tournoux    ["Right Insula": 0.82]["Right Precentral Gyrus...
Harvard-Oxford        ["Right Central Opercular Cortex": 0.51]["Righ...
Name: 158, dtype: object
'''


coordinates = plotting.find_parcellation_cut_coords(labels_img=atlas_filename)

#################################################################################
#ASD
#################################################################################

asd_coords = np.array([coordinates[118],coordinates[159],
                       coordinates[172],coordinates[319],
                       coordinates[104],coordinates[265],
                       coordinates[189],coordinates[244],
                       coordinates[227],coordinates[327],
                       coordinates[185],coordinates[342],
                       coordinates[145],coordinates[342],
                       coordinates[342],coordinates[367],
                       coordinates[244],coordinates[342],
                       coordinates[189],coordinates[342]])

size = 20

my_matrix = np.zeros([size,size])

for i,num1,num2 in zip(range(size),
                       [118,172,104,189,227,185,145,342,244,189],
                       [159,319,265,244,327,342,342,367,342,342]):

    my_matrix[2*i,2*i+1] = correlation_matrix_asd_mean[num1][num2]
    my_matrix[2*i+1,2*i] = correlation_matrix_asd_mean[num2][num1]
        
plotting.plot_connectome(my_matrix, asd_coords, edge_threshold="10%",
                         title='Brain connectome of ASD',edge_vmax=0.8,edge_vmin=-0.1)


#################################################################################
#TD
#################################################################################

td_coords = np.array([coordinates[118],coordinates[159],
                       coordinates[189],coordinates[244],
                       coordinates[244],coordinates[362],
                       coordinates[172],coordinates[319],
                       coordinates[104],coordinates[265],
                       
                       coordinates[185],coordinates[342],
                       coordinates[189],coordinates[342],
                       coordinates[342],coordinates[145],
                       coordinates[248],coordinates[342],
                       coordinates[248],coordinates[158]])

size = 20

my_matrix = np.zeros([size,size])

for i,num1,num2 in zip(range(size),
                       [118,189,244,172,104,185,189,342,248,248],
                       [159,244,362,319,265,342,342,145,342,158]):

    my_matrix[2*i,2*i+1] = correlation_matrix_td_mean[num1][num2]
    my_matrix[2*i+1,2*i] = correlation_matrix_td_mean[num2][num1]
        
plotting.plot_connectome(my_matrix, td_coords, edge_threshold="10%",
                         title='Brain connectome of TD',edge_vmax=0.8,edge_vmin=-0.1)