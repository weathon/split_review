- Decision: Reject
- Scores: 5, 5, 5

## Merged Review

### Summary
The paper proposes SimRec, an anomaly score that combines reconstruction error with a similarity score computed via a Radial Basis Function (RBF) layer inserted into deep learning architectures (LSTM, Transformer). The RBF layer performs nonparametric density estimation in the hidden representation; high output indicates similarity to normal data. Experiments on three real-world benchmark datasets show improvements over baselines.

### Strengths
- The motivation to overcome the limitation of reconstruction-error-only anomaly detection in unsupervised settings is clear, practical, and easy to grasp.
- The idea of combining reconstruction and density-based similarity via a lightweight architectural modification (RBF layer) is technically sound.
- Experimental results support the claims and show stable performance improvement on LSTM and Transformer across three datasets.
- The paper is overall readable and neatly written.
- Ablation studies on initialization methods, insertion position, and number of cluster centroids provide a firm analysis of the method’s behavior under different settings.

### Weaknesses
- **Novelty is limited.** The core idea of using similarity to centroids (k-means-style clustering in hidden space) has been applied many times; combining it with reconstruction error is a trivial adaptation. The RBF kernel itself is pre-existing, and the optimization (e.g., Eq. 3) is a simple reapplication of prior formulas.
- **Missing baselines and older models.** Experiments only use LSTM and Transformer, which are not specialized for anomaly detection. The paper lacks comparisons with modern SOTA methods such as Anomaly Transformer, OmniAnomaly, STAD-GAN (Zhang et al., TKDD 2023), Coupled Attention Networks (Xia et al., 2023), MST-GAT (Ding et al., Information Fusion 2023), and others from 2022–2023. Since the method claims generality, applying it to these stronger baselines is needed.
- **Narrow related work scope.** The literature review focuses on a small slice of recent DNN-based work and omits important benchmarks and evaluation measures: TSB-UAD (20 datasets, ~2000 time series, 10+ baselines) and the “Volume under the Surface” evaluation measure (both VLDB 2022). This limits the assessment of the method’s competitiveness.
- **Unclear experimental settings.** Parameters and settings for baselines are not fully specified, raising concerns about fairness of comparisons.
- **Threshold sensitivity.** The effect of SimRec appears sensitive to threshold selection; a reconstruction error graph of the Anomaly Transformer using the same threshold selection method should be shown to disentangle the contribution of the score from threshold tuning.
- **Experimental scope insufficient.** Despite strong motivation, the amount and variety of experiments (only three datasets, two base architectures) feels lacking relative to the claimed contribution. More datasets (e.g., from TSB-UAD) and specialized anomaly-detection models are needed.