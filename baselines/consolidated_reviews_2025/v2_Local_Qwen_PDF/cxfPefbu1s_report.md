## Summary
# Final Review Report

## Summary
This paper addresses "disguised procedural unfairness," a phenomenon where standard causal fairness constraints inadvertently alter neutral data generating components while mitigating discrimination. Inspired by Rawlsian pure procedural justice, the authors propose a framework that decouples objectionable causal edges from neutral ones using reference points and a value instantiation rule. The reference points are optimized to maximize outcomes for the least advantaged individuals. Experiments on simulated linear models and the UCI Adult dataset demonstrate that the proposed approach preserves neutral causal mechanisms while improving approval rates for disadvantaged groups compared to path-specific counterfactual baselines. The work offers a theoretically grounded alternative to outcome-focused fairness constraints, emphasizing process integrity over statistical parity.

## Strengths
1. **Theoretically Grounded Motivation:** The paper successfully bridges political philosophy (Rawlsian pure procedural justice) and algorithmic fairness, providing a principled foundation for prioritizing process integrity over outcome statistics.
2. **Novel Decoupling Mechanism:** The value instantiation rule with reference points offers a clean, retraining-free method to isolate objectionable causal edges without distorting neutral components, addressing a genuine gap in causal fairness literature.
3. **Rigorous Illustrative Example:** The linear model analysis effectively demonstrates how standard path-specific constraints inevitably introduce arbitrary deviations in neutral coefficients, making the problem of disguised procedural unfairness concrete and verifiable.
4. **Equity-Focused Optimization:** Configuring reference points to maximize outcomes for the least advantaged individuals aligns the framework with substantive equity goals, moving beyond mere statistical parity.

## Weaknesses
1. **Unclear Problem Framing & Narrative Flow:** The abstract and introduction lack a concrete "Big Picture -> Gap -> Solution" arc. The introduction reads as a citation-heavy catalog without explicitly explaining why outcome-focused constraints mechanistically distort neutral components. The transition to "disguised procedural unfairness" feels abrupt.
2. **Blurred Distinction Between Outcome and Procedural Fairness:** Section 2.2 maps Rawlsian principles to algorithmic fairness but conflates group-level outcome metrics (e.g., Equal Opportunity) with procedural mandates. The text does not clearly articulate why optimizing outcome statistics inherently violates procedural integrity, weakening the theoretical foundation.
3. **Implicit Mechanism of Disguised Unfairness:** The linear example in Section 3 demonstrates coefficient distortion but lacks explicit mathematical intuition explaining how constraining composite PSE terms forces arbitrary adjustments in neutral coefficients. The non-identifiability under constraints is not explicitly stated as the root cause.
4. **Insufficient Experimental Validation & Reporting:** Section 5.2 presents approval rate improvements but lacks statistical significance testing, variance reporting, or quantification of exact deltas. The conclusion is brief and omits discussion of accuracy-fairness trade-offs or concrete future work.
5. **Algorithmic Clarity & Scope Boundaries:** Algorithms 1 and 2 lack high-level plain-language summaries before pseudocode. The propagation mechanism for reference points is dense. Additionally, computational complexity and explicit scope boundaries (e.g., static DAG assumption) are not clearly stated.

## Key Issues
1. **Mechanistic Gap in Disguised Unfairness Explanation (Page 4 - Sec 3):** The paper demonstrates that PSE constraints distort neutral coefficients but does not explicitly explain the mathematical mechanism (non-identifiability under composite constraints). Without this, the motivation for the reference point framework lacks urgency.
2. **Conceptual Conflation of Fairness Types (Page 3 - Sec 2.2):** The text conflates group-level outcome metrics with procedural mandates. The distinction between optimizing outcome statistics (which may distort processes) and preserving procedural integrity is not clearly articulated, weakening the theoretical contribution.
3. **Insufficient Empirical Validation (Page 9 - Sec 5.2):** Experimental results lack statistical significance testing, variance reporting, and exact quantitative deltas. The claim of "boosts in approval rates" remains qualitative, and accuracy-fairness trade-offs are unaddressed.
4. **Algorithmic Opacity & Scope Ambiguity (Pages 6-7 - Algs 1-2):** The value instantiation rule and aggregation pipeline lack high-level intuition before pseudocode. Computational complexity and explicit scope boundaries (static DAG assumption) are not stated, raising scalability and applicability concerns.

## Actionable Suggestions
1. **Clarify Mechanism of Disguised Unfairness (Page 4):** Add a brief mathematical intuition explaining that constraining composite PSE terms without isolating objectionable edges forces the optimizer to adjust multiple coefficients simultaneously. Explicitly state that non-identifiability under constraints is the root cause of neutral coefficient distortion.
2. **Sharpen Theoretical Distinction (Page 3):** Explicitly distinguish outcome fairness (statistical parity) from procedural fairness (preserving neutral causal mechanisms). Clarify that Requirement I prohibits arbitrary coefficient alterations, while Requirement II mandates optimizing reference points for the least advantaged.
3. **Strengthen Experimental Reporting (Page 9):** Report mean ± std approval rates over multiple seeds. Quantify exact percentage point improvements for disadvantaged groups. Add a brief discussion on accuracy-fairness trade-offs to contextualize practical applicability.
4. **Improve Algorithmic Readability (Pages 6-7):** Add plain-language summaries before Algorithms 1 and 2 explaining the three instantiation cases and the sequential aggregation pipeline. Include a complexity analysis (e.g., O(V+E) for topological sort) and explicitly bound the scope to static DAGs.
5. **Restructure Abstract & Introduction (Page 1):** Adopt a compact 4-5 sentence arc: Problem -> Gap -> Method -> Result -> Implication. Remove citations from the abstract. Condense the introduction's citation list into thematic categories and explicitly link sociological examples to causal graph edges.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem/Domain):** Algorithmic fairness methods often inadvertently alter neutral aspects of the data generating process while mitigating discrimination, leading to disguised procedural unfairness.
- **S2 (Prior Gap):** Standard causal fairness constraints focus on bounding outcome disparities but lack mechanisms to preserve the integrity of neutral causal relationships during mitigation.
- **S3 (Proposed Method):** We propose a framework that decouples objectionable data generating components from neutral ones using reference points and a value instantiation rule, inspired by pure procedural justice.
- **S4 (Key Result):** Experiments on simulated and real-world datasets demonstrate that our approach preserves neutral causal mechanisms while significantly improving approval rates for disadvantaged groups compared to path-specific counterfactual baselines.
- **S5 (Bounded Implication):** These findings highlight the necessity of process-focused fairness interventions that avoid arbitrary distortions of legitimate data generating pathways.

