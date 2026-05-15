Now I have a thorough understanding. Here is my consolidated review.

---

## Summary

FMP-AE proposes a hybrid unsupervised method for univariate time series anomaly detection that combines a 1D-CNN-extracted Matrix Profile with an autoencoder. The core contribution is a loss function that integrates a normalized Matrix Profile loss (minimizing the mean MP value) with the autoencoder's reconstruction loss, weighted by a dynamically adjusted hyperparameter λ. Anomaly scores are computed as softmax-weighted MP values multiplied by reconstruction errors. The method is evaluated on the UCR250 benchmark (250 datasets) against 14 baselines.

## Strengths

- **Novel combination of Matrix Profile with deep learning through a joint loss function**: The idea of using MP as a differentiable regularizer for an autoencoder is genuinely underexplored in the literature. The dynamic λ weighting (starting low to learn global structure, then increasing to emphasize local anomalies) is a reasonable design choice that the ablation study supports — removing the MP loss drops F1 from 86.79% to 67.87%.

- **Systematic ablation study isolating each component's contribution**: Five ablations (replacing 1D-CNN with MLP, removing 1D-CNN, removing MP loss, removing autoencoder, removing MP) provide causal evidence that all components contribute to the final performance. The steepest drop occurs when removing 1D-CNN (F1 falls to 31.41%), confirming that convolutional feature extraction before MP computation is critical.

- **Large-scale evaluation scope**: Testing on 250 datasets spanning medicine, biology, industry, and meteorology is ambitious and provides a broad empirical foundation.

## Weaknesses

### Fatal
None. The paper's core idea is not invalidated by a single fatal flaw; however, the combination of issues below is severe enough to prevent acceptance.

### Major

- **Method severely underspecified — core technical mechanism not described**: The section titled "CALCULATE OPTIMIZED-MP BY 1D-CNN" (Section 3.1, lines 50–52) contains only a figure reference with no textual description. The paper never specifies: (a) how the Matrix Profile is computed from 1D-CNN feature maps (which MP variant — STAMP/STOMP/SCRIMP? Are pairwise distances computed on feature maps directly or on pooled representations?), (b) the CNN architecture (layers, filter sizes, strides, activations, pooling), (c) the autoencoder architecture, (d) the sliding window length k, or (e) the schedule or criterion for the dynamic λ increase (described only as "dynamically increased during training," line 94, with no algorithm, schedule, or hyperparameter values). The global normalization factors (Eqs. 3–4) define N as "the total number of batches," which is unknown until training completes, implying either an impractical two-pass procedure or a definition that cannot be executed in standard online mini-batch training. These omissions make the method non-reproducible and impossible to evaluate for correctness.

- **Evaluation protocol is unverifiable**: The paper reports Precision, Recall, and F1 across 250 datasets for 14 methods but never specifies how the anomaly detection threshold τ is chosen for any method (line 111 merely states "we use a threshold τ"). For unsupervised anomaly detection, Precision/Recall/F1 are threshold-dependent metrics; without a principled, documented thresholding strategy, the headline numbers are uninterpretable and the cross-method comparisons are invalid. The paper does not report whether metrics are macro-averaged or micro-averaged across datasets, provides no variance or confidence intervals, and does not report AUC for any baseline method (AUC is only shown for their own model and ablations in Figures 6–7). Without threshold-free metrics for all methods, the claim that FMP-AE "outperforms others" cannot be assessed. The ablation results (Table 2) suffer from the same protocol gap.

### Minor

- **Anomaly score's batch-relativity**: The softmax normalization in AS_i = softmax(p_i) · e_i makes anomaly scores relative within a batch rather than absolute. This is problematic for deployment where scores must be comparable across time and across data segments, and the paper does not discuss this design choice.

- **No runtime analysis despite efficiency claims**: The abstract and conclusion claim "computational efficiency" and "efficiently process large-scale datasets," yet the experiments contain no runtime comparison with any baseline. The stated motivation of "optimiz[ing] the MP computation to reduce costs" (Section 2) is not empirically supported.

- **AUC of baselines not reported**: AUC-ROC is the standard threshold-free metric for unsupervised TSAD and would allow fair comparison without thresholding artifacts. The paper computes AUC for its own model and ablations but not for any of the 14 baselines.

