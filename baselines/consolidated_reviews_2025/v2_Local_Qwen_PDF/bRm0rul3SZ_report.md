## Summary
This paper proposes Pano-I2I, a novel framework for unpaired panoramic image-to-image translation that leverages readily available pinhole images as style targets. The authors address two core challenges: (1) the geometric distortion gap between panoramic sources and pinhole targets, and (2) the scarcity of multi-condition panoramic datasets. The method introduces a versatile encoder with fixed ERP-offset deformable convolutions, spherical positional embeddings (SPE), distortion-free discrimination, and sphere-based rotation augmentation with ensemble. Experiments on StreetLearn translated to INIT and Dark Zurich datasets demonstrate improvements in FID and SSIM over strong baselines (CUT, FSeSim, MGUIT, InstaFormer). While the problem formulation is practical and the technical components are well-motivated, the manuscript requires tighter claim scoping, clearer methodological intuition, and more rigorous experimental reporting to strengthen its scientific credibility.

## Strengths
1. **Practical Problem Formulation:** The paper addresses a highly relevant and under-explored task: translating panoramic images using style references from narrow-FoV pinhole datasets. This leverages abundant pinhole data to overcome the scarcity of multi-condition panoramic datasets, offering clear practical value for AR/VR and autonomous driving applications.
2. **Cohesive Technical Design:** The proposed components—fixed ERP-offset deformable convolutions, spherical positional embeddings, distortion-free discrimination, and rotation ensemble—are well-aligned with the core challenges of geometric mismatch and edge discontinuity. The two-stage training strategy provides a stable initialization path.
3. **Comprehensive Empirical Validation:** The method is evaluated on two standard datasets (StreetLearn to INIT and Dark Zurich) with strong baselines. The ablation study effectively demonstrates the individual contributions of key components, particularly the distortion-free discriminator and ensemble technique.

## Weaknesses
1. **Unscoped Novelty Claims:** The abstract and introduction claim to tackle panoramic I2I "for the first time" without precise scoping. This risks invalidation by adjacent works in panoramic generation or cross-format style transfer. The contribution statements lack concrete metric deltas, relying instead on vague assertions like "notably outperforms."
2. **Insufficient Methodological Intuition:** Key components (e.g., fixed ERP-offset deformable convolutions, distortion-free discrimination) are presented with dense formulas but lack clear intuitive explanations. The data flow and the rationale for why pinhole projection stabilizes the discriminator are under-explained, reducing reproducibility and readability.
3. **Experimental Reporting Gaps:** The comparison setup lacks explicit training budget parity details (epochs, hyperparameter tuning schedules). The use of pseudo bounding boxes for instance-aware baselines (MGUIT, InstaFormer) introduces an uncontrolled variable. The user study lacks protocol transparency (pairwise vs. ranking) and statistical significance testing.
4. **Narrative Structure & Flow:** The introduction mixes data scarcity motivation with empirical failure analysis, diluting the impact of both arguments. The related work reads as a chronological list rather than a categorized comparison, failing to explicitly position the paper against strongest baselines on decision-relevant axes.

## Key Issues
1. **Claim-Evidence Misalignment (Novelty):** The "first time" claim in the abstract and contributions is not bounded by task/setting qualifiers. Without precise scoping (e.g., "first unpaired panoramic-to-pinhole I2I framework"), reviewers may reject this as an overclaim. **Impact:** Threatens novelty credibility. **Fix:** Replace with scoped qualifiers and ground performance claims with concrete metric deltas.
2. **Reproducibility Risk (Method Intuition):** Equation (1) for ERP offsets and the distortion-free discrimination mechanism lack intuitive motivation and clear data flow explanations. **Impact:** Reduces implementability and reviewer confidence. **Fix:** Add intuition paragraphs before formulas, explicitly contrast fixed offsets with learned deformable convolutions, and clarify the discriminator's pinhole projection rationale.
3. **Fairness & Statistical Rigor (Experiments):** Baseline comparison lacks explicit training budget parity, and pseudo-annotations for MGUIT/InstaFormer are not validated for sensitivity. User study lacks statistical significance testing. **Impact:** Undermines quantitative claims and subjective quality validation. **Fix:** Report matched training budgets, add pseudo-annotation sensitivity check, and include p-values/confidence intervals for user study.

## Actionable Suggestions
1. **Scope Novelty Claims:** Replace "first time" with precise qualifiers (e.g., "first unpaired panoramic I2I framework leveraging pinhole style targets"). Ground performance claims in contributions with representative metric deltas (e.g., "improves SSIM by up to 40% over FSeSim").
2. **Enhance Method Intuition:** Add a data flow paragraph in Section 3.2 explaining the forward pass. Before Eq (1), explain why fixed ERP offsets are used instead of learned offsets. Clarify that distortion-free discrimination projects panoramas to pinhole views to force the discriminator to evaluate local style consistency rather than global geometric mismatch.
3. **Strengthen Experimental Rigor:** Explicitly report training budget parity (epochs, batch size, learning rate schedule) across all baselines. Add a sensitivity analysis showing that performance gaps persist even with high-confidence pseudo-annotations. Report statistical significance (p-values or bootstrap confidence intervals) for the user study results.
4. **Reorganize Related Work:** Restructure Section 2 into three categories: (1) Unpaired I2I Methods, (2) Transformer-based Generation, and (3) Panoramic Image Modeling. For each, summarize representative methods, state limitations regarding geometric distortion or FoV mismatch, and explicitly contrast with Pano-I2I.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Unpaired panoramic image-to-image translation (Pano-I2I) aims to modify 360-degree scenes using style references from non-panoramic domains.
- **S2 (Significance/Challenge):** This task is challenging due to severe geometric distortions in panoramas and the scarcity of multi-condition panoramic datasets.
- **S3 (Prior Gap):** Existing I2I methods fail in this setting because they assume geometric consistency between source and target, leading to structural collapse when bridging panoramic and pinhole domains.
- **S4 (Proposed Method):** To address this, we propose a novel framework that harnesses readily available pinhole images as style targets, featuring a versatile encoder with deformable convolutions, distortion-free discrimination, and spherical positional embeddings to preserve panoramic continuity.
- **S5 (Key Result & Bounded Implication):** Experiments on StreetLearn demonstrate that our method significantly improves structural similarity and style relevance over strong baselines, establishing a robust baseline for panoramic I2I.

