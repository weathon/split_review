Now I have all the information needed to construct the final consolidated review.

---

## Summary

This paper introduces *spreading OOD detection*, a new benchmark for node-level OOD detection on graphs where OOD nodes spread from seed nodes via epidemic models (SI/SIS), capturing inter-node dependencies that prior random-node benchmarks ignore. It contributes the **Spreading COVID-19** dataset (symptom-based features with epidemic spread on a LastFM Asia social graph) and proposes **EDBD**, an energy-based detector that refines initial energies through a controlled aggregation scheme using similarity and consistency matrices. The benchmark formulation is a genuine and well-motivated contribution to the graph OOD community. The method shows promising results, especially on the Spreading COVID-19 dataset, though the statistical reliability of its reported superiority over strong baselines is not fully established.

## Strengths

- **Realistic problem formulation that addresses a genuine gap in graph OOD benchmarks.** The paper explicitly models the spreading of OOD nodes using Markov-chain-based epidemic models (SI/SIS), moving beyond the unrealistic i.i.d. random-node selection used in prior work. This reframes node-level OOD detection to capture inter-node dependencies that arise in real-world scenarios such as virus transmission, malware propagation, and product adoption. The problem statement is clearly formalized in Section 3.

- **Construction of the Spreading COVID-19 dataset as a concrete, domain-grounded benchmark.** The dataset simulates COVID-19 spread on a human-activity network with 23-dimensional symptom-based features across five health conditions (normal, allergies, cold, flu, COVID-19). It enables OOD detection evaluation where the detector has no prior knowledge of the novel disease — exactly the scenario the motivating examples describe. The paper provides justification for using LastFM Asia as a proxy for offline contact networks (Appendix A), including a degree-distribution comparison with the High School Contact network. The dataset is released with the supplementary material under a CC BY 4.0 license.

- **Strong empirical results on the Spreading COVID-19 dataset with large performance margins.** On Spreading COVID-19 (SI model), EDBD achieves 86.11% AUROC-T versus 75.50% for the next-best method (GNNSAFE), and 28.92% versus 42.42% in FPR95-T. These gaps are substantial and far exceed the reported standard deviations, providing convincing evidence of the method's effectiveness on the dataset most aligned with the paper's motivating scenario.

- **Principled aggregation design with component-level validation.** The energy distribution-based aggregation uses two complementary controllers: the energy similarity matrix (edge-level, weakening propagation between dissimilar-energy nodes) and the energy consistency matrix (node-level, reducing total aggregation at cluster boundaries). The ablation study (Table 4) confirms that each component contributes meaningfully and that their combination yields the best performance across multiple settings, including both spreading OOD detection and conventional label-leave-out tasks.

## Weaknesses

### Fatal

None.

### Major

- **Statistical significance of the method's reported superiority is not established.** The paper claims EDBD "demonstrates superiority over state-of-the-art methods" (abstract) and reports results on 10 test episodes per setting. However, many of the reported improvements over GNNSAFE (the closest competitor) are accompanied by overlapping standard deviations. For example, on LastFM with the SIS model, the FPR95-T values are 47.35±20.70 (GNNSAFE) vs. 46.54±20.88 (EDBD) — effectively tied. On Cora with the SI model, the gap is ~5 points but the error bars overlap. The paper reports no statistical tests (e.g., paired tests across episodes, bootstrapped confidence intervals). Given the small number of episodes (10), the observed differences could plausibly arise from random variation. The core claim of the method's superiority is therefore not fully supported by the evidence. This is especially consequential because much of the paper's framing positions EDBD as the main contribution alongside the benchmark.

### Minor

- **Cora's suitability as a spreading OOD detection dataset is not justified.** The paper motivates spreading OOD detection with virus transmission, computer malware, and product adoption — scenarios involving interaction/contact networks. Cora is a citation network where nodes are papers and edges are citation links. The paper does not explain why an OOD node (e.g., a paper from a new research area) would "spread" along citation links in the same way an infection spreads along social contacts. While Cora's inclusion as a standard benchmark is understandable, the paper should either justify its relevance to the spreading scenario or acknowledge this limitation. Omitting this discussion risks making the evaluation appear less principled.

