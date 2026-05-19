- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 5, 6, 8
Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper studies the effect of data augmentation (DA) in long-tailed learning, arguing that class-independent DA can "hypocritically" boost average accuracy while disproportionately harming tail classes ("augmentation-wise imbalance"). To remedy this, the authors propose DODA (Dynamic Optional Data Augmentation), which maintains a per-class probability distribution over a set of candidate augmentations and dynamically updates these preferences based on per-class positive sample counts. Experiments on CIFAR-100-LT, ImageNet-LT, and iNaturalist 2018 show consistent (though modest) improvements when DODA is added to several long-tailed learning baselines.

## Strengths

1. **Empirical demonstration that DA can harm specific classes (Figure 2):** The paper provides concrete visual evidence on CIFAR-100-LT that class-independent DA (Cutout, CUDA, both) improves average accuracy but degrades accuracy on many tail-class instances. This is a real and under-appreciated phenomenon in long-tailed learning, and the paper documents it clearly.

2. **Consistent improvements across multiple baselines on CIFAR-100-LT (Table 1):** DODA is integrated with six different methods (CE, CE-DRW, LDAM-DRW, BS, RIDE, BCL) and yields consistent gains (typically +1–2% overall, with larger gains on tail classes). This demonstrates flexibility and orthogonality to existing approaches on the primary evaluation dataset.

3. **Reduction in class sacrifice rate (Figure 4):** The paper shows that DODA reduces the number of classes whose accuracy drops after augmentation, directly validating that the method addresses the identified problem.

4. **Efficiency advantage over search-based augmentations (Figure 7):** DODA matches or outperforms AutoAugment, Fast AutoAugment, DADA, RandAugment, and CUDA without requiring expensive augmentation search, which is a practical benefit.

## Weaknesses

### Fatal
None. The paper's core claims are supported by some evidence, and the method is plausible.

### Major

1. **The "theorems" do not constitute a sound theoretical analysis and should not be presented as such.** The paper labels four statements as "Theorems" (lines 44, 52, 86, 140), but none is provided with a proof, formal hypothesis, or rigorous derivation. Theorem 1 and Theorem 2 are informal observations stated in prose with equations that assert a bias exists without deriving it. Theorem 2's equation is garbled — it ends with `\Longrightarrow c` (line 55), where `c` appears as a dangling symbol. Theorem 3's derivation of `ψ_{c_t} - ψ_{c_h} > 0` depends on the assumption `Δ_{c_h} = Δ_{c_t}` (line 84), which is asserted without justification — yet the paper itself notes that tail classes have "coarser, sparser clusters," which would likely cause the same augmentation to expand their distribution radius differently. Theorem 4 is stated without any formal framework for the "level-set bias" it references. The paper's motivation would be stronger if it simply presented the empirical observation (Figure 2) as the primary motivation, without claiming a rigorous theoretical framework that does not hold. This weakness undermines the paper's claim of providing a "theoretical analysis" as a contribution.

2. **The "state-of-the-art" claim is not supported on ImageNet-LT or iNaturalist 2018.** The abstract claims DODA "achieves the state-of-the-art performance across mainstream long-tailed benchmarks including CIFAR-100-LT, ImageNet-LT, and iNaturalist 2018." This is contradicted by Table 2: on ImageNet-LT, CE+DODA (48.8%) underperforms BCL (51.9%) and RIDE (50.7%); on iNaturalist 2018, CE+DODA (71.5%) underperforms CUDA (74.6%) and others. The paper only integrates DODA with CE on these large datasets — not with the stronger baselines (BS, RIDE, BCL) that were used on CIFAR-100-LT. Without showing DODA's effect on top of stronger methods at scale, the claim of state-of-the-art is not supported and the evaluation is incomplete.

3. **No ablation isolating the source of improvement.** The core mechanism — updating per-class preference probabilities based on whether the positive sample count increased compared to the previous epoch — is not validated against simpler alternatives. For example: (a) a fixed per-class augmentation chosen by validation-set search, (b) random per-class augmentation without any update rule, (c) an update rule based on validation accuracy rather than training positive count, or (d) a uniform probability over all augmentations. The 50-epoch random warmup period (out of 200 total epochs) is an arbitrary design choice that is not ablated or justified. Without these ablations, it is unclear whether the preference-list machinery is responsible for the reported improvements or whether a simpler scheme would match or exceed them.

### Minor

1. **The 10 augmentation methods are never enumerated.** The paper states "10 common DAs" are used (line 204) and gives three examples (rotation, horizontal flip, Gaussian blur, line 105) but never lists the full set. This is a reproducibility gap.

