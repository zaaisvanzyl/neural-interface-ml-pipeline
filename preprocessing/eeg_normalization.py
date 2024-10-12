import mne

def z_score_normalize_epochs(epochs):
    """
    Apply z-score normalization to epoched EEG data.

    Arguments
        epochs: mne.Epochs object

    Returns
        epochs_normalized: mne.EpochsArray object after normalization
    """
    data = epochs.get_data()
    mean = data.mean(axis=2, keepdims=True)
    std = data.std(axis=2, keepdims=True)
    data_normalized = (data - mean) / std
    epochs_normalized = mne.EpochsArray(data_normalized, info=epochs.info, events=epochs.events, event_id=epochs.event_id)
    return epochs_normalized