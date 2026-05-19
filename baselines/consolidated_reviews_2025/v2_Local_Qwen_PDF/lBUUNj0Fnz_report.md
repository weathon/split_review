## Summary
This paper proposes a novel active learning (AL) framework for semantic image segmentation that relies exclusively on binary (yes/no) queries regarding the presence or absence of semantic classes. The authors formulate image-class selection as a constrained optimization problem balancing class-presence uncertainty and image redundancy, solved efficiently via linear programming (LP) relaxation. Extensive experiments on three benchmarks (Flickr, Cityscapes, PASCAL VOC) demonstrate that the proposed method achieves competitive mIoU scores (within 0.5–1.9% of pixel-level baselines) while reducing total human annotation time by up to 134-fold. The paper also includes a user study validating the drastic reduction in per-query annotation effort. While the core idea is practical and well-motivated, the manuscript requires tighter bounding of novelty claims, clarification of the LP rounding strategy, and explicit framing of the information asymmetry between binary and pixel-level baselines.

## Strengths
1. **Practical Motivation & Clear Problem Framing:** The paper addresses a highly relevant bottleneck in semantic segmentation: the prohibitive cost of pixel-level annotation. The shift to binary class-presence queries is intuitively appealing and directly targets the human-in-the-loop efficiency gap.
2. **Rigorous Optimization Formulation:** The formulation of image-class selection as a constrained optimization problem (Eq. 4) effectively balances informativeness (uncertainty) and diversity (redundancy). The derivation of the LP relaxation (Theorem 1) is mathematically sound and provides a computationally tractable solution.
3. **Comprehensive Empirical Validation:** The experiments cover three standard benchmarks, multiple backbone architectures, and varied query budgets. The inclusion of a user study (Table 1) provides concrete, human-grounded evidence for the annotation time savings, strengthening the practical impact claim.
4. **Transparent Trade-off Analysis:** The authors honestly report that pixel-level baselines achieve marginally higher mIoU scores. By explicitly comparing annotation time (Table 3) alongside performance, the paper successfully positions the proposed method on a favorable efficiency-accuracy Pareto frontier.

## Weaknesses
1. **Information Asymmetry in Baseline Comparison:** The experimental setup uses disparate query budgets (200/400 binary queries vs. 48 pixel-level images per iteration). While acknowledged, this creates a significant information-theoretic mismatch. Pixel-level masks provide dense spatial supervision, whereas binary queries offer only coarse class-presence signals. Without a normalized comparison (e.g., equal annotation time or equal number of queried images), the mIoU gap may be partially attributed to budget disparity rather than query granularity alone.
2. **Ambiguous LP Rounding Strategy:** The text states that the integer solution is recovered by selecting the $B$ highest entries in $M$, "observing the constraints." However, a simple top-$B$ thresholding can violate the per-image constraint $(M.e)_i \leq C_{max}$. The lack of a precise rounding algorithm (e.g., greedy assignment or iterative projection) reduces reproducibility and raises concerns about constraint violation in practice.
3. **Terminology & Proxy Assumption Clarity:** Equation (2) defines $G(j,i) = \alpha H_{ij}$ and labels it a "confidence matrix," but $H_{ij}$ is entropy (uncertainty), creating a terminology mismatch. Additionally, $p_{ij}$ is computed as the average pixel-wise probability, which conflates class frequency with presence uncertainty. This proxy assumption is not explicitly bounded, potentially misleading readers about the spatial sensitivity of the uncertainty metric.
4. **Limited User Study Statistical Power:** The user study relies on only 3 annotators and 10 images per dataset. The ease-of-annotation scores for binary queries show a ceiling effect (10 ± 0.0), providing no variance for statistical analysis. This limits the generalizability of the effort-reduction claims, particularly regarding annotator fatigue over long sessions.

## Key Issues
1. **Constraint Violation Risk in Rounding (Major):** The LP relaxation rounding step lacks algorithmic precision. If the top-$B$ selection violates $C_{max}$, the query distribution becomes uneven, undermining the diversity guarantee. This must be resolved with a explicit greedy or projection-based rounding procedure to ensure reproducibility and constraint adherence.
2. **Information-Theoretic Fairness (Major):** Comparing 200 binary queries against 48 pixel-level masks creates an unbalanced supervision signal. While the time-trade-off framing mitigates this, the absence of a normalized comparison (e.g., equal annotation time budget) leaves room for reviewers to question whether the mIoU gap is due to query type or budget disparity.
3. **Novelty Claim Bounding (Moderate):** The claim of being the "first" binary-query AL framework for segmentation is strong but requires careful distinction from weakly supervised segmentation methods that use image-level tags. Without explicit differentiation, the novelty may be perceived as incremental rather than foundational.
4. **User Study Generalizability (Minor):** The small sample size and ceiling effect in ease scores limit the statistical robustness of the effort-reduction claims. While the time estimates are compelling, the subjective ease ratings lack discriminative power.

## Actionable Suggestions
1. **Clarify Rounding Algorithm:** Replace the vague "observing the constraints" statement with a precise greedy rounding procedure. Explicitly state how ties or $C_{max}$ violations are handled (e.g., iterative assignment respecting per-image limits). Add this detail to Algorithm 1 or the main text.
2. **Normalize Baseline Comparison:** Add a supplementary experiment or analysis comparing methods under equal estimated annotation time (using Table 1 estimates). This will strengthen the fairness claim and isolate the impact of query granularity from budget disparity.
3. **Bound Novelty Claim:** Add a sentence in the Introduction or Related Work distinguishing the proposed binary-query AL setting from weakly supervised segmentation (which uses tags during training but not for active sample selection). Rephrase "first research effort" to "first AL framework... under the exact binary presence/absence query setting."
4. **Fix Terminology Mismatch:** Rename $G$ to "uncertainty matrix" or explicitly state that $G(j,i)$ represents *inverse confidence*. Clarify that $p_{ij}$ serves as a spatially aggregated proxy and acknowledge potential edge cases (e.g., fragmented classes).
5. **Acknowledge User Study Limitations:** Add a brief note acknowledging the small sample size and ceiling effect in ease scores. Frame the time estimates as lower bounds for annotation effort and suggest future work on annotator fatigue analysis.