### Introduction Outline (Complete)
- **P1 (Big Picture & Motivation):** Define I2I and its success in pinhole domains. Contrast with the rising demand for 360-degree content in AR/VR and autonomous driving, highlighting the narrow-FoV limitation of current I2I methods.
- **P2 (Problem Context & Value):** Introduce panoramic cameras and their benefits. State the potential of translating panoramas for immersive applications. Explicitly identify the research gap: existing I2I assumes geometric consistency, breaking when style references are only available in pinhole formats.
- **P3 (Failure Analysis of Naive Approaches):** Separate geometric/style entanglement failure from computational projection limitations. Explain why naive adaptations collapse structurally or incur prohibitive costs. Transition to the need for a dedicated framework.
- **P4 (Data Scarcity & Task Formalization):** Articulate the scarcity of multi-condition panoramic datasets. Motivate leveraging pinhole style targets as a practical alternative. Formalize the Pano-I2I task with clear source/target definitions.
- **P5 (Method Overview & Contributions):** Provide intuition on how deformable convolutions, SPE, and distortion-free discrimination jointly address geometric gaps and edge discontinuities. List scoped, evidence-linked contributions with concrete metric deltas.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Scope novelty claims: Replace "first time" with precise task/setting qualifiers. Ground contribution statements with concrete metric deltas. | Strengthens novelty credibility and defensibility against adjacent works. | Low |
| **P0** | Enhance method intuition: Add data flow paragraph in Sec 3.2. Explain fixed ERP offsets vs learned offsets. Clarify distortion-free discrimination rationale. | Improves reproducibility and reviewer confidence in technical soundness. | Medium |
| **P1** | Strengthen experimental rigor: Report training budget parity across baselines. Add pseudo-annotation sensitivity check. Include statistical significance for user study. | Validates quantitative claims and subjective quality assessments. | Medium |
| **P1** | Reorganize Related Work: Categorize by Unpaired I2I, Transformer Generation, Panoramic Modeling. Explicitly contrast with strongest baselines. | Clarifies paper positioning and highlights decision-relevant differences. | Low |
| **P2** | Refine Introduction Narrative: Separate data scarcity motivation from failure analysis. Add transition sentences between paragraphs. | Improves narrative flow and reader engagement. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Main translation performance | StreetLearn -> INIT/Dark Zurich; Baselines: CUT, FSeSim, MGUIT, InstaFormer | FID, SSIM | Pano-I2I outperforms baselines in all metrics | Style relevance & content preservation | Lacks variance reporting (multi-seed) |
| E2 | Qualitative visual assessment | Day->Night, Day->Rainy comparisons | Visual inspection | Baselines show structural collapse/pinhole artifacts | Geometric handling superiority | Subjective, no failure rate analysis |
| E3 | User study | 60 users, 10 images/task, pairwise ranking | Preference % | Pano-I2I preferred 53-68% of trials | Subjective quality advantage | Lacks statistical significance testing |
| E4 | Ablation study | Remove df-D, ensemble, two-stage, SPE/deform conv | FID, SSIM | All components contribute positively | Component necessity | Lacks interaction effect analysis |

### Research-Theme Gap Diagnosis
The core research-value claims (new knowledge in panoramic I2I, reproducibility of geometric-aware encoding, impact on practice via pinhole style leveraging) are supported but lack robustness evidence. Missing multi-seed variance, OOD generalization tests, and statistical validation weaken the confidence in the reported gains.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Robustness & Stability | Gains are consistent across random seeds | Train/evaluate with 3 different seeds | Same baselines | FID/SSIM mean±std | Std < 5% of mean | Low | Validates reliability |
| Statistical Significance | User preference is statistically significant | Bootstrap resampling on user study data | Null hypothesis | p-value | p < 0.01 | Low | Strengthens subjective claims |
| OOD Generalization | Method generalizes to unseen conditions | Test on a held-out weather/time split | Baselines | FID, SSIM | Relative drop < 10% | Medium | Bounds external validity |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
Final Score: 6/10
Post-Revision Target: [7, 8]/10

**Scoring Rationale:** The paper addresses a practical and under-explored task with a cohesive technical design and comprehensive empirical validation. The core strengths lie in the problem formulation and the alignment of method components with geometric challenges. However, the score is moderated by unscoped novelty claims, insufficient methodological intuition, and gaps in experimental rigor (training budget parity, statistical significance). Addressing the P0/P1 revision items would materially improve scientific credibility and defensibility, justifying the post-revision target.