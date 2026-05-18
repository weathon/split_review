Now I have verified the paper content against all reviewer claims. Let me write the consolidated review.

## Summary

This paper formalizes the connection between Out-of-Distribution (OOD) detection and Conformal Prediction (CP) by showing that the empirical False Positive Rate used in OOD evaluation is an approximate p-value, which allows CP theory from Bates et al. (2022) to correct these metrics for finite-sample variability. It defines *conformal AUROC* and *conformal FPR@TPRβ* metrics that provide probabilistic conservativeness guarantees and demonstrates their effect on the OpenOOD and ADBench benchmarks. As a second direction, it explores using OOD scores (ReAct, Gram, KNN, Mahalanobis, ODIN) as non-conformity scores for CP, finding that some (KNN, Mahalanobis) can sometimes outperform classical softmax-based scores.

## Strengths

1. **Formalizes a clean conceptual bridge between OOD and CP**: The paper explicitly rewrites OOD detection evaluation in a hypothesis-testing framework (Section 4.1) and identifies the empirical FPR used in OOD metrics as an approximate p-value. This connection, while leveraging existing theory, is clearly articulated and enables the direct application of CP corrections to OOD benchmark metrics — a step beyond prior work that applied CP to OOD only for constructing prediction sets without establishing this two-way bridge.

2. **Defines well-motivated conformal metrics for OOD evaluation**: Conformal AUROC and conformal FPR@TPRβ (Section 4.4) are cleanly defined and provide probabilistic conservativeness guarantees that are genuinely useful for safety-critical applications. The paper correctly emphasizes that these are not "better" estimates but conservative ones, avoiding overclaiming.

3. **Effective empirical validation of the Beta-distribution phenomenon**: The SVHN experiment (Section 4.3.1, Figure 1) using 53 calibration folds convincingly demonstrates that the FPR fluctuations follow the predicted Beta distribution, with fitted parameters close to theoretical values. This grounds the abstract theory in a concrete, visual illustration.

4. **Application to two major benchmarks**: Demonstrating the correction on OpenOOD (Table 1) and ADBench (Figure 3) shows the practical relevance. The finding that the correction costs approximately 1–2% AUROC for OpenOOD (with larger effects for ADBench due to smaller test sets) is useful information for practitioners. The paper also correctly notes that the correction preserves the ranking of top baselines.

5. **Explores a genuinely open direction**: Section 5's investigation of OOD scores as non-conformity scores, while preliminary, opens a potentially fruitful avenue for CP research. The finding that KNN and Mahalanobis can sometimes outperform classical softmax-based scores is interesting and provides a concrete starting point for future work.

## Weaknesses

### Fatal
None. The paper's two main contributions are present, verifiable, and coherent. The reviewer concern about Section 5 being "unverifiable" is due to a parser artifact (Table 2 exists as an image in the original submission and contains the numeric results, which the paper's text also summarizes).

### Major

1. **Limited depth of the first contribution**: The analysis uses only the Monte Carlo correction with a single δ per benchmark (δ=0.01 for OpenOOD, δ=0.05 for ADBench). The paper mentions four correction functions (Simes, DKWM, Asymptotic, Monte Carlo) but does not compare their behavior — practitioners reading the paper would not know which correction to use or how the choice affects results. No sensitivity analysis to δ or calibration set size is provided. The ADBench results are shown only as aggregate scatter plots without per-dataset numeric tables, making it impossible to assess whether the correction changes per-dataset rankings. As a result, the paper's first contribution, while sound, reads as a proof-of-concept rather than a thorough investigation that would serve as a practical guide.

2. **Section 5 analysis is thin**: The exploration of OOD scores as nonconformity scores lacks depth. The adaptation of OOD scores to softmax-like scores via exp(s)/Σ exp(s) is introduced without justification — this transformation changes the score distribution in an unknown way, and its effect on CP validity is not examined. The results are described at a high level ("in some instances, some scores...perform better") without statistical significance tests, without per-coverage-level breakdowns (the paper mentions α ∈ {0.005, 0.01, 0.05} but does not show results broken down by coverage), and without analysis of *why* Mahalanobis and KNN work better (e.g., examination of the score distributions or resulting prediction set sizes). No comparison with other uncertainty-based scores (e.g., entropy, mutual information) is provided.