- **Departure from UCR evaluation standards without justification**: The UCR benchmark (Wu & Keogh, 2021) typically uses range-based evaluation or AUC. The paper uses point-wise Precision/Recall/F1 without describing or justifying a different protocol.

### Trivial
None.

## Nice-to-Haves

- **Multiple-run statistics** (mean and std over 5–10 seeds) would strengthen the reliability of the reported numbers.
- **Qualitative case studies** showing raw time series, MP profile, reconstruction error, and anomaly scores for representative datasets would help the reader understand failure modes.
- **Threshold sensitivity analysis** showing how F1 varies with threshold for different methods would document whether the reported F1 advantage is robust.

## Removed Points

The following criticisms from the reviews were removed as invalid, misinformed, or based on parser artifacts. They are listed for completeness but should not be weighed in the evaluation.

- **"Incoherent connection between training objective and inference"** (Harsh Critic Issue 3): The paper states (line 126) that training uses only normal data ("Each file contains a training set of normal data and a test set with one anomaly"). Minimizing mean MP on normal subsequences is reasonable — it makes normal patterns more similar. During inference, anomalies naturally produce higher MP values because they deviate from learned normal patterns. The alleged incoherence is not present; the critic appears to have overlooked the training-set composition. The softmax batch-relativity concern is retained as a minor weakness above.

- **"No single method consistently outperforms others" contradiction**: The paper states the well-known observation that no method dominates across all datasets, then claims its method is better. These are not contradictory — the paper is claiming a new SOTA, not claiming universal domination.

- **"MP+1D-CNN highest AUC but lowest F1 discrepancy glossed over"**: The paper explicitly discusses this (Section 4.2): "Among the models, the MP+1D-CNN achieved the highest AUC score... However, despite its superior AUC, the MP+1D-CNN model demonstrates a weaker ability to balance precision and recall compared to our model." This is a reasonable acknowledgment that AUC and F1 measure different things.

- **"Fails to review existing hybrid methods combining MP with neural networks"**: This assumes such methods exist. The paper's novelty claim is precisely that this combination is new, and no such methods are cited by the reviewer.

- **"Table 1 is an image with partially unreadable values"**: Parser artifact; the original submission's table is assumed readable.

- **"Missing appendix content"**: The parser strips appendix sections; they exist in the original submission. However, the main text's method description is independently too thin even accounting for appendix deferral.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Provide full method specification**: Include the CNN architecture (layers, filters, kernels, activations), autoencoder architecture, window size k, the specific MP algorithm used, and how MP is computed from feature maps. Pseudo-code for the training loop, including the dynamic λ schedule, would resolve the ambiguity in Equations 3–4.

2. **Report AUC for all baselines**: Threshold-free evaluation (AUC-ROC, AUC-PR) across all 14 baselines is essential to validate the claimed improvements without thresholding artifacts.

3. **Specify the threshold selection protocol**: Document how τ is chosen for every method (e.g., percentile of anomaly scores, grid search, or a fixed rule). Without this, the reported Precision/Recall/F1 cannot be trusted.

4. **Include runtime measurements**: Given the explicit efficiency claims, provide wall-clock training and inference times against at least the deep learning baselines (ADTransformer, OmniAnomaly) on comparable hardware.

5. **Clarify the global normalization**: Explain how N (total number of batches) is determined in practice — whether this requires precomputing statistics in an initial pass or can be approximated with running statistics.

## Score and Decision

This paper tackles an interesting and relevant problem (unsupervised TSAD) with a novel conceptual combination (MP + deep learning). The ablation study provides evidence that the hybrid design is meaningful. However, the paper has two severe problems that prevent acceptance. First, the method is critically underspecified — the core technical mechanism for computing MP from 1D-CNN features is not described in text, no architecture details are given, and the training procedure has definitional issues (the N in Equations 3–4). Second, the evaluation protocol is unverifiable — Precision/Recall/F1 are reported without any specification of threshold selection, making the headline results and cross-method comparisons uninterpretable. These are not minor presentation issues; they strike at the paper's core claims of "superior performance" and the definition of the method itself. The contribution, while interesting in concept, cannot be properly evaluated, reproduced, or built upon in its current form.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>