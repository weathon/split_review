Now I have sufficient information. Let me produce the final consolidated review.

## Summary

This paper identifies that standard class-independent data augmentation can harm tail classes in long-tailed learning (an "extrinsic augmentation-wise imbalance" atop the inherent data imbalance), and proposes Dynamic Optional Data Augmentation (DODA). DODA maintains a per-class probability distribution over candidate augmentations and dynamically updates it based on per-class positive sample counts, allowing each class to preferentially select augmentations that benefit it. Experiments on CIFAR-100-LT, ImageNet-LT, and iNaturalist 2018 show consistent improvements over multiple long-tailed learning baselines.

## Strengths

- **Important problem identification with empirical motivation.** The paper demonstrates (Figure 2) that three different DA strategies — Cutout, CUDA, and their combination — all reduce accuracy on many tail classes on CIFAR-100-LT even while improving average accuracy. This concretely validates the overlooked problem that DA can be "hypocritical" in long-tailed settings. The formalization of an "extrinsic augmentation-wise imbalance" that coexists with the inherent data imbalance is a genuinely useful conceptual framing.

- **Novel and intuitive solution direction.** DODA's idea of maintaining per-class augmentation preference lists that evolve during training is a clean, principled approach to the identified problem. Unlike prior work that adjusts augmentation *strength* per class (CUDA) or searches globally (AutoAugment), DODA allows different classes to converge to *different augmentation operations*, which directly addresses the observation that the same augmentation can help one class while harming another.

- **Consistent empirical gains across diverse settings.** DODA improves top-1 accuracy when combined with six different long-tailed methods (CE, CE-DRW, LDAM-DRW, BS, RIDE, BCL) on CIFAR-100-LT (e.g., CE+DODA 43.47% vs. CE 38.32% at IR=100), ImageNet-LT (CE+DODA 47.9% vs. CE 41.1%), and iNaturalist 2018 (CE+DODA 65.6% vs. CE 62.2%). The flexibility across backbones, datasets, and imbalance ratios is demonstrated.

- **Evidence that DODA reduces class sacrifice.** Figure 4 compares CE vs. CE+CUDA (showing classes being sacrificed) and CE vs. CE+DODA, reporting 31% and 24% reductions in sacrifice rate. This directly connects the proposed mechanism to the motivating problem.

## Weaknesses

### Fatal
None.

### Major

- **Attribution gap in the preference list update rule.** The core update mechanism (Section 3.2) compares the current epoch's total positive sample count for a class against the previous epoch's count, then applies uniform up/down-weighting to *all* DAs used for that class in the current epoch. However, multiple different augmentations are typically applied to different samples of the same class within an epoch. An aggregate increase in class accuracy could be driven by only a subset of the applied DAs (or by unrelated factors like learning rate schedule), yet the rule rewards all of them indiscriminately — and vice versa for decreases. The paper provides no mechanism to attribute changes in class accuracy to specific augmentations, and no controlled experiment (e.g., single-augmentation probes per epoch) to validate that the update rule converges to the correct ordering of DA utility. This is a logical gap between the stated mechanism ("up-weight positive DAs") and what the implementation actually measures (aggregate class accuracy). While the heuristic may still work in practice, the paper does not explain *why* it would, and this weakens the claimed methodological contribution.

- **Missing critical ablation: random/static per-class DA selection versus adaptive selection.** The paper does not compare DODA against a baseline where each class draws from the same pool of K augmentations with either a fixed uniform distribution or a random per-class distribution that is not updated. Without this control, the observed gains could partially stem from the mere introduction of multiple diverse augmentation options per class (increasing overall diversity) rather than from the adaptive selection mechanism. This ablation is essential to isolate DODA's core claim that the *adaptive* preference list drives improvements. The comparison to CUDA (strength-based) and global search methods does not substitute for this control.

- **Tail-class performance claims are partially overclaimed and unevenly supported.** The paper states "outstanding performance on tail classes" (Section 4.2), but Table 1 (CIFAR-100-LT) reports only overall accuracy with no head/medium/tail breakdown — the tail-class claim cannot be verified from that table. For ImageNet-LT (Table 2, Many/Medium/Few split), improvements on the "Few" split appear modest or negligible for several baselines, which undercuts the claim of universal tail-class advantage. The sacrifice rate reductions (31%, 24%) in Figure 4 are presented without a formal quantitative definition of "sacrifice rate" in the main text, making them difficult to interpret or reproduce.

### Minor

- **Theoretical analysis is informal and provides intuition rather than rigorous support.** Theorems 1–3 offer geometric intuition (level-set deviation, 2D circular class approximations) about why DA can harm tail classes, but they do not constitute rigorous proofs. Theorem 3's derivation assumes equal radius increase across classes (Δ_c_h = Δ_c_t) without justification, and the 2D circle approximation is not validated against empirical feature distributions. The paper acknowledges this framing as "approximating" and "intuitive," so this is not fatal, but the stated contribution of "first theoretical analysis" oversells what is provided.

