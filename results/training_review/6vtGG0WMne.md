Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

The paper proposes a framework for regulating model imbalance in deep learning to suit user-specified metrics (F1, G-means) rather than always pursuing class balance. It formalizes Model Imbalance State (MIS) as the average prediction probability per class, introduces Bias Adjustment (BA) to efficiently optimize the bias parameters to match a target MIS, and presents a training strategy that applies BA at each epoch. Experiments on three datasets (CIFAR-10, SST-2, AG News) at multiple imbalance ratios show strong performance gains.

## Strengths

- **Clean formalization of Model Imbalance State (MIS).** Eq. (4) defines MIS as the average prediction probability over the training set, providing a concrete, differentiable measure of a model's per-class bias. This formalization directly enables the paper's core capability: targeting a specific imbalance level rather than always pursuing balance.

- **Bias Adjustment (BA) is computationally efficient.** BA optimizes only K parameters (the biases) using gradient descent on the full dataset as a single batch. Figure 4 shows that class-weight hyperparameter tuning takes 2–3 orders of magnitude more time than BA, and Table 6 shows epoch-tuning for two-stage methods takes ~10× the BA time. This efficiency is a genuine practical advantage.

- **Empirical validation that different metrics require different imbalance states.** Figure 2 explicitly confirms the paper's central premise: accuracy, F1, and G-means peak at different minority-class probabilities (e.g., on SST-2, best F1 at ~0.05, best G-means at >0.25), and the balanced model (probability ≈ 0.5) is suboptimal for F1 and G-means. This justifies the need for a method that regulates imbalance rather than only balancing.

- **Consistent strong results across datasets and imbalance ratios.** Tables 2–5 show BA achieving the highest accuracy, F1, and G-means in nearly every setting, with large margins under severe imbalance (e.g., Table 3: +7.9 F1 on SST-2 500:1; Table 4: +13.0 G-means on SST-2 500:1).

## Weaknesses

### Fatal
None.

### Major

1. **Method is demonstrated only for binary classification, limiting the claimed "wide applicability."** Section 3.2 explicitly states "This work mainly discusses the binary classification" and the search strategy for \(r\) assumes \(r_2 = 1 - r_1\). Extending to \(K > 2\) would require a \(K\)-dimensional search that does not scale with the current coarse-grid approach. The paper does not discuss any extension to multiclass settings and tests only on binary datasets (SST-2, binarized CIFAR-10, binarized AG News). This substantially narrows the scope of the contribution relative to the abstract's claim of "wide applicability."

2. **Baseline methods are compared on F1 and G-means without adaptation to those metrics.** Methods like cRT, LWS, POT, and Proportion are designed for balanced accuracy — they achieve balanced predictions by re-balancing the classifier or weighting by inverse frequency. Evaluating them on F1 and G-means without allowing them to adjust class weights or decision thresholds to optimize those metrics creates an asymmetry favoring BA. The paper partially addresses this in Section 4.3.2 (grid-search class weighting), where weighting can beat BA on F1 for CIFAR-10 (Figure 4: "our method is slightly lower than the weighting method on F1 value"). This concession directly undercuts the paper's strongest claims of universal superiority. A fair comprehensive comparison would adapt all baselines to the target metrics.

### Minor

3. **No ablation isolating the benefit of per-epoch BA correction vs. one-shot BA after training.** The paper's training strategy (Section 3.3) applies BA at every epoch and validates, and claims this "facilitates the discovery of optimal model parameters." However, no experiment compares (a) training normally then applying BA once at the end, vs. (b) the proposed per-epoch strategy. Figure 3 shows results vary across epochs, but this is true of any training process. Without this ablation, it is unclear whether the epoch-level correction or simply checkpoint selection drives the improvement, and the novelty of the "training strategy" contribution is reduced.

4. **No comparison with decision-threshold tuning.** BA adjusts the bias to achieve a target MIS. A simpler, standard baseline is to keep the model fixed and tune the decision threshold on the validation set to optimize the target metric. This is the most direct competitor to BA and is not discussed or compared, making it hard to assess whether the bias-adjustment mechanism itself is necessary or whether threshold tuning would achieve similar results.

5. **Validation set used for searching \(r^*\) is not described.** The paper states that the optimal target MIS \(r^*\) is found by evaluating metrics on a validation set (Section 3.2), but never reports the validation set size, its class ratio (balanced or imbalanced), or whether it comes from the same distribution as the test set. This hinders reproducibility and assessment of sensitivity.

