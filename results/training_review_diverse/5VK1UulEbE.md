Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes FredNormer, a plug-and-play frequency-domain normalization module for non-stationary time series forecasting. It provides a theoretical analysis showing that time-domain normalization (z-score) uniformly scales all non-zero frequency components, motivating a frequency-aware approach. FredNormer computes a frequency stability metric (mean/standard deviation of amplitudes across training samples) and uses a learnable linear weighting layer to up-weight stable frequency components and suppress unstable ones. Experiments on seven datasets with DLinear, PatchTST, and iTransformer backbones show improvements over the bare backbone and over existing normalization methods (RevIN, SAN).

## Strengths

1. **Formal theoretical motivation.** Lemma 1 and Theorem 1 rigorously prove that z-score normalization in the time domain uniformly scales all non-zero frequency components and preserves the energy proportion between stable and unstable subsets. This is a clean formal insight that (a) is absent from prior normalization works (RevIN, SAN) and (b) legitimately motivates the need for frequency-selective weighting.

2. **Clear and practical method design.** FredNormer is well-described: compute a stability statistic S(k) = μ(A(k))/σ(A(k)) across the training set, transform each sample via DFT, apply a learned affine transformation based on S(k) to the spectrum, then invert. The method adds minimal parameters (two linear layers per frequency) and is explicitly designed as a plug-and-play module compatible with any backbone. The efficiency advantage over SAN (60–70% speedup in 16/28 settings, Figure 4) is a genuine practical benefit.

3. **Directionally positive empirical results.** In the main comparison against RevIN and SAN (Table 2), FredNormer ("Ours") achieves the best MSE in 8 out of 14 settings when used alone, and the best MSE+MAE in 18 out of 28 settings. The improvements over RevIN and SAN are sometimes modest (3–5% relative) but consistent across datasets, and on specific datasets (e.g., Traffic with iTransformer: 0.424 vs SAN 0.520, an 18.5% improvement) the gains are substantial.

4. **Ablation supports the stability metric over simple alternatives.** Table 3 shows that replacing the stability metric with a low-pass filter or random frequency selection (as in FEDformer) consistently yields worse MSE across all datasets and horizons tested (e.g., ETTh1/DLinear/horizon96: 0.371 vs 0.379 low-pass vs 0.393 random). This provides meaningful evidence that the data-driven stability weighting contributes beyond trivial alternatives.

5. **Visualization provides interpretability.** Figure 3 plots the stability measure alongside input and target amplitudes, showing that the metric assigns higher weights to frequency components that are consistent between input and target, even when those components have low absolute magnitude. This helps build intuition for why the method works.

## Weaknesses

### Fatal
None.

### Major

1. **Missing PatchTST from the main baseline comparison (Table 2).** The paper states it evaluates on three backbones (DLinear, PatchTST, iTransformer) with all three normalization methods (FredNormer, RevIN, SAN) — yet Table 2, the primary comparison table, only shows DLinear and iTransformer. PatchTST, one of the most widely used TS forecasting backbones, is entirely absent from the comparison against existing normalization methods. Table 1 shows PatchTST+Ours vs Ori (bare backbone), which is not a substitute. This is a significant methodological gap: the claimed generality across backbones is not adequately supported for PatchTST, and a reader cannot assess how FredNormer compares to RevIN/SAN on this backbone. The paper should include PatchTST+RevIN and PatchTST+SAN in Table 2.

2. **Headline improvement claims are inflated by comparison against an ambiguous baseline.** The paper prominently reports "33.3% and 55.3% MSE reduction on ETTm2" in the abstract, introduction, and conclusion. These numbers come from Table 1, which compares "+ Ours" against "Ori." What "Ori" means is not defined — it appears to be the bare backbone without any normalization. Comparing against a no-normalization baseline inflates the apparent gains; when compared against proper baselines (RevIN, SAN) in Table 2, the improvements on ETTm2 drop to 3–13% relative (e.g., iTransformer: 0.283 vs 0.287 SAN). While reporting raw-backbone improvement is not unreasonable as a secondary result, leading with these numbers as the headline claim without caveat gives a misleading impression of the method's advantage over existing practice. The paper should lead with the fair comparisons (Table 2) and place the "Ori" comparison in secondary position.

### Minor

1. **Ambiguous z-score normalization pipeline.** Line 425 states: "We combine our module with a z-score normalization-denormalization operation in all experiments." It is unclear whether "all experiments" includes the baseline methods (RevIN, SAN). If so, stacking z-score on top of RevIN/SAN is unusual and the comparison may be unfair. If not, the statement is ambiguous. The paper should specify exactly which preprocessing pipeline applies to each method.

2. **Running time comparison only against SAN.** Figure 4 compares FredNormer's per-epoch time against SAN, but not against RevIN. Since RevIN is the most common lightweight normalizer (and the paper claims efficiency as a selling point), including RevIN in the runtime comparison is necessary to contextualize the efficiency claims. FredNormer is almost certainly slower than RevIN but faster than SAN — the paper should state this explicitly.

