- Decision: Reject
- Avg Score: 3.80
- Scores: 5, 3, 3, 3, 5
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces FMP-AE, a hybrid model that combines Matrix Profile (MP) techniques with a 1D-CNN and Autoencoder for unsupervised time series anomaly detection. The key idea is a novel combined loss function — reconstruction loss (MSE from the autoencoder) plus a MP loss (mean of MP values computed on 1D-CNN feature maps) — with dynamic weighting of the MP term during training. Anomaly scores combine softmax-weighted MP values with reconstruction errors. Experiments on the UCR250 benchmark (250 datasets) show an F1 of 86.79%, outperforming 14 baselines. Five ablation studies isolate the contribution of each component.

## Strengths

- **Novel hybrid loss with demonstrated synergy**: The paper defines a joint loss combining normalized reconstruction error and MP loss (Section 3.2, Equations 1–4). The ablation study (Table 2) provides concrete evidence: removing the MP loss (Only AE) drops F1 from 86.79% to 67.87%, and removing the Autoencoder (MP+1D-CNN) drops F1 to 40.12%. This confirms the two loss terms are complementary and both necessary for the reported performance.

- **Strong empirical results on a large, established benchmark**: The model achieves the highest F1 (86.79%) and precision (81.03%) among 14 baselines on the UCR250 dataset (Table 1), outperforming methods including ADTransformer (82.37% F1), OmniAnomaly, and LSTM-VAE. The benchmark spans 250 diverse time series across medical, biological, industrial, and meteorological domains, supporting generalization claims.

- **Systematic ablation study**: Five controlled ablations (replacing 1D-CNN with MLP, removing CNN, removing MP loss, removing Autoencoder, removing MP) isolate each component's contribution. The largest performance drop (F1 from 86.79% to 31.41%) occurs when 1D-CNN is removed, demonstrating its importance for local temporal feature extraction.

- **AUC-ROC evaluation complements main results**: The paper provides ROC curves and AUC scores for all ablation variants (Figure 7), offering threshold-independent evidence of discriminative performance. The discrepancy where MP+1D-CNN has highest AUC but lower F1 is addressed — the paper notes AUC measures ranking quality while F1 reflects precision-recall balance at an operating point (Section 4.2).

## Weaknesses

### Fatal
None.

### Major

1. **Missing experimental details prevent reproducibility**: The paper omits critical architectural and training specifications:
   - **1D-CNN architecture**: number of layers, kernel sizes, stride, padding, number of channels — none specified (Section 3.1).
   - **Autoencoder architecture**: depth, latent dimension, layer structure — not given.
   - **Hyperparameters**: optimizer, learning rate, batch size, number of training epochs — absent.
   - **Sliding window length** \( k \): mentioned but never given a concrete value or selection method.
   - **\(\lambda\) schedule**: described as "gradually increased" and "dynamically adjusted" (Section 3.2) but no schedule, initial value, final value, or annealing strategy is provided.
   - **Threshold \(\tau\)**: used for anomaly classification (Section 3.3) but how it is determined (per-dataset? fixed? tuned on validation?) is never stated. If thresholds were optimized on test data, the reported Precision/Recall/F1 would be invalid.

   These omissions make it impossible to reproduce the method or verify the reported results. This is the most significant weakness in the paper.

2. **Unsupported computational efficiency claim**: The abstract states the approach "enhances computational efficiency" and "efficiently process[es] large-scale datasets," and the conclusion repeats "enhances computational efficiency." No runtime measurements, complexity analysis, or efficiency comparison against baselines is provided anywhere in the paper. The method requires sliding-window extraction, a 1D-CNN forward pass, an autoencoder forward pass, and MP computation on feature maps — it is not obvious why this would be more efficient than baselines. This claim should either be substantiated with evidence or removed.

### Minor

3. **Underspecified evaluation protocol relative to the UCR benchmark**: The paper reports Precision, Recall, and F1 (Table 1) but does not specify whether these are computed via the UCR benchmark's standard *range-based* evaluation (an anomalous segment is considered detected if any point within it is flagged) or point-wise evaluation. The paper also does not specify the threshold selection methodology used for the main results (as noted above). The UCR benchmark has a well-defined evaluation protocol (Wu & Keogh, 2021); the paper should clarify whether it follows that protocol and, if deviations exist, justify them.

