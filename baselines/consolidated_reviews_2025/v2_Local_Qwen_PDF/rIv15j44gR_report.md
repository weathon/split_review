## Summary
# Final Review Report

## Summary
This paper addresses the problem of estimating Heterogeneous Treatment Effects (HTE) under delayed response, where treatments take time to produce causal effects on outcomes. The authors formalize the problem by introducing potential response times alongside eventual potential outcomes, leading to a "false negative" label noise issue when observation windows are short. Theoretically, the paper proves the identifiability of eventual outcomes in the whole population and response times in the always-positive stratum under assumptions including unconfoundedness, time independence, and monotonicity. Methodologically, the authors propose CFR-DF, a learning approach that extends Counterfactual Regression using a modified EM algorithm to jointly estimate outcomes and response times. Experiments on synthetic and semi-synthetic real-world covariate datasets demonstrate that CFR-DF outperforms standard HTE baselines, particularly under short observation times.

## Strengths
1. **Clear Problem Formulation:** The paper effectively identifies a practical gap in HTE estimation—delayed response causing false negative label noise—and formalizes it using a principled potential outcomes framework with response times.
2. **Theoretical Identifiability:** The authors provide rigorous identifiability proofs for eventual outcomes and response times under clear assumptions, bridging causal inference and survival analysis concepts.
3. **Novel Algorithmic Approach:** CFR-DF creatively adapts the EM algorithm to handle latent eventual outcomes while incorporating IPM-based balancing to address confounding bias, showing strong performance on synthetic benchmarks.
4. **Comprehensive Synthetic Evaluation:** The experiments systematically vary observation times and response time heterogeneity, clearly demonstrating the method's advantage over standard HTE baselines under short observation windows.

## Weaknesses
1. **Strong Monotonicity Assumption:** The identifiability of response time HTE relies on Assumption 4 (Monotonicity: $Y(0) \le Y(1)$), which excludes scenarios with harmful treatments. This significantly limits the method's applicability in domains like precision medicine where adverse effects are possible.
2. **Semi-Synthetic Real-World Experiments:** The "real-world" experiments on AIDS, JOBS, and TWINS datasets actually simulate treatment, outcomes, and response times using real covariates. This is a semi-synthetic setup, not a true real-world evaluation with verified delayed feedback, which overstates the practical validation.
3. **Hyperparameter Overfitting Risk:** Hyperparameters $\alpha_Y$ and $\alpha_D$ are selected by minimizing MSE on the *training data*. This practice leads to overfitting and invalidates the generalization claims; a validation set should be used for tuning.
4. **Coupled Optimization Clarification:** The text claims the outcome and response time models "can be optimized independently," but the posterior $p_i$ depends on both, creating a coupled optimization problem. The training procedure (joint vs. alternating) needs clarification for reproducibility.

## Key Issues
1. **Validity of Monotonicity Assumption (Major):** The proof for response time HTE identifiability requires $Y(0) \le Y(1)$. If harmful treatments exist (PN stratum), the always-positive stratum probability cannot be identified via Lemma 1, breaking Theorem 2. This must be explicitly bounded as a limitation.
2. **Misleading "Real-World" Claims (Major):** Labeling semi-synthetic experiments as "real-world experiments" misleads readers about the method's deployment readiness. The method has not been tested on true observational data with delayed feedback.
3. **Training Data Hyperparameter Tuning (Major):** Selecting IPM weights based on training MSE introduces selection bias. The reported performance gains may partly reflect overfitting to the training distribution rather than true generalization.
4. **Optimization Coupling Ambiguity (Minor):** The claim of independent optimization for $h_Y$ and $h_D$ contradicts the dependency of $p_i$ on $h_D$. This needs clarification to ensure correct implementation by other researchers.

## Actionable Suggestions
1. **Clarify Monotonicity Limitations:** Add a dedicated paragraph in the Conclusion or Limitations section explicitly stating that $\tau_D(x)$ identifiability currently requires the absence of harmful treatments. Frame relaxing this assumption as a key future direction.
2. **Rename Real-World Experiments:** Change the section title to "Semi-Synthetic Experiments on Real-World Covariates." Add a sentence acknowledging that while covariates are real, the delayed feedback mechanism is simulated, and true validation remains future work.
3. **Fix Hyperparameter Tuning Protocol:** Retrain models using a train/validation/test split. Select $\alpha_Y$ and $\alpha_D$ based on validation set performance (e.g., validation PEHE or expected log-likelihood) to prevent overfitting.
4. **Clarify Optimization Procedure:** Replace "optimized independently" with a precise description of the training loop. If using joint gradients, state that both heads are updated simultaneously using computed $p_i$. If alternating, specify the order and frequency.
5. **Strengthen Abstract Conclusion:** Replace the generic final sentence with a specific result preview, e.g., "CFR-DF reduces PEHE by up to 46% compared to standard baselines under short observation windows."

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** HTE estimation is critical in medicine and marketing, but standard methods assume outcomes are observed timely and accurately.
- **S2 (Challenge/Gap):** In practice, treatments take time to produce effects; short observation windows convert eventual positives into false negatives, biasing HTE estimates.
- **S3 (Prior Limitation):** Existing HTE and time-to-event methods either ignore response delays or focus on continuous survival curves rather than binary eventual outcomes with delayed feedback.
- **S4 (Proposed Method):** We formalize HTE with delayed response and propose CFR-DF, a principled EM-based algorithm that jointly recovers eventual outcomes and estimates response times while correcting for confounding.
- **S5 (Key Result):** Theoretical identifiability is proven under clear assumptions, and experiments show CFR-DF significantly reduces estimation bias compared to baselines, particularly under short observation times.

