Now let me write the consolidated review.

## Summary

CausalNovo introduces a model-agnostic framework that incorporates causal principles into *de novo* peptide sequencing. The key idea is to encourage sequencing models to focus on signal fragment ions (b, y, a ions) and ignore spurious noise peaks, grounded in a Structural Causal Model from which the authors derive *independence* (invariance to noise perturbations) and *sufficiency* (retaining predictive information) objectives. The framework adds a Causality Extraction Module with contrastive learning on intervened spectra and cross-entropy losses, and is applied on top of three existing encoder-decoder models without changing their architecture. Results across three benchmark datasets (Nine-species, Seven-species, HC-PT) show consistent improvements of 2–14 absolute percentage points at the amino acid, peptide, and PTM levels.

## Strengths

- **Principled causal framing with clean implementation**: The SCM (Section 3.2, Figure 2A) is clearly presented, and the two derived principles (independence and sufficiency) map directly to concrete losses. The *do*-intervention on non-causal factors via replace-based perturbation (Section 3.4.1) is a domain-appropriate operationalization of causal intervention for spectral data, and the use of theoretical spectra to identify noise peaks leverages established domain knowledge.

- **Consistent gains across three baselines and three datasets**: Table 1 shows that CausalNovo improves CasaNovo, AdaNovo, and π-HelixNovo on all three datasets at amino acid, peptide, and PTM levels. The improvements are often large (e.g., +12.0 percentage points for CasaNovo on Seven-species AA precision, +14.2 for AdaNovo on HC-PT). This consistency across models and datasets directly supports the claim that the framework provides value beyond tuning any single architecture.

- **Multi-faceted evaluation beyond main results**: The paper provides a thorough empirical analysis: component ablation (Table 4) and intervention ablation (Table 5) confirm each piece contributes; cross-species validation (Table 3) shows generalization beyond the yeast test set; vulnerability analysis (Figures 1, 3) quantifies robustness to noise perturbations; NSR generalization (Figure 4) tests on naturally noisy rather than artificially perturbed spectra; and attention analysis (Table 7) provides mechanistic evidence that the model actually shifts focus toward causal peaks.

- **Open discussion of limitations**: The Conclusion explicitly acknowledges the ~2.3× training time overhead and the fact that the evaluation follows the NovoBench protocol rather than more realistic out-of-distribution settings used by some recent methods.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Numerical inconsistencies in reported improvement percentages**: In Section 4.3, the text reports that on Seven-species, CausalNovo improves π-HelixNovo by "+9.1%" in precision. However, from Table 1, the retrained π-HelixNovo baseline is 0.465 and CausalNovo is 0.536, giving a difference of 0.071 (7.1 percentage points), not 9.1%. Similarly, on HC-PT, the text reports "+9.0%" for CasaNovo, but 0.635 − 0.525 = 0.110 (11.0 percentage points). The raw numbers in the table are the primary evidence, and the overall claims remain supported, but these errors in the text erode confidence in the reporting. The authors should correct them and clarify whether they report absolute differences throughout.

- **No variance or confidence intervals**: All main results (Tables 1–5) appear to come from single runs. Reporting means and standard deviations over multiple seeds would strengthen the evidence, especially for the ablation results where differences are small (e.g., +0.4% from symmetric training). This is common in the field but still a notable omission.

- **Ground-truth dependence of the intervention is a structural limitation**: The causal intervention (Section 3.4.1) requires knowing which peaks are non-causal, which in turn requires the theoretical spectrum computed from the *true* peptide label. This means the method cannot be applied to unlabeled data or in a fully self-supervised manner. The paper partially addresses this by showing generalization on natural NSR variations (Figure 4) and cross-species (Table 3), but the limitation is inherent. It should be stated more prominently rather than just implied.

### Trivial

- **Some hyperparameter values not stated in the main text**: The tolerance threshold γ (Equation 4) and the replacement fraction α (Section 3.4.1) are not explicitly reported in the paper. These would help reproducibility.
- **PTM-level metrics are not formally defined**: The paper reports PTM-level precision and recall but does not specify exactly how a PTM prediction is scored as correct (e.g., correct amino acid + correct modification type?).
- **The attention analysis metric (Table 7) partially measures what was optimized**: Since "causal peaks" are defined as those matching the theoretical spectrum—the same criterion used during training—the improvement partly reflects optimization alignment, not an independent behavioral change. However, the gap (19% → 33% for three attended peaks) is substantial enough that it still supports the claim.

