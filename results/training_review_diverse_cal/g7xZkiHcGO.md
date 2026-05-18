Here is my consolidated meta-review.

---

## Summary

This paper proposes the first domain adaptation benchmark for indoor 3D object detection. It introduces two large-scale synthetic datasets (SimRoom, SimHouse) generated via the ProcTHOR framework, combines them with existing real-world datasets (ScanNet, SUN RGB-D), and defines four adaptation scenarios: high-to-low quality, low-to-high quality, synthetic-to-real, and single-room-to-multi-room. Through controlled experiments, it identifies the synthetic-to-real gap as the most challenging domain gap. The paper also provides baselines using several unsupervised domain adaptation methods adapted from other tasks.

## Strengths

- **First domain adaptation benchmark for indoor 3D object detection.** The paper constructs four cross-dataset scenarios (Section 3.3.3) and shows drastic performance drops in cross-dataset evaluation (Table 2: e.g., ScanNet→SUN RGB-D drops from 37.52 to 20.96 mAP), establishing a previously missing evaluation framework for this problem.
- **Large-scale synthetic datasets with precise annotations.** SimRoom (176k objects) and SimHouse (686k objects) provide an order of magnitude more annotated objects than ScanNet (~37k) and SUN RGB-D (~37k) (Table 1). The generative framework eliminates manual labeling costs and enables flexible control over scene configuration.
- **Systematic factor analysis identifying synthetic-to-real as the hardest gap.** Controlled experiments (Table 2, Table 5) show SimRoom→ScanNet yields only 11.20 mAP, lower than any other cross-dataset setting, and data-scale matching experiments confirm this gap remains dominant even with 3,000 synthetic training scenes (5.25 mAP vs. ScanNet's 22.54 mAP with 230 scenes).
- **Controlled decomposition of synthetic-vs-real factors.** By inserting real ScanNet objects into simulated layouts (Table 4), the paper isolates the semantic gap from layout differences, finding that object placement layout is a more critical factor than object appearance—an insight uniquely enabled by the controllability of their generative pipeline.

## Weaknesses

### Fatal
None.

### Major

1. **UDA method adaptations are underspecified.** Section 4.3.2 states: "Note that due to the difference on task setting, we re-implement all the methods and make some adjustments to achieve better results on object detection task." However, the paper provides zero detail on what these adjustments were for any of the four methods (VSS, PPFA, RV, OHDA)—no architectural changes, loss modifications, or hyperparameter choices are documented. Since the paper's value as a benchmark depends on baselines being usable by future work, this undocumented "black-box" re-implementation undermines reproducibility. This is particularly acute for OHDA, which is cited as unpublished, giving readers no way to assess its implementation. The paper needs either a detailed appendix describing each adaptation or a released codebase to serve its stated purpose as a benchmark foundation.

2. **Label space merging process lacks transparency.** Section 3.3.2 describes merging fine-grained categories into 15 broader categories and selecting those with "at least 150 objects," but: (a) the threshold is ambiguous—does "each contains at least 150 objects" mean *per dataset* or *in total across all datasets*? (b) No explicit mapping from original category names to merged categories is provided (only the single example of "dining table" / "office table" → "table"). (c) No per-dataset object counts for the final 15 categories are reported. Since domain adaptation assumes the same semantic categories across source and target, an unclear or unreproducible label mapping introduces ambiguity into every experiment. The paper should provide a full mapping table and per-dataset counts.

### Minor

1. **Single-run results without uncertainty quantification.** All mAP numbers in Tables 2–5 are reported as point estimates with no standard deviations, confidence intervals, or indication of replication. While single-run evaluation is common practice in 3D detection benchmarks and the largest claims (e.g., synthetic-to-real is the hardest gap) are supported by large performance gaps unlikely to be noise, the smaller differences between UDA methods (e.g., ~1–2 mAP differences in some rows of Table 3) cannot be assessed for significance. At minimum, the paper should acknowledge this as a limitation.

2. **No limitations section.** The paper does not discuss limitations such as: the 15-category space may miss realistic scenarios with more categories; only VoteNet results are shown in the main text (transformer detectors are deferred to supplementary); or that the synthetic datasets, while large, may have systematic biases (e.g., furniture styles, object placement patterns) not representative of real-world diversity. Adding a brief limitations paragraph would strengthen scholarly tone.

3. **Size prior baseline lacks sensitivity analysis.** The "Size prior" baseline (Section 4.3.1) improves performance by using target-domain mean object sizes, but the paper does not analyze how sensitive this improvement is to the accuracy of the size estimates (e.g., if estimated from a small labeled subset of target data). This would be a straightforward and informative ablation.

### Trivial
None.

## Nice-to-Haves

- **Release datasets and code.** The paper does not mention any plan for releasing SimRoom/SimHouse or the implementation of the UDA baselines. A clear statement about public release would substantially increase the benchmark's practical value.
- **Include a simple statistical adaptation baseline.** Methods like CORAL (feature covariance alignment) or MMD minimization are standard in domain adaptation but not evaluated. Including at least one simple alignment baseline would contextualize the gains from the more complex UDA methods.
- **Acknowledge the conservatism in data-scale control.** Table 5 controls for scene count but not objects-per-scene or point density. Since SimRoom has an order of magnitude more objects per scene, the synthetic gap is *even larger* than reported—a nuance worth discussing that would further strengthen the paper's central claim.
- **Document per-dataset object counts** for the 15 merged categories to resolve the ambiguity in label merging and enable consistent use by future work.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Table garbling/layout issues"** — These are parser artifacts from PDF extraction, not errors in the original submission.
- **"Single-room to multi-room is synthetic→synthetic, weakening generalization claims"** — The paper explicitly acknowledges this scope (Section 3.3.3: "To control other domain gap factors, we focus on SimRoom→SimHouse adaptation"), and the scenario is clearly scoped as isolating layout configuration. This is not a weakness; it is a controlled experimental design.
- **"No comparison to simple statistical baseline (CORAL/MMD)"** — Moved to Nice-to-Haves since more complex UDA methods are already provided and the paper covers representative approaches from classification/segmentation/LiDAR settings.
- **"Data scale control does not control for objects per scene"** — Moved to Nice-to-Haves since the reviewer acknowledges this makes the result *conservative* (strengthening the paper's claim).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an interpretation of the results that goes beyond what the paper already provides.

## Suggestions

1. **Document the UDA method adaptations in detail.** For each of VSS, PPFA, RV, and OHDA, describe: what architectural changes were made to adapt them from classification/segmentation to indoor 3D object detection with VoteNet; any loss function modifications; and key hyperparameter choices. A short appendix section would suffice.
2. **Provide the full label mapping table and per-dataset object counts.** Include a table mapping original category names → merged 15 categories for each dataset, along with object counts per dataset for the final categories.
3. **Run at least the main experiments (Table 2, key rows of Table 3) with 3 random seeds and report mean ± std.** For a benchmark paper intended as a foundation, this would greatly increase reliability.
4. **Add a brief limitations section** to the paper discussing the scope of the 15-category space, potential synthetic-data biases, and the current focus on VoteNet in the main text.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>