Here's my consolidated review.

## Summary

This paper presents a large-scale empirical study (400,000+ GPU-hours) of reinforcement learning compute scaling for LLMs. It introduces a sigmoidal compute-performance scaling law (Equation 1) that enables extrapolation from smaller runs to larger compute budgets, and validates it in a 100,000 GPU-hour run where the curve fitted on the first 50k GPU-hours accurately tracks observed performance at 100k. Through systematic ablations of six algorithmic axes, the paper identifies which choices shift the asymptotic ceiling (loss type, FP32 precision) versus those that primarily affect compute efficiency. The resulting recipe, SCALERL, demonstrates predictable scaling across model size (8B dense and 17B×16 MoE), batch size, generation length, and multi-task training.

## Strengths

1. **First validated predictive scaling framework for RL compute.**  
   Figure 1 shows that a sigmoidal curve fitted on the first 50k GPU-hours of an 8B dense run extrapolates to match the observed trajectory at 100k GPU-hours — the first demonstration of such predictive capability for RL in LLMs. The same pattern holds for the MoE run and across multiple scaling axes in Section 5.

2. **Large-scale systematic ablation at unprecedented compute.**  
   The study spans 400k GPU-hours and evaluates six algorithmic dimensions (off-policy setup, loss type, loss aggregation, advantage normalization, precision, curriculum) using the scaling parameters *A* (asymptote) and *B* (efficiency) instead of fixed-budget comparisons. This is a 25× scale increase over the largest prior study (ProRL at 16k GPU-hours).

3. **Disentanglement of asymptote-affecting vs. efficiency-affecting choices.**  
   The paper cleanly separates design decisions into those that shift the performance ceiling (loss type, FP32 precision, batch size) and those that mainly modulate how quickly that ceiling is reached (advantage normalization, curriculum, loss aggregation). This gives practitioners a principled prioritization, grounded in the LOO ablations of Figure 5.

4. **SCALERL achieves high asymptotic performance with predictable scaling.**  
   SCALERL reaches the highest fitted asymptote (A = 0.610, tied with MiniMax) and the best compute efficiency (B = 1.97) among compared recipes (Figure 2). Critically, its scaling trajectory remains predictable when extrapolated from 8k to 16k GPU-hours in LOO experiments and from 50k to 100k GPU-hours in the main run.

5. **Methodological rigor in curve fitting.**  
   The paper follows pre-training best practices: holding out an iid validation set (1k prompts from Polaris-53k), excluding the unstable early-compute regime, and selecting a sigmoidal form that respects the bounded nature of accuracy metrics — a principled departure from power-law fits that proved less robust (Appendix A.4).

## Weaknesses

### Fatal
None.

### Major

1. **Limited diversity in validation of the scaling framework.**  
   The sigmoidal scaling law (Eq. 1) is presented as a general *scientific framework* for analyzing RL compute scaling, yet its core validation is concentrated on one model family (8B dense with one 17B×16 MoE variant) and one task domain (verifiable math on Polaris-53k). The multi-task math + code experiment (Section 7, Figure 16) is encouraging but deferred to the appendix and preliminary. While the framework is tested across multiple scaling knobs (batch size, generation length, cross-recipe variants), all experiments share the same base data distribution and model architecture family. Broader validation — e.g., a different base model (non-Llama family), a different data distribution (GSM8K-level or scientific reasoning), or a substantially different model scale (1.5B or 70B) — would be needed to fully support the generality claimed for the framework. The paper's own discussion (Section 7) acknowledges this scope, but the claims in the abstract and introduction ("scientific framework") outrun the current evidence.

2. **Insufficiently controlled cross-recipe comparisons for the "state-of-the-art" claim.**  
   Figure 2 compares SCALERL against DeepSeek GRPO, Qwen 2.5 DAPO, Magistral, and MiniMax. The paper states that recipes are described in Appendix A.17, but does not specify in the main text whether these are faithful reimplementations, whether hyperparameters (e.g., KL regularization coefficient for GRPO, learning rates, clipping ranges) were tuned per baseline, or whether the same base model and data were used in a controlled manner for each. The extended-run validation points (× markers) partially mitigate this concern for *predictability*, but the claim that SCALERL "establishes a new state-of-the-art" (Section 1) requires stronger evidence that the baselines were configured competitively. (Note: the paper does use a common base model and dataset; the concern is about implementation fidelity and tuning effort.)

### Minor

3. **No uncertainty quantification on fitted scaling parameters.**  
   The parameters *A*, *B*, and *C*ₘᵢₔ are reported as point estimates without confidence intervals or bootstrap error bars. The validation pass rate is estimated from 16 generations per prompt on 1,000 prompts, so the fits have inherent noise. Key comparisons (e.g., SCALERL A = 0.610 vs. MiniMax A = 0.610; efficiency differences in Figure 5) would be more informative with uncertainty estimates. Without them, it is difficult to assess whether observed differences are meaningful or within noise.

