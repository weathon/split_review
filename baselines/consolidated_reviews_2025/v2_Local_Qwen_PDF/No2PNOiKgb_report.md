## Summary
This paper proposes an improved convex decomposition method for indoor scenes that combines two key innovations: (1) the incorporation of negative primitives via constructive solid geometry (CSG) to carve away geometry and represent free space, and (2) an ensembling strategy that trains multiple networks with varying primitive counts and selects the best configuration using a refine-then-choose approach. Extensive experiments on the NYUv2 dataset demonstrate substantial improvements in depth, normal, and segmentation accuracy compared to prior state-of-the-art regression and descent methods. The paper also includes practical improvements such as a biasing sample loss, annealing schedules, and corrected data augmentation. While the method shows strong empirical performance, the manuscript would benefit from clearer algorithmic descriptions, more precise scoping of novelty claims, and a more comprehensive discussion of limitations and failure modes.

## Strengths
1. **Strong Empirical Performance:** The proposed method achieves substantial improvements over existing SOTA methods on the NYUv2 dataset, particularly in absolute relative depth error. The refine-then-choose ensembling strategy effectively addresses the non-convex optimization landscape of primitive fitting.
2. **Innovative Use of Negative Primitives:** Incorporating CSG set differencing expands the representational capacity of convex primitives, allowing more parsimonious modeling of complex concavities and free space. The ablation studies clearly demonstrate the utility of negative primitives in specific scene configurations.
3. **Comprehensive Ablation and Analysis:** The paper includes thorough ablation studies on primitive counts, negative primitive ratios, biasing loss weights, learning rate decay, and data augmentation. This provides valuable insights into the training dynamics and hyperparameter sensitivity of the method.
4. **Practical Implementation Improvements:** The correction of camera calibration parameters during horizontal flip augmentation and the introduction of annealing schedules are practical contributions that improve training stability and accuracy, addressing overlooked details in prior work.

