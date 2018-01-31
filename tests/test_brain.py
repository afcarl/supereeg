# -*- coding: utf-8 -*-

import pytest
import os
import superEEG as se
import numpy as np
import pandas as pd
import nibabel as nib
import matplotlib.pyplot as plt

data = np.random.multivariate_normal(np.zeros(10), np.eye(10), size=100)
locs = np.random.multivariate_normal(np.zeros(3), np.eye(3), size=10)
bo = se.Brain(data=data, locs=locs)


def test_create_bo():
    assert isinstance(bo, se.Brain)

def test_bo_data_df():
    assert isinstance(bo.data, pd.DataFrame)

def test_bo_locs_df():
    assert isinstance(bo.locs, pd.DataFrame)

def test_bo_sessions_series():
    assert isinstance(bo.sessions, pd.Series)

def test_bo_nelecs_int():
    assert isinstance(bo.n_elecs, int)

def test_bo_nsecs_list():
    assert (bo.n_secs is None) or (type(bo.n_secs) is (np.ndarray, int))

def test_bo_nsessions_int():
    assert isinstance(bo.n_sessions, int)

def test_bo_kurtosis_list():
    assert isinstance(bo.kurtosis, np.ndarray)

def test_samplerate_array():
    assert (bo.sample_rate is None) or (type(bo.sample_rate) is list)

def test_bo_getdata_nparray():
    assert isinstance(bo.get_data(), np.ndarray)

def test_bo_zscoredata_nparray():
    assert isinstance(bo.get_zscore_data(), np.ndarray)

def test_bo_get_locs_nparray():
    assert isinstance(bo.get_locs(), np.ndarray)

def test_bo_save(tmpdir):
    p = tmpdir.mkdir("sub").join("example")
    bo.save(fname=str(p))
    test_bo = se.load(os.path.join(str(p) + '.bo'))
    assert isinstance(test_bo, se.Brain)

def test_nii_nifti():
    assert isinstance(bo.to_nii(), nib.nifti1.Nifti1Image)


## can't get tests for plots to work

# def test_bo_plot_locs(tmpdir):
#     p = tmpdir.mkdir("sub").join("example")
#     fig = bo.plot_locs(pdfpath=str(p))
#     assert os.path.exists(os.path.join(str(p), '.pdf'))
#     assert isinstance(fig, plt.Figure)
#
#
# def test_bo_plot_data(tmpdir):
#     p = tmpdir.mkdir("sub").join("example")
#     fig = bo.plot_data(filepath=str(p))
#     assert os.path.exists(os.path.join(str(p), '.png'))
#     assert isinstance(fig, plt.Figure)