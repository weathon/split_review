## Summary

This paper investigates the combination of dynamic sparse training (specifically Cannistraci-Hebb Training, CHT) with ANN-to-SNN conversion. The authors show that sparse SNNs obtained by converting CHT-trained sparse ANNs can achieve accuracy comparable to or exceeding dense SNNs while reducing theoretical energy consumption by up to 99%. Additionally, they identify and analyze a time lag phenomenon where firing rate saturation precedes accuracy saturation in converted SNNs, with sparse networks exhibiting a significantly larger time lag than dense networks.

## Strengths

- **First study of DST+ANN2SNN conversion**: The paper addresses a genuine gap—prior ANN2SNN conversion work has focused almost exclusively on dense networks, and the combination with dynamic sparse training is novel. The empirical investigation across multiple architectures (MLP, VGG-16, ViT-B), datasets (CIFAR-10/100, ImageNet), and conversion methods (QCFS, SNM, AEC, SpikeZIP-TF) is reasonably comprehensive.

- **Interesting time lag finding**: The discovery that firing rate saturation systematically precedes accuracy saturation in converted SNNs, and that this time lag differs between sparse and dense networks, is a genuinely novel observation. The statistical analysis (Wilcoxon signed-rank test with p-values ~10^-41 to 10^-43) provides strong evidence for the phenomenon.

- **Clear demonstration of accuracy preservation**: The results convincingly show that sparse SNNs can maintain accuracy comparable to dense SNNs across diverse settings, and in some cases (MLP on CIFAR-100) even outperform them. This is a practically useful finding.

## Weaknesses

### Major

- **Theoretical energy savings are essentially tautological**: The "up to 99% energy reduction" claim follows directly from the 99% connection sparsity in MLP linear layers. The energy model (total spikes × energy per spike) scales linearly with the number of active connections, so removing 99% of connections trivially yields ~99% fewer spike transmissions. The paper does not account for overheads of sparse computation (indexing, irregular memory access, control logic) that real hardware would incur. Without hardware measurements or a more realistic energy model that includes these overheads, the energy claims are significantly overstated.

- **Suspiciously large accuracy gains for sparse MLP suggest baseline issues**: On CIFAR-100, the dense MLP achieves only 31.26% accuracy, while the sparse MLP reaches 34.86–42.31% after conversion. A 10+ percentage point improvement from sparsity alone is unusual and suggests the dense baseline may be poorly tuned or the MLP architecture is too small for the task. The paper mentions grid search but does not report the search space or confirm that the dense baseline is competitive. This undermines the claim that "sparse SNNs can achieve accuracy surpassing dense SNNs" as a general result.

- **Limited technical depth**: The core contribution is an empirical study combining existing methods (CHT for sparse ANN training + existing ANN2SNN conversion). There is no new algorithm, no theoretical analysis of why the combination works, and no investigation of how sparse topology interacts with the conversion process (e.g., numerical stability, information loss in sparse layers during conversion). The paper reads more as a benchmark report than a methodological contribution.

- **Time lag analysis lacks mechanistic depth**: While the statistical finding of a time lag is solid, the explanation ("it takes additional time for firing rate of neurons in the last layer to stabilize") is superficial. No analysis is provided of why sparse networks have a larger lag, how this relates to network topology, or whether this is a cause or effect of the accuracy/energy trade-off. The claim that this "may be a potential cause of the accuracy and theoretical energy advantage" is speculative and unsupported.

### Minor

- **Saturation detection algorithm is arbitrary**: The threshold of "no greater than 1% improvement over 10 time steps" is not justified, and no sensitivity analysis is provided. Different thresholds could change the reported time lags and energy comparisons.

- **Missing comparison details**: The paper mentions comparisons to pruned networks (Appendix C) and STBP (Appendix D) but does not summarize these results in the main text. Without seeing these comparisons, it is difficult to assess whether CHT offers advantages over simpler sparsification methods for SNN conversion.

- **VGG-16 results show modest energy savings**: For VGG-16 (50% sparsity), energy reduction is only 31–47%, which is far less dramatic than the MLP results. This is acknowledged implicitly but not discussed in terms of practical significance.

## Nice-to-Haves

- Hardware measurements or a more realistic energy model that accounts for sparse computation overheads would substantially strengthen the energy claims.
- An ablation study isolating the effect of CHT topology learning from the effect of sparsity itself (e.g., comparing CHT to random sparse topologies at the same sparsity level) would clarify the source of accuracy preservation.
- A deeper analysis of why sparse networks exhibit larger time lags—e.g., examining layer-wise firing rate dynamics or topological properties—would elevate the time lag finding from an observation to a mechanistic insight.

## Novel Insights

Beyond the paper's own contributions, the most novel insight is the empirical finding that firing rate saturation precedes accuracy saturation in converted SNNs, and that this time lag is modulated by network sparsity. This suggests that the temporal dynamics of information propagation in SNNs are influenced by structural connectivity in a non-trivial way, which could inform the design of more efficient conversion protocols (e.g., early stopping based on firing rate rather than accuracy). However, the paper does not fully develop this insight into a practical recommendation or theoretical framework.

## Suggestions

- Address the dense MLP baseline issue by either (a) reporting a stronger dense baseline (e.g., a larger MLP or better hyperparameter tuning) or (b) reframing the claims to acknowledge that CHT finds better topologies than the default dense initialization, rather than claiming sparsity itself improves accuracy.
- Provide a more nuanced energy analysis that includes estimates of hardware overheads (e.g., from sparse matrix computation literature) or at minimum discusses the gap between theoretical and practical energy savings.
- Move the comparison with pruned networks and STBP to the main text, as these are critical for assessing the value of CHT over simpler alternatives.
- Add a sensitivity analysis for the saturation detection threshold to demonstrate robustness of the time lag findings.

## Score and Decision

**Score**: 5

**Decision**: Reject

**Rationale**: The paper addresses a relevant and underexplored question, and the time lag finding is genuinely novel. However, the core energy claims are inflated by a simplistic theoretical model that ignores real hardware overheads, the dense baselines appear suboptimal in key experiments, and the technical contribution is primarily empirical rather than methodological. The paper would benefit from stronger baselines, hardware-aware energy analysis, and deeper mechanistic investigation of the time lag phenomenon before it meets the bar for acceptance at a top venue.

MY FINAL SCORE: 5.0</score>
MY FINAL DECISION: Reject</decision>