4. **Generalization to downstream tasks only partially shown.**  
   AIME-24 results (Figure 1b) are presented only for SCALERL, not for all compared methods. The paper acknowledges that "a full characterization of generalization is beyond the scope of our work" (Section 7), and this is a reasonable scope choice. However, given that the scaling curves are fitted on iid validation (held-out training prompts), the framework's utility for predicting *generalization* would be strengthened by showing that the iid asymptote ranking across methods correlates with downstream asymptotic rankings. Currently this connection is only demonstrated for SCALERL itself.

5. **Batch-size asymptote claim is based on not-fully-saturated runs.**  
   The claim that "larger batch is slower but settles at a higher asymptote" (Figure 6c) rests on extrapolations from runs where the 2k-batch curve appears still rising. The qualitative pattern is plausible and consistent with the 100k GPU-hour run, but the conclusion would benefit from hedging until the smaller-batch curves more clearly plateau.

6. **Early-training cutoff sensitivity not quantified in the main text.**  
   The decision to exclude the first ~1.5k GPU-hours from fitting is justified by reference to pre-training practice and appendix discussion (A.7), but the main text provides no quantitative analysis of how fitted parameters vary when this cutoff is moved (e.g., 1k–2k GPU-hours). This would help readers assess the robustness of the reported fits.

### Trivial
None.

## Nice-to-Haves

- **Uncertainty quantification** via bootstrapping over validation prompts or training seeds would significantly strengthen the parameter comparisons.
- **Validation on a second base model family** (e.g., Qwen-3 8B or a smaller 1.5B model) would substantially increase confidence in the framework's generality.
- **Controlled baseline tuning**: reporting the hyperparameter search budget and final configuration used for each compared recipe would clarify the fairness of Figure 2.
- **A systematic plot of fitted *A* and *B* as a function of the early-training cutoff** would improve confidence in the fitting methodology.
- **Release of the full training code/pseudocode** for the asynchronous RL pipeline (beyond just the curve-fitting code) would aid reproducibility, though the paper's practical contribution is already substantial without this.
- **Ablation over number of generations per prompt** for the validation metric (8, 16, 32) to assess how it affects curve shape.

## Removed Points

These points were considered but removed from the main review for the reasons stated:

- **"Sigmoidal fit novelty not sufficiently credited to prior work (Ruan et al. 2024, Srivastava et al. 2022)"** — The paper explicitly cites both works in Section 2.1 as justification for the sigmoidal choice. The attribution is adequate.
- **"ProRL also conducted scaling experiments, so 'first large-scale systematic study' should be softened"** — ProRL used 16k GPU-hours on a 1.5B model. This paper uses 400k GPU-hours across 8B and 17B×16 MoE. The 25× scale difference makes the claim defensible. The paper also explicitly discusses ProRL in Section 6.
- **"The paper should discuss more candidly that asymptotic performance of SCALERL may not be substantially higher than simpler variants"** — The LOO analysis in Section 4 and the Discussion (Section 7: "we find very little impact on asymptotic performance from each decision, but each component helps efficiency") already make exactly this point.
- **"GPU-hours conflates computational cost; token-level would be more precise"** — GPU-hours is the standard practical measure in this field and is appropriate for the paper's audience.
- **"Missing grid search over interruption threshold"** — This is a specific hyperparameter that the paper reasonably fixes; a sweep would be nice-to-have but not required.
- **"Missing analysis of generations-per-prompt null result in main text"** — The paper highlights this finding in Section 5: "fitted scaling curves essentially unchanged"; the level of emphasis is appropriate.
- **"Reproducibility: only curve-fitting code released"** — While releasing the full training pipeline would be valuable, the paper provides detailed algorithmic descriptions (Eqs. 2–5, pseudo-J for SCALERL) and references to prior work for each component. This is a reasonable level of reproducibility for a systems-empirical paper.

## Novel Insights

None beyond the paper's own contributions. The key novelty — that RL compute scaling follows a predictable sigmoidal trajectory, and that most algorithmic choices affect efficiency rather than the asymptote — is well stated by the authors. The observation that SCALERL and MiniMax reach the same estimated asymptote (~0.61) despite different recipe details is an interesting point that the paper could discuss more explicitly, as it suggests convergence of distinct approaches to a common ceiling under this training distribution.

## Suggestions

- Add bootstrap confidence intervals (or at least standard errors) on *A* and *B* for all fits, especially Figure 2 and Figure 5. This would immediately clarify which differences are robust.
- For the "state-of-the-art" claim, either include a brief statement of tuning effort per baseline in the main text, or soften the claim to "competitive with and more predictable than existing recipes."
- Show AIME-24 (or another held-out benchmark) scaling curves for at least two additional comparison methods (e.g., MiniMax and Magistral) to demonstrate that iid asymptote ranking transfers to downstream generalization.
- Add a short paragraph or figure in the main text showing how fitted *A* and *B* change when the early-training exclusion cutoff is varied over 1–2k GPU-hours.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>