import mne
import numpy as np
from scipy.ndimage import shift

def time_shift_epochs(epochs, shift_seconds, sfreq):
    """
    Apply time shifting to EEG epochs.

    # Arguments
        epochs: mne.Epochs object
        shift_seconds: float, time to shift in seconds
        sfreq: float, sampling frequency

    # Returns
        epochs_shifted: mne.Epochs object after time shifting
    """
    shift_samples = int(shift_seconds * sfreq)
    data = epochs.get_data()
    data_shifted = np.roll(data, shift_samples, axis=2)
    epochs_shifted = mne.EpochsArray(data_shifted, info=epochs.info, events=epochs.events, event_id=epochs.event_id)
    return epochs_shifted