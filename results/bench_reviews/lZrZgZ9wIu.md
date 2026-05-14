## Summary

This paper empirically investigates the combination of dynamic sparse training (via Cannistraci-Hebb Training, CHT) with ANN-to-SNN conversion. Across MLP (CIFAR-10/100, 99% linear sparsity), VGG-16 (CIFAR-10/100, 50% conv sparsity), and ViT-B (ImageNet, 70% linear sparsity) with multiple conversion methods, it shows that CHT-derived sparse SNNs can match or exceed dense SNN accuracy while achieving substantial theoretical energy savings (up to 99%). The paper additionally reports a novel temporal phenomenon: firing-rate saturation (MASFR) consistently precedes accuracy saturation in converted SNNs, and this time lag is significantly larger for sparse networks than dense ones.

## Strengths

- **First study of DST for ANN2SNN conversion.** The paper is the first to systematically investigate whether dynamically sparsely trained ANNs (via CHT) can be successfully converted to SNNs, covering three architectures, four conversion methods, and three datasets. This fills a genuine gap in the literature.

- **Novel empirical finding: firing-rate-vs-accuracy time lag.** The discovery that MASFR saturates significantly before accuracy (p < 1e-40 for both dense and sparse SNNs, Wilcoxon signed-rank test) and that sparse SNNs exhibit a larger lag (p = 1.152e-6, Mann-Whitney) is a genuinely novel quantitative observation about the temporal dynamics of converted SNNs. The statistical tests are rigorous and the effect is convincingly demonstrated across diverse hyperparameter configurations.

- **Broad evaluation scope.** Experiments span simple MLPs, CNNs (VGG-16), and Transformers (ViT-B), across three datasets and four conversion methods (QCFS, SNM, AEC, SpikeZIP-TF). This breadth gives confidence that the main findings are not artifacts of a single architecture or conversion approach.

## Weaknesses

### Fatal
None.

### Major

1. **Energy reduction is a trivial arithmetic consequence of sparsity, not a research finding that needs to be "discovered."**  
   The paper's headline result — up to 99% theoretical energy reduction — follows directly from the chosen sparsity levels (99% for MLP linear layers) applied to a standard energy model where energy scales with synaptic operations. The paper itself acknowledges this ("sparse SNNs benefit from structure connection sparsity that reduces active links"). Yet the abstract and introduction present this as a key finding and it dominates the discussion. The genuinely non-trivial research question is whether accuracy is *maintained* despite this sparsity. By foregrounding the energy number as a result of the pipeline rather than a known consequence of the sparsity input, the paper overstates the novelty of this aspect.

2. **No error bars, confidence intervals, or multi-seed replication for any accuracy result.**  
   All accuracy numbers in Table 1 and the main text are reported as point estimates. Without standard deviations or multiple random seeds, the reader cannot assess whether the reported improvements (e.g., +4.13% for MLP CIFAR-10) are statistically significant or simply noise. This is a critical gap for an empirical paper whose central claim rests on accuracy comparisons between dense and sparse models.

3. **Discrepancy between Table 1 accuracy improvements and the reported max accuracy values.**  
   For example, MLP-CIFAR10 method1: max dense SNN = 69.18%, max sparse SNN = 71.40% (difference = 2.22 pp), but Table 1 reports +4.13% accuracy improvement. For MLP-CIFAR100 method2: max dense SNN = 41.31%, max sparse SNN = 41.50% (diff = 0.19 pp), yet Table 1 reports +10.17%. The paper states that accuracy is computed at the *saturation time step* rather than at the maximum, which could explain part of the gap, but this is never explicitly clarified for the accuracy column. The mismatch undermines trust in the numbers and needs clear reconciliation.

### Minor

1. **Comparison to alternative sparsity methods is deferred to the appendix.**  
   The paper mentions comparisons against pruned ANN conversion and STBP sparse training, but relegates them to Appendices C and D (which are stripped by the parser, so their quality cannot be assessed here). While putting ablations in the appendix is common, having no other sparsity method in the main evaluation weakens the paper's ability to argue that CHT specifically, rather than generic sparsity, drives the observed results.

2. **Energy formula contains a typo.**  
   The stated formula reads `reduction = (E_sparse - E_dense)/E_sparse × 100%`, which would yield a negative value when E_sparse < E_dense (as is the case). The correct formula should be `(E_dense - E_sparse)/E_dense × 100%`. The values in the table are clearly computed correctly, so this is a presentation error that should be fixed.

3. **Saturation detection algorithm (≤1% improvement over 10 steps) is used without sensitivity analysis.**  
   The 1% threshold and 10-step window are plausible but ad-hoc. No analysis is provided to show how results change with different criteria, which matters because the energy numbers and time-lag analysis both depend on this definition.

