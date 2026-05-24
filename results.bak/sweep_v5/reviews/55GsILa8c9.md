Now I have a thorough understanding of the paper and the calibration anchors. Let me write the consolidated review.

## Summary

This paper presents CausalNovo, a model-agnostic framework for de novo peptide sequencing that uses causal principles (independence and sufficiency derived from a Structural Causal Model) combined with contrastive learning and information-theoretic objectives to encourage models to rely on signal fragment ions rather than spurious noise peaks. The framework introduces a Causality Extraction Module that learns importance scores over peaks, a replacement-based data augmentation strategy simulating intervention on noise peaks, and multiple training objectives. The method is evaluated on three public datasets (Nine-species, Seven-species, HC-PT) with three Transformer-based backbone models (CasaNovo, AdaNovo, π-HelixNovo), showing consistent improvements at amino acid, peptide, and PTM levels.

## Strengths

- **Consistent and substantial empirical improvements across diverse settings.** CausalNovo improves amino acid precision across all three datasets and all three backbone models—e.g., +12.0% for CasaNovo on Seven-species, +9.0% on HC-PT—with especially large gains on the challenging HC-PT and Seven-species datasets. The pattern of improvement is systematic rather than cherry-picked.

- **Well-designed ablation studies isolating each component.** Table 4 ablates the independence, purification, and symmetric training components individually, while Table 5 ablates replace, enhance, and drop operations in the causal intervention. This gives clear evidence about which design decisions matter. Notably, the "causality enhancement" (adding theoretical peaks) and "replace" are ablated separately, refuting the concern that the enhancement effect is conflated with replacement.

- **Attention analysis provides mechanistic support.** Table 7 shows that CausalNovo increases the proportion of predictions attending to three causal peaks from 19.26% to 32.87%, and reduces the proportion attending to zero causal peaks. This directly links the framework's design to a measured change in model behavior.

- **Cross-species validation.** Table 3 shows consistent improvements across all 8 held-out species on Nine-species, with an average +2.6% peptide precision improvement. This demonstrates generalizability beyond dataset-specific effects.

- **Robustness analysis across varying noise-signal ratios and perturbation thresholds.** Figures 1, 3, and 4 show that CausalNovo maintains higher performance as noise increases, with relative improvements growing larger at higher perturbation levels (e.g., 28.5% RI at threshold=1 on HC-PT in Table 6). This directly targets the paper's core motivation.

## Weaknesses

### Fatal
None.

### Major

- **The causal framing is partly aspirational; the method reduces to label-guided data augmentation + contrastive learning, and the SCM is not empirically validated as a causal model.** The SCM (Eq. 2: X = f(C,S), Y = g(C)) uses Reichenbach's Common Cause Principle to posit a latent causal variable C. While this is a justifiable design choice in causal representation learning (as the paper acknowledges by citing Chen et al. 2022), the paper does not provide evidence that the learned representations correspond to causal mechanisms in any testable sense—no causal discovery, no do-calculus, no interventional data at test time. The "causal intervention" is a label-dependent noise replacement augmentation, and the claimed disentanglement is not directly evaluated (e.g., the paper does not measure whether learned importance scores M correlate with known causal b/y ions on held-out data). The improvements could plausibly arise from the contrastive regularization and data augmentation alone. This gap between the causal language and what is actually demonstrated weakens the paper's central claim.

- **Results are reported without error bars or statistical significance.** All numbers in Tables 1–6 are single-run evaluations with no standard deviations or confidence intervals. Many improvements are modest in absolute terms (2–6% in some settings), making it impossible to assess significance. Given that the retrained baselines differ from originally published numbers (e.g., CasaNovo on Nine-species: published 0.697 AA precision vs. retrained 0.741), variance estimation is important. This is a standard expectation for benchmarking papers and should be addressed.

- **The retrained baseline numbers differ substantially from published values without explanation.** For example, CasaNovo published 0.697 AA precision on Nine-species but the retrained version achieves 0.741; AdaNovo published 0.698 but retrained yields 0.681; π-HelixNovo published 0.481 on Seven-species but retrained is 0.465. These discrepancies suggest configuration differences that are not discussed, and could potentially affect the fairness of comparison between "baseline + CausalNovo" and the originally published numbers.

### Minor

- **The claim of "model-agnostic" is supported only on Transformer-based models.** While three architectures (CasaNovo, AdaNovo, π-HelixNovo) are tested, they are all Transformer encoder-decoders. Non-Transformer baselines (PointNovo, DeepNovo) appear in comparison tables but are never integrated with the CausalNovo framework, limiting the generality claim.

- **The hyperparameter γ (tolerance threshold for noise identification) and α (fraction of noise peaks replaced) during training are not specified.** The paper reports the threshold for evaluation (in Table 6) but not the values used during training. Sensitivity analysis on these parameters would be helpful for reproducibility.

