Now I have all the calibration data I need. Let me finalize my review and score.

**Comparison with anchors:**
- **ReNovo (6.50, Accept)**: Directly comparable — same task, same datasets. CausalNovo has more thorough evaluation (vulnerability analysis, NSR, attention, cross-species) and model-agnostic design. Both face capacity-matching concerns. CausalNovo has an additional weakness in the AdaNovo retraining inconsistency. Roughly comparable or slightly above.
- **CL-MFAP (5.75, Accept)**: CausalNovo clearly stronger — more baselines, more datasets, more analysis.
- **Neural Causal Graph (6.25, Accept)**: CausalNovo has more thorough evaluation. Comparable quality.
- **Weak anchors (3.0-3.67)**: CausalNovo is clearly much better — consistent improvements, multiple baselines, thorough evaluation.
- **Strong anchors (8.0)**: CausalNovo is below these — no wet-lab validation, narrower scope.

**Round 1 bracket: 5.5–7.0. Round 2 narrows to 6.0–6.5.** CausalNovo sits slightly above ReNovo (6.50) in evaluation thoroughness but has the retraining inconsistency weakness. I'll settle on **6.5**.

## Summary
CausalNovo is a model-agnostic framework that integrates causal reasoning into de novo peptide sequencing by adding a Causality Extraction Module (CEM) to existing models. It uses contrastive learning on perturbed spectra (independence objective) and a purification loss to encourage models to rely on causal signal peaks rather than spurious noise peaks. Evaluated across three baselines (CasaNovo, AdaNovo, π-HelixNovo) and three benchmark datasets, it demonstrates consistent improvements of up to ~14% in amino acid precision along with robustness to varying noise conditions.

## Strengths
- **Well-motivated empirical vulnerability analysis**: Figure 1 systematically perturbs noise peaks in three pre-trained models and demonstrates significant precision degradation, directly and quantitatively establishing the spurious correlation problem before proposing a solution. This is a strong, domain-grounded motivation.
- **Consistent model-agnostic improvements across all baselines and datasets**: Tables 1–2 show CausalNovo improves all three baselines across all three datasets at amino acid, peptide, and PTM levels. Improvements range from ~2% to ~14% and are consistent in direction.
- **Multi-faceted evaluation beyond accuracy**: The paper includes vulnerability analysis (Figures 1, 3), NSR robustness analysis (Figure 4), cross-species validation (Table 3), attention analysis (Table 7 showing causal peak attention increases from 19.26% to 32.87%), and ion-type robustness (Table 6). This is unusually thorough for the domain.
- **Honest about limitations**: The paper acknowledges the 2.3× training overhead, the training-time-only nature of causal intervention, and the limitation of the NovoBench evaluation protocol vs. more realistic OOD settings.

## Weaknesses

### Fatal
None.

### Major
- **Missing capacity-matched control ablation**: The CEM adds 3 Transformer layers (512 hidden dim, 8 heads, FFN 1024) + MLP head on top of the 9-layer encoder (Section 4.2, line 221: "The causal extraction module contains 3 Transformer layers followed by an MLP head"). This represents a ~33% increase in Transformer-layer parameters. Table 4 ablates training objectives incrementally but never tests the CEM architecture alone (3 extra layers + MLP with only the baseline CE loss). Without this control, improvements cannot be cleanly attributed to the causal mechanism rather than added capacity. The attention analysis (Table 7) partially mitigates this by showing causal focus shifts, but doesn't rule out that the extra capacity alone could improve attention patterns.
- **Retraining inconsistency for AdaNovo inflates some improvement claims**: AdaNovo's retrained performance degrades from published 0.698 → 0.681 (−1.7%) on Nine-species AA precision (lines 131–132), while CasaNovo improves (+4.4%) and π-HelixNovo stays stable (0.765). The +6.3% CausalNovo improvement over AdaNovo is measured against this weakened baseline; against the published number it would be +4.6%. The paper does not explain why retraining hurts AdaNovo, and since all CausalNovo results are relative to retrained baselines, this inconsistency affects reported gain magnitudes.

### Minor
- **"Sufficiency" principle restates the baseline training loss**: The paper acknowledges this explicitly (line 260: "the sufficiency principle... is already included in the baseline model"). While honest, presenting the standard CE loss as one of two "fundamental principles" derived from the SCM somewhat overstates the novelty framing. The genuine new objectives are the independence contrastive loss and purification loss.
- **Hand-wavy justification for purification objective**: The claim that maximizing I(z_s; Y) "can indirectly lead to the purification of z_c" (line 97) lacks a formal argument. The reasoning could equally suggest the masking mechanism becomes less selective or that Y-relevant information is redundantly encoded in both branches. No empirical analysis of the M distribution is provided. The +0.8% improvement is real but the mechanism explanation is speculative.
- **Ablations conducted only on CasaNovo**: Tables 4–5 only test components on CasaNovo. Given that improvement magnitudes vary substantially across baselines (+2.2% to +14.2%), results may not generalize to other base models.
- **No variance estimates**: No standard deviations, confidence intervals, or multi-seed results are reported anywhere. Given improvement magnitudes of 2–14%, understanding variance is important for interpreting significance.