### Introduction Outline (Complete)
- **P1 (Big Picture & Gap):** Algorithmic fairness literature has extensively explored outcome-based and causal fairness notions. However, these approaches primarily focus on bounding discrimination from protected features to final outcomes, often overlooking the procedural integrity of the underlying data generating process.
- **P2 (Mechanistic Problem):** By imposing constraints directly on causal effects or predictive rates, existing methods inevitably distort the coefficients of neutral components. This non-identifiability under constraints introduces arbitrary alterations to legitimate causal relationships, a phenomenon we term disguised procedural unfairness.
- **P3 (Formal Motivation):** We formalize procedural fairness through two Rawlsian mandates: (1) preserving neutral causal mechanisms without arbitrary distortion, and (2) arranging remaining inequalities to maximize outcomes for the least advantaged.
- **P4 (Proposed Solution):** To satisfy these requirements, we introduce a value instantiation rule that utilizes reference points to isolate and neutralize objectionable edges without retraining or altering model parameters.
- **P5 (Contributions & Evidence):** Our contributions include: (1) a formal characterization of disguised procedural unfairness, (2) a scalable reference point framework for edge-specific decoupling, and (3) empirical validation demonstrating improved equity for disadvantaged groups while maintaining process integrity.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Clarify mechanistic explanation of disguised procedural unfairness in Sec 3 (non-identifiability under PSE constraints). | Strengthens theoretical motivation and justifies the need for reference points. | Low |
| **P0** | Add statistical significance testing, variance reporting, and exact quantitative deltas to Sec 5.2. | Validates empirical claims and improves reproducibility. | Medium |
| **P1** | Restructure Abstract and Introduction to follow Problem -> Gap -> Solution -> Evidence arc. | Improves narrative flow and reader engagement. | Low |
| **P1** | Add plain-language summaries and complexity analysis to Algorithms 1 & 2. | Enhances algorithmic clarity and scalability assessment. | Low |
| **P2** | Explicitly distinguish outcome fairness from procedural fairness in Sec 2.2. | Sharpens theoretical contribution and reduces conceptual conflation. | Low |
| **P2** | Discuss accuracy-fairness trade-offs and expand conclusion with bounded limitations. | Improves practical applicability and scientific rigor. | Medium |

**Execution Strategy:** Begin with P0 items to solidify the core theoretical and empirical foundations. Proceed to P1 items to enhance readability and narrative coherence. Finally, address P2 items to refine theoretical boundaries and practical implications.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Demonstrate Requirement II violation in linear model | Simulated linear DAG, varying thresholds | Approval rates by group | Disadvantaged group disproportionately rejected | Yes | Lacks variance reporting |
| E2 | Evaluate framework on UCI Adult | Real-world dataset, causal graph from prior work | Approval rates (Y=0, Y=1) | Improved rates for females vs baselines | Yes | No statistical significance tests |
| E3 | Scalability analysis | Synthetic DAGs (1024 nodes, avg degree 102) | Parameters, MACs | Comparable to vanilla regressor | Yes | Inference-only, no training cost |

### Research-Theme Gap Diagnosis
The current experiments validate the framework on static, low-dimensional settings but lack robustness checks under distribution shift, multi-seed variance reporting, and accuracy-fairness trade-off analysis. The claim of procedural fairness preservation is theoretically sound but empirically thin.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Robustness to distribution shift | Reference points remain effective under covariate shift | Apply framework to shifted UCI Adult/Folktables splits | Unconstrained, PC-Fairness | Approval rate delta, accuracy drop | Stable gains across shifts | Low | Validates generalizability |
| Statistical reliability | Gains are consistent across random seeds | Run E2 over 5 seeds with different train/test splits | Same baselines | Mean ± std approval rates, p-values | p < 0.05 for improvements | Medium | Strengthens empirical validity |
| Accuracy-fairness trade-off | Decoupling preserves predictive performance | Evaluate AUC/F1 alongside approval rates | Same baselines | AUC, F1, approval rates | Minimal accuracy degradation | Low | Contextualizes practical utility |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10  
The paper presents a theoretically grounded and novel framework for addressing disguised procedural unfairness. The reference point mechanism is elegant and avoids retraining, offering a clear alternative to outcome-focused constraints. However, the score is moderated by implicit mechanistic explanations in Section 3, lack of statistical validation in experiments, and narrative clarity issues in the abstract/introduction. The conceptual contribution is strong, but empirical rigor and presentation need refinement.

**Post-Revision Target:** [7.5, 8.5]/10  
If the authors clarify the mathematical mechanism of coefficient distortion, add statistical significance testing and variance reporting, and restructure the narrative for better flow, the paper would significantly strengthen its empirical validity and readability. These revisions would make the work highly competitive for top-tier venues.