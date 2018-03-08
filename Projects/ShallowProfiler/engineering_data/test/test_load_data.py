import os
from datetime import datetime,timedelta
import pandas as pd
import pytest

import sp_eng_data as ed


import constants as c

def test_valid_load_pc():
    data = ed.load_sp_eng_data('PC01A',c.valid_start,c.valid_end)
    assert isinstance(data, pd.DataFrame )


def test_valid_load_sc():
    data = ed.load_sp_eng_data('SC01A',c.valid_start,c.valid_end)
    assert isinstance(data, pd.DataFrame )



def test_invalid_platform():
    with pytest.raises(RuntimeError):
        ed.load_sp_eng_data('FOOBAR',c.valid_start,c.valid_end)


# def test_invalid_daterange():
#     with pytest.raises(RuntimeError):
#         ed.load_sp_eng_data('PC01A', c.invalid_start, c.invalid_end)