- **The similarity function in Equation (5) is designed ad-hoc without comparison against alternatives.** The function `sim(E_i, E_j) = (ε·(max−min) + (1−ε)·|E_i−E_j|)^{-1}` combines global energy range with pairwise absolute difference using a tunable ε. The paper does not justify why this particular form is chosen, nor does it compare against alternative similarity measures (e.g., Gaussian kernel with a bandwidth rule, cosine similarity, or a simpler inverse-distance weighting). Since this function controls the edge-level aggregation that is central to the method's performance, the lack of comparison or justification weakens the claim that the design is principled rather than handcrafted. The ablation study (Table 4) only removes S entirely rather than varying its formulation.

- **No hyperparameter sensitivity analysis is provided.** The method introduces four free parameters (α, β, ε, K) that control the aggregation process. The paper states that hyperparameters are "tuned on validation sets" but does not analyze how performance varies over their range. A sensitivity study (e.g., showing how FPR95-T changes with ε or K on a validation set) would substantially improve reproducibility and credibility.

### Trivial

- The paper could clarify how random seeds are drawn for episode generation (e.g., fixed per episode or varied) and whether the variance across episodes properly reflects stochasticity in both the epidemic process and the seed selection.
- The metrics FPR95-T, AUROC-T, AUPR-T average over time stamps within each episode, discarding information about how detection difficulty changes during the spread (e.g., early stages with few OOD nodes may differ from later stages). Reporting performance at a few key time points (t=0, t=T/2, t=T) would provide a more informative picture.

## Nice-to-Haves

- **Comparison against a simple feature propagation/diffusion baseline** (e.g., standard label propagation on initial energies with a fixed damping factor) would help isolate the benefit of the non-uniform S and C components over naive smoothing.
- **Time-step information leakage analysis**: The paper states that G^t is provided without the current time stamp t, but does not discuss whether the proportion of infected nodes or the graph structure could implicitly reveal t. A brief discussion would strengthen the evaluation.
- The consistency matrix uses standard deviation normalized by the global maximum, which may behave differently across graphs with different energy distributions. An alternative normalization (e.g., median absolute deviation or node-specific baseline) could be explored.

## Removed Points

- **"Circularity" concern** (reviewer: using the same initial energies as both targets for refinement and as the basis for constructing S and C): This is not a flaw — using the same representation for attention weights and the values being aggregated is standard practice in graph attention networks and self-attention mechanisms. The paper's design is that energies serve as both the signal to refine and the signal that controls the refinement, which is an intentional architectural choice, not a logical flaw.
- **Criticism that the consistency matrix standard deviation "depends on the scale of energies"**: This is already handled by the max-normalization step (dividing by the global maximum of standard deviations), which bounds entries to [0,1]. The hyperparameter β then controls how much to penalize inconsistency.
- **Formatting/style nitpicks** and **criticisms about missing appendix content** (appendix exists in original submission; parser stripped it).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an unexpected observation about the paper's implications or limitations that the authors themselves did not identify.

## Suggestions

1. **Add statistical tests or confidence intervals** across the 10 test episodes. A paired test (e.g., Wilcoxon signed-rank or paired t-test comparing EDBD vs. GNNSAFE per episode) would clarify which improvements are reliable. If many results are not statistically significant, reframe the method as a promising approach rather than a definitive advance.

2. **Include a hyperparameter sensitivity analysis** on the validation set showing how α, β, ε, and K affect FPR95-T and AUROC-T on at least one dataset (e.g., Cora or Spreading COVID-19).

3. **Add a brief discussion justifying or acknowledging the limitations of Cora** as a spreading OOD detection dataset. If possible, include one additional graph that better aligns with the motivating examples (e.g., a communication network or contact network).

4. **Compare the similarity function against at least one well-understood alternative** (e.g., a Gaussian kernel sim = exp(-|E_i-E_j|²/σ²) with a simple bandwidth heuristic) to demonstrate that the method's performance is not dependent on the specific functional form.

5. **Report performance at a few representative time points** (t=0, t=T/2, t=T) in addition to the averaged metrics, to show how detection difficulty evolves during the spread.

## Score and Decision

The paper introduces a genuinely new and well-motivated benchmark problem (spreading OOD detection) that fills a clear gap in graph OOD research, contributes a concrete dataset (Spreading COVID-19) with realistic grounding, and proposes a plausible method (EDBD) with an interesting aggregation scheme. The main weakness is that the empirical evidence for the method's superiority is not fully statistically substantiated, though the method shows clear large-margin gains on the most relevant dataset (Spreading COVID-19). The benchmark contribution stands on its own as a valuable resource for the community. The weaknesses are addressable and do not negate the paper's core contributions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>