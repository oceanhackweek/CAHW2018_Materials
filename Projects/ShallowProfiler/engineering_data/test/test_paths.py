
import os
import sp_eng_data as ed

import constants as c

def test_path():
    setup_path = os.path.join(ed.csv_path(),'setup.py')
    assert os.path.isfile(setup_path)

def test_make_csv_filename():
    assert ed.make_csv_filename('PC01B', c.valid_start) == 'pc01b_ahrsdata_20170821.csv'
    assert ed.make_csv_filename('PC01A', c.valid_start) == 'pc01a_ahrsdata_20170821.csv'

def test_data_exists():
    test_data_path = os.path.join(ed.csv_path(), '2017-08-21', 'pc01a_ahrsdata_20170821.csv')
    assert os.path.isfile(test_data_path)

def test_make_csv_path():
    assert os.path.isfile(ed.make_csv_path('PC01A', c.valid_start))
    assert os.path.isfile(ed.make_csv_path('PC01B', c.valid_start))
    assert os.path.isfile(ed.make_csv_path('PC03A', c.valid_start))
