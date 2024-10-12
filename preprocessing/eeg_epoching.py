import mne

def epoch_data(raw, event_id, tmin=-0.2, tmax=0.8, baseline=(None, 0)):
    """
    Segment continuous EEG data into epochs around events.

    Arguments
        raw: mne.io.Raw object
        event_id: dict, mapping of event labels to IDs
        tmin: float, start time before the event
        tmax: float, end time after the event
        baseline: tuple, time interval for baseline correction

    Returns
        epochs: mne.Epochs object containing epoched data
    """
    events, _ = mne.events_from_annotations(raw)
    epochs = mne.Epochs(raw, events, event_id=event_id, tmin=tmin, tmax=tmax,
                        baseline=baseline, preload=True)
    return epochs