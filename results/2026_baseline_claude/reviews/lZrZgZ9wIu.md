## Summary

This paper investigates combining Dynamic Sparse Training (DST), specifically Cannistraci-Hebb Training (CHT), with ANN-to-SNN (ANN2SNN) conversion to produce sparse SNNs that are both accurate and theoretically energy efficient. The authors test this pipeline across MLP, VGG-16, and ViT-B architectures on CIFAR-10, CIFAR-100, and ImageNet using four established conversion methods. Additionally, the paper introduces the analysis of a "time lag" phenomenon: the Model Average Spike Firing Rate (MASFR) saturates before accuracy saturates, and this lag is significantly larger in sparse SNNs than in dense SNNs.

---

## Strengths

- **Novel pipeline at the intersection of DST and ANN2SNN**: To the best of the reviewers' knowledge, no prior work has systematically investigated converting dynamically sparsely trained ANNs into SNNs. The pipeline (CHT → sparse ANN → freeze topology → ANN2SNN conversion) is clean and generally applicable.
- **Comprehensive empirical coverage**: Three architectures, three datasets, and four conversion methods are evaluated, giving a well-rounded empirical picture. Results consistently demonstrate that sparse SNNs match or exceed dense SNN accuracy while being more energy efficient.
- **Time lag discovery with strong statistical support**: The observation that MASFR saturation precedes accuracy saturation is novel and supported by very low p-values (e.g., p = 3.865×10⁻⁸² across all SNNs) across a large and diverse set of grid-search experiments. The further finding that sparse SNNs have a larger mean time lag than dense SNNs (p = 1.152×10⁻⁶) adds genuine mechanistic insight.
- **Honest acknowledgment of limitations**: The paper clearly distinguishes theoretical from real energy savings and acknowledges the hardware gap, which is crucial for reproducible claims in the neuromorphic computing field.

---

## Weaknesses

### Fatal
None.

### Major

1. **The headline energy saving is mechanistically trivial for MLP.** The MLP uses 99% sparsity in linear layers, so removing ~99% of connections directly predicts ~99% fewer AC operations. The energy reduction is nearly perfectly proportional to the sparsity level; there is no emergent efficiency beyond what basic arithmetic predicts. The paper presents the 99% energy reduction as a major finding (highlighted in abstract and title), but it adds little scientific insight when sparsity level essentially determines energy savings by construction. The more scientifically interesting cases—VGG-16 at 50% sparsity (31–47% energy reduction) and ViT-B at 70% sparsity (59% energy reduction)—are in fact consistent with the same trivial proportionality and are not discussed from this perspective.

2. **Confounded accuracy comparison.** The sparse and dense ANNs are optimized separately via grid search. In many experiments the sparse ANN already outperforms the dense ANN before conversion (e.g., MLP-CIFAR10: sparse 66.54% vs. dense 63.89%). The transferred accuracy advantage in the SNN is therefore inherited from the ANN, not a property of the SNN conversion itself. The paper does not disentangle whether the conversion preserves accuracy faithfully or whether the sparse SNN advantage simply mirrors the ANN advantage. A proper control would be comparing sparse and dense SNNs converted from ANNs matched at equal accuracy.

3. **No comparison against non-CHT sparse SNNs or dedicated efficient SNN baselines.** There is a brief mention in Appendix C and D of comparisons with pruned ANNs and STBP-based sparse training, but the main results section does not benchmark against other sparse SNN approaches (e.g., direct sparse SNN training methods or magnitude pruning after SNN training). Without these baselines the claim that CHT specifically provides competitive trade-off is difficult to evaluate.

4. **ViT-B results are actually unfavorable for the sparse case.** Sparse ANN (80.36%) underperforms dense ANN (81.27%), and sparse SNN (80.99%) underperforms dense SNN (81.80%). The claim of accuracy "comparable to or even surpassing" is not supported for the most practically relevant architecture-dataset combination (ViT-B/ImageNet), which is a notable inconsistency.

### Minor

1. **Qualitative explanation of the time lag is underdeveloped.** The paper explains the lag by noting that MASFR is an average over all neurons and that output-layer neurons take longer to stabilize. This is logical but somewhat circular and not quantitatively validated. It is unclear why sparse SNNs should exhibit a *larger* time lag—the proposed mechanism ("potential cause") is not substantiated beyond speculation.

2. **Grid search is applied asymmetrically.** Section 2.4 notes that grid search is applied except for Vision Transformer. This asymmetry may affect fair comparison but is not discussed.

3. **MASFR metric conflates all neurons equally.** Using a flat average across all layers conflates early versus late layers. A layer-wise saturation analysis would provide cleaner mechanistic insight and would better support the proposed causal explanation of the time lag.

### Trivial

- The energy formula (Eq. 1) omits the distinct treatment of the first layer under Direct Input Encoding (mentioned in Sec. 2.2) but Table 1 does not clarify whether this correction is applied.

---

## Nice-to-Haves

- Ablation on sparsity level (e.g., varying CHT sparsity from 10% to 99%) to directly characterize the accuracy–energy trade-off curve rather than using a single fixed sparsity point.
- Layer-wise firing rate saturation analysis to validate the proposed explanation for the time lag.
- An experiment controlling for ANN accuracy parity between sparse and dense models before conversion to isolate the SNN conversion contribution.

---

## Novel Insights

The most genuinely novel finding is the systematic quantification of the time lag between MASFR saturation and accuracy saturation across a large and diverse experimental sweep. This is not a trivially predicted phenomenon in the literature and adds to the mechanistic understanding of rate-coded ANN2SNN systems. The secondary finding—that sparse SNNs exhibit a larger mean time lag than dense SNNs—is interesting and raises questions about how structural connectivity shapes temporal dynamics in converted SNNs, though the mechanism remains unresolved. The pipeline combining CHT with existing conversion methods is straightforward to implement and represents a useful practical contribution for neuromorphic practitioners.

---

## Suggestions

- Plot energy reduction versus sparsity level explicitly to help readers assess whether the savings scale trivially or super-/sub-linearly with sparsity.
- Conduct matched-accuracy experiments: prune the dense ANN to the same test accuracy as the CHT sparse ANN, then compare the resulting SNNs to isolate the effect of the conversion vs. the effect of the initial ANN quality.
- Add a layer-wise breakdown of firing rate saturation times to better explain and support the proposed mechanism for the time lag.
- Include a direct comparison in the main body with the STBP sparse training baseline to clarify the added value of CHT vs. alternative sparse training methods for SNN conversion.

---

## Score and Decision

The paper addresses a meaningful and novel intersection (DST + ANN2SNN), presents a clean methodology, and reports a genuinely interesting empirical phenomenon (the time lag). However, the central energy-savings claim is largely explained by trivial arithmetic for the MLP case, the accuracy comparisons are confounded by separately optimized ANN baselines, the ViT-B results contradict the paper's main claim, and the mechanistic interpretation of the time lag remains speculative. As an empirical study it lacks the depth to distinguish CHT's contribution from that of sparsity itself.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>