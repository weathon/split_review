## Summary
# Final Review Report

## Summary

This paper proposes Co-MOT, an end-to-end Transformer-based Multi-Object Tracking (MOT) method that addresses the "tracking terminal" problem and positive sample scarcity in existing e2e-MOT frameworks. The authors identify that the strict separation of tracking and detection queries in Tracking Aware Label Assignment (TALA) leads to feature starvation for detection queries and premature track loss. To mitigate this, Co-MOT introduces two key innovations: (1) Coopetition Label Assignment (COLA), which allows detection queries to match tracked objects in intermediate decoders to enrich feature representation via self-attention, and (2) a Shadow Set mechanism, a one-to-set matching strategy that augments each query with multiple shadow counterparts to enhance discriminative learning through hard-mining optimization. Extensive experiments on DanceTrack, BDD100K, and MOT17 demonstrate that Co-MOT achieves superior end-to-end performance (e.g., 69.4% HOTA on DanceTrack) while maintaining high efficiency (38% FLOPs of MOTRv2). The paper provides a compelling motivation, clear ablation studies, and a practical, deployment-friendly solution for e2e-MOT.

## Strengths
1. **Compelling Motivation and Problem Identification:** The paper correctly identifies a critical bottleneck in e2e-MOT: the strict separation of tracking and detection queries in TALA leads to feature starvation and premature tracking termination. The empirical analysis in Table 1 and Figure 1 effectively demonstrates that removing tracking queries significantly improves detection mAP, validating the hypothesis that joint inference interferes with detection capability.

2. **Innovative and Efficient Method Design:** The proposed COLA strategy is conceptually elegant, leveraging intermediate decoders for feature augmentation while maintaining competitive assignment in the final decoder to avoid redundancy. The Shadow Set mechanism provides a computationally lightweight alternative to one-to-many auxiliary branches, enhancing generalization through intra-set hard-mining without significant FLOPs overhead.

3. **Strong Empirical Performance and Efficiency:** Co-MOT achieves state-of-the-art end-to-end performance on DanceTrack (69.4% HOTA) and competitive results on BDD100K and MOT17. The efficiency comparison (Figure 4) convincingly shows that Co-MOT matches MOTRv2's performance while requiring only 38% of its FLOPs, highlighting its practical value for deployment.

4. **Comprehensive Ablation Studies:** The ablation experiments (Table 3) systematically validate the contributions of COLA and Shadow sets, including sensitivity analyses on initialization strategies, shadow count ($N_S$), and representative sampling strategies. The attention weight analysis (Figure 3) provides valuable mechanistic insights into how detection queries contribute to tracking queries.

## Weaknesses
1. **Insufficient Mechanistic Explanation for Shadow Set Optimization:** While the paper introduces the Shadow Set concept and reports its effectiveness, the theoretical justification for why optimizing the "most challenging query in the set with the maximal cost" enhances generalization is underdeveloped. The connection between intra-set hard-mining and improved discriminative feature learning needs clearer articulation to distinguish it from standard one-to-many auxiliary training.

2. **Computational Complexity of Expanded Query Count:** The architecture expands the total query count by a factor of $N_S$ (shadow set size). Although $N_S$ is kept small (e.g., 3), the self-attention complexity scales quadratically with sequence length. The paper claims "no extra costs" but does not explicitly analyze the computational overhead introduced by the expanded query sequence in the decoder layers, which may concern reviewers focused on strict efficiency bounds.

3. **Overstated Efficiency Comparison with Hybrid Baselines:** The claim that Co-MOT requires "38% FLOPs of MOTRv2" compares a pure end-to-end model against a hybrid model (MOTRv2 + YOLOX). While this highlights deployment advantages, it risks being perceived as an unfair architectural comparison if not carefully contextualized. The FLOPs calculation should explicitly account for the detector overhead in MOTRv2 to ensure scientific rigor.

4. **Limited Generalization Evidence on Smaller Datasets:** The performance gain on MOT17 is modest compared to DanceTrack, and the authors attribute this to the "data-hungry nature" of Transformers. However, the paper lacks analysis on whether COLA or Shadow sets introduce any negative interference in data-scarce regimes. A more detailed failure case analysis or sensitivity study on smaller datasets would strengthen the robustness claims.

## Key Issues
1. **Causal Attribution of Detection Deterioration:** The motivation section asserts that detection deteriorates "due to the nearby tracked objects," which is imprecise. The deterioration is actually caused by the TALA suppression mechanism and the resulting feature starvation for detection queries, not merely spatial proximity. Clarifying this causal link is essential for grounding the COLA proposal.

2. **Mechanistic Justification for Shadow Set Strategies:** The training strategy selects a representative query based on cost aggregation (e.g., Max), while inference selects the shadow with the highest confidence score. The paper describes *what* is done but lacks a clear explanation of *why* this combination works. Explicitly framing the Max-cost training as intra-set hard-example mining and the Max-score inference as confidence-based ensemble selection would significantly strengthen the theoretical foundation.