## Storyline Options + Writing Outlines
## Abstract Outline (S1-S5)
- **S1 (Problem):** Semantic segmentation requires pixel-level annotations that are extremely labor-intensive to acquire.
- **S2 (Gap):** While active learning reduces the number of images to label, existing frameworks still demand detailed pixel- or region-level queries, which remain burdensome.
- **S3 (Method):** We propose a novel AL framework that poses only binary (yes/no) queries regarding class presence, formulated as a constrained optimization problem solved via LP relaxation.
- **S4 (Result):** Experiments on three benchmarks show our method achieves competitive mIoU (within 0.5–1.9% of pixel-level baselines) while reducing annotation time by up to 134-fold.
- **S5 (Impact):** This work establishes a highly efficient human-in-the-loop paradigm for segmentation, enabling scalable model training under strict labeling budgets.

## Introduction Outline (P1-P4)
- **P1 (Big Picture & Bottleneck):** Semantic segmentation powers critical applications but relies on costly pixel-level data. Active learning addresses this by selecting informative samples, yet conventional AL still requires detailed annotations per query.
- **P2 (Proposed Solution):** We introduce a binary-query AL framework that asks only whether specific classes are present in selected images. This drastically lowers per-query effort while maintaining model performance.
- **P3 (Method Intuition):** We formulate image-class selection as an optimization problem balancing class-presence uncertainty and image redundancy, solved efficiently via LP relaxation.
- **P4 (Evidence & Contributions):** User studies and extensive experiments demonstrate up to 134-fold time savings with marginal mIoU loss. Contributions include the first binary-query AL framework for segmentation, the LP-based selection algorithm, and a comprehensive efficiency-accuracy trade-off analysis.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Clarify LP rounding strategy with explicit greedy/projection algorithm. | Ensures reproducibility and constraint adherence; removes major validity concern. | Low |
| **P0** | Bound novelty claim and distinguish from weakly supervised segmentation. | Strengthens contribution positioning; prevents novelty challenges. | Low |
| **P1** | Add normalized comparison (equal annotation time) or explicit fairness framing. | Mitigates information-asymmetry criticism; strengthens trade-off claim. | Medium |
| **P1** | Fix terminology mismatch ($G$ as uncertainty vs confidence) and clarify $p_{ij}$ proxy. | Improves mathematical clarity and reader comprehension. | Low |
| **P2** | Acknowledge user study limitations (sample size, ceiling effect). | Increases scientific honesty and bounds generalizability claims. | Low |
| **P2** | Expand conclusion with validated limitations and specific future directions. | Provides balanced view and guides subsequent research. | Low |

## Experiment Inventory & Research Experiment Plan
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Limitation |
|---|---|---|---|---|---|---|
| E1 | Binary queries reduce effort with competitive mIoU | Flickr/Cityscapes/PASCAL, 25 iters, B=200/400 | mIoU, Time | Proposed outperforms RR/EE; close to pixel-level | Yes | Budget mismatch vs pixel-level |
| E2 | User study validates time savings | 3 annotators, 10 imgs/dataset | Time, Ease | Binary: 2-4s vs 7-37mins pixel | Yes | Small sample, ceiling effect |
| E3 | Backbone robustness | Cityscapes, Xception/ResNet50 | mIoU | Consistent trade-off across backbones | Yes | Single dataset tested |
| E4 | Query budget sensitivity | Flickr, B=200/300/400 | mIoU, Time | Performance scales with B; time savings hold | Yes | Limited to one dataset |
| E5 | Ablation (uncertainty/redundancy) | Flickr, B=400 | mIoU | Both terms necessary for optimal performance | Yes | Standard ablation |

## Research-Theme Gap Diagnosis
The core claim of efficiency-accuracy trade-off is well-supported, but the information asymmetry between binary and pixel-level baselines remains a validity gap. Additionally, the spatial limitations of binary queries (inability to resolve class overlap/fragmentation) are not empirically stress-tested.

## Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Cost | Gain |
|---|---|---|---|---|---|---|---|
| Fairness | Equal annotation time yields comparable mIoU | Scale pixel-level budget to match binary time (Table 1) | Proposed vs Scaled Pixel | mIoU | Gap < 1% | Low | Validates trade-off |
| Spatial Limitation | Binary queries struggle with fragmented classes | Test on dataset with high fragmentation (e.g., medical) | Proposed vs Pixel | mIoU, Class-wise IoU | Identify failure modes | Medium | Bounds applicability |
| Statistical Significance | mIoU gap is within variance | Paired t-test across 3 seeds | Proposed vs Coreset | p-value | p > 0.05 | Low | Strengthens claim |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper addresses a highly practical problem with a well-motivated and mathematically sound approach. The LP-based optimization and comprehensive empirical validation are strong points. However, the score is moderated by the information asymmetry in baseline comparisons, the ambiguous LP rounding strategy, and the need for tighter novelty bounding. These issues are fixable and do not invalidate the core contribution, but they currently limit decision confidence.

**Post-Revision Target:** [7.5, 8.5]/10

**Path to Target:** Clarifying the rounding algorithm, adding a normalized time-based comparison, and explicitly bounding the novelty claim against weakly supervised methods would significantly strengthen the paper's defensibility and impact. Addressing these P0/P1 items would elevate the manuscript to a strong acceptance candidate.