4. **No statistical significance measures**: For 250 datasets, only mean metrics are reported (Table 1). There are no confidence intervals, standard deviations, distribution plots, or statistical significance tests (e.g., critical difference diagrams). Given the diversity of dataset lengths (6,680–900,000 points) and domains, reporting only point estimates masks potential variance in performance.

### Trivial
None.

## Nice-to-Haves
- Provide runtime comparisons against deep learning baselines (Anomaly Transformer, LSTM-VAE, OmniAnomaly) on the largest UCR datasets if the efficiency claim is kept.
- A critical difference diagram or per-dataset score distributions would strengthen the comparative evaluation.

## Removed Points

These points were raised by reviewers but are removed with justification:

- **Differentiability of MP loss is unsupported / fatal flaw** (Harsh Critic #1): **REMOVED — factually incorrect.** The claim that gradients through the MP computation are "zero almost everywhere" misunderstands the min operation. The MP value at position \(i\) is \(p_i = \min_{j \neq i} d(f_i, f_j)\), where \(d\) is a distance function and \(f_i\) are CNN feature maps. The gradient of \(p_i\) with respect to \(f_i\) is the gradient of \(d(f_i, f_{j^*})\) where \(j^*\) is the argmin — this is non-zero and well-defined almost everywhere (except at ties, measure zero). Standard deep learning frameworks (PyTorch, TensorFlow) handle backpropagation through min/argmin operations naturally. The training procedure as described is implementable.

- **Evaluation protocol conflates point-level and event-level metrics** (Harsh Critic): **REMOVED — speculative.** The paper does not specify whether it uses point-wise or range-based evaluation, but it never says it uses point-wise evaluation either. The critic assumes a deviation from the standard protocol without evidence. The underspecification is a real concern (kept as a Minor weakness above), but the claim of metric conflation is not supported by the paper's text.

- **Baselines are "trivially weak"** (Harsh Critic): **REMOVED.** LOF, IForest, and OC-SVM are standard baselines in the UCR benchmark (Wu & Keogh, 2021). Including them is standard practice, not a weakness.

- **Ablation drops are "suspiciously large"** (Harsh Critic): **REMOVED.** Large performance drops when removing a core component are expected in a valid ablation — they demonstrate that the component is important. The critic speculates about hyperparameter re-tuning, which is not supported by evidence in the paper or its absence.

- **AUC vs F1 discrepancy for MP+1D-CNN** (Harsh Critic): **REMOVED — the paper addresses this.** Section 4.2 explicitly notes that MP+1D-CNN achieves the highest AUC but "demonstrates a weaker ability to balance precision and recall" — this is a standard observation about the difference between ranking quality (AUC) and operating-point performance (F1), not an inconsistency.

- **Missing appendix, figures, proofs, related works, formatting nitpicks**: **REMOVED** per instructions (parser artifacts, cannot verify external references, or not substantive).

## Novel Insights

None beyond the paper's own contributions. The reviewers did not contribute genuinely novel observations that extend beyond what the paper itself claims.

## Suggestions

1. **Add a complete experimental setup section** specifying: (a) 1D-CNN and autoencoder architectures (layer counts, dimensions, kernel sizes), (b) all hyperparameters (learning rate, batch size, optimizer, epochs), (c) the \(\lambda\) schedule (initial value, final value, growth function), (d) the sliding window length \(k\) and how it was chosen, and (e) how the threshold \(\tau\) is determined for each dataset (e.g., percentile of normal training data, held-out validation, etc.).

2. **Clarify the evaluation protocol**: State explicitly whether Precision/Recall/F1 follow the UCR benchmark's range-based evaluation or a point-wise protocol. If the latter, justify and report range-based metrics for comparability.

3. **Either substantiate or remove the computational efficiency claim**: Provide wall-clock runtime comparisons against at least the deep-learning baselines (Anomaly Transformer, LSTM-VAE, OmniAnomaly) on the largest UCR datasets, or add a formal complexity analysis. If no evidence can be produced, remove the claim from abstract and conclusion.

4. **Add confidence intervals or per-dataset performance distributions for the 250-dataset benchmark** to give readers a sense of variance.

5. **Describe how the MP is computed** (STAMP/STOMP/SCRIMP?) in the training loop and how the self-join exclusion of trivial matches is handled, as these details affect both the differentiability path and computational cost.
