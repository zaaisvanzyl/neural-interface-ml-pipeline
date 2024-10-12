

def apply_average_reference(raw):
    """
    Apply average reference to the EEG data.

    Arguments
        raw: mne.io.Raw object

    Returns
        raw_ref: mne.io.Raw object after re-referencing
    """
    raw_ref = raw.copy().set_eeg_reference('average', projection=True)
    return raw_ref