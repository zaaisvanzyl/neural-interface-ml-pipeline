import os
import numpy as np
from mne import set_log_level
set_log_level('WARNING')  # Suppress MNE info messages

# Import preprocessing functions
from preprocessing.eeg_data_import import load_eeg_data
from preprocessing.eeg_filtering import apply_bandpass_filter
from preprocessing.eeg_notch_filter import apply_notch_filter
from preprocessing.eeg_ica import apply_ica
from preprocessing.eeg_referencing import apply_average_reference
from preprocessing.eeg_epoching import epoch_data
from preprocessing.eeg_baseline_correction import apply_baseline_correction
from preprocessing.eeg_bad_channel import detect_and_interpolate_bad_channels
from preprocessing.eeg_normalization import z_score_normalize_epochs
from preprocessing.csp_feature_extraction import extract_csp_features
from preprocessing.eeg_data_augmentation import add_gaussian_noise
from preprocessing.eeg_time_shift import time_shift_epochs

data_dir = 'data/'
subject_file = 'subject01.edf'
file_path = os.path.join(data_dir, subject_file)
file_type = 'edf'
event_id = {'idle': 2, 'move_right': 1}
tmin, tmax = -0.2, 0.8
baseline = (None, 0)

# Load EEG data
raw = load_eeg_data(file_path, file_type)

# Apply band-pass filter
raw_filtered = apply_bandpass_filter(raw, l_freq=0.5, h_freq=50.0)

# Apply notch filter to remove line noise
raw_notched = apply_notch_filter(raw_filtered, freqs=[50, 100, 150, 200])

# Detect and interpolate bad channels
raw_interp = detect_and_interpolate_bad_channels(raw_notched, method="auto")

# Apply ICA to remove artifacts
raw_clean, ica = apply_ica(raw_interp, n_components=20, method="infomax")

# Apply average referencing
raw_ref = apply_average_reference(raw_clean)

# Epoch the data
epochs = epoch_data(raw_ref, event_id, tmin=tmin, tmax=tmax, baseline=baseline)

# Apply baseline correction
epochs_corrected = apply_baseline_correction(epochs, baseline=baseline)

# Normalize the epochs
epochs_normalize = z_score_normalize_epochs(epochs_corrected)

# Define labels for CSP
labels = epochs_corrected.events[:, -1]
labels_binary = (labels == event_id['move_right']).astype(int)

# Extract CSP features
features = extract_csp_features(epochs_corrected, labels_binary, n_components=4)

# Data augmentation: Add Gaussian noise
features_augmented = add_gaussian_noise(features, noise_level=0.02)

# Time shift augmentation

epochs_shifted = time_shift_epochs(epochs_corrected, shift_seconds=0.05, sfreq=raw.info['sfreq'])

# Extract features from shifted epochs if needed
labels_shifted = epochs_shifted.events[:, -1]
labels_shifted_binary = (labels_shifted == event_id['move_right']).astype(int)
features_shifted = extract_csp_features(epochs_shifted, labels_shifted_binary, n_components=4)

# Combine original and augmented features
featuers_final = np.vstack((features, features_augmented, features_shifted))
labels_final = np.hstack((labels_binary, labels_binary, labels_shifted_binary))

print(f"Features shape: {features_final.shape}")
print(f"Labels shape: {labels_final.shape}")