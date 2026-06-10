## Summary

This paper studies discriminative probabilistic modeling (DPM) over continuous domains for self-supervised representation learning. It uses multiple importance sampling (MIS) to Monte Carlo integrate the intractable partition function in the DPM objective, showing that the InfoNCE/GCL family of losses corresponds to a uniform approximation of the "popularity" measure (the sum of conditional densities). A generalization bound (Theorem 1) reveals that this uniform approximation incurs a non-diminishing error for continuous Y. To address this, the paper proposes a non-parametric convex optimization approach to learn the popularity weights, yielding the NUCLR algorithm. Experiments on CC3M and CC12M bimodal pretraining show improved retrieval performance over strong baselines like SogCLR.

## Strengths

1. **Novel theoretical identification of a structural limitation in InfoNCE/GCL.** Theorem 1 derives a generalization bound decomposing the error into standard terms plus ℰ\_w(q̃,q;Ŝ), and Remark (line 131) proves that the uniform popularity approximation used by GCL produces a **non-diminishing** error term for continuous Y, vanishing only when Y is finite (line 132). This is a genuine insight that prior work (Arora et al. 2019, Lei et al. 2023) did not identify — it isolates a concrete mathematical limitation of InfoNCE tied to continuous domains.

2. **Elegant non-parametric method for popularity estimation with rigorous characterization.** The convex optimization in Eq. 14–15 and Theorem 2 show that optimal solutions satisfy a fixed-point equation matching the MIS-based approximation of the true popularity q. The toy experiment (Figure 1, right panel) empirically validates that this method reduces generalization error to nearly match the exact-MLE oracle, while GCL's error plateaus — directly confirming the theory.

3. **The NUCLR algorithm is clean and well-motivated.** The alternating optimization scheme (Algorithm 1) is principled: the ζ-update learns popularity weights, the w-update optimizes representations. The EMA technique handles gradient bias, and the ξ-trick prevents pushing positive pairs away. The ablation study (Figure 3) systematically isolates each component's contribution, and the learned q̃' values capture semantically meaningful popularity (human-centric vs. abstract images, Figure 4).

4. **Consistent empirical improvements on retrieval tasks.** On both CC3M and CC12M, NUCLR improves retrieval Recall@1 over SogCLR by ~1–3% relative on MSCOCO and Flickr30k, with the mean score across all tasks improving by ~1 point (CC3M: 40.26 vs. 39.16; CC12M: 43.20 vs. 42.28). These gains are achieved at batch size 512, substantially smaller than CLIP's 32k+.

## Weaknesses

### Major

1. **Theoretical advantage fails to materialize on ImageNet1k classification, and the paper does not analyze why.** Theorem 1 and the toy experiment predict that better popularity approximation should reduce generalization error. Yet on ImageNet1k, NUCLR and SogCLR achieve identical top-1 accuracy on CC12M (49.82) and differ by only 0.09 on CC3M (40.49 vs. 40.40) — well within one standard deviation. The paper notes this ("marginally better or comparable," line 282) but does not investigate *why* the theoretical advantage disappears on the most standard classification benchmark. Remark 2 claims that DPM provides statistical guarantees for downstream discriminative tasks, so this disconnect between theory and the flagship classification result is a significant evidential gap. The contribution would be substantially stronger if the paper explained whether (a) classification is inherently less sensitive to popularity estimation than retrieval, or (b) some aspect of the evaluation protocol masks the advantage.

2. **Narrow empirical scope relative to the generality of the claims.** The abstract and introduction claim "superior overall performance" for "self-supervised representation learning," but the experiments are confined to: one architecture (ResNet-50 + DistilBert), one batch size (512), and two datasets from the same domain (image-text captioning). No batch size ablation is performed — surprising given that SogCLR's central motivation was enabling small-batch training, and NUCLR inherits this claim. No vision-only contrastive learning experiments (e.g., SimCLR on CIFAR/ImageNet) are included, despite the framework being presented as general. The evaluation is acceptable for a first empirical validation, but the strength of the claims ("superior overall performance," "discriminative probabilistic modeling for self-supervised representation learning") exceeds what the evidence supports.

### Minor

3. **Unverified assumption in Theorem 1.** The bound assumes q^(j) ≥ Ω(n) almost surely for all j (line 124) — i.e., each data point's total popularity grows linearly with n. For outlier or atypical points, this may not hold. The paper neither verifies this assumption on real data nor discusses when it might be violated. While a standard technical assumption, its validity for the tested datasets is unclear.

4. **Missing training cost comparison.** The paper claims "only minor computational and memory overheads" (line 230) but reports no wall-clock time, memory usage, or throughput comparison. For a practical algorithm targeting large-scale pretraining, this information is needed to assess the overhead of storing and updating 2n additional floating-point values.

5. **Limited transparency about the SogCLR baseline.** The footnote (line 237) states that the SogCLR implementation comes from "the updated codebase of Qiu et al. (2023), which yields better results than that reported in Qiu et al. (2023)." Without specifying what changed, the reader cannot assess whether the comparison is to the original SogCLR or a modified version. Since SogCLR is the most directly comparable baseline (NUCLR reduces to SogCLR when ζ=0 and ξ=0), this matters.

