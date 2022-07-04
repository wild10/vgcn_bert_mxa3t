import random
import numpy as np
import scipy.sparse as sp
import pickle as pkl
import re
import time
import argparse
import os
import sys
from sklearn.utils import shuffle

import pandas as pd

from nltk.corpus import stopwords
import nltk

random.seed(44)
np.random.seed(44)

parser = argparse.ArgumentParser()
parser.add_argument('--ds', type=str, default='mexa3t')
parser.add_argument('--sw', type=int, default=0)
args = parser.parse_args()
cfg_ds = args.ds
cfg_del_stop_words=True if args.sw==1 else False

dataset_list={'sst', 'mexa3t'}

if cfg_ds not in dataset_list:
    sys.exit("Dataset choice error!")

will_dump_objects=True
dump_dir='data/dump_data'
if not os.path.exists(dump_dir):
    os.mkdir(dump_dir)

if cfg_del_stop_words:
    freq_min_for_word_choice=5
    # freq_min_for_word_choice=10 #best
else:
    freq_min_for_word_choice=1 # for bert+

valid_data_taux = 0.05
test_data_taux = 0.10

# word co-occurence with context windows
window_size = 20
if cfg_ds in ('mr','sst','mexa3t'):
    window_size = 1000 # use whole sentence

tfidf_mode='only_tf'
# tfidf_mode='all_tfidf'

# 在clean doc时是否使用bert_tokenizer分词, data3时不用更好
cfg_use_bert_tokenizer_at_clean=True
#bert-base-uncased, bert-base-multilingual-uncased
#bert_model_scale='bert-base-multilingual-uncased'
bert_model_scale = 'dccuchile/bert-base-spanish-wwm-uncased'
#bert_model_scale='bert-large-uncased'
bert_lower_case=True

print('---data prepare configure---')
print('Data set: ',cfg_ds,'freq_min_for_word_choice',freq_min_for_word_choice,'window_size',window_size)
print('del_stop_words',cfg_del_stop_words,'use_bert_tokenizer_at_clean',cfg_use_bert_tokenizer_at_clean)
print('tfidf-mode',tfidf_mode,'bert_model_scale',bert_model_scale,'bert_lower_case',bert_lower_case)
print('\n')

#%%
'''
Get the tweets,y,confidence etc from data file
'''
print('Get the tweets,y,confidence etc from data file...')
start=time.time()
