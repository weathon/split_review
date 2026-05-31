Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes a two-step test-time adaptation (TTA) method for GNNs. First, BN statistics (mean/variance) are adapted using a JS-divergence-based weighting matrix *A* and a learnable binary mask *M*. Second, BN scale/shift parameters are refined via an energy-based model (EBM) with entropy- and confidence-filtered pseudo-labels. Experiments span 7 datasets and 3 backbones, showing competitive accuracy.

## Strengths

1. **Consistent top-tier accuracy across diverse settings.** Table 1 shows the method achieves best or second-best accuracy on most of the 21 dataset×backbone combinations, with several clear-margin gains (e.g., +2.84% Cora/GCN, +2.60% Elliptic/GraphSAGE). This directly supports the claimed out-of-distribution improvement.

2. **Principled data-driven BN statistic weighting.** Rather than tuning the mixing weight α by grid search (standard in prior work), Section 3.1 computes α per BN dimension via JS-divergence between non-parametrically estimated activation distributions from training and test data. The learnable binary mask *M* (Eq. 5–6) further allows selective dimension-level adjustment. The ablation (Table 2, "BNSA w/o A" and "BNSA w/o M") confirms both components contribute.

3. **EBM-based BN parameter refinement as an alternative to entropy minimization.** Section 3.2 replaces standard entropy minimization with a joint energy-based objective (Eq. 10–14) combined with entropy and confidence-based pseudo-label filtering (Eq. 15–16). Ablation results (Table 2, "BNPA w/o CEselc") support the claim that filtering unreliable pseudo-labels matters.

4. **Thorough empirical scope.** The evaluation covers 7 datasets (incl. OGB-Arxiv, OGB-Products) with varied distribution shifts, 3 GNN backbones (GCN, GraphSAGE, GAT), and 7 SOTA baselines spanning statistic modification, parameter optimization, and input augmentation.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Ambiguous description of mask learning phase.** Section 3.1 says "In the training process, the modified BN layers are in Eq. 6" and then "During test-time adaptation (TTA), the modified BN layers operate as shown in Eq. 6" (lines 117–118). This dual reference creates confusion about whether the Bernoulli mask variables *B* are learned during pre-training or during TTA. Line 125 ("We employ contrastive learning for training at test-time adaptation") clarifies it happens during TTA, but the inconsistent phrasing undermines readability and will confuse readers. The method as described works correctly, but the text needs tightening.

2. **No variance metrics for any reported result.** All results are reported as 10-run averages without standard deviations or confidence intervals (lines 229, 239). Several gains are small (<1–2 pp on some datasets). Without error bars it is impossible to assess whether these differences are meaningful or within run-to-run noise. Given the added complexity (storing per-dimension distributions, mask learning, SGLD sampling), this is a significant omission for calibrating the reader's trust in the reported margins.

3. **SGLD hyperparameters unspecified and "closest sample" selection unjustified.** The paper defines δ (step size) and T (number of steps) for SGLD (Eq. 13, line 193) but never gives their experimental values. The deviation from standard JEM/PCD — selecting the SGLD sample whose energy is closest to the real sample (line 193) — is introduced without any theoretical or empirical motivation. A reader cannot reproduce or assess the method without these details.

4. **Pseudo-label filtering thresholds with no guidance.** Three thresholds (τ_e, τ_c¹, τ_c²; Eqs. 15–16) control entropy-based selection and confidence-based filtering. The visible text provides no discussion of how these are set, no sensitivity analysis, and no ablation showing their individual impact.

5. **Activation distribution representation not specified.** The JS-divergence computation (Eqs. 3–4) requires per-dimension activation distributions P_m and P_n. The paper mentions a "small histogram matrix" (line 29) but does not specify how the distributions are binned or stored, making it impossible to assess the storage/computation overhead claimed to be small.

### Trivial
- The notation `\hat{\mu}` and `\hat{\sigma}` is used for both moving-average training statistics (Section 2.2) and the adapted TTA statistics (Eq. 9), which may cause confusion. Using distinct symbols would help.

## Nice-to-Haves
- A wall-clock time comparison against simpler baselines would contextualize the added computational cost of SGLD sampling and per-dimension distribution storage.
- An ablation on the number of SGLD steps *T* would help readers understand the accuracy-cost trade-off.

## Removed Points

These points surfaced in the reviews but are removed after verification:

1. **"Mask learning timing is a structural/fatal flaw"** — The paper's line 125 ("contrastive learning for training at test-time adaptation") and the loss optimization at lines 131–137 make clear the mask is learned during TTA. The ambiguous phrasing in lines 117–118 is a presentation issue, not a method flaw.

2. **"Missing calibration evidence"** — The paper references "Section 4.4" (line 255) for calibration results. Section 4.4 is stripped by the parser; its content exists in the original submission. Per policy, parser-stripped content is not treated as missing.

3. **"Missing fixed-α baseline"** — The paper explicitly states "Using a fixed weight instead of our proposed distribution shift-based approach negatively impacts performance" (line 255), confirming this comparison was performed.

4. **"Baseline fairness (a-BN/DUA designed for images)"** — These methods are architecture-agnostic BN statistic modification techniques. Applying them to GNNs with published settings is standard practice.

5. **"GTRANS comparison concern"** — The paper acknowledges the different adaptation space by categorizing GTRANS under "Input augmentation" separately from parameter-based methods (line 237).

6. **"Missing related works"** — Per policy, this is not assessed without external sources to verify.

7. **Parser-stripped content complaints** (missing figures, tables, Section 4.4) — These are parser artifacts, not author errors.

8. **Formatting/typo nitpicks** — Parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The two-phase approach (statistics then parameters) combined with distribution-aware weighting for BN statistics is the paper's main novel idea; the reviews do not surface a deeper insight about GNN TTA that the authors themselves missed.

## Suggestions

1. Clarify the mask learning phase: explicitly state that Bernoulli variables *B* are optimized during TTA via the contrastive + KL loss (Eq. 8), and remove or rephrase "In the training process" when referring to Eq. 6 to avoid confusion with the original pre-training phase.

2. Add standard deviations or 90% confidence intervals to all main results and ablation tables. If the 10-run seeds are available, report the range or std σ.

3. Report SGLD hyperparameter values (step size δ, number of steps T) and provide a brief justification for the "closest sample" selection rule (line 193) — e.g., does it reduce gradient variance or stabilize EBM training?

4. Specify how activation distributions are represented for JS-divergence computation (histogram bin count, bin range, storage format, memory per BN dimension) to enable reproducibility.

## Score and Decision

**Originality:** Moderate. Combining JS-divergence weighting + learnable mask + EBM refinement for GNN TTA is novel, though each component individually is known.

**Importance of research question:** Relevant — GNN TTA under distribution shift is an open problem.

**Claims support:** Accuracy claims are supported by broad experiments, though lacking variance metrics. Calibration claims are referenced to a parser-stripped section. Some design choices (closest-sample selection, threshold values) lack justification.

**Soundness of experiments:** Reasonable scope (7 datasets, 3 backbones, 7 baselines), but missing error bars is a notable gap for assessing small-margin gains.

**Clarity of writing:** The mask learning description is ambiguous. Otherwise reasonably clear, though some implementation details are omitted.

**Value to the community:** A usable contribution to GNN TTA, but the marginal gains and missing variance information limit immediate impact.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>