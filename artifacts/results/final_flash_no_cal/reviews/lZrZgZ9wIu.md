## Summary

This paper combines Cannistraci-Hebb Training (CHT), a dynamic sparse training method, with ANN-to-SNN conversion to produce sparse SNNs. It demonstrates across MLP, VGG-16, and ViT-B architectures that CHT-derived sparse SNNs can match or exceed dense SNN accuracy while achieving substantial theoretical energy reductions (up to ~99% on MLP with 99% sparsity). Separately, it uncovers and rigorously validates a novel empirical finding: firing-rate saturation systematically precedes accuracy saturation in converted SNNs, with a significantly larger lag in sparse networks than dense ones.

## Strengths

- **First integration of dynamic sparse training (CHT) with ANN-to-SNN conversion.**  
  The paper explicitly identifies and fills a gap: prior ANN2SNN conversion worked exclusively with dense networks. This is a concrete, verifiable novelty (Section 1: *"prior ANN2SNN conversion works have focused most exclusively on dense networks… conversion on dynamically sparsely trained networks have never been studied"*).

- **Well-supported discovery of a time lag between firing-rate saturation and accuracy saturation, with a significant sparse/dense difference.**  
  Section 3.3 uses principled non-parametric tests (Wilcoxon signed-rank: p = 3.245×10⁻⁴¹ dense, 4.485×10⁻⁴³ sparse; Mann-Whitney between groups: p = 1.152×10⁻⁶) across a diverse set of grid-search experiments. This is a genuinely novel observation about SNN temporal dynamics that goes beyond prior qualitative observations of saturation.

- **Demonstrates large theoretical energy reductions, especially on MLP.**  
  Table 1 reports theoretical energy reductions of 98.63–99.16% for 99%-sparse MLP, with simultaneous accuracy improvements (up to +11.84%). Even on VGG-16 (50% sparsity) and ViT-B (70% sparsity), reductions exceed 30% and 58% respectively. The trend—that structural sparsity from CHT translates to reduced theoretical energy post-conversion—is consistent across all 13 configurations.

- **Systematic evaluation across multiple architectures, datasets, and conversion methods.**  
  The study covers MLP (CIFAR-10/100), VGG-16 (CIFAR-10/100), and ViT-B (ImageNet), with four distinct conversion methods (QCFS, SNM, AEC, SpikeZIP-TF). This breadth supports the generalizability of the main findings.

- **Clear saturation detection criterion and reproducible methodology.**  
  The saturation algorithm (≤1% relative improvement over 10 consecutive steps) and the theoretical energy model (Eq. 1 based on published MAC/AC costs from Yao et al., 2023) are clearly specified.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The accuracy "advantage" over dense SNNs is primarily driven by the MLP experiments; results on VGG-16 and ViT-B show near-parity, not consistent improvement.**  
  In 5 of 13 configurations, sparse SNNs show very small accuracy decreases (≤0.61%). The paper's framing (e.g., *"superiority of CHT training"*, *"consistently achieve higher accuracy"* in Section 3.1) over-generalizes from the MLP results. The paper would be better served by a more precise claim: CHT-based sparse SNNs match dense SNN accuracy on larger architectures while significantly reducing theoretical energy, and sometimes (primarily on MLP) improve accuracy as well.

- **No analysis of firing-rate magnitudes, only saturation time.**  
  The energy calculation (Eq. 1) depends on total spike counts. The paper thoroughly analyzes *when* firing rates saturate, but never reports the *magnitude* of firing rates for dense vs. sparse models. If sparse networks compensate for fewer connections by increasing per-neuron firing rates, the total spike count may not drop proportionally with connection count. The 99% reduction figure implicitly assumes firing rates are unchanged, which is unverified. This does not invalidate the qualitative finding (sparse SNNs are more energy-efficient), but the headline number is presented without necessary supporting evidence. A simple comparison of average firing rates across dense/sparse models would address this.

- **The paper claims a causal link between the time-lag phenomenon and the accuracy/energy trade-off without evidence.**  
  The text states the time-lag difference *"may be a potential cause of the accuracy and theoretical energy advantage of sparse SNNs"* (Section 3.3) and *"might be a potential cause for the performance and the theoretical energy gap"* (Discussion). While the language is hedged ("may", "potential", "might"), no causal mechanism or correlational evidence for this link is provided. The time-lag analysis and the pipeline evaluation are independent contributions; connecting them speculatively dilutes both. The paper would be stronger by either severing this link or providing evidence for it.