- **Reproducibility gaps.** The set of K augmentations used in experiments is mentioned as "10 common DAs" (line 204) with examples (Gaussian blur, rotation, horizontal flip), but the complete list and associated hyperparameters are not specified. The up-weight/down-weight update magnitude is also not disclosed. These details are necessary for exact reproduction.

- **No variance reported.** Table 1 states "average results of three random trials" (line 162) but reports no standard deviations, making it impossible to assess the significance of observed differences. This is standard practice for the field, but given the modest margins for some comparisons, variance would improve confidence.

### Trivial
- The "b i a s" and "c" artifacts in Theorem statements (lines 47, 55) are parser extraction issues, not author errors, and do not affect the intended meaning.

## Nice-to-Haves

- **Oracle baseline:** An upper bound where an oracle selects the best augmentation per class (e.g., identified via held-out validation) would help calibrate how much room for improvement remains.
- **Attribution validation experiment:** A small-scale study where single-augment models are trained per class and their accuracy is compared to DODA's preference list decisions would help validate that the update rule converges to meaningful orderings.
- **Per-class accuracy breakdown for CIFAR-100-LT** in Table 1 would directly support the tail-class performance claims made in the text.
- **K (pool size) ablation:** Varying the number of candidate augmentations to test robustness.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"The method does not address the case where no augmentation is applied"** — The paper explicitly addresses this: Section 3.1 defines `p_aug < 1` and states "each sample has a probability of p_aug of being augmented." When not augmented, the original sample is used. The reviewer missed this passage.

2. **"The paper does not acknowledge that many augmentations are designed to be label-preserving"** — Theorem 2 (line 58) explicitly states "a DA cannot guarantee that it is label-preserving on all classes," which directly acknowledges the issue and argues that label-preserving status is class-dependent.

3. **"The paper does not relate random warmup strategy to preference list initialization"** — Lines 172-173 state "We use a random strategy (up-weight and down-weight operations aren't active) for the first 50 epochs to avoid cold-boot issues," which directly describes the initial state (effectively uniform) and the transition.

4. **"Algorithm pseudocode is missing from main text"** — Algorithm 1 is referenced (line 146) but was likely stripped during PDF-to-text extraction. This is a parser artifact, not an author omission.

5. **"Theorem 2 ends with an uninterpretable 'c'"** — The "c" in the theorem corresponds to "class c" and is a notation artifact, not an error. The theorem is interpretable in context.

6. **Sacrifice rate numbers claimed to be "presented without context"** — The paper states "compared with CUDA" (line 202) and the setting is CIFAR-100-LT IR=100 (line 194), providing the missing context. The criticism about missing *definition* of sacrifice rate is kept in Minor.

## Novel Insights

The harsh critic's most substantive contribution is identifying the attribution gap in the update rule — the disconnect between aggregate class-level accuracy signals and per-augmentation credit assignment. This is a genuinely insightful observation that the authors should address, as it reveals that the current heuristic may work for reasons not fully captured by the paper's explanation. The reviewer's calibration also surfaces an important tension: the paper claims "first theoretical analysis" but provides geometric intuition rather than formal results, and overclaims tail-class advantages on data that only partially supports them. These insights sharpen the assessment beyond the paper's own self-presentation.

## Suggestions

1. **Fix the attribution mechanism.** Either (a) track per-augmentation accuracy by logging which augmentation was applied to each sample and computing separate positive counts per augmentation per class, or (b) provide a theoretical argument for why the aggregate-level heuristic converges to the correct ordering (e.g., under a stochastic dominance assumption), or (c) explicitly reframe the update as a noisy heuristic and validate it with a small-scale controlled experiment.

2. **Add the missing ablation.** Compare DODA against a version where each class samples augmentations uniformly at random from the same pool (or a fixed per-class distribution). This is essential to isolate the effect of the adaptive preference list.

3. **Report head/medium/tail breakdown for CIFAR-100-LT (Table 1)** to substantiate the claim of "outstanding performance on tail classes," and tone down claims on ImageNet-LT few-shot where gains are inconsistent.

4. **Specify the full augmentation pool** and the up-weight/down-weight update magnitude. Provide the K hyperparameter explicitly across experiments (the paper mentions "10 common DAs" for Figure 5 but not for other experiments).

5. **Formally define "sacrifice rate"** (e.g., fraction of classes whose per-class accuracy decreases after applying DA) and report it alongside the headline reductions.

## Score and Decision

This paper identifies a genuinely overlooked problem and proposes a novel, intuitive solution that delivers consistent empirical gains across multiple benchmarks and baselines. The core weaknesses — the attribution gap in the update rule and the missing ablation isolating the adaptive mechanism — are significant and prevent the paper from being a clean contribution. However, they do not invalidate the empirical results, and the problem framing alone is a useful contribution to the community. With a redone ablation and clarified mechanism, the paper would be substantially stronger.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>