import mne

def detect_and_interpolate_bad_channels(raw, method='auto'):
    """
    Detect and interpolate bad EEG channels.

    Arguments
        raw: mne.io.Raw object
        method: str, method for automatic bad channel detection ('auto' or custom criteria)

    Returns
        raw_interp: mne.io.Raw object after interpolation
    """
    if method == 'auto':
        # Automatically detect bad channels based on variance or other criteria
        raw.info['bads'] = []  # Reset bads
        raw.info['bads'] += mne.preprocessing.find_bad_channels_maxwell(raw, h_freq=50)
    # Manually add bad channels if known
    # raw.info['bads'] += ['EEG 053']
    
    # Interpolate bad channels
    raw_interp = raw.copy().interpolate_bads(reset_bads=True)
    
    return raw_interp