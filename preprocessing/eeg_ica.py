import mne

def apply_ica(raw, n_components=15, method='fastica', random_state=42):
    """
    Apply ICA to remove artifacts from EEG data.

    Arguments
        raw: mne.io.Raw object (filtered EEG data)
        n_components: int, number of ICA components to compute
        method: str, ICA algorithm to use (e.g., 'fastica', 'infomax')
        random_state: int, seed for reproducibility

    Returns
        raw_clean: mne.io.Raw object after ICA artifact removal
        ica: mne.preprocessing.ICA object containing ICA results
    """
    ica = mne.preprocessing.ICA(n_components=n_components, method=method, random_state=random_state)
    ica.fit(raw)
    
    # Identify ICA components corresponding to EOG (eye) artifacts
    eog_indices, eog_scores = ica.find_bads_eog(raw, measure='correlation')
    
    # Exclude identified EOG components
    ica.exclude = eog_indices
    
    # Apply ICA to remove artifacts
    raw_clean = ica.apply(raw.copy())
    
    return raw_clean, ica