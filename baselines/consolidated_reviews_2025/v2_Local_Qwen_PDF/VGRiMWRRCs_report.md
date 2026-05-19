## Summary
# Final Review Report

## Summary
This paper proposes "Learn from Known Unknowns," a method for improving group robustness without explicit group annotations. The authors unify existing group robustness approaches under an Empirical Bayesian (EB) framework, treating group information as a latent variable. Building on this framework, they leverage evidential deep learning to quantify the epistemic uncertainty of biased Empirical Risk Minimization (ERM) models. This uncertainty is then used to reweight samples during a last-layer retraining phase, effectively prioritizing minority or spurious-correlation-affected samples. The method is evaluated on standard vision and language benchmarks (Waterbirds, CelebA, MultiNLI, CivilComments, Colored MNIST), demonstrating competitive worst-group accuracy compared to group-label-free baselines and narrowing the gap with oracle methods that use group annotations.

## Strengths
1. **Unified Theoretical Perspective:** The paper provides a coherent Empirical Bayesian framework to interpret existing group robustness methods (e.g., JTT, LfF, SELF). This unification helps clarify the common goal of estimating latent group distributions and highlights the limitations of heuristic priors in prior work.
2. **Practical Method Design:** The proposed method leverages evidential deep learning to quantify epistemic uncertainty, offering a scalable and computationally efficient approach. By focusing on last-layer retraining with uncertainty-guided reweighting, the method maintains the high-quality representations learned by ERM while effectively mitigating spurious correlations.
3. **Comprehensive Empirical Evaluation:** The method is evaluated across diverse vision and language datasets, demonstrating consistent improvements in worst-group accuracy. The inclusion of both group-label-free and oracle baselines provides a clear context for the method's performance and efficiency.

## Weaknesses
1. **Mathematical Rigor in Theoretical Guarantee:** Theorem 3.1 relies on Tweedie's formula to approximate the posterior mean of the latent group variable, assuming differentiability with respect to the label $y$. However, in standard classification tasks, $y$ is discrete. The theorem does not explicitly state a continuous relaxation for $y$, making the derivative $\frac{\partial}{\partial y} \log p(y|x, \theta)$ mathematically ill-defined in the reported setting.
2. **Inconsistent Hyperparameter Claims:** The abstract and introduction claim that the method "reduces reliance on hyperparameter tuning" and operates "without introducing additional hyperparameters." However, Section 5.2 reveals that ten hyperparameter configurations are sampled and the best is selected, and the KL regularization coefficient $\lambda$ requires dynamic scheduling. This contradicts the claim of hyperparameter insensitivity.
3. **Misuse of Bayesian Terminology:** The retraining step is described as performing "Bayesian Model Averaging (BMA)" by reweighting the loss with uncertainty estimates. BMA traditionally involves averaging predictions or parameters over a posterior distribution of models, not sample-wise loss reweighting. This terminology overstates the Bayesian rigor of the approach.
4. **Lack of Quantitative Validation for Core Mechanism:** The paper claims that "quantitative analysis showed correlations between uncertainty values and true group labels," but no correlation metrics (e.g., Pearson/Spearman coefficients) are reported. The evidence is primarily qualitative (GradCAM, t-SNE), leaving the core assumption unsubstantiated statistically.

## Key Issues
1. **Differentiability Assumption for Discrete Labels (Critical):** The theoretical foundation in Theorem 3.1 assumes the marginal likelihood is differentiable with respect to the label $y$. Without explicitly defining a continuous relaxation for discrete class labels, the gradient term is undefined. This gap must be addressed to validate the theoretical guarantee.
2. **Factual Inconsistency in Hyperparameter Claims (Major):** The manuscript repeatedly claims reduced or no additional hyperparameter tuning, yet the experimental setup involves sampling ten configurations and selecting the best. This inconsistency undermines the reproducibility and practical efficiency claims.
3. **Terminological Inaccuracy Regarding BMA (Major):** Describing sample-wise uncertainty reweighting as Bayesian Model Averaging is technically incorrect and may mislead readers about the method's statistical properties. The mechanism should be accurately framed as uncertainty-weighted risk minimization.
4. **Missing Quantitative Correlation Evidence (Major):** The claim that uncertainty correlates with group labels is central to the method's validity but lacks quantitative support (e.g., correlation coefficients). Relying solely on qualitative visualizations is insufficient for a rigorous empirical paper.