3. **Computational Overhead of Expanded Queries:** The architecture expands the query count to $(N_T + N_D) \times N_S$. Without explicitly addressing the quadratic scaling of self-attention with sequence length, the "no extra cost" claim is vulnerable to scrutiny. The manuscript should quantify the marginal FLOPs increase from shadow sets and confirm that $N_S$ remains small enough to preserve efficiency.

4. **Fairness of Efficiency Comparison:** Comparing Co-MOT's FLOPs directly to MOTRv2 (which includes a YOLOX detector) may be misleading if not properly contextualized. The efficiency claim should explicitly note that MOTRv2's FLOPs include detector overhead, ensuring a fair architectural comparison.

## Actionable Suggestions
1. **Clarify Causal Mechanism in Motivation:** Revise the motivation paragraph to explicitly state that TALA's strict separation starves detection queries of positive supervision, leading to poor detection of reappearing objects. Replace "detection will deteriorate due to the nearby tracked objects" with a precise explanation of feature starvation and suppression mechanisms.

2. **Strengthen Shadow Set Theoretical Grounding:** In Section 3.5, explicitly frame the Max-cost training strategy as intra-set hard-example mining and the Max-score inference strategy as confidence-based ensemble selection. This will clarify why optimizing the hardest shadow enhances discriminative feature learning and generalization.

3. **Address Computational Complexity:** Add a brief analysis in Section 3.3 quantifying the marginal FLOPs increase from expanding queries by $N_S$. Confirm that $N_S$ is kept small (e.g., 3) and that the linear projection overhead remains negligible compared to the backbone, validating the "no extra cost" claim.

4. **Contextualize Efficiency Comparison:** In the abstract and Section 4.5, clarify that the 38% FLOPs comparison accounts for MOTRv2's YOLOX detector overhead. Use phrasing such as "Co-MOT matches MOTRv2's performance while requiring only 38% of its total FLOPs (including detector overhead), highlighting its deployment-friendly efficiency."

5. **Expand Limitations Discussion:** Add method-specific failure modes to Section 4.6, such as potential noise introduction from detection queries in COLA (mitigated by the final competitive decoder) and sensitivity of shadow sets to initialization and $N_S$ size. This will improve scientific rigor and guide future work.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Existing end-to-end Multi-Object Tracking (e2e-MOT) methods often lag behind tracking-by-detection pipelines due to label assignment strategies that strictly separate tracking and detection queries.
- **S2 (Significance/Challenge):** This separation leads to scarce positive samples for detection queries and premature tracking termination, particularly in scenes with few new objects or heavy occlusions.
- **S3 (Prior Gap):** Current remedies, such as bootstrapping with pre-trained detectors (e.g., MOTRv2), introduce significant computational overhead, hindering efficient deployment.
- **S4 (Proposed Method):** We propose Co-MOT, which introduces a coopetition label assignment (COLA) allowing detection queries to match tracked objects in intermediate decoders, alongside a novel shadow set concept that augments queries for robust optimization via hard-mining.
- **S5 (Key Result & Implication):** Co-MOT achieves superior end-to-end performance (69.4% HOTA on DanceTrack) while requiring only 38% of MOTRv2's FLOPs, demonstrating a deployment-friendly path for efficient e2e-MOT.

