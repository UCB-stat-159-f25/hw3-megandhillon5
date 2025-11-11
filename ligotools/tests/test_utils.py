from ligotools import utils
import numpy as np


def test_whiten_changes_data():
    fs = 4096
    dt = 1.0 / fs
    t = np.linspace(0, 1, fs)
    strain = np.sin(2 * np.pi * 60 * t)
    interp_psd = lambda f: np.ones_like(f)
    
    whitened = utils.whiten(strain, interp_psd, dt)
    assert not np.allclose(strain, whitened)


def test_reqshift_phase_shift():
    fs = 4096
    t = np.linspace(0, 1, fs)
    data = np.sin(2 * np.pi * 60 * t)
    
    shifted = utils.reqshift(data, fshift=200, sample_rate=fs)
    assert not np.allclose(data, shifted)