### Trivial

- The paper writes "Camnistraci-Hebb Training" inconsistently (both "Camnistraci" and "Cannistraci" appear).
- The energy formula typo (noted above) should be corrected.

## Nice-to-Haves

- A Pareto-style scatter plot of accuracy vs. energy across multiple sparsity levels (e.g., 0%, 50%, 75%, 90%, 99%) for at least one architecture would make the "trade-off" promised in the title quantitative rather than binary.
- Layer-wise firing-rate saturation times would strengthen the (currently speculative) explanation that output-layer stabilization lags behind MASFR saturation.
- The time-lag finding is intriguing; an analysis of whether this lag correlates with accuracy improvement across individual hyperparameter configurations would strengthen the claim that it is a "potential cause."

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's claim that dense MLP baseline (63.89% on CIFAR-10) is "far below what a simple tuned MLP can achieve (typically ~55–60%)."** — This is factually self-contradictory: 63.89% is *above* 55–60%, not below. A simple MLP on CIFAR-10 achieving 63.89% is reasonable, not suspicious. Removed for being factually wrong.

- **Harsh critic's claim that no comparison to other sparsity methods exists in the paper.** — The paper explicitly states these comparisons exist in Appendices C and D. While it's reasonable to criticize their absence from the main text, the claim that they are missing entirely is incorrect. Moved here with this clarification.

- **Strength Finder's claim about "consistent and large theoretical energy savings across diverse settings" as a core strength.** — This is a generic consequence of the input sparsity level, not a finding that requires empirical validation. Retained as context but not weighted as a strength.

## Novel Insights

The most novel insight to emerge from these reviews — one that goes beyond what the paper itself claims — is that the paper's main non-obvious contribution is the *time-lag analysis*, not the accuracy-energy trade-off. The energy reduction is a foregone conclusion given the sparsity levels; the accuracy comparisons with a dense baseline would benefit from statistical rigor; but the observation that firing-rate saturation systematically precedes accuracy saturation, and that sparse networks exhibit a larger lag, is a genuinely new empirical finding about the dynamics of converted SNNs that could inform future work on conversion latency and coding efficiency. The reviewers collectively did not identify any fundamental flaw in this finding, which suggests it is the most robust part of the paper.

## Suggestions

1. **Add standard deviations and multi-seed replication** to all accuracy results — this is the single most impactful fix. Without it, the central comparative claims cannot be evaluated.
2. **Reconcile the discrepancy between Table 1's accuracy improvements and the max accuracy values** by explicitly stating which time step is used for the accuracy comparison in Table 1 and, if needed, adding a column showing both saturation-time accuracy and max accuracy.
3. **Bring at least one alternative sparsity method comparison (e.g., magnitude pruning) into the main paper**, even as a single small table or figure, to reduce reliance on the appendix.
4. **Re-frame the energy results** as an expected consequence of the chosen sparsity levels and focus the narrative on the non-trivial question: does the accuracy hold up? The time-lag analysis could become a more central contribution.

## Score and Decision

**Calibration anchors** (all from ICLR 2026 human reviews, same topic area):

| Path | Avg Score | Comparison to current paper |
|------|-----------|-----------------------------|
| `O3CuUy5XAX` (ANN2SNN, T=1 conversion) | 3.00 | Weaker: that paper's method was essentially not an SNN, while this paper's contributions are at least real even if limited. Current paper is stronger. |
| `9pZhYkf80k` (QVM for ANN-SNN) | 4.00 | Similar: both have a novel empirical insight but suffer from framing and rigor issues. Roughly comparable. |
| `PBz9CMIOtn` (Parallel ANN2SNN) | 4.00 | Similar: empirical study with some analytical contribution but limited novelty. Comparable quality. |
| `meDMftHUlX` (Distribution-aware phase coding) | 5.00 | Stronger: proposes a new method with convergence guarantees and achieves SOTA. Current paper has less methodological novelty. |
| `qDLVgr8ESB` (CH-SNN direct training) | 5.50 | Stronger: proposes a new 4-stage framework for SNN sparse training, more extensive experiments. Current paper applies existing methods. |
| `6UpstNltZ4` (Recovery guarantee for sparse nets) | 6.40 | Much stronger: rigorous theoretical contribution with proofs. Not comparable in depth. |

Relative to these anchors, the paper sits between the ~3–4 range of rejected empirical ANN2SNN papers and the ~5+ range of accepted papers with new methodological contributions. It has a genuinely novel finding (the time lag) and broad evaluation, but the lack of statistical rigor and the overclaimed framing of trivial energy results prevent it from reaching the acceptance bar.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>