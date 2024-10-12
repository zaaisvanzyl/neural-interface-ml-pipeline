from mne.decoding import CSP
import numpy as np

def extract_csp_features(epochs, labels, n_components=4):
    """
    Extract CSP features from epoched EEG data.

    # Arguments
        epochs: mne.Epochs object
        labels: array-like, shape (n_epochs,), class labels
        n_components: int, number of CSP components to extract

    # Returns
        features: NumPy array, shape (n_epochs, 2 * n_components)
    """
    csp = CSP(n_components=n_components, reg=None, log=True, norm_trace=False)
    features = csp.fit_transform(epochs.get_data(), labels)
    return features