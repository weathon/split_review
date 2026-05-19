## Summary
# Final Review Report

## Summary
This paper introduces REMASKER, a tabular data imputation method that extends the masked autoencoding (MAE) framework. The core idea is a "re-masking" strategy: during training, in addition to naturally missing values, the method randomly masks a subset of observed values and optimizes a Transformer-based autoencoder to reconstruct them. This self-supervised task encourages the model to learn missingness-invariant representations. The authors evaluate REMASKER on 12 UCI benchmark datasets under MCAR, MAR, and MNAR settings, comparing it against 13 baselines. Results show that REMASKER matches or outperforms existing methods in imputation fidelity (RMSE, Wasserstein distance) and utility (AUROC), with gains becoming more pronounced at higher missing ratios. The paper also provides a theoretical analysis and empirical CKA similarity measures to support the claim of missingness-invariant representation learning.

## Strengths
1. **Simple and Effective Methodology:** REMASKER introduces a straightforward "re-masking" strategy that adapts the successful MAE paradigm to tabular imputation. The approach avoids complex density estimation or adversarial training, making it easier to implement and train stably.
2. **Comprehensive Empirical Evaluation:** The paper evaluates the method across 12 diverse UCI datasets under MCAR, MAR, and MNAR settings, comparing against 13 strong baselines. The inclusion of both fidelity (RMSE, WD) and utility (AUROC) metrics provides a well-rounded assessment.
3. **Insightful Analysis:** The ablation studies on model depth, width, masking ratio, and reconstruction loss components are thorough. The theoretical analysis and CKA similarity experiments provide valuable intuition about why re-masking encourages missingness-invariant representations.
4. **Practical Utility:** Demonstrating that REMASKER can serve as a strong base imputer within ensemble frameworks (e.g., HyperImpute) highlights its practical value and flexibility in real-world pipelines.