3. **The two contributions are loosely connected**: The paper presents CP→OOD (Section 4) and OOD→CP (Section 5) as two separate vignettes without a unified framework or synthesis. The claimed "cross-fertilization" and "synergy" are more of a juxtaposition than an integrated story. There is no discussion of how the corrected metrics from the first part could inform the use of OOD scores in the second part, or vice versa.

### Minor

1. **No discussion of assumption violations**: The paper mentions (line 76) that marginal validity assumes i.i.d. data and continuous score distributions, but does not discuss what happens when these are violated — e.g., discrete scores (common in some OOD methods) or non-exchangeable calibration data. The paper would benefit from acknowledging these limitations.

2. **The claim that the correction "does not significantly impact" top baselines is unsupported**: The paper states this without confidence intervals, hypothesis tests, or quantitative criteria. While the raw numbers (~1–2% AUROC drop) are shown, "significantly" is a claim about statistical and/or practical significance that is not formally established.

3. **SVHN experiment uses an unusually large calibration set (10,000 points)**: This is not representative of typical OOD benchmark validation sets, which limits the generalizability of the illustration. The Beta-distribution theory holds for any n_val, but the concrete visual demonstration uses a larger size than what practitioners would typically encounter.

### Trivial

- The abstract uses "FRP@TPRβ" (line 8) while the body consistently uses "FPR@TPR95" — a minor typo carried over from the abstract.
- The paper refers to "Table 5" in lines 207 and 209 when the table is labeled "Table 2" (line 203). These are presentation issues, not content problems.

## Nice-to-Haves

- A comparison of the four correction functions (Simes, DKWM, Asymptotic, Monte Carlo) on at least one benchmark, with varying δ and calibration set sizes, would turn the first contribution into a practical guide.
- Per-dataset numeric tables for ADBench results (even as supplementary material) would strengthen reproducibility.
- A discussion synthesizing the two directions — e.g., how conformally corrected scores from Section 4 could be used as non-conformity measures in Section 5, creating a closed loop.
- Ablation of the exp(s)/Σ exp(s) transformation in Section 5 to justify its use or compare with alternatives.

## Removed Points

These points were raised by reviewers but are removed or downgraded per guidelines:

- **"Section 5 is unverifiable / Table 2 has no entries"** — Removed. The table exists as an image in the original submission. This is a parser artifact, not a paper defect.
- **"The paper's Section 5 findings are 'vacillating statements'"** — Removed. The paper gives a clear, internally consistent finding: most OOD scores are inefficient for CP, but some (KNN, Mahalanobis) can sometimes outperform classical scores. This is a nuanced result, not a contradiction.
- **"Missing Section 2 / background section"** — Removed. Sections may have been stripped by the parser; the paper's exposition is coherent without it.
- **"The paper does not discuss assumptions (i.i.d., continuity)"** — Partially removed. The paper does mention these assumptions on line 76 ("if the x_i are i.i.d and the distribution of s(x) under the ID law is continuous"). The remaining valid concern about *violations* of these assumptions is kept as a Minor weakness.
- **"Fatal for the second claimed contribution"** — Downgraded. The severity label is overblown; the second contribution is present and verifiable, though thinner than ideal.
- **Reproducibility concerns about undisclosed hyperparameters / missing code** — Removed per guidelines; the experiments use standard benchmarks (OpenOOD, ADBench) and the paper states they run on a standard laptop CPU, making the experimental setup largely reproducible via existing public benchmark code.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective or insight that the paper itself does not already articulate.

## Suggestions

1. Deepen the first contribution by comparing the four correction functions, testing multiple δ values and calibration set sizes, and providing per-dataset numeric tables for ADBench. This would turn a proof-of-concept into a practical guide.
2. Expand Section 5 with: justification and/or ablation of the softmax-like score transformation, statistical significance tests, per-coverage-level breakdowns, analysis of why specific OOD scores work better (e.g., examining score distributions), and comparison with additional CP non-conformity scores.
3. Add a synthesis section connecting the two directions — e.g., discussing how the conformally corrected metrics from Section 4 could guide the selection or design of OOD-based non-conformity scores for CP, or how the findings from Section 5 inform the design of more reliable OOD evaluation.

## Score and Decision

The paper makes a genuine conceptual contribution by formalizing the OOD-CP connection and demonstrates it on standard benchmarks. The first contribution is sound but analysis is limited in depth; the second contribution is interesting but preliminary. The weaknesses are real but not fatal, and the core ideas have clear value to both communities. The paper would benefit from expansion but is publishable in its current form at a venue that values cross-domain connections and practical tools.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>