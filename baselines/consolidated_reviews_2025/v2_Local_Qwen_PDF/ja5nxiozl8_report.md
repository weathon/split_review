## Summary
# Final Review Report

## Summary
This paper addresses a critical methodological gap in Machine Learning research: the lack of a rigorous, quantifiable framework for assessing the generalizability of experimental studies. While reproducibility and statistical significance have mature tooling, generalizability (external validity) remains largely qualitative. The authors propose a mathematical formalization of ML experimental studies as distributions over rankings and introduce a quantifiable notion of generalizability based on the Maximum Mean Discrepancy (MMD). Leveraging this framework, they develop an algorithm to estimate the minimum number of experiments ($n^*$) required to achieve a desired level of generalizability. The approach is validated through two case studies on recent benchmarks (categorical encoders and BIG-bench), revealing that many published studies are underpowered. The paper also releases an open-source Python module, GENEXPY, to facilitate generalizability analysis.

## Strengths
1. **High Practical Relevance:** The paper tackles a pressing issue in ML research—the reproducibility and generalizability crisis—by providing a concrete tool (GENEXPY) and methodology for researchers to pre-validate their study designs.
2. **Rigorous Mathematical Formalization:** The formalization of experimental studies as distributions over rankings is elegant and bridges the gap between statistical benchmarking and probability theory. The use of MMD to measure distributional similarity is well-motivated and theoretically sound.
3. **Clear Case Studies:** The application of the framework to two recent, large-scale benchmarks (Matteucci et al., Srivastava et al.) effectively demonstrates the method's utility. The finding that many studies are underpowered is a compelling empirical takeaway that underscores the need for the proposed framework.
4. **Goal-Aware Kernels:** The introduction of goal-specific kernels (Borda, Jaccard, Mallows) allows the framework to flexibly capture different research objectives, from identifying the best alternative to assessing full ranking consistency.

## Weaknesses
1. **Heuristic Nature of $n^*$ Estimation:** The algorithm for estimating the minimum sample size $n^*$ relies on a log-log linear relationship (Proposition 4.2) that is presented largely as an empirical observation. While a simplified proof is provided in the appendix, the main text could better clarify the theoretical guarantees versus the practical heuristic nature of this extrapolation.
2. **Lack of Mechanistic Insight in Case Studies:** The case studies correctly identify that variance in $n^*$ stems from different design factors (e.g., model type, metric). However, the analysis stops at observation and does not explain *why* certain configurations (e.g., SVM with balanced accuracy) require significantly more datasets than others. Adding mechanistic insights would greatly enhance the paper's practical value.
3. **Copy-Paste Errors in Case Study 2:** Section 5.2 contains noticeable copy-paste errors from the previous case study, such as referring to "encoders" instead of "LLMs" and referencing "Figure 2" instead of "Figure 3." These errors reduce the perceived rigor of the manuscript.
4. **Justification for Rankings in Appendix:** The critical design choice to model results as rankings is justified only in Appendix A.1. Moving this justification to the main text (Section 3.1) would strengthen the methodological narrative and improve flow.

## Key Issues
1. **Theoretical vs. Empirical Status of Log-Log Linearity:** The core algorithm for estimating $n^*$ depends on the assumption that $\log(n)$ scales linearly with $\log(\epsilon_n^{\alpha^*})$. The manuscript should explicitly state whether this is a rigorous theoretical guarantee derived from MMD concentration bounds or a practical heuristic. If heuristic, reporting the $R^2$ of the linear fit in the case studies would demonstrate its reliability.
2. **Missing Mechanistic Analysis in Case Studies:** The observation that certain design factors (e.g., SVMs with balanced accuracy) require more datasets to achieve generalizability is valuable but incomplete without explanation. Understanding the root causes (e.g., higher sensitivity to dataset distribution shifts) is crucial for guiding practitioners.
3. **Copy-Paste Errors in BIG-bench Analysis:** The presence of "encoders" instead of "LLMs" and incorrect figure references in Section 5.2 indicates a lack of careful proofreading. These errors must be corrected to maintain scientific rigor.
4. **Placement of Ranking Justification:** Justifying the use of rankings in the appendix weakens the main narrative. This critical design choice should be motivated in Section 3.1 to help readers bridge the gap between intuition and formalism.

## Actionable Suggestions
1. **Clarify $n^*$ Estimation Heuristic:** In Section 4.3, explicitly state that the log-log linear relationship serves as a practical interpolation/extrapolation heuristic derived from MMD concentration bounds. Recommend reporting the $R^2$ of this fit in the case studies to demonstrate its reliability.
2. **Add Mechanistic Discussion to Case Studies:** In Sections 5.1 and 5.2, add a short discussion paragraph hypothesizing why specific design factors increase the required sample size. For example, discuss whether more complex models or stricter metrics inherently exhibit higher variance across datasets.
3. **Correct Copy-Paste Errors:** In Section 5.2, replace "encoders" with "LLMs" in goal (g2) and update the figure reference from "Figure 2" to "Figure 3."
4. **Move Ranking Justification to Main Text:** Move the three points from Appendix A.1 to Section 3.1, immediately after introducing the experiment function $E$. This will strengthen the methodological argument and improve narrative flow.
5. **Tighten Abstract and Conclusion:** Restructure the abstract into a tight 5-sentence arc (Problem, Gap, Method, Algorithmic Insight, Empirical Payoff). In the conclusion, add a final sentence calling for a cultural shift in ML benchmarking toward generalizability-aware study designs.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem/Context):** Experimental studies are a cornerstone of ML research, yet results often fail to generalize across unseen datasets or conditions.
- **S2 (Gap):** Existing frameworks for measuring generalizability, largely borrowed from causal inference, lack the mathematical formalization needed to capture the complexity and specific goals of ML benchmarks.
- **S3 (Method):** To address this, we formalize experimental studies as distributions over rankings and introduce a quantifiable notion of generalizability based on the Maximum Mean Discancrepancy (MMD).
- **S4 (Algorithmic Insight):** Leveraging this framework, we develop an algorithm to estimate the minimum number of experiments required to achieve a desired level of generalizability.
- **S5 (Empirical Payoff):** Applying our method to two recent large-scale benchmarks, we reveal that many published studies are underpowered, often requiring significantly more datasets than currently evaluated to yield robust conclusions.