## Weaknesses
1. **Overstated Theoretical Rigor:** The "theoretical justification" in Section 5 relies on a strong assumption of a lossless decoder, which is an idealized condition. The leap from minimizing representation distance to guaranteeing "missingness-invariant representations" is more of an intuitive interpretation than a rigorous proof. The term "theoretical justification" overstates the mathematical rigor.
2. **Missing Reproducibility Details:** The evaluation setup lacks explicit information on random seeds, variance reporting protocols, and hyperparameter tuning procedures (e.g., grid search ranges, validation strategy). This makes it difficult to assess the fairness of comparisons, especially against adaptive ensemble methods like HyperImpute.
3. **Notation and Typographical Errors:** Several minor but distracting errors exist, such as "withd features," "ad-dimensional," "an mask variable," and repeated subscripts in the re-masking notation ($\tilde{x}_{m \land m'}$ used twice). These reduce perceived rigor and clarity.
4. **Limited Scope of Datasets:** The evaluation relies solely on 12 small-to-medium UCI datasets. While standard for the field, these datasets may not fully represent the complexity, scale, and heterogeneity of real-world tabular data (e.g., high-dimensional sparse data, mixed continuous/categorical features at scale).
5. **Unbounded Claims:** The abstract and conclusion claim that REMASKER "outperforms state-of-the-art methods" without qualifying the specific settings or acknowledging cases where it underperforms (e.g., WD on the climate dataset). The mechanism-agnostic claim is also slightly overstated given performance variations across MCAR/MAR/MNAR.

## Key Issues
1. **Theoretical Assumption Validity:** The derivation in Section 5 assumes the existence of a lossless decoder $d_{\vartheta^*}$ to reformulate the reconstruction loss as a distance between representations. This assumption is rarely met in practice due to finite model capacity. The authors should explicitly acknowledge this as an idealized condition and clarify that the formulation provides an interpretive lens rather than a rigorous proof of invariance.
2. **Reproducibility and Fair Comparison:** The lack of explicit reporting on random seeds, variance estimation, and hyperparameter tuning protocols undermines reproducibility. Given that REMASKER is compared against adaptive methods like HyperImpute, it is critical to confirm that baselines were tuned with comparable computational budgets and that results reflect stable performance across multiple runs.
3. **Notation Consistency:** The re-masking notation contains a typo where $\tilde{x}_{m \land m'}$ is used for both re-masked and unmasked values. This creates ambiguity and should be corrected to clearly distinguish the subsets (e.g., using $\tilde{x}_{remask}$ and $\tilde{x}_{unmask}$).
4. **Claim Bounding:** Statements such as "outperforms state-of-the-art methods" and "without specific assumptions about the missingness mechanisms" are slightly overstated. Performance does vary across mechanisms (MCAR vs. MNAR), and REMASKER does not uniformly dominate all baselines on all metrics (e.g., WD on climate). Claims should be bounded to the evaluated settings and metrics.

## Actionable Suggestions
1. **Clarify Theoretical Assumptions:** In Section 5, explicitly state that the lossless decoder assumption is idealized. Replace "theoretical justification" with "theoretical analysis" or "intuition," and clarify that the distance minimization provides an interpretive lens for the observed empirical behavior (supported by CKA similarity).
2. **Enhance Reproducibility Reporting:** Add a dedicated paragraph in Section 4 specifying: (a) the number of random seeds used (e.g., 5) and that results report mean ± std, (b) the hyperparameter tuning protocol (e.g., grid search over learning rate, masking ratio, depth on a validation split), and (c) confirmation that baselines were configured using official implementations or recommended settings.
3. **Fix Notation and Typos:** Correct the repeated subscript typo in Section 3.2 ($\tilde{x}_{m \land m'}$) to clearly distinguish re-masked and unmasked values. Fix minor typos such as "withd features," "ad-dimensional," and "an mask variable" in Section 3.1.
4. **Bound Performance Claims:** In the Abstract and Conclusion, qualify statements like "outperforms state-of-the-art methods" by specifying the evaluated settings (e.g., "on 12 UCI benchmarks under MCAR/MAR/MNAR"). Acknowledge cases where REMASKER trades off fidelity metrics (e.g., RMSE vs. WD) to provide a more balanced view.
5. **Expand Dataset Scope (Optional but Recommended):** If feasible, include 1-2 larger or more heterogeneous datasets (e.g., from Kaggle or industry benchmarks) to demonstrate scalability and robustness beyond small UCI tables.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Tabular data imputation is critical for downstream tasks but remains challenging due to intricate feature correlations and diverse missingness mechanisms.
- **S2 (Prior Gap):** Existing discriminative and generative methods often struggle with error accumulation, complex training procedures, or explicit density estimation assumptions.
- **S3 (Proposed Method):** We introduce REMASKER, a masked autoencoding approach that randomly "re-masks" observed values during training to encourage the learning of missingness-invariant representations.
- **S4 (Key Results):** Evaluated on 12 UCI benchmarks under MCAR, MAR, and MNAR settings, REMASKER matches or exceeds 13 baselines in fidelity and utility, with gains increasing at higher missing ratios.
- **S5 (Implication):** Our analysis shows that re-masking promotes robust representations, indicating that masked modeling is a promising direction for tabular imputation.

### Introduction Outline (Complete)
- **P1 (Motivation & Problem):** Establish the ubiquity of missing data in real-world tabular datasets and the critical need for high-fidelity imputation before downstream analysis. Highlight challenges: high-order correlations, varied missingness mechanisms, and data scarcity.
- **P2 (Prior Work & Limitations):** Categorize existing methods into discriminative (iterative conditional modeling, error accumulation) and generative (GAN/VAE complexity, density estimation limits). Explicitly state why these paradigms fall short under high missing ratios.
- **P3 (Proposed Solution & Intuition):** Introduce REMASKER and the re-masking strategy. Explain the intuition: by forcing the model to reconstruct randomly masked observed values, we create a self-supervised task that encourages holistic, missingness-invariant representations without explicit mechanism modeling.
- **P4 (Contributions & Evidence):** Summarize three contributions: (1) simple yet effective MAE adaptation for imputation, (2) comprehensive empirical validation across 12 datasets and 3 missingness mechanisms, (3) theoretical analysis and CKA evidence supporting missingness invariance. Preview that REMASKER also integrates well into ensemble frameworks.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Clarify theoretical assumptions in Section 5; replace "theoretical justification" with "theoretical analysis" and acknowledge the lossless decoder assumption. | Prevents reviewer criticism on mathematical rigor; aligns claims with empirical evidence. | Low |
| **P0** | Add reproducibility details in Section 4: number of seeds, variance reporting, hyperparameter tuning protocol, and baseline configuration. | Ensures fair comparison and enables replication; critical for acceptance. | Low |
| **P1** | Fix notation typos in Section 3.2 ($\tilde{x}_{m \land m'}$ repetition) and Section 3.1 ("withd", "ad-dimensional"). | Improves clarity and perceived rigor. | Low |
| **P1** | Bound performance claims in Abstract/Conclusion; specify evaluated settings and acknowledge metric trade-offs (e.g., RMSE vs. WD). | Increases scientific defensibility and objectivity. | Low |
| **P2** | Expand evaluation to 1-2 larger/heterogeneous datasets (if feasible) to demonstrate scalability beyond UCI benchmarks. | Strengthens generalization claims and practical relevance. | Medium |
| **P2** | Add a brief discussion on computational complexity and training time compared to baselines. | Provides complete practical context for deployment. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Overall performance vs. 13 baselines | 12 UCI datasets, MAR 0.3 | RMSE, WD, AUROC | REMASKER matches/exceeds baselines | SOTA performance | Limited to small UCI datasets |
| E2 | Sensitivity to dataset size/features/missing ratio | Letter dataset, varying params | RMSE, WD, AUROC | Performance improves with data/features; robust to missing ratio | Scalability & robustness | Single dataset focus |
| E3 | Ablation: encoder/decoder depth, width, backbone | Letter dataset | RMSE, WD, AUROC | Optimal config found; Transformer best | Model design validity | No variance reported |
| E4 | Ablation: reconstruction loss components | Letter, California | RMSE, WD, AUROC | Including unmasked loss improves performance | Loss design validity | Limited datasets |
| E5 | Training regime & masking ratio impact | Letter, California | RMSE, WD, AUROC | Loss converges; optimal ratio varies | Trainability & hyperparameter sensitivity | No seed variance |
| E6 | Ensemble integration (HyperImpute base) | Letter, California | RMSE, WD, AUROC | REMASKER improves ensemble performance | Practical utility | Limited datasets |
| E7 | Theoretical analysis & CKA similarity | Letter dataset | CKA similarity | CKA increases with training | Missingness invariance | Empirical proxy, not proof |

### Research-Theme Gap Diagnosis
The core claim of missingness-invariant representation learning is supported by CKA similarity but lacks causal controls. The SOTA performance claim is bounded to UCI datasets and may not generalize to larger, more heterogeneous real-world tables. Reproducibility is hindered by missing seed/variance and tuning protocol details.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Reproducibility & Stability | REMASKER gains are stable across random seeds. | Run E1 with 5 seeds, report mean±std. | Same baselines, tuned identically. | RMSE, WD, AUROC | Gains remain significant (p<0.05) | Low | Validates SOTA claims |
| Missingness Invariance Causality | Re-masking directly causes invariance, not just capacity. | Ablate re-masking ratio (0% vs 50%) with matched capacity. | Standard MAE (no re-masking). | CKA, RMSE | Re-masking improves CKA & RMSE | Low | Strengthens mechanism claim |
| Scalability & Real-World Generalization | REMASKER scales to larger datasets. | Evaluate on 2-3 larger datasets (e.g., Kaggle tabular). | HyperImpute, MissForest. | RMSE, WD, Training Time | Competitive performance & reasonable time | Medium | Broadens applicability |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
Final Score: 6.5/10
Post-Revision Target: [7.5, 8.5]/10

**Rationale:** The paper presents a simple, effective, and well-motivated adaptation of masked autoencoding for tabular imputation. The empirical evaluation is comprehensive across multiple datasets and missingness mechanisms, and the ablation studies are thorough. However, the score is moderated by overstated theoretical claims (relying on a strong lossless decoder assumption), missing reproducibility details (seeds, tuning protocols), and minor notation/typographical errors. Addressing these issues—particularly by bounding claims, clarifying assumptions, and enhancing reproducibility reporting—would significantly strengthen the paper's scientific rigor and defensibility, justifying the post-revision target.