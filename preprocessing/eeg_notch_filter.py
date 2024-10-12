def apply_notch_filter(raw, freqs=50.0):
    """
    Apply a notch filter to remove power line noise.

    Arguments
        raw: mne.io.Raw object
        freqs: float or list of floats, frequency/frequencies to remove

    Returns
        raw_notched: mne.io.Raw object after notch filtering
    """
    raw_notched = raw.copy().notch_filter(freqs=freqs, fir_design='firwin')
    return raw_notched