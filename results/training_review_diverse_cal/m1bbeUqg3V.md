Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper introduces HyperPg, a novel prototype representation that models a truncated Gaussian distribution over cosine similarities on the hypersphere (defined by anchor vector α, scalar mean μ, and scalar standard deviation σ). The authors propose HyperPgNet, an architecture using HyperPg prototypes aligned with human-defined concepts via pixel-level annotations and a "Right for the Right Concept" (RRC) loss. A concept extraction pipeline using Grounding DINO and SAM2 generates pixel-level annotations with reduced human effort. Experiments on CUB-200-2011 and Stanford Cars under a challenging protocol (full images, ~30 training images/class) show HyperPgNet outperforming ProtoPNet with fewer prototypes and faster convergence.

## Strengths

1. **Novel and principled prototype representation.** HyperPg (Section 3.3) combines the benefits of hyperspherical prototypes (cosine similarity, classification benefits) with Gaussian prototypes (statistical confidence, adaptive spread). A single HyperPg prototype with μ=0 can cover an entire hyperplane orthogonal to its anchor — a pattern that would require infinitely many point-based hyperspherical prototypes. This is a genuine theoretical advance over deterministic prototypes.

2. **Clear within-protocol accuracy and efficiency gains.** Table 1 shows HyperPgNet (without RRC) achieves 76.5% on CUB and 88.6% on Cars with 300/180 prototypes in ~40 epochs, versus ProtoPNet at 68.0%/86.4% with 2000/1960 prototypes in ~490 epochs — all under the same training protocol. The intermediate comparison ProtoPNet vs. ProtoPNet+HyperPg (68.0% → 70.5%, 490→200 epochs) isolates the benefit of the HyperPg representation itself before introducing concept alignment.

3. **Practical concept extraction pipeline.** Section 5 describes a pipeline using Grounding DINO + SAM2 that labels the entire Stanford Cars dataset in under 2 hours on consumer hardware (NVIDIA 4060 Ti). This is a concrete practical contribution that reduces the barrier to using concept-aligned training.