- **The "purification" objective's claim that maximizing I(z_s; Y) "indirectly leads to the purification of z_c" is not formally justified.** The paper states this could also cause z_s to capture label-relevant noise. An explicit analysis or regularization to prevent this would strengthen the theoretical grounding.

### Trivial
None.

## Nice-to-Haves

- A simple data augmentation baseline where noise peaks are replaced randomly (without the contrastive objective or the CEM module) would clarify how much of the gain is from augmentation versus the claimed causal disentanglement.
- An analysis of whether high-scoring peaks in M correspond to known b/y ions on held-out spectra would directly validate the causal nature of the representations.
- Testing on the more realistic evaluation protocol used by ContraNovo/RankNovo (training on large external corpora, OOD test sets) is mentioned by the authors as future work but would strengthen the real-world claims.

## Removed Points

- **"SCM is at odds with known causal direction (Y→X)"**: The harsh critic misunderstands the role of the SCM. The paper uses Reichenbach's Common Cause Principle to posit a latent common cause C, which is a standard modeling convention in causal representation learning (citations provided). The SCM is not claiming to model the physical fragmentation process but rather to guide representation learning. This is a valid design choice, not an error.

- **"Causality enhancement leaks ground-truth signal into input, not ablated separately"**: This is factually incorrect. Table 5 explicitly ablates "Replace" and "Enhance" as separate rows, showing each contributes ~0.6% improvement independently.

- **"Contrastive loss does not condition on Y"**: The paper explicitly describes the approximation via standard contrastive learning on the batch (Eq. 5), which is a well-known approximation for conditional mutual information. The critic's claim that "conditioning on Y is not implemented" ignores the stated approximation.

- **"Variability of gains across baselines is not discussed"**: Section 4.3 explicitly enumerates improvement percentages for each baseline across datasets. The critic missed this discussion.

- **"Table 6 threshold varied only during evaluation"**: The paper explicitly states "without retraining." The table is presented as an analysis of model robustness, not as a claim of adaptive training.

- **"NSR evaluation uses same noise definition"**: The paper acknowledges the noise identification procedure. The NSR analysis simply shows that the method is more robust to the defined noise type. Whether it generalizes to completely different noise types is a separate question, but the presented analysis is internally valid.

## Novel Insights

The most interesting observation that emerges from the reviewer cross-analysis is the tension between the paper's strong empirical results and its over-reaching causal framing. The attention analysis (Table 7) provides some of the most concrete evidence: CausalNovo demonstrably shifts model attention toward causal peaks (from 19.26% to 32.87% attending to three causal peaks). This mechanical evidence is arguably more compelling for the paper's core claim than the causal vocabulary itself. The paper would benefit from centering this finding rather than the speculative causal graph. Another insight is that the largest improvements occur on the most challenging datasets (HC-PT, Seven-species), suggesting the method's primary value is in handling noisy, low-quality spectra rather than in "causal disentanglement" per se.

## Suggestions

1. Report all main results with standard deviations over at least 3 random seeds.
2. Add an analysis computing precision/recall of high-scoring peaks (from M) against theoretical b/y ions on a held-out set.
3. Include a simple augmentation-only baseline (random noise peak replacement without contrastive objectives).
4. Specify the training-time values of γ and α.
5. Tone down the causal claims in framing—the method is better described as "invariant representation learning guided by domain knowledge about noise peaks" rather than "causal representation learning."

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| ReNovo (`uQnvYP7yX9`) | 6.50 (Accept) | Similar domain (de novo sequencing); comparable experimental scope, both lack std devs. CausalNovo has stronger ablation analysis but more overclaimed framing. |
| RankNovo (`87B3zDRMjv`) | 5.50 (Reject) | Same domain. RankNovo had modest improvements and computational cost concerns. CausalNovo has larger, more consistent gains. |
| Causal IB (`qac43AwuL9`) | 6.00 (Reject) | Causal representation learning paper; strong theory but toy experiments. CausalNovo has far more extensive empirical validation but less rigorous causal theory. |
| Genomic Foundationless (`kDZKEtDnT1`) | 4.25 (Reject) | Bioinformatics paper with insufficiently supported claims. CausalNovo's claims are better supported by multi-dataset, multi-baseline experiments. |
| CaLMol (`0Ra0E43kK0`) | 3.50 (Reject) | Causal + molecular paper. Weak empirical support. CausalNovo has substantially stronger and more consistent empirical evaluation. |

CausalNovo compares favorably to the mid-score anchors (ReNovo at 6.50, Causal IB at 6.00) on experimental thoroughness, though the over-claimed causal framing and missing error bars hold it back from the higher end. It is clearly stronger than the low-scoring bioinformatics/causal papers. The paper's consistent, multi-faceted empirical evidence across 3 datasets, 3 backbones, and multiple analyses (ablation, attention, cross-species, noise robustness) represents a genuine contribution. However, the disconnect between the causal narrative and what the method actually does, combined with the lack of statistical rigor, prevents a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>