## Weaknesses
1. **Insufficient Algorithmic Detail for Ensembling and Loss Modifications:** The ensembling strategy is described intuitively but lacks precise algorithmic specification (e.g., exact network configurations, selection metric formulation). Similarly, the loss modifications for negative primitives are described qualitatively without mathematical definitions, hindering reproducibility.
2. **Overclaims and Unscoped Novelty Statements:** The contribution claims use strong language ("only one that can fit CSG... to indoor scenes") without adequate scoping or literature verification. The ensembling novelty is not clearly differentiated from standard model averaging or diversity techniques in computer vision.
3. **Weak Segmentation Evaluation Justification:** The segmentation metric relies on a heuristic (assigning the most common GT label to a primitive's face) that assumes clean primitive-object alignment. This is rarely true in cluttered indoor scenes and may inflate scores without reflecting true semantic parsing quality.
4. **Incomplete Limitations and Failure Mode Discussion:** The limitations section acknowledges compute costs but omits critical failure modes, such as reliance on accurate depth for selection, performance degradation with noisy monocular depth, and geometric challenges like reflective/transparent surfaces.

## Key Issues
1. **Reproducibility Risk in Method Description:** The lack of explicit mathematical formulations for the negative primitive loss modifications and the exact ensembling selection criterion makes it difficult for other researchers to reproduce the results. This is a critical barrier for methodological papers.
2. **Claim-Evidence Misalignment in Contributions:** The contribution statements make strong novelty claims ("only one," "novel ensembling") that are not sufficiently bounded or supported by related work analysis. This risks being challenged during review.
3. **Segmentation Metric Validity:** The heuristic used for segmentation evaluation does not robustly measure semantic alignment in cluttered scenes. Without acknowledging this limitation or providing complementary metrics, the segmentation results may be misleading.
4. **Missing Failure Mode Analysis:** The paper does not discuss scenarios where the method is likely to fail (e.g., depth noise, reflective surfaces, severe occlusion). This limits the reader's understanding of the method's practical boundaries.

## Actionable Suggestions
1. **Clarify Algorithmic Details:** Add a subsection or algorithm box explicitly defining the ensembling construction (network configurations, K values), the refine-then-choose selection metric, and the exact mathematical formulation of the modified losses for negative primitives.
2. **Scope Novelty Claims:** Rephrase contribution claims to be more precise. Use "to our knowledge, the first to apply CSG set differencing specifically to complex indoor scene decomposition from single RGBD images" instead of "only one." Explicitly differentiate the ensembling strategy from standard model averaging.
3. **Improve Segmentation Evaluation:** Acknowledge the limitations of the current segmentation heuristic. Consider adding an object-level IoU metric or clarifying that segmentation accuracy reflects geometric coverage of dominant labels rather than strict semantic parsing.
4. **Expand Limitations Discussion:** Add a paragraph discussing depth dependency, performance degradation with noisy monocular depth, and geometric failure modes (reflective/transparent surfaces, severe occlusion). This will strengthen the scientific rigor and practical utility of the paper.

## Storyline Options + Writing Outlines
**Abstract Outline:**
- S1: Define primitive decomposition as a challenging fitting problem due to varying scene complexity and strong primitive interactions.
- S2: Highlight limitations of current SOTA (fixed-count regression, positive-only unions) in capturing complex concavities and free space.
- S3: Introduce the proposed method: ensembling multiple predictors with varying primitive counts and incorporating negative primitives via CSG.
- S4: Describe the refine-then-choose selection strategy that overcomes local minima in the optimization landscape.
- S5: Report key quantitative results (e.g., >40% AbsRel reduction on NYUv2) and state code availability.

**Introduction Outline:**
- P1: Establish motivation for primitive representations (simpler reasoning, scene editing) and the specific challenge of obtaining accurate, parsimonious abstractions.
- P2: Contrast descent methods (local minima, start-point sensitivity) with regression methods (fixed capacity, biased predictions).
- P3: Identify the gap: lack of flexible representational primitives and robust selection strategies for complex real-world scenes.
- P4: Present the proposed solution: negative primitives for enriched geometry vocabulary + ensembling with refine-then-choose for robust selection.
- P5: Preview key empirical outcomes and list scoped contributions.

## Priority Revision Plan
**P0 (Critical - Must Fix):**
- Add explicit mathematical formulations for negative primitive loss modifications and ensembling selection criteria to ensure reproducibility.
- Scope novelty claims in the contributions list and abstract to avoid overstatements.

**P1 (Major - Should Fix):**
- Revise the segmentation evaluation discussion to acknowledge heuristic limitations and clarify what the metric actually measures.
- Expand the limitations section to include depth dependency, noisy depth scenarios, and geometric failure modes (reflective/transparent surfaces).

**P2 (Minor - Nice to Have):**
- Improve the introduction narrative flow to better connect the motivation with the proposed solution.
- Add concrete metric deltas to the abstract and introduction for stronger immediate impact.

## Experiment Inventory & Research Experiment Plan
**Completed Experiment Inventory:**
- Main results on NYUv2 (depth, normals, segmentation) comparing individual networks and ensembles against SOTA baselines.
- Ablation on primitive counts (K ∈ [8, 16, 24, 32, 40]) and negative primitive ratios.
- Ablation on biasing loss weight, learning rate decay, and data augmentation.
- Qualitative evaluations showing primitive configurations and negative primitive usage.

**Research-Theme Gap Diagnosis:**
- Missing analysis of robustness to depth noise (e.g., using monocular depth estimators with varying quality).
- No evaluation of failure modes on challenging geometric conditions (reflective surfaces, transparency, severe occlusion).
- Limited discussion of computational efficiency trade-offs in real-time or resource-constrained settings.

**Proposed Research Experiments:**
1. **Depth Noise Robustness Test:** Evaluate the method using depth maps from monocular estimators (e.g., MiDaS, Depth Anything) with varying noise levels. Measure performance degradation and selection accuracy.
2. **Failure Mode Analysis:** Curate a subset of NYUv2 scenes with reflective/transparent objects or severe occlusions. Qualitatively and quantitatively analyze primitive fitting failures.
3. **Efficiency Benchmark:** Report inference time and memory usage for different ensemble sizes and primitive counts, comparing against single-network baselines to clarify practical deployment trade-offs.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper presents a strong empirical contribution with substantial improvements over SOTA methods on NYUv2. The combination of negative primitives and ensembling is intuitive and effective. However, the score is moderated by insufficient algorithmic detail (hindering reproducibility), overclaims in the contribution statements, and a lack of comprehensive failure mode analysis. With the suggested revisions, particularly clarifying the method details and scoping the claims, the paper would be significantly stronger.

**Post-Revision Target:** [7.5, 8.5]/10