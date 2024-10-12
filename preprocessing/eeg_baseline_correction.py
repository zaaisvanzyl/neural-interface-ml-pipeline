

def apply_baseline_correction(epochs, baseline=(None, 0)):
    """
    Apply baseline correction to epoched EEG data.

    Arguments
        epochs: mne.Epochs object
        baseline: tuple, time interval for baseline correction

    Returns
        epochs_corrected: mne.Epochs object after baseline correction
    """
    epochs_corrected = epochs.copy().apply_baseline(baseline=baseline)
    return epochs_corrected