## Actionable Suggestions
1. **Clarify Theoretical Relaxation:** Explicitly state in Theorem 3.1 and the proof that the discrete label $y$ is relaxed to a continuous vector (e.g., one-hot or soft label) for the purpose of differentiation. Justify this relaxation and ensure the notation reflects it.
2. **Correct Hyperparameter Claims:** Remove statements claiming "no additional hyperparameters" or "reduced reliance on tuning" if grid/random search is used. Instead, emphasize that the method uses a standard evidential loss with a single dynamically scheduled coefficient $\lambda$, which is more stable than methods requiring complex multi-model training.
3. **Fix BMA Terminology:** Replace "Bayesian Model Averaging" with "uncertainty-weighted risk minimization" or "epistemic uncertainty-guided reweighting." Clarify that upweighting high-uncertainty samples prioritizes learning from ambiguous or minority regions, rather than averaging over model posteriors.
4. **Add Quantitative Correlation Metrics:** Report Spearman or Pearson correlation coefficients between the estimated uncertainty $u(x)$ and the true minority group indicators for each dataset. Include these in a table or appendix to quantitatively validate the core mechanism.
5. **Expand Conclusion with Limitations:** Add a sentence acknowledging current limitations (e.g., reliance on last-layer retraining, performance variations on datasets like CelebA) and suggest concrete future work (e.g., extending to full-model fine-tuning, exploring alternative uncertainty quantification methods).

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Group robustness is critical for real-world ML, but standard ERM exploits spurious correlations, leading to poor worst-group accuracy.
- **S2 (Significance/Challenge):** Mitigating these correlations without explicit group annotations remains challenging due to the lack of principled frameworks for latent group estimation.
- **S3 (Prior Gap):** Existing heuristic reweighting methods often exhibit inconsistent performance and rely heavily on hyperparameter tuning.
- **S4 (Proposed Method):** We unify prior approaches under an Empirical Bayesian framework and propose Learn from Known Unknowns, which leverages epistemic uncertainty from biased ERM models to guide uncertainty-weighted last-layer retraining.
- **S5 (Key Result & Bounded Implication):** Empirical evaluations across vision and language benchmarks demonstrate consistent worst-group accuracy improvements (e.g., +X% on Waterbirds) while maintaining competitive average performance, offering a scalable pathway to mitigate spurious correlations.