### Trivial
None.

## Nice-to-Haves
- Analysis of the masking mechanism M distribution: does it correlate with known signal/noise peaks? does the purification loss change the distribution?
- Comparison of improvements on low-noise vs. high-noise test spectra to clarify why CausalNovo helps on clean data.
- Wall-clock training time comparison (2.3× is mentioned but absolute times are not provided).
- Ablation on at least one additional baseline beyond CasaNovo.

## Removed Points
These points are flagged to be removed, treat them with caution:
- The figure caption labeling "C (charge state)" vs. text "C (causal factors)" was flagged but appears to be a parser artifact in the Figure 2 description, not an actual paper error. The paper consistently uses C for causal factors.

## Novel Insights
The paper's most notable contribution beyond its specific results is demonstrating that causal reasoning frameworks from the causal ML literature can be productively applied to domain-specific sequence prediction problems in proteomics. The vulnerability analysis methodology (systematically perturbing noise peaks and measuring degradation as a function of m/z tolerance) provides a reusable diagnostic tool for assessing spurious correlation dependency in any de novo sequencing model. The finding that a model-agnostic causal intervention framework can transfer across architecturally diverse baselines (encoder-decoder, conditional mutual information, spectrum augmentation) is a useful empirical contribution.

## Suggestions
- Add a capacity-matched control: replace the CEM with 3 plain Transformer layers + MLP trained only with the baseline CE loss to isolate the causal mechanism's contribution from added capacity.
- Report results against the published AdaNovo numbers as an additional comparison point and discuss why retraining degrades its performance.
- Analyze the learned importance scores M: their distribution, correlation with known signal/noise peaks, and sensitivity to the purification loss.
- Add multi-seed variance estimates for at least the main results table.

## Calibration Report

**All anchors retrieved:**

| Round | Path | Avg Score | Comparison |
|-------|------|-----------|------------|
| 1 | qi5dkmEE91 | 3.00 | Motif Explainer for TF binding — much weaker, rejected |
| 1 | AvXrppAS2o | 3.00 | Causal structure learning for medical prediction — much weaker, rejected |
| 1 | PoB6QGAM38 | 3.00 | Causal explanations for DNN — much weaker, rejected |
| 1 | fSxiromxAq | 3.00 | Sparse causal model — much weaker, rejected |
| 1 | nmvmPIi185 | 6.25 | Neural Causal Graph — comparable quality, CausalNovo has more thorough evaluation |
| 1 | ctvVXwUlnw | 5.25 | Causal framework for IQA/DNN robustness — CausalNovo clearly stronger |
| 1 | Q0s6kgrUMr | 6.67 | Robust causal/anticausal detection — theoretical focus, less evaluation |
| 1 | 7Fh57rIpXT | 3.67 | Causal mechanisms for algorithm selection — much weaker |
| 1 | k38Th3x4d9 | 8.00 | Granger causal root cause analysis — stronger, broader scope |
| 1 | zMPHKOmQNb | 8.00 | Protein discovery dWJS — much stronger with wet-lab validation |
| 1 | 0ctvBgKFgc | 8.00 | ProtComposer — much stronger, broader capabilities |
| 1 | I4e82CIDxv | 8.00 | Sparse feature circuits — much stronger, broader impact |
| 2 | 34xYxTTiM0 | 5.50 | Calibration optimization — CausalNovo clearly stronger |
| 2 | FM21yYBhuE | 5.00 | Equally Critical samples — CausalNovo clearly stronger |
| 2 | uBU33YNVL3 | 5.25 | Bounded loss robustness — CausalNovo clearly stronger |
| 2 | sejvgf030w | 5.25 | Flexible unknown rejection — CausalNovo clearly stronger |
| 2 | uQnvYP7yX9 | 6.50 | **ReNovo** — directly comparable (same task, same datasets); CausalNovo has more thorough evaluation but also has the retraining inconsistency weakness |
| 2 | fv9XU7CyN2 | 5.75 | CL-MFAP — CausalNovo clearly stronger |
| 2 | xJDxVDG3x2 | 6.33 | MolSpectra — comparable quality |
| 2 | 760br3YEtY | 5.60 | PEEP enzyme promiscuity — CausalNovo stronger |

**Round 1 bracket: 5.5–7.0.** The paper is clearly above the rejected 3.0–3.67 anchors and below the 8.0 anchors. It sits in the range of accepted papers with thorough but not exceptional contributions.

**Round 2 narrowing: 6.0–6.5.** The most directly comparable anchor is ReNovo (6.50), which addresses the same task on the same datasets. CausalNovo provides more thorough analysis (vulnerability, NSR, attention, cross-species) and a cleaner conceptual framework, but has the AdaNovo retraining inconsistency as a unique weakness. I position CausalNovo at 6.5, comparable to ReNovo.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>