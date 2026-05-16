Now I have a thorough understanding of the paper. Let me construct the consolidated review.

## Summary

This paper proposes a complementary learning system for open-vocabulary continual classification, combining a frozen CLIP zero-shot model with an exemplar-based "tree probe" model that hierarchically clusters exemplars and trains local linear classifiers. A novel Adaptive Instance Marginalization (AIM) mechanism weights the two models' predictions based on CLIP's estimated probability that a test image's label is covered by the exemplar set. The method is evaluated across data, class, and task incremental settings plus three flexible inference scenarios, consistently matching or exceeding the prior state-of-the-art ZSCL while offering dramatically faster training.

## Strengths

1. **Tree probe achieves near-linear-probe accuracy with orders-of-magnitude faster training.**  
   The paper demonstrates that TreeProbe (100k) slightly surpasses LinProbe in accuracy (Fig. 3a) while its learning time plateaus at constant complexity after node capacity is reached, versus LinProbe's linear scaling (Fig. 3b). TreeProbe (50k) achieves 80.5 average target accuracy vs. LinProbe's 80.07 and ZSCL's 78.02, yet requires only 2.3 hours of total training versus 15.9 for CLIP Fine-tune (Table 1). This directly validates the core claim of a fast, accurate exemplar model.

2. **Adaptive Instance Marginalization (AIM) demonstrably balances zero-shot and exemplar predictions.**  
   In class incremental learning, CLIP+LinProbe (AIM-Emb) maintains reasonable unseen-class accuracy (~50% at early stages) where Avg-Emb collapses unseen-class performance to near zero (Fig. 2b). In task incremental learning, AIM-Emb beats the zero-shot model at every stage, whereas Avg-Emb only surpasses it after stage six (Fig. 2c). The flexible inference results (Fig. 2d) further show AIM-Emb dramatically improves zero-shot task performance over averaging-based fusion.

3. **Comprehensive evaluation across multiple continual learning and flexible inference scenarios.**  
   The paper introduces three incremental settings (data, class, task) and three flexible inference protocols (Zero-shot, Union+Zero-shot, Mix+Zero-shot). Across all settings, CLIP+TreeProbe (AIM-Emb) consistently matches or exceeds every compared method. On the ZSCL benchmark, TreeProbe (50k) achieves the best Harmony (79.1) and Full (76.8) scores (Table 2), while requiring no task-specific hyperparameter tuning — unlike ZSCL which used different learning rates per task.

4. **Efficient incremental update with theoretically grounded and empirically verified constant-time learning.**  
   The paper derives the training complexity of TreeProbe as O(ψ + log n) with ψ >> log n, yielding practically constant update time (Section 3.2). Fig. 3(b) confirms this empirically: TreeProbe's learning time plateaus at ~0.01 seconds per sample after node capacity, while LinProbe scales linearly to over 0.06 seconds. This matters for interactive applications where fast adaptation is required.

5. **Minimal degradation of zero-shot performance.**  
   On the ZSCL benchmark, TreeProbe (50k) retains a Transfer score of 70.7, nearly identical to CLIP zero-shot's 71.2 (Table 2). In flexible inference, AIM-Emb preserves strong zero-shot accuracy (~54%) compared to exemplar-only models that drop to ~1% (Fig. 2d). This supports the claim that the method maintains zero-shot effectiveness while improving on target tasks.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Limited baseline comparisons weaken the positioning claim.**  
   The paper compares against ZSCL, CLIP Fine-tune, CLIP zero-shot, KNN, and LinProbe — which covers the most directly relevant prior work. However, several methods share related ideas and would contextualize the contribution more strongly:
   - **Tip-Adapter** (Zhang et al., ICLR 2022) stores cached image features and combines zero-shot and cache predictions via learned weights — a close cousin of the exemplar-model-plus-fusion approach. The paper does not cite it or discuss the relationship.
   - **WiSE-FT** is cited in related work but not compared; the paper uses "CLIP Fine-tune" (full fine-tuning) but does not apply WiSE-FT's weight-space interpolation, which has been shown to mitigate forgetting in distribution-shift settings.
   
   The paper's claim of "outperforming all compared approaches" (abstract) is technically true but carries limited force given the comparison set. Adding these baselines would significantly strengthen the empirical positioning.

2. **Per-stage zero-shot accuracy is not clearly presented.**  
   The paper states that "results are reported as the average accuracy of target and zero-shot tasks at each stage" (line 232), but the analysis of Fig. 2(a-c) focuses entirely on target task performance. Zero-shot task accuracy is only reported at the end via the flexible inference evaluation (Fig. 2d) and the Transfer metric in Table 2. Since CLIP is frozen, zero-shot degradation can only occur through the AIM mechanism over-weighting the exemplar model — a concern that per-stage tracking would directly address. The final evaluation is reassuring but does not show _when_ or _how_ zero-shot performance evolves during training.

3. **AIM's adaptive weight relies on CLIP's probability calibration, which is not analyzed.**  
   The AIM weight α = p(y∈Y_e|I) is computed by summing CLIP's zero-shot probabilities over exemplar classes. This treats CLIP's probabilities as calibrated estimates of label-set membership — a strong assumption. The paper notes that in the Union+Zero-shot scenario (where ~91% of candidate labels are exemplar-covered), AIM can over-weight the exemplar model, but does not analyze whether this is a calibration issue or a fundamental limitation. A reliability diagram or sensitivity analysis (e.g., comparing against oracle α) would clarify whether the fusion mechanism or the probability estimate is the bottleneck.

