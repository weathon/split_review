Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the consolidated review.

---

## Summary

This paper introduces HyperPg, a novel prototype representation that models a 1D truncated Gaussian distribution over cosine similarities on the hypersphere, with learnable mean and standard deviation. The authors build HyperPgNet, which uses these probabilistic prototypes aligned to human-defined concepts via pixel-level annotations, and propose an automated concept extraction pipeline using SAM2 and Grounding DINO. Experiments on CUB-200-2011 and Stanford Cars show HyperPgNet achieves 76.5% and 88.6% accuracy respectively—outperforming ProtoPNet and CBM baselines with 6–10× fewer prototypes and ~12× faster convergence.

## Strengths

1. **Novel probabilistic prototype representation on the hypersphere.** HyperPg (Section 3.3) learns a truncated Gaussian PDF over cosine similarities, with anchor vector α, scalar mean μ, and scalar std σ. This enables a single prototype to model complex latent structures (e.g., ring-shaped regions for μ between -1 and 1) that would otherwise require many point-based prototypes. The density-based similarity score provides a natural measure of statistical confidence, which point-based L₂ or cosine prototypes lack. The mathematical formulation and 3D visualizations (Figure 2) clearly illustrate this contribution.

2. **Substantial accuracy and efficiency gains over tested baselines.** HyperPgNet without L_RRC achieves 76.5% on CUB and 88.6% on Cars using only 300/180 prototypes, compared to ProtoPNet's 68.0%/86.4% with 2000/1960 prototypes (Table 1). Convergence accelerates from ~490 epochs (ProtoPNet) to ~40 epochs (HyperPgNet) as shown in Figure 4. The "ProtoPNet + HyperPg" ablation (replacing only the prototype layer) already improves accuracy to 70.5%/87.4%, isolating the contribution of the HyperPg representation itself.

3. **Modular, swappable architecture design.** The HyperPg Module separates cosine similarity computation (first layer) from density estimation with learnable μ, σ (second layer), as described in Section 4.3 and Figure 3. This modularity allows the approach to be adapted to other similarity measures or probability distributions, making the idea transferable beyond prototype learning.

4. **Automated concept labeling pipeline.** The SAM2 + Grounding DINO pipeline (Section 5) generates pixel-level concept annotations for the Stanford Cars dataset (10 car parts) in 2 hours on a single RTX 4060 Ti, reducing human labeling effort. For CUB, it leverages existing point annotations to produce segmentation masks via SAM2 with negative points.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient comparative evaluation.** The paper claims HyperPgNet "outperforms other prototype learning architectures" (Abstract, Conclusion) but only evaluates against ProtoPNet (L₂ and HyperPg variants) and Concept Bottleneck Models. Several recent prototype architectures cited in the related work—ProtoPShare, ProtoPool, ProtoTree, PIPNet, MCPNet, ProtoSeg—are never compared experimentally. These methods differ in design (shared prototypes, decision trees, multi-scale concepts) and several are concept-aligned. Without direct comparison under the same protocol, the paper's central claim is broader than its evidence. This is the most significant gap in the current submission.

2. **Confounded ablation prevents attribution of contributions.** HyperPgNet differs from "ProtoPNet + HyperPg" simultaneously in: (i) number of prototypes (300 vs 2000), (ii) use of concept-based (vs class-based) prototype assignment, (iii) density loss L_Den (vs L_Clst+L_Sep), and (iv) the RRC loss. The only ablation provided is with/without L_RRC. The 6-point gain on CUB and 1.2-point gain on Cars relative to "ProtoPNet + HyperPg" cannot be attributed to any single component. An ablation isolating (a) HyperPgNet with class-based prototypes (same architecture, no concept annotations, no L_RRC), (b) HyperPgNet with concept annotations but without L_Den or L_RRC, and (c) varying the number of prototypes, is needed to support claims about what drives the improvement.

### Minor

3. **No quantitative evaluation of the concept extraction pipeline or interpretability.** The paper claims "enhanced interpretability" from concept-aligned prototypes, but provides only qualitative gradient maps (Figure 5) for three variants. No metric quantifies concept faithfulness—e.g., Intersection-over-Union between prototype activation heatmaps and ground-truth concept masks (available for CUB from part annotations). The RRC loss consistently reduces accuracy (by 2.4% on CUB, 7.4% on Cars) with the justification that it improves transparency, but without a quantitative faithfulness metric, the trade-off is not empirically justified. Similarly, the concept extraction pipeline (SAM2 + Grounding DINO) is presented as a contribution but its segmentation quality is never evaluated against ground truth.