3. **Ablation covers limited alternatives.** The ablation (Table 3) compares the stability metric against a low-pass filter and random selection. While these are reasonable baselines, stronger comparisons would include: (a) the stability measure *without* the learnable weighting layer, (b) a learned weight that is *not* based on stability (e.g., a fixed learned frequency mask), or (c) alternative frequency significance criteria (energy ratio, spectral entropy). Without these, it is unclear how much of the benefit comes from the stability metric itself versus the learnable weighting architecture.

4. **No discussion of limitations.** The paper does not discuss when or why FredNormer might fail. For example: the stability metric assumes that stable frequencies in the training set remain stable at test time (may fail under regime shifts), the DFT assumes periodic boundaries (may not hold for non-stationary signals), and the 1-D differencing step could amplify high-frequency noise. A brief limitations section would strengthen the paper.

5. **Hyperparameter details not reported.** The paper does not specify training hyperparameters (learning rate, scheduler, epochs, batch size) beyond mentioning a single A6000 GPU. Standard deviations are reported in some tables (1 and 3) but not in the main baseline comparison (Table 2), making it harder to assess the significance of small gaps.

### Trivial

1. **Minor inconsistency in the introduction.** Line 81 states "such as Traffic, we improved PatchTST and iTransformer by 33.3% and 55.3%," but these exact percentages correspond to ETTm2 in Table 1 (line 427), not Traffic (where improvements are ~26–31%). The paper should correct this to ETTm2.

2. **The 1-D differencing step** (Algorithm 2, line 235) is mentioned as "smoothing" (line 294) but not motivated or ablated. A brief justification or ablation of this step would be helpful.

3. **k=0 handling.** Algorithm 2 loops from k=1 to K-1, skipping the DC component — this should be explicitly noted in the text.

## Nice-to-Haves

- A synthetic experiment where non-stationarity is introduced at known frequencies, to test whether the stability metric correctly identifies and suppresses them.
- Analyze which frequencies are deemed stable/unstable across datasets and relate them to known periodicities.
- Hyperparameter sensitivity analysis (e.g., initialization of the linear weighting layer, sensitivity to the number of frequency components selected).

## Removed Points

These points are flagged to be removed; treat them with caution:
- **"Ours* is counted among these top-1 results"** — Factually incorrect. The Count row in Table 2 clearly separates Ours (18 top-1) and Ours* (11 top-1). The paper's text (line 589) explicitly says "Ours." Removed as factually wrong.
- **"Paper does not explain why two separate linear projections are needed"** — The paper does explain this at line 315: "they correspond to different basis functions." The reviewer apparently missed this sentence. Removed as factually wrong.
- **"Lemma and Theorem are elementary, not new insights"** — Pure opinion/nitpick. The contributions of these results are in their application to motivate the method, not in mathematical novelty. Removed.
- **"The paper should note that CV is not a novel metric"** — The paper already cites CV references (lines 67–68). Removed as the paper already does what is requested.
- **"Definition 1 is not novel"** — The paper never claims the metric is fundamentally new; it credits CV literature. Removed.

## Novel Insights

Beyond the paper's own contributions, the reviews surface the observation that the paper's strongest empirical signal is arguably the **consistency** of FredNormer's advantage: in Table 2, Ours (FredNormer alone) achieves the best or second-best result in nearly every setting, even when the margin is small. This consistency across datasets, backbones, and horizons is more compelling than any single large percentage, and is what the authors should foreground. The existing literature's focus on time-domain statistics (RevIN's mean/var, SAN's sub-series statistics) appears to miss the frequency-domain insight that different frequencies contribute unequally to generalization — and the paper provides a reasonable first cut at capturing this.

## Suggestions

1. **Add PatchTST to Table 2.** This is the single most impactful fix: show PatchTST+RevIN and PatchTST+SAN alongside PatchTST+FredNormer. This would immediately strengthen the claim of backbone generality.
2. **Clarify "Ori" and the z-score pipeline.** Define what "Ori" means explicitly. Specify whether z-score normalization is applied to baselines. If the paper's "all experiments" includes baselines, separate the pipeline descriptions clearly.
3. **Reframe the headline numbers.** Lead with the fair comparisons (FredNormer vs RevIN vs SAN from Table 2) and relegate the "Ori" comparison to a supplementary/secondary position. The 33.3%/55.3% figures in the abstract create an unrealistic expectation.
4. **Strengthen the ablation.** At minimum, compare the full FredNormer against (a) the stability metric without the learnable weighting layer (i.e., hard selection of top-M stable frequencies), and (b) a learned but non-stability-based frequency weighting (e.g., learn a per-frequency weight directly without the stability prior).

## Score and Decision

This paper proposes an interesting and well-motivated idea — frequency-domain normalization with a stability-based weighting scheme — supported by a clean theoretical observation and a clear method description. However, the empirical validation has two structural gaps: (1) a major backbone (PatchTST) is absent from the primary baseline comparison, and (2) the headline performance claims are inflated by comparison against an ambiguous baseline. These issues prevent the paper from convincingly establishing its contribution in its current form, but they are fixable with revisions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>