

def apply_bandpass_filter(raw, l_freq=0.5, h_freq=30):
    """
    Apply a band-pass filter to the raw EEG data

    Arguments:
        raw: mne.io.Raw object
            The raw EEG data
        l_freq: float
            The lower frequency bound of the filter
        h_freq: float
            The upper frequency bound of the filter

    Returns:
        raw_filtered: mne.io.Raw object after band-pass filtering

    """
    raw_filtered = raw.copy().filter(l_freq=l_freq, h_freq=h_freq, fir_design='firwin')
    return raw_filtered