### Introduction Outline (Complete)
- **P1 (Big Picture):** Introduce HTE estimation and its importance in personalized decision-making (medicine, recommendations).
- **P2 (Existing Methods & Gap):** Summarize standard HTE methods (CFR, DragonNet) and their assumption of timely outcomes. Introduce the "delayed response" problem: treatments take time, leading to false negative label noise when observation windows are short.
- **P3 (Technical Challenge):** Explain why this is hard: we cannot distinguish false negatives from true negatives, and response times are censored. Contrast with time-to-event literature (which models continuous survival curves, not binary eventual outcomes).
- **P4 (Proposed Solution):** Introduce the formalization with potential response times and the CFR-DF algorithm. Highlight the use of EM to handle latent eventual outcomes and IPM for confounding bias.
- **P5 (Contributions):** List the four contributions: (1) Problem formalization, (2) Identifiability proofs, (3) CFR-DF algorithm, (4) Empirical validation on synthetic and semi-synthetic datasets.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0 (Critical)** | Retrain with validation set for hyperparameter tuning. | Fixes overfitting risk; ensures reported gains are generalizable. | Medium |
| **P0 (Critical)** | Rename "Real-World Experiments" to "Semi-Synthetic Experiments" and clarify limitation. | Prevents misleading claims; aligns text with actual experimental setup. | Low |
| **P1 (Major)** | Explicitly discuss monotonicity assumption limitation in Conclusion. | Bounds the scope of response time HTE identifiability; improves scientific rigor. | Low |
| **P1 (Major)** | Clarify coupled optimization procedure for $h_Y$ and $h_D$. | Improves reproducibility; removes ambiguity about independent optimization. | Low |
| **P2 (Minor)** | Strengthen abstract conclusion with specific performance preview. | Increases reader engagement and highlights practical impact. | Low |
| **P2 (Minor)** | Add intuitive bridge to survival analysis in Appendix proofs. | Improves accessibility for readers unfamiliar with hazard rate recovery. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | CFR-DF outperforms baselines under delayed response. | Synthetic TOY datasets (varying $b_D$). | PEHE, $\epsilon_{ATE}$ | CFR-DF significantly lower error. | Yes | Fully synthetic data. |
| E2 | CFR-DF estimates response time HTE accurately. | Synthetic TOY datasets. | PEHE on $P(D(1)>d) - P(D(0)>d)$, $\tau_D(x)$ | CFR-DF better than T-DF. | Yes | Relies on monotonicity. |
| E3 | Performance stabilizes with longer observation time. | TOY datasets (varying $\bar{T}$). | PEHE | Error decreases as $\bar{T}$ increases. | Yes | Synthetic setting. |
| E4 | Robustness to covariate distribution. | Semi-synthetic AIDS, JOBS, TWINS. | PEHE, $\epsilon_{ATE}$ | CFR-DF outperforms baselines. | Partially | Outcomes simulated, not true real-world delayed feedback. |

### Research-Theme Gap Diagnosis
The core gap is the lack of validation on *true* observational data with delayed feedback. The semi-synthetic experiments validate robustness to real covariate structures but do not test the method's ability to recover ground truth from genuine delayed feedback noise. Additionally, the hyperparameter tuning on training data introduces a validity gap.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Generalization validity | Validation-based tuning improves generalization. | Retrain with 80/10/10 split; tune $\alpha$ on validation. | Same baselines. | Test PEHE | Lower test error than current training-tuned model. | Low | Fixes overfitting risk. |
| True delayed feedback | CFR-DF works on real delayed data. | Use a dataset with known delayed outcomes (e.g., clinical trial follow-up). | Standard HTE methods. | PEHE, Calibration | CFR-DF reduces bias compared to baselines. | High | Validates practical deployment. |
| Monotonicity relaxation | Method fails or degrades with harmful treatments. | Synthetic data with PN stratum ($Y(0)=1, Y(1)=0$). | CFR-DF, T-DF. | PEHE on $\tau_D(x)$ | Quantify error increase; identify failure mode. | Low | Bounds assumption scope. |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
Final Score: 5/10
Post-Revision Target: [6, 7]/10

**Rationale:** The paper addresses a meaningful and practical problem (delayed response in HTE) with a solid theoretical foundation and a creative algorithmic solution. The synthetic experiments clearly demonstrate the method's advantage over standard baselines. However, the score is limited by three major issues: (1) the strong monotonicity assumption that excludes harmful treatments, limiting practical applicability; (2) the misleading labeling of semi-synthetic experiments as "real-world," which overstates validation; and (3) the use of training data for hyperparameter tuning, which introduces overfitting risk. Addressing these issues—particularly by fixing the tuning protocol and clarifying the experimental setup—would significantly improve the paper's rigor and credibility, justifying a post-revision target of 6-7/10.