2. **No discussion of limitations.** The paper does not address scenarios where DODA might fail — e.g., extreme tail classes with only 1–2 samples where the positive-count update signal is essentially noise, or settings where augmentations are not label-preserving. The paper would benefit from a brief limitations paragraph.

3. **Unusual learning rate for CIFAR-100-LT.** The learning rate is set to `10^{-4}` for ResNet-32 on CIFAR-100-LT (line 172), which is three orders of magnitude below the standard value of 0.1 used in the cited work (Cao et al., 2019). The paper claims to "follow the general experimental setup from Cao et al. (2019)," creating a discrepancy that warrants clarification.

4. **Ambiguous sacrifice-rate claim.** The text states "DODA reduces the sacrifice rate by 31% and 24%, respectively" (line 202) without clearly specifying the two baselines being compared. The figure caption (line 199–200) mentions "CE and CE with CUDA" but the "respectively" is unresolved.

### Trivial
None.

## Nice-to-Haves

- Report DODA integrated with stronger baselines (e.g., BCL, RIDE) on ImageNet-LT and iNaturalist 2018 to demonstrate that the improvement transfers beyond the CE baseline at scale.
- Include standard deviations or confidence intervals for the main accuracy results, particularly for tail-class accuracy where variance is high.
- Add a sensitivity analysis on the number of candidate augmentations K and on the augmentation probability p_aug.

## Removed Points

These points were flagged by the reviewers but are either not supported by the paper, factually incorrect, or otherwise inappropriate for inclusion:

1. **"No code or reproducibility details beyond high-level optimizer settings"** — Removed per hard rules: requests for code release and minor implementation details are nitpicks about reproducibility artifacts impractical to include in the submission.
2. **"Missing related works"** — Removed per hard rules: a meta-reviewer should not comment on missing related works.
3. **"Missing appendix, missing proofs in appendix"** — Removed per hard rules: the parser strips those sections from all papers.
4. **"Formatting nitpicks, typos, etc."** — Removed per hard rules: these are parser artifacts.
5. **"The comparison to methods like TSC, GCL, DiVE is missing"** — Partially removed: the harsh critic's point about unlisted recent methods is a form of "missing related works" complaint. The core concern about SOTA overclaiming is already captured in Major Weakness #2.
6. **Strength (from Strength Finder): "Theoretical analysis of DA's class-wise harm (Theorems 1–3)"** — Removed because, as verified in Major Weakness #1, these "theorems" are not rigorous and do not constitute a genuine strength of the paper. The empirical observation (Figure 2) is the genuine strength; the theoretical framing is a liability.
7. **Strength (from Strength Finder): "State-of-the-art results across three benchmarks"** — Weakened: as verified in Major Weakness #2, this claim is not supported on ImageNet-LT and iNaturalist 2018. Retained only as a partial strength (CIFAR-100-LT results) in the Strengths section.
8. **"The level-set discussion is imprecise"** and similar generality about the theory — Removed because the specific, verifiable problems with the theory are already captured in Major Weakness #1. The general complaint adds no new information.
9. **"The 'two birds' metaphor is overused"** — Removed as a pure formatting/style nitpick.
10. **"The assumption that Δ_c_h = Δ_c_t is unsupported and likely false"** — Retained and folded into Major Weakness #1 (it is a specific, verifiable claim about the paper's content, not speculation).
11. **"The update signal for tail classes with few samples will be extremely noisy"** — Retained as a sub-point in Minor Weakness #2 (limitations).

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder do not surface a genuinely novel observation that the authors themselves missed; they primarily re-litigate the paper's own claims and evidence quality.

## Suggestions

1. Remove the "theorem" framing entirely. Present the level-set and distribution-span discussion as motivation and intuition, not as a formal theoretical framework. Cite the empirical observation (Figure 2) as the primary motivation for DODA.
2. Add an ablation study comparing the proposed update rule to at least two simpler alternatives: (a) fixed per-class augmentation selected by a validation set, and (b) random per-class augmentation. This would establish whether the adaptive mechanism is necessary.
3. Tone down the "state-of-the-art" claim. The results on CIFAR-100-LT support "competitive" or "strong improvements on multiple baselines," but the large-scale results do not support a SOTA claim.
4. Integrate DODA with at least one stronger baseline (e.g., BCL or RIDE) on ImageNet-LT and iNaturalist 2018, or acknowledge the limitation that the large-scale evaluation is restricted to CE.
5. List the 10 augmentation methods used, clarify the "31% and 24%" baseline comparisons, and add a brief limitations paragraph.