6. **The ζ₀ hyperparameter is tuned per dataset** (−0.05 for CC3M, 0 for CC12M) with no sensitivity analysis. It is unclear how robust the algorithm is to this choice, and whether it interacts strongly with the ξ-trick or the ζ-freezing schedule.

### Trivial

7. **Ablation results (Figure 3) are presented as line plots without numerical values**, making precise cross-comparison difficult. The reader cannot determine, for example, whether NUCLR-† (fixed ζ) is closer to SogCLR or to full NUCLR.

## Nice-to-Haves

- A batch-size ablation (B = 256, 128, 64) would substantially strengthen the practical case for NUCLR's small-batch viability.
- Analysis of the learned ζ values over training (stability, convergence) would help bridge the toy experiment and real-world implementation.
- Vision-only experiments (SimCLR on CIFAR-100 or ImageNet-100) would broaden the evidence base without large resources.
- A discussion of why classification benefits less than retrieval from better popularity estimation would sharpen the contribution.

## Removed Points

These points from the inputs were evaluated against the paper and removed:

- **"Circularity in the approximation chain"** (Harsh Critic's Critical Issue 2): The fixed-point formulation in Eq. 14/Theorem 2 is a self-consistent estimation approach standard in statistics (method of moments, estimating equations). The paper marks the approximation with "≈" (line 140) and Theorem 2 characterizes the fixed-point solution. The toy experiment empirically validates the approach. The critic's framing of this as a structural flaw overstates the issue — no theoretical paper in this area provides a complete chain of proven error bounds linking practical optimization to the true q. **Demoted from "Critical" to Removed.**

- **"JEPA comparison is overdrawn"** (Section-by-Section Notes): The paper's statement that JEPA "lacks some statistical guarantees of probabilistic models" (line 40) is a factual distinction between DPM and energy-based models, not an overstatement. The paper does not claim JEPA is inferior — it merely notes a structural difference. **Removed.**

- **"The generalization bound does not compute d_L for the encoders used"** (Missing Parts): This is standard for qualitative Rademacher complexity bounds; quantitative tightness is not expected. **Removed.**

- **"No experiments on vision-only contrastive learning"** / **"No comparison of training cost"** (Missing Parts): These are valid suggestions but moved to Nice-to-Haves as they test scope beyond what the paper claims to evaluate.

- **Strength about "superior overall performance"** (Strength Finder point 4): The empirical improvements are real but modest on classification. This strength is kept but tempered by the ImageNet1k gap. The strength finder's framing as a pure strength without caveats is too strong; it's included in the strengths section above with appropriate qualification.

- **"Remark 1 about ∞-InfoNCE not being a valid PDF is tangential"** (Section-by-Section Notes): This remark resolves a conceptual ambiguity in prior literature about what probabilistic interpretation (if any) the ∞-InfoNCE loss carries. It is directly relevant to the paper's framing. **Removed.**

## Novel Insights

Beyond the paper's own contributions: The harsh critic's observation about the theory-practice gap — that the elegant toy experiment (Figure 1, right) shows near-perfect agreement with theory, yet real-world ImageNet1k results show zero improvement — is the most insightful synthesis across the two reviews. This gap suggests that either (a) the uniform popularity approximation is *not* the bottleneck limiting classification performance on large-scale bimodal pretraining (other factors like architecture, data quality, or optimization may dominate), or (b) the ImageNet1k zero-shot evaluation protocol is too coarse to detect representational improvements that the theory predicts. Neither reviewer, nor the paper itself, fully resolves this tension, and it points toward a concrete direction for future work: understanding when and why popularity estimation matters for different downstream task families.

## Suggestions

1. Investigate why ImageNet1k classification shows no benefit. Analyze the learned ζ values per class or per image type; compare representation geometry (e.g., k-NN classification, probing) to see if NUCLR representations capture different information despite identical linear-probe accuracy.
2. Add a batch-size ablation (even just B=256) to demonstrate small-batch robustness.
3. Report wall-clock time and peak memory for SogCLR vs. NUCLR.
4. Provide numerical values for the ablation study, and test ζ₀ sensitivity over a small grid.
5. Clarify what changed in the "updated codebase" of Qiu et al. (2023) for the SogCLR implementation.

## Score and Decision

This paper makes a genuine theoretical contribution: identifying the non-diminishing error of InfoNCE's uniform popularity approximation on continuous domains, and proposing a principled non-parametric fix via convex optimization. The NUCLR algorithm is well-motivated, clean, and backed by an informative toy experiment. The empirical results show consistent improvements on retrieval tasks.

However, the evaluation is narrow, and the most theoretically significant prediction — that better popularity estimation should improve generalization across all downstream tasks — is not borne out on ImageNet1k classification, the most standard benchmark. This gap is acknowledged but not analyzed. The paper's claims of "superior overall performance" slightly overstate what the evidence supports.

For ICLR, the theoretical contribution is solid and novel, but the empirical validation needs broadening to match the scope of the claims. I rate this as a solid paper with a clear contribution, held back by a significant theory-practice gap that the authors should address.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>