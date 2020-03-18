import os.path, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)+os.path.sep+'..')*2)
import biketrauma
from biketrauma.io import url_db, path_target

import numpy as np
import hashlib

def test_df():
    df = biketrauma.Load_db().save_as_df()
    assert(df['departement'].value_counts()['21']==459)

def test_df_log():
    df = biketrauma.Load_db().save_as_df()
    assert(np.allclose(np.log(df['departement'].value_counts()['92']),7.651120176))

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def test_dl():
    assert(md5(path_target),'ee8c4e0e7989bc6aac7876d7501bbf4d')

