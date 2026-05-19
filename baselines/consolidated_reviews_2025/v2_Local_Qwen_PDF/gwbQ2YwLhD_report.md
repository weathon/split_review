## Summary
This paper investigates the impact of variable measurement scale on score-based Directed Acyclic Graph (DAG) structure learning algorithms. The authors theoretically prove that common loss functions, including Model Mean Squared Error (MMSE), Bayesian Information Criterion (BIC), and Evidence Lower Bound (ELBO), are inherently sensitive to variable scales under Gaussian noise assumptions. They provide exact conditions under which these losses are minimized for incorrect DAG structures (e.g., reversed chains, forks, colliders) in d-dimensional cases. Empirically, the paper demonstrates that popular structure learners like NOTEARS, DAG-GNN, and GraN-DAG are severely impaired by scale differences, even when only a subset of variables is scaled. The authors propose a Scale Robust Loss (SRL) that excludes free variance terms, showing improved robustness for discrete learners like GES. The work highlights a critical, often overlooked confounder in causal structure learning and provides both theoretical insights and practical mitigation strategies.

## Strengths
1. **Theoretical Rigor and Generalization:** The paper provides clear, mathematically sound propositions (Prop. 1-10) that generalize prior low-dimensional, linear results to d-dimensional and non-linear cases. The decomposition of MMSE into variance and MSE terms (Prop. 1) offers a transparent mechanism for understanding scale-induced biases.
2. **Comprehensive Empirical Validation:** The experimental evaluation is extensive, covering multiple structure learners (NT, GES, DAG-GNN, GraN-DAG), both linear and non-linear dependencies, and various graph structures (chains, forks, colliders). The inclusion of real-world data (Sachs dataset) strengthens the practical relevance of the findings.
3. **Constructive Mitigation Strategy:** The proposal of Scale Robust Loss (SRL) is a practical and theoretically grounded solution for discrete learners. The paper clearly demonstrates how excluding free variance terms improves robustness, providing actionable guidance for practitioners.
4. **Clear Problem Formulation:** The medical example effectively illustrates the high stakes of incorrect structure recovery, making the motivation accessible and compelling to a broad audience.

## Weaknesses
1. **Overly Strong Assumption on Variance Source (Sec 3.1):** The paper assumes that variance differences *only* depend on the unit of measurement. In reality, variance differences also arise from inherent process properties (e.g., different noise levels, functional gains). This conflation limits the generalizability of the theoretical results and requires clarification.
2. **Ambiguity in Table 1 Reporting:** Table 1's percentages are ambiguous. It is unclear whether they represent the frequency of predicting the ground truth or the frequency of predicting the *scale-induced wrong structure*. This ambiguity reduces the empirical impact and requires explicit clarification in the caption.
3. **Limited Applicability of SRL to Continuous Learners:** While SRL is proposed as a mitigation strategy, it is explicitly noted to be applicable only to discrete learners. The paper defers extending SRL to continuous learners (like NT) to future work, which limits the immediate practical impact of the proposed solution for the most popular modern methods.
4. **Sensitivity vs. Correctness in Real-World Experiments (Q4):** The protocol used on the Sachs dataset demonstrates structural *instability* under scaling but does not prove that the original predictions were *incorrect*. Without ground truth validation, the results show sensitivity rather than incorrectness, a distinction that needs to be explicitly stated.

## Key Issues
1. **Variance Source Conflation (Critical):** The assumption that variance differences stem *only* from measurement units (Sec 3.1) is scientifically inaccurate. Variance is also determined by the underlying data generating process. This conflation risks invalidating the theoretical claims when applied to real-world data where process-induced variance differences are common.
2. **Table 1 Interpretability (Major):** The ambiguity in Table 1 regarding what the percentages represent (ground truth recovery vs. scale-induced error frequency) prevents readers from accurately assessing the severity of the scale sensitivity. This must be clarified to maintain empirical credibility.
3. **SRL Applicability Gap (Major):** The proposed mitigation (SRL) is limited to discrete learners. Without a practical extension for continuous learners (e.g., via thresholding heuristics), the solution's impact is significantly reduced for the most widely used modern methods like NOTEARS.
4. **Real-World Validation Limitation (Minor):** The Sachs dataset experiment demonstrates structural instability but not incorrectness. Failing to distinguish between sensitivity and correctness may lead to overinterpretation of the real-world results.