### Introduction Outline (Complete)
- **P1 (Big Picture):** Establish experimental studies as the foundation of ML progress and the community's push for higher methodological standards.
- **P2 (Gap - Internal vs External Validity):** Contrast established tools for reproducibility and significance (internal validity) with the under-addressed challenge of generalizability (external validity).
- **P3 (Motivation - Non-Generalizable Results):** Cite recent examples (Matteucci et al., Lu et al.) where significant findings fail to replicate, highlighting the practical stakes.
- **P4 (Solution - Formalization & Quantification):** Introduce the core idea: formalizing studies as distributions over rankings and using MMD to quantify result stability.
- **P5 (Evidence - Case Studies):** Preview the empirical findings: applying the framework to recent benchmarks reveals widespread underpowering.
- **P6 (Contributions):** List the five contributions, emphasizing theoretical novelty, practical algorithm, and empirical insights.

## Priority Revision Plan
| Priority | Action | Expected Impact |
| :--- | :--- | :--- |
| **P0** | Correct copy-paste errors in Section 5.2 ("encoders" -> "LLMs", "Figure 2" -> "Figure 3"). | Eliminates confusion and restores scientific rigor. |
| **P0** | Clarify the theoretical vs. heuristic status of the log-log linear relationship in Section 4.3. | Strengthens methodological credibility and sets accurate expectations. |
| **P1** | Add mechanistic discussion to Case Studies (Sections 5.1 & 5.2) explaining why certain design factors increase $n^*$. | Enhances practical value by guiding practitioners on robust study design. |
| **P1** | Move ranking justification from Appendix A.1 to Section 3.1. | Improves narrative flow and bridges intuition with formalism. |
| **P2** | Tighten Abstract and Conclusion with a 5-sentence arc and a strong call-to-action. | Increases reader engagement and reinforces the paper's practical payoff. |
| **P2** | Report $R^2$ of the linear fit in case studies to demonstrate heuristic reliability. | Provides empirical evidence for the algorithm's stability. |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **E1** | Evaluate generalizability of categorical encoder benchmark (Matteucci et al.) | 48 design factor combinations, datasets as allowed-to-vary factor | $n^*$, MMD quantiles | Many configurations require >30 datasets for (0.95, 0.05)-generalizability | Framework utility | Lacks mechanistic explanation for variance across design factors |
| **E2** | Evaluate generalizability of BIG-bench (Srivastava et al.) | 24 design factor combinations, subtasks as allowed-to-vary factor | $n^*$, MMD quantiles | Some tasks (e.g., conlang translation) require 44 subtasks; others (arithmetic) need only 1 | Framework utility | Copy-paste errors in text; missing value handling (80% threshold) could be discussed more |
| **E3** | Assess sensitivity of $n^*$ estimate to number of preliminary experiments $N$ | Synthetic data & real benchmarks, $N \in \{10, 20, 40, 80\}$ | Relative error $|n^*_N - n^*_{50}|/n^*_{50}$ | Mallows kernel stabilizes quickly ($N=10$); Borda kernel needs $N=20-30$ | Algorithm reliability | Does not report $R^2$ of the log-log linear fit |

### Research-Theme Gap Diagnosis
The core research value (providing a tool to pre-validate study designs) is well-supported. However, the *mechanistic understanding* of why certain experimental setups are less generalizable is weakly supported. Additionally, the *theoretical grounding* of the $n^*$ estimation heuristic could be strengthened with more empirical diagnostics (e.g., $R^2$).

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Mechanistic Insight** | Complex models/metrics exhibit higher ranking variance across datasets. | Analyze variance of rankings for SVM vs Decision Tree across 50 datasets. | Raw performance variance | Ranking variance, $n^*$ | SVM shows significantly higher $n^*$ | Low | Explains *why* certain factors require more data |
| **Heuristic Reliability** | Log-log linear fit is highly reliable for MMD quantiles. | Report $R^2$ of linear fit for all 48+24 design factor combinations. | None | $R^2$, prediction error | $R^2 > 0.9$ for >90% of cases | Low | Validates the extrapolation algorithm |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 7/10

**Post-Revision Target:** [8, 9]/10

**Rationale:** The paper addresses a highly relevant methodological gap in ML research with a rigorous mathematical formalization and a practical algorithm for estimating study size. The case studies effectively demonstrate the framework's utility, revealing that many recent benchmarks are underpowered. The score is held back slightly by the heuristic nature of the $n^*$ estimation algorithm (which lacks explicit theoretical guarantees in the main text), the absence of mechanistic insights into why certain design factors require more datasets, and some copy-paste errors in the case study analysis. Addressing these issues—particularly by clarifying the algorithm's theoretical status and adding mechanistic discussion—would significantly strengthen the paper's impact and credibility.