4. **Qualitative interpretability improvement.** Figure 5 shows gradient maps demonstrating that the RRC loss sharpens prototype focus onto annotated concept regions (e.g., the "head" prototype concentrating on the bird's head rather than other bright body regions). The progression from class-based → concept-aligned → RRC-regularized is visually clear.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaimed breadth of comparison.** The paper states that "HyperPgNet outperforms other prototype learning architectures" (abstract, introduction, conclusion), but among prototype-based methods, only ProtoPNet is directly compared under the same protocol. Other approaches discussed in the related work (ProtoPShare, ProtoPool, Deformable ProtoPNet, ProtoTree, PIPNet, ProtoGMM) are never implemented or compared. Since ProtoPNet is the most foundational prototype method, showing improvement over it is meaningful, but the claims should be scoped to what was actually tested. The current language implies a breadth of comparison that does not exist in the experiments.

2. **No quantitative evaluation of interpretability or concept alignment.** Interpretability is a central motivation (title, abstract, RRC loss design), yet the paper provides only qualitative gradient maps (Figure 5) as evidence. There are no concept-level metrics: no prototype-concept IoU, no prototype purity scores, no human evaluation, no comparison of activation regions to ground-truth concept masks. The paper asserts that the accuracy drop with RRC is "offset by increased transparency" (line 392), but transparency is never measured. Given the paper's framing, this is a significant gap.

### Minor

3. **No uncertainty quantification.** All results in Table 1 are single numbers without standard deviations or evidence of multiple runs. With only ~30 training images per class, variance across random seeds could be nontrivial, and the reader cannot assess whether the reported differences (e.g., 76.5% vs. 74.1% on CUB) are reliable. This is a standard expectation for empirical deep learning papers.

4. **Ablation confounds multiple changes.** The full comparison from ProtoPNet (2000 class prototypes, L₂) to HyperPgNet (300 concept prototypes, HyperPg) changes prototype type, prototype count, prototype-to-class assignment scheme, and training losses simultaneously. While the paper does include ProtoPNet vs. ProtoPNet+HyperPg to isolate the representation change (both use 2000 class prototypes), the jump to HyperPgNet is not cleanly ablated. It is unclear how much of the gain comes from (a) the HyperPg representation, (b) fewer prototypes trained per-concept, (c) the density loss, or (d) the different training dynamics of concept-aligned vs. class-aligned prototypes.

5. **Learned σ values not empirically validated.** The paper claims HyperPg "adapts to the spread of clusters" via learned σ, but no experiment shows that learned σ values differ meaningfully across concepts or improve robustness to intra-class variation. The theoretical illustration (Figure 2) uses a fixed σ=0.1. Without an analysis of learned σ values or a fixed-σ ablation, this claimed advantage is asserted but not demonstrated.

6. **No total parameter or FLOP counts.** The paper claims "fewer parameters" but only reports prototype counts (300 vs. 2000). The backbone is shared across all models, so the savings are limited to the prototype layer. Total model parameters and FLOPs should be reported to contextualize this claim.

7. **Segformer baseline performance is very low (17.7% CUB, 1.9% Cars).** While the paper correctly notes this is due to overfitting on the small training set, the extreme gap between the Segformer baseline and all other models raises the question of whether hyperparameters (e.g., learning rate, optimizer settings) were tuned appropriately for each backbone, or whether the Segformer backbone is simply poorly suited to this data-scarce, full-image protocol. The paper reports no hyperparameter tuning procedure.

### Trivial

8. **Learning rate and optimizer details not reported.** The paper specifies batch size and convergence criterion but omits learning rate, schedule, and optimizer choice, which are needed for reproducibility.

9. **"At scale" framing for Cars concept extraction is slightly overstated.** The Cars pipeline requires a manually defined list of 10 car parts (Section 5). This is a reasonable approach, but calling the pipeline fully "automated" (line 269) elides the human domain knowledge needed to define the concept vocabulary.

## Nice-to-Haves

- A fixed-σ ablation of HyperPg to quantify the empirical benefit of learning σ.
- An ablation of prototype count (e.g., HyperPgNet with 2000 prototypes) to isolate the effect of count from the effect of concept alignment.
- A brief discussion of the difference between the original RRR loss (which penalizes gradients *outside* relevant regions) and the RRC loss (which penalizes gradients *inside* concept regions) — the equations are clear but the design rationale for this difference is not discussed.
- Analysis of failure cases where concept alignment hurts accuracy.

## Removed Points

- **"Segformer baseline is worse than random"** — Factually incorrect. The critic claimed 17.7% (CUB) is "worse than random (0.5% for 200 classes)." Random is 1/200 = 0.5%; 17.7% is well above random.
- **"ConvNeXt baseline is far below the ~90% one would expect"** — This criticism evaluates against the standard protocol (bounding-box crops + 1200 images/class) whereas the paper explicitly uses a harder protocol (full images, ~30 images/class). The paper's own within-protocol comparisons are what matter.
- **"The experimental setup invalidates direct comparison to prior work" (framed as fatal)** — The paper never directly compares its numbers to published results under the standard protocol. All core comparisons are within-protocol. The protocol difference is acknowledged. The valid concern is about claim breadth, not about invalidity of the comparisons themselves.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between a genuinely novel technical idea (HyperPg) and an evaluation that is narrower than the claims. The most interesting unresolved question is whether HyperPg's representational advantage (the ring-shaped activation pattern from a single prototype with μ=0) is what drives the accuracy gains — this could be tested with a simple synthetic experiment or by visualizing which concepts learn μ values close to zero.

## Suggestions

1. **Scope the claims to what is actually tested.** Replace "outperforms other prototype learning architectures" with "outperforms ProtoPNet" or "outperforms comparable prototype methods" throughout.
2. **Add quantitative interpretability metrics.** The most straightforward is to compute the IoU between prototype gradient masks and ground-truth concept masks for held-out images. This directly validates the RRC loss's stated purpose.
3. **Report results over at least 3 random seeds (mean ± std)** for all key numbers.
4. **Add at least one more prototype-learning baseline** under the same protocol (e.g., a simple reimplementation of ProtoPool or ProtoPShare) to substantiate the broader claim.
5. **Ablate prototype count** — run HyperPgNet with 2000 prototypes to separate the effect of count from architecture design.
6. **Analyze learned σ values** — show the distribution of learned σ across concepts and compare against a fixed-σ baseline.
7. **Report total parameter counts and FLOPs** for all models.

## Score and Decision

The paper presents a genuinely novel and mathematically well-motivated prototype representation (HyperPg) and a practical architecture (HyperPgNet). The within-protocol comparisons convincingly show improvement over ProtoPNet. However, the evaluation has substantial gaps: the claim of outperforming "other prototype learning architectures" is unsupported by the breadth of baselines tested; interpretability — a central contribution — is not quantitatively evaluated; and results lack uncertainty quantification. These gaps are addressable but prevent the paper from meeting the standard for acceptance in its current form.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>