## Actionable Suggestions
1. **Clarify Variance Assumptions (Sec 3.1):** Revise the assumption to acknowledge that variance differences can stem from both measurement units and inherent process properties. Frame the theoretical analysis as studying the impact of *relative variance differences*, regardless of their source.
2. **Explicitly Interpret Proposition 1 (Sec 3.2.1):** Add a sentence after Equation (1) that explicitly states the implication: "This decomposition reveals that MMSE inherently penalizes graphs with high-variance root nodes, creating a structural bias independent of the true dependencies."
3. **Extend SRL to Continuous Learners (Sec 3.3):** Propose a simple thresholding heuristic for continuous learners: apply a sparsity threshold to the adjacency matrix W to identify effective root nodes, then compute SRL using this approximate root set. This makes SRL immediately applicable to methods like NOTEARS.
4. **Clarify Table 1 Caption (Sec 4):** Explicitly state that the percentages represent the frequency with which the *scale-induced wrong structure* was predicted instead of the ground truth. Consider adding SHD metrics to quantify error magnitude.
5. **Distinguish Sensitivity from Correctness (Sec 4, Q4):** Add a sentence in the Real World Data section explicitly stating that the protocol demonstrates structural instability under scaling, and that ground truth validation would require additional biological knowledge or independent datasets.
6. **Strengthen Conclusion Takeaway (Sec 5):** Add a final sentence recommending that practitioners always standardize their data and consider scale-robust scoring strategies as a best practice in structure learning pipelines.

## Storyline Options + Writing Outlines
**Abstract Outline:**
- S1 (Problem): Structure learning aims to recover DAGs representing underlying probability distributions, but wrong identifications have significant implications in fields like medicine.
- S2 (Challenge): Many prominent DAG learners rely on least square or log-likelihood losses, which are heavily influenced by variable scales.
- S3 (Gap): Prior work has demonstrated scale sensitivity only in low-dimensional, linear systems, leaving d-dimensional and non-linear cases unexplored.
- S4 (Method): We provide exact conditions under which square-based and log-likelihood losses are minimal for wrong DAGs in d-dimensional cases and propose a Scale Robust Loss (SRL) to mitigate this bias.
- S5 (Result): Extensive experiments on synthetic and real-world data confirm that scale severely impairs structure learners, and SRL improves robustness for discrete methods.

**Introduction Outline:**
- P1 (Big Picture & Gap): Introduce DAG structure learning and the rise of score-based methods (NOTEARS). Highlight that these methods optimize MMSE/log-likelihood, which are inherently scale-sensitive.
- P2 (Prior Work & Limitations): Discuss Loh & Bühlmann (2014) and Reisach et al. (2021), noting their focus on low-dimensional, linear cases. Emphasize the lack of understanding for d-dimensional and non-linear scenarios.
- P3 (Practical Stakes): Present the Medical Example (Fig. 1) to illustrate how scale-induced structural errors can flip critical decisions (e.g., treatment assignments).
- P4 (Contributions): Clearly list the three contributions: (1) generalization to d-dimensional/non-linear cases, (2) exact failure conditions for MMSE, and (3) susceptibility of log-likelihood losses (BIC, ELBO) with empirical validation.

## Priority Revision Plan
**P0 (Critical - Validity & Clarity):**
- Revise Sec 3.1 assumption to acknowledge that variance differences stem from both measurement units and inherent process properties.
- Clarify Table 1 caption to explicitly state that percentages represent the frequency of scale-induced errors, not ground truth recovery.
- Add explicit interpretation of Proposition 1's decomposition to highlight the structural bias mechanism.

