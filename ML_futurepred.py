import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

DATA_FOLDER = '/mnt/a25e8cca-e722-4bcc-ae6b-e73124ab090c/IIITB/ML/project/'

train           = pd.read_csv(os.path.join(DATA_FOLDER, 'train.csv'))
test            = pd.read_csv(os.path.join(DATA_FOLDER, 'test.csv'))
items           = pd.read_csv(os.path.join(DATA_FOLDER, 'items.csv'))
item_categories = pd.read_csv(os.path.join(DATA_FOLDER, 'item_categories.csv'))
shops           = pd.read_csv(os.path.join(DATA_FOLDER, 'shops.csv'))

print train.head()
# print 'Train shape\n', train.shape
# print 'test shape\n', test.shape