## Nice-to-Haves

- Visualizing the learned importance scores M for a few example spectra would make the "causal representation" concept more concrete and interpretable.
- A sensitivity analysis of the intervention hyperparameters γ and α would provide practical guidance for applying the framework to new datasets.
- Explicit comparison of the loss formulation to the prior causal disentanglement work of Chen et al. (2022) would clarify what is adapted versus newly introduced.

## Removed Points

- *"The paper does not discuss missing related work"* — Removed per instruction (cannot verify related work completeness without external sources).
- *"Formatting/style nitpicks"* — Removed per instruction (parser artifacts, not author errors).
- *"Reproducibility concerns about undisclosed hyperparameters"* — Removed as minor beyond the γ/α values noted above; most hyperparameters are reported.
- Generic concerns from the harsh critic about circularity of the attention analysis are retained in the Minor section but demoted from their original framing because the paper partially addresses this through NSR analysis (Figure 4), which tests on natural rather than artificial noise.
- *"The harsh critic's framing of the ground-truth issue as 'fundamental'"* — Retained but softened to Minor since it is an inherent property of supervised learning for this task, and the paper provides alternative validation (NSR, cross-species) that does not depend on the artificial intervention.
- Generic strengths from the Strength Finder about "addressing an important problem" — Removed as generic/superficial.
- Various speculative weaknesses about "what if the metric measures a proxy" — Removed as unfounded speculation.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective that the paper itself misses.

## Suggestions

1. **Fix the numerical errors** in Section 4.3 (π-HelixNovo Seven-species should be ~7.1%, not 9.1%; CasaNovo HC-PT should be ~11.0%, not 9.0%) and clarify that all percentage differences are reported as absolute percentage points.
2. **Report variance** over at least 3 random seeds for the main results (Tables 1, 4, 5). Even a single statement like "results are averaged over three seeds with standard deviations < 0.005" would help.
3. **State the γ and α values** explicitly in the main paper or in the experimental setup section.
4. **Define PTM-level metrics** precisely: is a PTM considered correct only if both the modified amino acid and the modification type match?

## Score and Decision

**Calibration procedure:**

**Round 1 (bracketing):** Three queries on "causal framework for peptide sequencing mass spectrometry proteomics" with score filters (‑1,3.5), (3.5,7.5), (7.5,11). Low-band anchors (scores 2.5–3.2) were clearly weaker papers with withdrawn/reject decisions. High-band anchors (8.0) were oral/spotlight-level contributions with broader scope. The paper clearly belongs in the middle band.

**Round 2 (narrowing):** Two queries targeting the (4.5,6.5) and (5.5,7.5) ranges on de novo peptide sequencing and causal representation learning for biological data. Key anchors:

- **ReNovo** (avg 6.5, accepted poster): Directly comparable de novo sequencing paper. Both papers show consistent improvements across benchmarks. ReNovo's weaknesses (novelty concerns about combining existing ideas, data splitting issues, no variance) are similar in severity to CausalNovo's. CausalNovo has a more principled contribution (causal framework) but slightly more presentational sloppiness (numerical errors). **Comparable or slightly better.**

- **SENA-discrepancy-VAE** (avg 6.0, accepted poster): Causal representation learning for biological data. Validated on a single dataset; some reviewers questioned novelty beyond prior CRL work. CausalNovo has broader empirical validation (3 datasets × 3 baselines) and a more practical contribution. **Slightly better.**

- **CrossNovo (Distilling NAT)** (avg 4.25, rejected): De novo sequencing. Criticized for being a straightforward engineering combination. CausalNovo's principled causal framing and stronger empirical evaluation are clearly superior. **Much better.**

**Final placement:** The paper sits between the 6.0 and 6.5 anchors. It is a well-motivated, empirically solid contribution with a genuine methodological advance (adapting causal principles to proteomics), let down slightly by avoidable numerical errors and the absence of variance reporting. Score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>