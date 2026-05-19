Now I have sufficient calibration data. Let me write the consolidated review.

**Calibration summary:**
- **Round 1 bracket:** Between 4.0 and 5.5 based on CARPRT (4.00, Poster), FGA (5.00, Poster), PEA (5.50, Poster)
- **Round 2 narrows:** AutoCLIP is stronger than CARPRT (per-image operation, broader evaluation, controlled analysis), comparable to FGA (simpler method, weaker gains), and slightly weaker than PEA (tackles harder problem, stronger results, but requires source statistics). This places the paper at **5.0**.
- The paper is a clean, practical contribution with thorough evaluation but modest improvements. Not a breakthrough, but solid.

---

## Summary

This paper proposes AutoCLIP, a method that reweights prompt templates per-image at inference time for zero-shot classification with vision-language models like CLIP. Instead of averaging all class descriptors uniformly, AutoCLIP performs one step of gradient ascent on a logsumexp objective to emphasize prompts whose descriptors are more similar to the image embedding, then uses entropy-controlled step-size tuning to avoid dataset-specific hyperparameters. The method is evaluated on 7 datasets, 6 VLMs, and 3 prompt strategies (990 settings total), showing a 0.45 pp average improvement over uniform weighting, with gains in ~85% of settings.

## Strengths

1. **Extensive and systematic evaluation**: AutoCLIP is tested across 7 datasets (including ImageNet variants), 6 VLMs (CLIP variants, DataComp, CoCa), and 3 prompt construction methods (CLIP, DCLIP, WaffleCLIP) with K ranging from 4 to 500. Results are averaged over 7 runs with standard errors reported — this breadth supports the claim of broad applicability (Figure 2, Table 1).

2. **Controlled analysis provides mechanistic insight**: The synthetic embedding experiment (Section 5, Figure 7) systematically varies class-prompt entanglement and instance noise, showing that AutoCLIP outperforms mean and max aggregation for moderate-to-high entanglement and matches mean aggregation for low entanglement. This explains the empirical trend of larger gains on smaller VLMs and provides a testable hypothesis for when the method works best.

3. **Principled entropy tuning eliminates dataset-specific hyperparameters**: The bisection-based step-size selection (Section 3.4) converts the dataset-dependent step-size α into a globally interpretable entropy reduction factor β, with ablation (Figure 4) showing robustness in the range [0.7, 0.9]. This is critical for zero-shot settings where labeled validation data is unavailable.

4. **Interpretable weight patterns confirm the core intuition**: Figure 6 shows that templates like "A tattoo of..." get consistently low weights on Food101 while "A photo of..." gets high weights, with weights varying meaningfully across classes. This visual evidence directly supports the paper's motivating intuition.

## Weaknesses

### Fatal
None.

### Major

1. **No empirical comparison to the test-time adaptation methods the paper positions itself against.** The Introduction and Related Work explicitly contrast AutoCLIP with TPT (Shu et al.), RLCF (Zhao et al.), and ZPE (Allingham et al.), arguing for lower cost and single-sample operation. Yet none of these methods appear in the experiments. Without even a small-scale comparison (e.g., TPT on 3–4 datasets with a standard ViT-B/16), the reader cannot assess whether the claimed practical advantages come at a meaningful accuracy cost. The paper would be significantly stronger with this comparison added.

2. **Runtime overhead is claimed but never measured.** The paper repeatedly describes AutoCLIP's overhead as "minor" and "essentially free" (Abstract, Section 3, Conclusion), but provides no wall-clock times, FLOPs, or latency numbers. The method requires computing a closed-form gradient (O(K²C)), running bisection, and recomputing class queries. For K=500 and C=1000 (ImageNet scale), this is non-negligible. Without quantification, the practical advantage over competing approaches cannot be evaluated.

### Minor