### Introduction Outline (Complete)
- **P1 (Big Picture & Problem):** Introduce spurious correlations and group robustness, highlighting the failure of ERM on minority groups. Emphasize the practical stakes (e.g., healthcare, fairness).
- **P2 (Prior Work & Gap):** Discuss existing mitigation strategies (reweighting, last-layer retraining). Highlight the gap: methods either require group labels or rely on heuristic rules that fail to fully exploit posterior uncertainty, leading to inconsistent performance.
- **P3 (Proposed Solution & Framework):** Introduce the Empirical Bayesian framework as a unifying lens. Explain how treating group information as a latent variable allows for principled estimation.
- **P4 (Method Intuition):** Describe how evidential deep learning quantifies epistemic uncertainty, serving as a proxy for latent group probabilities. Explain the uncertainty-guided reweighting mechanism.
- **P5 (Evidence Preview & Contributions):** Preview key empirical outcomes (competitive worst-group accuracy, efficiency). List explicit contributions: (1) EB unification, (2) Learn from Known Unknowns method, (3) comprehensive empirical validation.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0 (Critical)** | Fix Theorem 3.1 differentiability assumption by explicitly defining continuous label relaxation. | Resolves mathematical validity risk; ensures theoretical guarantee applies to classification settings. | Medium |
| **P0 (Critical)** | Correct hyperparameter claims in Abstract/Intro to align with Section 5.2 tuning procedure. | Eliminates factual inconsistency; improves reproducibility and scientific credibility. | Low |
| **P1 (Major)** | Replace "Bayesian Model Averaging" with "uncertainty-weighted risk minimization" and clarify mechanism. | Fixes terminological inaccuracy; aligns method description with actual implementation. | Low |
| **P1 (Major)** | Add quantitative correlation metrics (Spearman/Pearson) between uncertainty and group labels. | Provides statistical validation for the core mechanism; strengthens empirical claims. | Medium |
| **P2 (Minor)** | Expand Conclusion with bounded limitations and concrete future work directions. | Improves scientific rigor and provides clear roadmap for follow-up research. | Low |
| **P2 (Minor)** | Update Appendix Pseudo-code to reflect last-layer freezing and dynamic $\lambda$ scheduling. | Enhances reproducibility for practitioners implementing the method. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Synthetic validation of uncertainty-guided reweighting | Colored MNIST (pcorr=0.9/0.1), LeNet-5, ERM vs Ours | Worst-group accuracy | Minority group accuracy improved from 3.74% to 84.58% | Uncertainty identifies minority groups | Simple synthetic setting |
| E2 | Comparison with group-label-free methods | Waterbirds, CelebA, MultiNLI, CivilComments; ResNet-50/BERT | Worst/Avg accuracy | Competitive worst-group accuracy; narrows gap with oracles | Method efficacy across domains | Lacks quantitative uncertainty-group correlation |
| E3 | Qualitative uncertainty analysis | Waterbirds GradCAM, Colored MNIST t-SNE | Visual clustering | High-uncertainty samples highlight spurious backgrounds | Mechanism intuition | Qualitative only |

### Research-Theme Gap Diagnosis
The core claim that epistemic uncertainty reliably proxies latent group information lacks quantitative statistical validation. Additionally, the method's performance on CelebA lags behind contrastive methods (CnC), suggesting limitations in representation learning when spurious attributes are highly entangled with core features.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Uncertainty-Group Correlation | Higher uncertainty correlates with minority group membership | Compute Spearman $\rho$ between $u(x)$ and minority indicator across all datasets | None | Correlation coefficient | $\rho > 0.3$ consistently | Low | Quantitative validation of core mechanism |
| Representation Robustness | Last-layer retraining is sufficient if backbone captures core features | Compare full-model fine-tuning vs last-layer retraining under identical uncertainty weights | ERM, DFR | Worst-group accuracy | Full-tuning shows marginal gain | Medium | Bounds the applicability of last-layer approach |
| Hyperparameter Sensitivity | Method performance is stable across $\lambda$ schedules | Test linear, cosine, and constant $\lambda$ schedules | Baseline schedules | Worst-group accuracy variance | Std dev < 1% across schedules | Low | Supports reduced-tuning claim |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 5.5/10

**Rationale:** The paper presents a promising and practically motivated approach to group robustness, effectively unifying prior methods under an Empirical Bayesian framework and leveraging evidential deep learning for uncertainty-guided reweighting. The empirical results are competitive and the method is computationally efficient. However, the score is moderated by critical mathematical gaps in the theoretical guarantee (differentiability w.r.t. discrete labels), factual inconsistencies regarding hyperparameter tuning claims, and the misuse of Bayesian terminology (BMA). Additionally, the lack of quantitative validation for the core uncertainty-group correlation mechanism weakens the empirical rigor. Addressing these issues would significantly strengthen the paper's validity and credibility.

**Post-Revision Target:** [7.0, 8.0]/10

**Justification:** If the authors rigorously fix the theoretical relaxation, correct the hyperparameter claims, replace the BMA terminology with accurate descriptions, and add quantitative correlation metrics, the paper will meet the standards for a strong acceptance. The core idea is sound and the empirical performance is compelling, making it highly salvageable with targeted revisions.