4. **No statistical significance or multiple-seed results.**  
   The main results (Table 2, Table 3, Fig. 2–3) are reported without error bars or standard deviations. The paper states it uses "the same...seed" (line 286), suggesting single-run evaluation. Given the relatively small number of stages (e.g., 7 for data incremental), variance could be meaningful. This is standard practice for large-scale benchmarks but should be acknowledged.

5. **Key KNN hyperparameter (k) is not specified or analyzed.**  
   The paper uses k nearest neighbors for both KNN and TreeProbe inference (lines 133, 157) but never states the value of k or evaluates sensitivity to this choice. This matters because TreeProbe ensembles classifiers from the k nearest leaf nodes, and the behavior likely depends on k.

### Trivial

- The embedding-weighted averaging for exemplar predictions (lines 138–139, 160–161) is stated to "give better performance" without a supporting ablation or quantification. A brief comparison against using the majority-class text embedding directly would improve reproducibility.
- Hyperparameter values (learning rate, regularization, exact k) are not reported — the paper states "selected from a hyperparameter sweep" (line 278). These are easy to include.
- The choice of target vs. zero-shot datasets is justified primarily by sample size (>220k total for target tasks). A sentence on why ImageNet/DTD/UCF101 were chosen as zero-shot (e.g., generality, domain dissimilarity from targets) would help.

## Nice-to-Haves

- **Exemplar management under bounded memory:** The paper explicitly does not consider memory constraints (line 302). A discussion of how the exemplar set could be bounded (e.g., reservoir sampling per class) and its impact on tree probe accuracy would strengthen practical applicability.
- **Ablation of the embedding-weighted averaging:** A simple comparison between similarity-weighted text embedding and majority-class text embedding for the exemplar prediction would clarify whether this design choice is critical.
- **Calibration analysis for AIM:** Reliability diagrams for the p(y∈Y_e|I) estimate, or an ablation where α is set to the true oracle probability, would separate the quality of the estimate from the fusion design.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Missing related works (prompt-based methods should be compared):"** The paper discusses prompt-based methods (L2P, DualPrompt, CODA-Prompt) and gives concrete reasons they are unsuitable: they tend to overfit and lose generalization (line 61), and they require running through CLIP encoders, violating the efficiency goal (line 101). This is a reasoned dismissal, not an omission. Demanding empirical comparison against methods the paper argues are misaligned with the problem goals is scope creep.

- **"Memory constraints not considered is a weakness:"** The paper explicitly lists this as a limitation (line 302). The reviewer's request for exemplar management strategies is a nice-to-have extension, not a flaw in the presented work.

- **"Dataset selection seems arbitrary:"** The paper states that all target tasks collectively provide >220k samples "sufficient to give a reliable assessment" (line 225). This is a reasonable justification.

- **"Discussion of prompt-based methods is dismissive:"** The paper provides specific technical reasons (overfitting to task-specific prompts, efficiency cost). Dismissive yes, but it is _reasoned_ dismissal based on stated goals.

## Novel Insights

The reviews reveal that the paper's most distinctive contribution is not just the tree probe or AIM individually, but the specific design space it carves out: a system where the consolidated model is _never updated_ and the exemplar model is _never used alone_, but the two are fused via a lightweight membership-probability estimate derived from the consolidated model itself. This is a notably different philosophy from prior CLS-inspired methods (DualNet, FearNet, CLS-ER) that update both systems over time, and from ZSCL/WiSE-FT which fine-tune the consolidated model with regularization. Whether this frozen-CLIP + dynamic-fusion paradigm generalizes to other foundation models and modalities is an open question worth pursuing.

## Suggestions

1. **Add Tip-Adapter and WiSE-FT as baselines** on the ZSCL benchmark (Table 2). Tip-Adapter can be adapted by treating the task-incremental stream as sequential few-shot episodes. WiSE-FT can be evaluated by fine-tuning CLIP per stage with weight-space interpolation. This directly addresses the most significant empirical concern.

2. **Include a per-stage zero-shot accuracy plot** in the task incremental setting, alongside the target accuracy already shown. This would directly demonstrate whether zero-shot capability degrades as exemplars accumulate.

3. **Add a sensitivity analysis for the AIM weight α.** Either show reliability diagrams for p(y∈Y_e|I) or compare AIM performance against an oracle variant where α is set to 1 if the true label is exemplar-covered and 0 otherwise.

4. **Report the value of k** used in KNN and TreeProbe inference, and add a brief sensitivity analysis (e.g., varying k from 1 to 20) in the supplement.

5. **Run main results with at least 3 different seeds** and report means ± std. This is especially important for the data-incremental and class-incremental settings where random sampling introduces variability.

## Score and Decision

The paper presents a well-motivated, clearly described system with solid empirical support. The tree probe and AIM mechanisms are novel, practically useful, and convincingly demonstrated. The weaknesses are evidential gaps and missing details — not methodological flaws — and none threaten the core claims. With the suggested additions, the paper would be substantially stronger, but even in its current form it makes a clear contribution to open-vocabulary continual learning.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>