6. **Search strategy for \(r^*\) lacks sensitivity analysis.** The search uses a coarse-to-fine grid with powers of 10 (Section 3.2). The paper claims "precision taken to \(10^{-2}\) or \(10^{-3}\) is enough" without evidence. No analysis is provided on how sensitive the final results are to the search precision or whether finer-grained search would change outcomes.

7. **The training-validation MIS gap is not discussed.** The BA objective minimizes KL divergence between the *training* MIS and target \(r\), but \(r^*\) is selected by evaluating a metric on the *validation* set. If the distribution of predictions differs between training and validation sets (likely under class imbalance), the optimal \(r\) on validation may not correspond to the optimal training MIS. This assumption is standard but unexamined.

### Trivial

- The MIS definition (Eq. 4) as average prediction probability is sensitive to the training class prior — even a perfectly calibrated model on imbalanced data would have per-class probabilities proportional to the training prior. The paper does not discuss this confound, though the practical impact appears limited since the method works on the imbalanced test sets as well.

## Nice-to-Haves

- **Multiclass extension:** A sketch or proposal for extending the search over \(r\) to \(K>2\) (e.g., constrained optimization, temperature scaling, or gradient-based search) would strengthen the paper's claimed generality.
- **Ablation of training strategy:** Comparing BA-at-each-epoch vs. BA-only-at-end would isolate the value of the epoch-level correction.
- **Threshold-moving baseline:** Direct comparison with decision-threshold tuning would clarify whether BA's bias-adjustment mechanism offers advantages beyond a simpler post-hoc approach.

## Removed Points

- **"AG dataset Table 5 appears to compare only Proportion and Ours"** — Removed because the table contents cannot be verified from the text extraction; the paper lists six comparison methods and the text states "Table 5 shows the results," making it likely all baselines are included but the table image is not machine-readable.
- **"The derivation from Eq. (1) to Eq. (3) is correct but standard"** — Removed as a generic complaint that does not identify a problem; standard derivations are appropriate in methodology sections.
- **"The paper does not discuss why adjusting bias alone is sufficient"** — Removed because the paper does discuss this (Eq. 3 shows bias encodes class probability estimates); the critic misread the section.
- **"The training strategy novelty is thin"** — Removed as an opinion not grounded in a specific flaw; the strategy is a legitimate engineering contribution even if conceptually simple.
- **"Missing appendix/Section A"** — Removed because appendices are stripped by the parser; they exist in the original submission.
- **Multiple formatting and typo-related complaints** — Removed per hard rules; these are parser artifacts.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a multiclass experiment or at minimum a clear discussion of how the search strategy would scale to \(K > 2\) (e.g., gradient-based optimization of a shared temperature parameter).
2. Include an ablation that compares BA applied at each epoch vs. BA applied only after training is complete, to isolate the benefit of the per-epoch correction.
3. Add a baseline where the decision threshold is tuned on the validation set for each target metric. This is the simplest competitor to BA and would clarify whether bias adjustment offers advantages beyond threshold tuning.
4. Report validation set characteristics (size, class ratio) and analyze sensitivity of the optimal \(r^*\) to validation set composition.
5. Provide a sensitivity analysis of the search precision for \(r^*\) (e.g., compare \(10^{-2}\) vs. \(10^{-3}\) precision on one dataset).
6. For F1 and G-means comparisons, either adapt the baseline methods (e.g., allow them to use a validation-tuned threshold) or clearly caveat that the comparison is against their off-the-shelf versions designed for balanced accuracy.

## Score and Decision

**Originality:** Moderate — the idea of targeting a specific imbalance state rather than always balancing is novel, and the MIS formalization is clean. However, the mechanism (bias adjustment) is simple.

**Importance of research question:** High — many real applications care about F1 or G-means, not accuracy, and the paper correctly identifies that balanced models are not always optimal.

**Claims support:** Moderate — the method works well empirically, but the F1/G-means comparisons are weakened by not adapting baselines, and the binary-only scope limits generalizability claims.

**Soundness of experiments:** Moderate — extensive but missing key ablations (per-epoch vs. one-shot BA, threshold-tuning baseline) and the validation set is not described.

**Clarity of writing:** Good — the paper is well-structured and the key ideas are clearly conveyed.

**Value to the research community:** Moderate — the core insight (different metrics need different imbalance levels) is practically useful and BA is efficient enough to be adopted as a standard tool.

The paper makes a real, practical contribution and the core idea is well-motivated and validated. The weaknesses are addressable and do not invalidate the core claims. However, the binary-only scope and the absence of a threshold-tuning baseline prevent a stronger assessment.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>