1. **Modest average improvement with notable failure cases.** The average gain is 0.45 pp, which is genuine but small. EuroSAT shows consistent negative Δ across several models (Table 1), and the two ViT-L/14 variants on ImageNet-C have negative Δ (Figure 3). The paper offers hypotheses for these failures but no diagnostic analysis (e.g., similarity distributions, weight behavior) to verify them.

2. **β hyperparameter inconsistency.** The paper defaults to β=0.85 throughout the main experiments but then states in the ablation (Section 4) that β=0.7 "performs favorably" and "we recommend this choice for future work." While the sensitivity analysis shows robustness to β, this inconsistency between the default and the recommended value is confusing.

3. **Softmax weighting baseline omitted from the main ablation.** The controlled experiment (Figure 7) includes softmax weighting (weights ∝ exp(τ·s̄ᵢ)), which is computationally cheaper than AutoCLIP (no gradient, no bisection), but this baseline is absent from the main ablation (Figure 5). Including it would disentangle the effect of gradient-based optimization from simple reweighting.

### Trivial

- Table 1 shows only the Δ accuracy in parentheses without the baseline's absolute accuracy, making it harder to assess the practical significance of the gains on individual settings.

## Nice-to-Haves

- Statistical significance tests (e.g., paired t-tests) for the main results would help distinguish reliable gains from noise, especially for the small Δ values.
- A discussion of why the logsumexp objective (which maximizes a soft maximum of similarities) tends to increase the correct class's similarity relative to incorrect ones would strengthen the theoretical motivation.

## Removed Points

These points were flagged by reviewers but are removed for the reasons stated:

- **"Objective function is not clearly justified for classification accuracy"** — The paper provides empirical justification (Figure 5 shows logsumexp outperforms mean, max, and entropy across all datasets) and a clear motivation as a "smooth compromise between max and mean aggregation." The paper is an empirical systems contribution, not a theoretical optimization paper; the empirical validation is sufficient.
- **"Number of bisection iterations not given"** — Implementation detail inappropriate as a review weakness.
- **"Upper bound of 10¹⁰ is ad hoc"** — The paper states this works for all settings considered and the monotonicity ensures bisection will terminate. Minor speculation.
- **"Controlled setting parameters are small"** — The controlled experiment is clearly positioned as a simplified mechanistic study ("strongly simplified") to understand trends; its role is illustrative, not definitive.
- **"Missing open-source code"** — Not appropriate to cite as a weakness; code release is independent of paper quality.
- **Various formatting/typo/stylistic nitpicks** — These are parser artifacts, not author errors.
- **"Missing comparison to softmax weighting in main ablation"** — Kept as minor weakness above but downgraded from how it was framed since the controlled experiment does include it.
- Several generic strengths from the Strength Finder (e.g., "Fully unsupervised, minimal computation overhead" — the overhead claim is not measured, so this strength is partially unsupported; "Hyperparameter-free" — the β inconsistency weakens this claim).

## Novel Insights

None beyond the paper's own contributions. The synthetic controlled experiment (varying entanglement and instance noise to explain when reweighting helps) is the most novel analytical contribution — it goes beyond typical ablation studies by proposing a concrete mechanism.

## Suggestions

1. **Add a direct comparison to at least one test-time adaptation method** (TPT would be the most natural choice) on 3–4 datasets with a standard ViT-B/16 backbone. Even a single well-motivated configuration would establish whether AutoCLIP's accuracy is competitive.

2. **Report wall-clock inference time** per image (or relative slowdown vs. uniform weighting) for a few K values (e.g., K=10, 50, 100, 500) to substantiate the "minor overhead" claim.

3. **Resolve the β inconsistency** by either adopting β=0.7 as the default (and updating main experiments) or providing a clear rationale for keeping 0.85 despite recommending 0.7.

4. **Add the softmax weighting baseline** to the main ablation (Figure 5) to clarify whether the gradient update adds value beyond any reweighting.

5. **Show baseline absolute accuracies** alongside Δ in the main table for easier interpretation.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>