- **Formula error in Table 1 caption.**  
  The caption writes: *reduction = (E_sparse − E_dense) / E_sparse × 100%*. For E_sparse < E_dense (which is the claim), this yields a negative number. The reported positive values are consistent with (E_dense − E_sparse) / E_dense, which is the intended formula. This is clearly a writing mistake, not a computational error, but it should be fixed.

- **Baseline comparisons with pruning and direct SNN training are deferred to the appendix.**  
  The paper claims to investigate *"the advantage of dynamically sparsely trained ANNs for conversion"*, but the main experimental body (Sections 3.1–3.2) only compares against dense conversion. The comparisons with pruning-then-conversion and with surrogate-gradient-based direct SNN training (STBP) are mentioned (Section 3) and placed in Appendices C and D. This weakens the "advantage" claim in the main narrative. Moving a summary of these comparisons into the main text would strengthen the paper.

### Trivial

- The saturation threshold (1% over 10 steps) is a reasonable heuristic, but no sensitivity analysis is provided to show how the time-lag results change with different threshold choices.

## Nice-to-Haves

- **Practical implication of the time-lag finding.** If firing rates saturate before accuracy, could inference be truncated at the firing-rate saturation point (rather than the accuracy saturation point) to save energy without losing accuracy? Evaluating this would turn the observational finding into a practical design principle and is a natural next step.
- **Report firing-rate magnitudes** (average MASFR values for dense vs. sparse models in each configuration) alongside saturation times. This would directly address the energy-model concern.
- **Saturation threshold sensitivity analysis** (e.g., vary the threshold parameter and report whether the time-lag conclusions hold).

## Removed Points

- **"Comparisons with pruning/direct training should be in main body or the paper is structurally incomplete"** — The paper explicitly states these comparisons exist in Appendices C and D. While putting them in the main text would strengthen the narrative, it is standard practice to place extended comparisons in appendices. The paper does not hide them. The claim that the paper is "structurally incomplete" is too strong. (Demoted from harsh critic's "Critical Issue #1" to a Minor weakness above.)
- **"The paper's central claim of being 'first' overpromises relative to evidence"** — The paper is transparent about what it compares against and the appendices address the missing comparisons. The novelty claim is about the CHT+conversion pipeline specifically, which is genuine.
- **Several of the Strength Finder's claimed strengths are generic and removed** (e.g., *"Systematic evaluation across multiple architectures"* is kept above; generic framing like *"the paper addresses an important problem"* is dropped as it lacks paper-specific evidence.)
- **"The 99% energy reduction rests on an unverified assumption"** — This was kept in Minor form above (firing-rate magnitudes not reported). The harsh critic's framing as a "fatal" methodological gap is removed because (1) the energy calculation is explicitly theoretical, (2) the paper acknowledges limitations (theoretical vs. real energy), and (3) even with moderate firing-rate changes, the qualitative conclusion that sparsity reduces energy holds. The missing analysis is a gap, not an invalidation.

## Novel Insights

None beyond the paper's own contributions. The time-lag finding (firing-rate saturation systematically precedes accuracy saturation, with larger lag in sparse networks) is itself the most novel insight in the paper. The pipeline contribution (CHT + ANN2SNN conversion) is a straightforward but useful combination that has not been previously studied. The review process did not surface additional novel observations beyond what the paper already claims.

## Suggestions

1. **Tone down accuracy superiority claims** to reflect that the advantage is clearest on small MLPs, while on VGG-16 and ViT-B the sparse SNNs are essentially on par with dense ones (with small fluctuations in both directions).
2. **Include a brief summary of pruning and direct-training comparisons in the main text** (a sentence or two and a row in the table) rather than only referencing appendices.
3. **Add a simple per-configuration firing-rate magnitude comparison** (e.g., average MASFR for dense vs. sparse models at the accuracy saturation time) to support the energy claim.
4. **Fix the formula in Table 1** to correctly state `(E_dense − E_sparse) / E_dense × 100%`.
5. **Either remove or support the causal link** between the time-lag difference and the accuracy/energy trade-off. As it stands, the speculation weakens a clean empirical finding.
6. **Test a practical implication of the time lag** — e.g., does stopping inference at the firing-rate saturation point preserve accuracy while saving energy?

## Score and Decision

The paper makes two distinct contributions: (1) a useful empirical evaluation of CHT-based ANN-to-SNN conversion showing that structural sparsity from DST can be preserved through conversion to produce energy-efficient SNNs, and (2) a clean, statistically-rigorous discovery of the firing-rate/accuracy saturation time lag. Both are novel. The main weaknesses are that the accuracy advantage is overstated (MLP-driven, not consistent across all settings), the energy model lacks firing-rate magnitude verification, and the causal link between the two contributions is unsupported speculation. These are addressable in revision. The paper's contributions are solid but not transformative.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>