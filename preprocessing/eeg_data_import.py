import mne

def load_eeg_data(file_path, file_type="edf"):
    """
    Load EEG data using MNE-Python.

    Arguments
        file_path: str
            Path to the EEG data file.
        file_type: str
            Type of the EEG data file. Default is "edf".

    Returns
        raw: mne.io.Raw object containing the EEG data
    """
    if file_type == 'edf':
        raw = mne.io.read_raw_edf(file_path, preload=True)
    elif file_type == 'bdf':
        raw = mne.io.read_raw_bdf(file_path, preload=True)
    elif file_type == 'fif':
        raw = mne.io.read_raw_fif(file_path, preload=True)
    elif file_type == 'set':
        raw = mne.io.read_raw_eeglab(file_path, preload=True)
    else:
        raise ValueError("Unsupported file type.")
    
    return raw