### Introduction Outline (Complete)
- **P1 (Big Picture):** Introduce MOT and the shift from tracking-by-detection to e2e-MOT via Transformers, highlighting the advantage of global optimization.
- **P2 (Concrete Gap):** Explain TALA's strict separation of tracking/detection queries, leading to feature starvation for detection queries and "tracking terminal" failures. Cite MOTRv2's hybrid workaround and its deployment costs.
- **P3 (Proposed Idea):** Present the core intuition: detection queries can be conducive to tracking queries through shared feature learning. Introduce COLA for intermediate decoders and Shadow Sets for robust optimization.
- **P4 (Evidence Preview):** Briefly preview empirical results: significant HOTA gains on DanceTrack/BDD100K, ablation validation of COLA/Shadow contributions, and efficiency advantages over hybrid baselines.
- **P5 (Contribution Summary):** List threefold contributions: (i) COLA for cooperative feature learning, (ii) Shadow Set one-to-set matching for discriminative training, (iii) State-of-the-art e2e performance with high deployment efficiency.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Clarify causal mechanism in Motivation (Section 3.1): Replace "deteriorate due to nearby tracked objects" with precise explanation of TALA suppression and feature starvation. | Strengthens theoretical grounding and justifies COLA proposal. | Low |
| **P0** | Strengthen Shadow Set justification (Section 3.5): Explicitly frame Max-cost training as intra-set hard-mining and Max-score inference as ensemble selection. | Improves methodological rigor and distinguishes from one-to-many baselines. | Low |
| **P1** | Address computational complexity (Section 3.3): Quantify marginal FLOPs from expanded query count $(N_T + N_D) \times N_S$ and confirm $N_S$ remains small. | Validates "no extra cost" claim against efficiency-focused reviewers. | Low |
| **P1** | Contextualize efficiency comparison (Abstract/Section 4.5): Clarify that 38% FLOPs comparison accounts for MOTRv2's YOLOX detector overhead. | Ensures fair architectural comparison and prevents misinterpretation. | Low |
| **P2** | Expand Limitations (Section 4.6): Add method-specific failure modes (COLA noise risk, shadow sensitivity to $N_S$). | Improves scientific honesty and guides future work. | Medium |
| **P2** | Fix grammatical errors: Correct "address the hungry for positive samples" to "address the scarcity of positive samples" in Intro and Contributions. | Enhances professionalism and readability. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Validate COLA/Shadow impact | DanceTrack val, MOTR baseline | HOTA, DetA, AssA | COLA +3.8% HOTA, Shadow +2.6% HOTA | C1, C2 | Single backbone tested |
| E2 | Compare SOTA e2e methods | DanceTrack test, BDD100K val, MOT17 test | HOTA, TETA | Co-MOT 69.4% HOTA (DanceTrack) | C3 | MOT17 gain modest |
| E3 | Efficiency analysis | DanceTrack test, FLOPs/FPS | HOTA vs FLOPs | 38% FLOPs of MOTRv2, 1.4x faster | C3 | Hybrid vs pure comparison |
| E4 | Shadow hyperparameter sensitivity | DanceTrack val, 5 epochs | HOTA, DetA, AssA | $N_S=3$ optimal, Max/Min strategy best | C2 | Limited epoch sweep |
| E5 | Attention weight analysis | DanceTrack val, decoder layers | Attention % | D2T > T2T in later layers | C1 | Qualitative visualization |

### Research-Theme Gap Diagnosis
The core claim of "coopetition enhancing tracking via feature enrichment" is well-supported by ablation (E1) and attention analysis (E5). However, the robustness of COLA in data-scarce regimes (MOT17) and the computational overhead of expanded queries remain partially unaddressed. Additionally, variance reporting (multi-seed) is missing, which limits statistical confidence in small-margin gains.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| C1 (COLA robustness) | COLA improves tracking without degrading detection in low-data regimes. | Train on MOT17 subset (50% data), evaluate full MOT17. | MOTR, MeMOTR | HOTA, DetA, AssA | HOTA gain >1%, DetA drop <0.5% | Low | Validates data efficiency |
| C2 (Shadow overhead) | Expanded queries add negligible FLOPs when $N_S \le 3$. | Profile FLOPs/latency for $N_S \in \{1, 2, 3, 4\}$. | Baseline MOTR | FLOPs, FPS | $N_S=3$ overhead <5% | Low | Quantifies efficiency bound |
| C3 (Statistical reliability) | Gains are stable across random seeds. | 3-seed evaluation on DanceTrack val. | Co-MOT (single seed) | Mean±Std HOTA | Std <0.5% | Medium | Strengthens result credibility |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 7/10

**Rationale:** The paper presents a compelling and efficient solution to a well-identified bottleneck in e2e-MOT (tracking terminal problem and positive sample scarcity). The proposed COLA and Shadow Set mechanisms are conceptually elegant, empirically validated, and deployment-friendly. The strong performance on DanceTrack and BDD100K, combined with significant FLOPs reduction compared to hybrid baselines, demonstrates high practical value. However, the score is moderated by the need for clearer mechanistic justification (especially for shadow set optimization), explicit computational complexity analysis for expanded queries, and more rigorous contextualization of efficiency comparisons. With targeted revisions to strengthen theoretical grounding and clarify claims, the paper has strong potential for acceptance.

**Post-Revision Target:** [8, 9]/10

**Page Coverage Audit:**
| Page | Annotation Count | Coverage Status | Skip Reason (if skipped) |
|---|---|---|---|
| 1 | 3 | Covered | Abstract, Intro P2, Intro P3 annotated |
| 2 | 2 | Covered | Intro P4, Contributions annotated |
| 3 | 1 | Covered | Motivation annotated |
| 4 | 1 | Covered | Architecture annotated |
| 5 | 1 | Covered | Shadow Training/Inference annotated |
| 6 | 0 | Skipped | Standard Datasets/Metrics description |
| 7 | 0 | Skipped | Implementation details & SOTA comparison (standard reporting) |
| 8 | 1 | Covered | Ablation Study annotated |
| 9 | 1 | Covered | Limitations annotated |
| 10-12 | 0 | Skipped | References (non-substantive) |