**P1 (Major - Impact & Applicability):**
- Propose a thresholding heuristic in Sec 3.3 to extend SRL applicability to continuous learners (e.g., NOTEARS).
- Distinguish between structural sensitivity and correctness in the Real World Data (Q4) section, adding a limitation statement about ground truth validation.
- Move the Medical Example in the Introduction to precede the contribution list for stronger narrative flow.

**P2 (Minor - Polish & Takeaway):**
- Strengthen the Conclusion with a practical recommendation for practitioners to standardize data and consider scale-robust scoring.
- Improve Section 2.2 by explicitly linking each learner's loss function to the scale sensitivity theme.
- Ensure consistent terminology and smooth transitions between theoretical propositions and empirical validations.

## Experiment Inventory & Research Experiment Plan
**Completed Experiment Inventory:**
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| Q1 | Confirm theoretical scale sensitivity | 3/10-node chains/forks/colliders, linear/non-linear, scaled data | Prediction frequency | NT/DG/GND predict wrong structures 100% of time | C1, C2 | Table 1 ambiguity |
| Q2 | Severity of subset scaling | Scale single variable with ≥2 neighbors | Prediction frequency | Single variable scaling provokes severe effects | C2 | Limited to synthetic data |
| Q3 | Ablation of (A1) Immiscible Structures | 20 random 10-node DAGs, substructure scaling | Prediction frequency | Scale affects substructures even in complex graphs | C1 | GES robustness unexplained |
| Q4 | Real-world scale sensitivity | Sachs dataset, scale perturbation protocol | SHD, substructure match | Scale changes predictions in 100% of simulations | C3 | Demonstrates sensitivity, not correctness |

**Research-Theme Gap Diagnosis:**
The current experiments strongly support the theoretical claims but lack validation of the proposed mitigation (SRL) on continuous learners. Additionally, the real-world experiment demonstrates instability but not correctness, leaving a gap in practical impact validation.

**Proposed Research Experiments:**
1. **SRL Extension Validation (P0):** Apply the proposed thresholding heuristic to NOTEARS and GraN-DAG. Compare SHD and structural accuracy against standard baselines under varying scale conditions. *Expected Gain:* Demonstrates immediate practical utility of SRL for continuous learners.
2. **Ground Truth Validation (P1):** Use a dataset with known biological ground truth (e.g., yeast signaling pathways) to validate whether scale-induced changes actually move predictions away from the true structure. *Expected Gain:* Confirms that sensitivity translates to incorrectness in real-world scenarios.
3. **Hyperparameter Sensitivity (P2):** Investigate how regularization parameters (λ in NT) interact with scale sensitivity. *Expected Gain:* Provides practical guidance on tuning structure learners to mitigate scale biases.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper addresses a critical and often overlooked issue in causal structure learning: the sensitivity of score-based methods to variable scales. The theoretical analysis is rigorous, providing clear conditions under which common losses (MMSE, BIC, ELBO) fail. The empirical validation is extensive and well-designed. However, the score is moderated by the overly strong assumption regarding variance sources (Sec 3.1), the ambiguity in Table 1 reporting, and the limited immediate applicability of the proposed SRL mitigation to continuous learners. With the suggested clarifications and extensions, the paper's impact and validity would be significantly strengthened.

**Post-Revision Target:** [7.5, 8.5]/10

**Expected Gains from Revision:**
- Clarifying the variance assumption and Table 1 will resolve validity and interpretability concerns, boosting confidence in the theoretical and empirical claims.
- Extending SRL to continuous learners via thresholding heuristics will substantially increase the practical impact and applicability of the proposed solution.
- Strengthening the narrative flow and practical takeaways will improve readability and ensure the findings are actionable for practitioners.