4. **No standard deviations or confidence intervals.** Results in Table 1 are reported as single-run accuracy values. Given the small training set size (~30 images/class after online augmentation), variance across runs could be substantial. Reporting mean and std over at least 3 seeds is standard practice and would strengthen the reliability of the claims.

5. **Prototype count selection not justified or ablated.** The paper uses 300 prototypes for CUB (30 concepts × 10 per concept) and 180 for Cars (10 parts × 18 per concept). No explanation is given for the choice of 10 or 18 prototypes per concept, and no sensitivity analysis is provided. Since the prototype count differs substantially from ProtoPNet's 2000/1960 (10 per class), this hyperparameter could influence the comparison.

### Trivial

6. **No analysis of learned μ and σ parameters.** The paper does not report how μ and σ behave during training or whether they converge to sensible values. Reporting learned σ values for a sample of prototypes would demonstrate that the model actually adapts to cluster spread rather than collapsing to degenerate values.

7. **No explicit total parameter count.** The abstract claims "fewer parameters" but only prototype counts are reported. While fewer prototypes implies fewer learned parameters in the prototype layer, providing total model parameter counts (including backbone and neck) would substantiate the claim.

## Nice-to-Haves

- An ablation varying the number of prototypes per concept (e.g., 5, 10, 20) to show sensitivity.
- A quantitative interpretability metric such as mIoU between prototype gradient maps and concept masks.
- Evaluation against at least one additional recent prototype method (e.g., ProtoPool or ProtoTree) under the same experimental protocol would significantly strengthen the paper.

## Removed Points

- **"Segformer backbone is ill-suited / comparison is unfair"** — The paper clearly states (line 302) that all compared models use the same pretrained Segformer backbone. The Segformer baseline's poor performance (17.7%) applies equally to all methods sharing that backbone; the comparison is fair and symmetric.
- **"Potential dimension mismatch in RRC loss"** — The gradient ∂/∂xᵢ is taken element-wise over input pixels, and A_{xᵢ,k} is a binary mask over pixel space. Multiplying a gradient by a binary mask is standard practice (identical to the original RRR loss). No dimensional mismatch exists.
- **"Truncated Gaussian PDF instability"** — Speculative concern about as σ→0 behavior. The paper reports no training instability, and the model converged successfully in all reported runs. The concern about gradient clipping or σ schedules is a trivial implementation detail.
- **"Training setup makes numbers incomparable with published results"** — The paper explicitly acknowledges this difference (line 304) and applies it uniformly to all methods. This is a deliberate design choice, not a flaw.

## Novel Insights

Beyond the paper's own contributions, the most interesting insight emerging from the reviews is the tension between two design goals: concept-aligned prototypes improve interpretability but incur an accuracy cost (2.4–7.4% with L_RRC). The paper presents this as a trade-off controllable via λ weights, but does not validate whether the accuracy drop is justified by measurable gains in faithfulness. This mirrors a broader question in the interpretability literature—whether alignment objectives that reduce accuracy are actually yielding more truthful explanations or merely imposing spurious constraints.

## Suggestions

1. **Expand the baseline set.** Include at least one recent concept-aligned method (MCPNet) and one recent non-concept prototype method (ProtoPool or ProtoTree) under the same training protocol. This is the single highest-impact improvement.

2. **Add ablations to isolate contributions.** Specifically: (a) HyperPgNet with class-based prototypes (no concept annotations) using L_Den; (b) HyperPgNet with concept annotations but without L_Den; (c) HyperPgNet with varying prototype counts (e.g., 500, 1000) to match ProtoPNet settings.

3. **Quantify interpretability.** Report mIoU or Dice between prototype gradient activation maps and ground-truth concept masks for CUB. This would justify the accuracy drop from L_RRC by showing a measurable faithfulness improvement.

4. **Report statistics over multiple seeds.** Three runs with mean and std for Table 1 would significantly increase confidence in the results.

## Score and Decision

**Originality:** 7/10 — HyperPg's truncated Gaussian on the hypersphere is genuinely novel.
**Importance:** 7/10 — Interpretable prototype learning with human-aligned concepts is an active, important area.
**Claims supported:** 5/10 — The core claims about HyperPg's benefits over ProtoPNet are supported, but the broader claim of "outperforming other prototype learning architectures" is overclaimed given the narrow baseline set.
**Soundness of experiments:** 6/10 — The experimental design is internally consistent but incomplete (missing baselines, ablations, statistics).
**Clarity:** 7/10 — Well-organized and clearly written.
**Value to community:** 6/10 — The HyperPg representation has genuine potential; the paper would benefit from a more thorough evaluation.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>