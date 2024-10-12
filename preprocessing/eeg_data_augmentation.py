import numpy as np

def add_gaussian_noise(features, noise_level=0.01):
    """
    Add Gaussian noise to the feature set.

    Arguments
        features: NumPy array, feature set
        noise_level: float, standard deviation of Gaussian noise

    Returns
        augmented_features: NumPy array with added noise
    """
    noise = np.random.normal(0, noise_level, features.shape)
    augmented_features = features + noise
    return augmented_features