## Summary
This paper investigates combining Cannistraci-Hebb Training (CHT), a brain-inspired dynamic sparse training (DST) method, with established ANN-to-SNN (ANN2SNN) conversion pipelines to produce sparse spiking neural networks. Experiments span three architectures (MLP, VGG-16, ViT-B), three datasets (CIFAR-10, CIFAR-100, ImageNet), and four conversion methods (CS-QCFS, SNM, AEC, SpikeZIP-TF). The paper claims that sparse SNNs match or exceed dense SNN accuracy while achieving up to 99% theoretical energy reduction, and additionally discovers a statistically significant time lag between firing-rate saturation and accuracy saturation that differs between sparse and dense networks.

---

## Strengths

- **First systematic study of DST+ANN2SNN**: The combination of structural connection sparsity (from CHT) and temporal sparsity (from SNN event-driven computation) has not been investigated before, and the paper fills this gap with broad empirical coverage across architectures, datasets, and conversion methods.

- **Comprehensive empirical breadth**: Using 3 architectures, 3 datasets, and 4 conversion methods produces a robust set of results. The positive findings are consistent across all settings, strengthening the generality of the claims.

- **Novel and statistically rigorous time-lag analysis**: The discovery that MASFR (firing rate) saturates significantly before accuracy in converted SNNs—with p-values on the order of 10⁻⁴¹ to 10⁻⁸²—is an original quantitative finding. The further observation that sparse SNNs exhibit larger time lags than dense ones (p=1.15×10⁻⁶, Mann-Whitney test) is properly tested and represents a new lens through which to understand SNN temporal dynamics.

- **Practical pipeline clarity**: The proposed conversion pipeline (train sparse ANN via CHT → freeze topology → convert to SNN) is simple, non-invasive to the conversion algorithms, and straightforward to replicate.

---

## Weaknesses

### Fatal
None.

### Major

1. **Theoretical energy only, no real-hardware validation**: All energy comparisons rely on the formula E = (total spikes) × E_s with fixed constants E_MAC = 4.6 pJ and E_AC = 0.9 pJ. Actual energy on neuromorphic hardware also depends on memory access patterns, spike routing overhead, and hardware utilization—none of which are modeled. The paper's most headline-grabbing claim ("up to 99% energy reduction") therefore rests on an idealized proxy metric. The authors acknowledge this limitation but do not bound the gap between theoretical and actual energy, which undermines the practical impact.

2. **Energy savings are directly proportional to sparsity and largely expected**: The ~99% theoretical energy savings are entirely explained by the 99% sparsity of MLP linear layers. For VGG-16 at 50% sparsity the reduction is 30–47%, and for ViT-B at 70% sparsity it is 58.87%. These reductions scale roughly linearly with sparsity. Given that fewer active connections directly reduce spike counts, the energy savings are not surprising and do not represent a novel mechanism beyond the structural sparsity itself.

3. **Accuracy improvements are weak or negative for the most practically relevant architectures**: For VGG-16 and ViT-B—the architectures with more real-world relevance—accuracy improvements are marginal or slightly negative: e.g., ViT-B on ImageNet shows −0.48% accuracy at 58.87% energy reduction; VGG-16 shows mixed results (−0.61% to +0.51%). The stronger accuracy gains occur primarily on the 99%-sparse MLP on CIFAR-10/100, where dense accuracy is already low (31.26% on CIFAR-100), suggesting CHT's advantage there is architecture-specific rather than general.

4. **Time-lag mechanism is observational, causal claim is speculative**: Section 3.3 concludes that the time lag "may be a potential cause of the accuracy and theoretical energy advantage of sparse SNNs." However, the analysis is purely correlational—no experiment is designed to test whether manipulating the time lag (e.g., by stopping inference at different time points) causally alters the accuracy/energy tradeoff. The proposed qualitative explanation (MASFR averages all layers, so last-layer rates stabilize later) is reasonable but is not formalized or validated.

### Minor

1. **Saturation detection algorithm is ad hoc**: The threshold (≤1% relative improvement over 10 consecutive steps) is a single hardcoded choice. The sensitivity of the time-lag distribution and statistical conclusions to this threshold is never analyzed, making it unclear how robust the time-lag findings are.

2. **ViT-B is evaluated with only one conversion method**: SpikeZIP-TF is the only conversion method used for ViT-B, so conclusions about Transformer architectures rest on a single configuration without cross-method validation.

3. **Grid search scope potentially unequal**: The paper states that grid search is performed to obtain best-performing models. It is unclear whether the same grid-search budget was applied to both dense and sparse configurations, leaving open the possibility that sparse results are better-tuned.

### Trivial
- Some duplicated table entries in the parsed tables (e.g., "MLP-CIFAR100-method1" appears twice in the OCR-extracted output) appear to be parser artifacts and do not affect the scientific content.

---

## Nice-to-Haves
- A real-hardware energy measurement on a neuromorphic chip (e.g., Loihi or TrueNorth), even for a single architecture, would substantially strengthen the energy claims.
- An ablation varying sparsity level continuously would clarify whether accuracy gains are threshold effects or smooth functions of sparsity.
- A controlled experiment testing whether the time lag causally mediates the accuracy/energy tradeoff (e.g., truncating inference at firing-rate saturation time vs. accuracy saturation time) would upgrade the time-lag finding from correlation to mechanism.

---

## Novel Insights
The most genuinely novel contribution is the quantitative characterization of a time lag between MASFR saturation and accuracy saturation in converted SNNs, and the discovery that this lag is significantly larger in sparse than dense networks. This provides a new empirical quantity—measurable across diverse architectures and methods—that connects structural connectivity to temporal dynamics in rate-coded SNNs. While the paper stops short of a mechanistic causal model, the statistical consistency of this finding across hundreds of grid-search configurations suggests it is a robust property worth building on.

---

## Suggestions
- Provide a sensitivity analysis of the saturation detection threshold (the 1%/10-steps criterion) and report how time-lag statistics change under alternative thresholds.
- Report a single real-hardware energy number (or an upper-bound gap analysis) to anchor the theoretical predictions.
- Separate the accuracy and energy claims more carefully: the headline "up to 99% energy reduction" should be contextualized by noting it requires 99% sparsity in MLP, which is an extreme architectural choice.
- For the time-lag finding, design an experiment where inference is halted exactly at MASFR saturation time (not accuracy saturation time) and compare accuracy/energy tradeoff; this would directly test the causal hypothesis stated in the Discussion.

---

## Score and Decision

The paper addresses a legitimate and unexplored gap (sparse DST + ANN2SNN conversion), provides broad empirical coverage, and contributes an original time-lag observation. However, the energy savings are theoretical and scale trivially with sparsity; the accuracy benefits are meaningful only for the least-relevant architecture (99%-sparse MLP); and the most interesting mechanistic claim (time lag as cause of the tradeoff) is not experimentally substantiated. The work reads more as a competent empirical audit of a natural combination of existing tools than as a conceptual or algorithmic advance. For ICLR, the contribution level sits below what is typically needed for acceptance.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>