import pytest
from ligotools import readligo
import os

def test_loaddata_exists():
    """Check that loaddata returns data and metadata properly"""
    strain, time, chan_dict = readligo.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5")
    assert len(strain) == len(time)
    assert isinstance(chan_dict, dict)

def test_sampling_rate_positive():
    """Check that sampling rate is positive"""
    strain, time, chan_dict = readligo.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5")
    dt = time[1] - time[0]
    fs = 1.0 / dt
    assert fs > 0