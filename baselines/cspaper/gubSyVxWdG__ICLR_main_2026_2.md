---
job_id: fb3fb77e-51e3-4bc2-8aa7-b8fe403f55c9
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: gubSyVxWdG.pdf
paper: A Relative Error-Based Evaluation Framework of Heterogeneous Treatment Effect Estimators
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining causal reasoning, uncertainty quantification, learning theory, and neural-network-based methodology for evaluating and learning heterogeneous treatment effects.

## Minimum Quality
Pass ✅. The paper includes an abstract, introduction with related-work discussion, methodological sections, theoretical analysis, experiments with quantitative results, and a conclusion; despite several notation and clarity issues, it clears the minimum bar for a full scientific submission rather than a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, suspicious reviewer-directed instructions, or other manipulative content in the provided paper text or figures.

# Expected Review:
## Summary
This paper studies evaluation of heterogeneous treatment effect estimators through a relative-error criterion, rather than trying to estimate absolute error against an unavailable ground truth. The main technical claim is that, by enforcing certain moment conditions through a weighted outcome loss and propensity-score balance regularization in a Dragonnet-style neural architecture, the resulting relative-error estimator can remain $\sqrt{n}$-consistent and asymptotically normal when the propensity score model is correctly specified, even if the outcome regressions are misspecified.

Beyond evaluation, the paper also proposes an HTE learning procedure that aggregates pairwise estimators derived from the same nuisance-learning framework. Experiments on IHDP, Twins, and Jobs are used to assess confidence-interval coverage, estimator-selection accuracy, and downstream HTE estimation performance.

## Strengths
1. **The paper targets an important and genuinely underdeveloped problem.** Much of the HTE literature focuses on proposing new estimators, while model evaluation and comparison under unobserved counterfactuals remain much less mature. Framing the problem around *relative* error between candidate estimators is a sensible and practically meaningful direction.

2. **There is a clear conceptual connection between the theory and the method.** The paper does not just present a heuristic neural architecture; it first derives the moment conditions in **Equation (4)** and then uses them to motivate the weighted least-squares loss and balance regularization in **Section 4.2**. Whether every step is fully convincing is debatable, but the overall pipeline is coherent.

3. **The central theoretical goal is meaningful.** Relative-error inference that tolerates misspecification of $\mu_a(x)$ while retaining valid large-sample behavior under a correctly specified propensity score model would be useful in practice, especially because outcome regression extrapolation is indeed a common failure mode in observational causal inference.

4. **Some empirical evidence is genuinely encouraging.** In **Figure 1**, the confidence-interval coverage on both IHDP and Twins is visually close to the nominal $90\%$ target across the displayed estimator pairs, which supports the uncertainty-quantification claim at least at a high level. This is one of the more persuasive pieces of evidence in the paper.

5. **The comparison against simple nuisance choices in Table 2 is useful.** On both IHDP and Twins, “Ours” preserves coverage while substantially improving selection accuracy over regression and boosting nuisances. In particular, the jump from 0.44/0.48 to 0.80 on IHDP selection and from 0.86/0.88 to 0.94 on Twins suggests the proposed nuisance-learning scheme is doing something beyond cosmetic engineering.

6. **The downstream HTE results in Table 1 are strong on the chosen benchmarks.** The proposed method is best across all reported metrics on IHDP and Twins, both in-sample and out-of-sample. On IHDP, the gap in $\sqrt{\epsilon_{\text{PEHE}}}$ between “Ours” and the strongest baselines is not tiny, for example 0.638 vs 0.741 for DRCFR in-sample; that is a meaningful empirical improvement on this benchmark.

7. **The ablation evidence is directionally supportive.** In **Table 5**, removing $\mathcal{L}_{\mathrm{const}}$ hurts both inference quality and HTE estimation quality substantially, which is consistent with the paper’s claim that the balance-style constraints are central rather than decorative.

## Weaknesses
1. **The mathematical exposition is much sloppier than it needs to be, and in a theory-heavy paper this is not a cosmetic issue.**  
   Several equations and theorem statements contain notation inconsistencies or apparent typographical errors that materially obstruct verification. For example, on **Page 5**, the Taylor expansion compares
   $\check{\delta}(\check{\tau}_{1},\check{\tau}_{2};\check{\gamma},\check{\beta}_{0},\check{\beta}_{1})-\check{\delta}(\check{\tau}_{1},\check{\tau}_{2};\check{\gamma},\check{\beta}_{0},\check{\beta}_{1})$,
   which is obviously zero as written, so the intended expansion point must be different. The same page repeatedly mixes checked, barred, and hatted quantities in ways that make it unclear which object is the estimator and which is its probability limit. Similar issues appear in **Theorem 1** and **Proposition 2** on **Pages 6 to 7**, where $\hat{u}_a$, $\bar{u}_a$, $\check{\mu}_a$, and $\hat{\mu}_a$ are not used consistently.  
   This matters because the paper’s main contribution is not just empirical, it is the claimed large-sample robustness result. If the notation around the expansion and limiting argument is unstable, it becomes hard to tell whether the proof is merely poorly written or whether a substantive step is missing.

2. **The proposed weighted least-squares objective in Section 4.2 is underspecified and potentially problematic because the “weights” can be negative.**  
   In **Page 5**, the loss
   \[
   \mathcal{L}_{\text{wls}}(\beta_0,\beta_1;\check{\gamma})
   \]
   is multiplied by $(\check{\tau}_1(X_i)-\check{\tau}_2(X_i))$. Since this quantity can clearly be negative for some $X_i$, the objective is not a standard weighted least-squares criterion with nonnegative weights. If some weights are negative, the objective need not be convex in $(\beta_0,\beta_1)$, may be unbounded below in pathological cases, and the “argmin” interpretation used immediately afterward becomes questionable.  
   The paper then states that setting the population derivatives to zero makes the first condition in **Equation (4)** hold, but this relies on the optimization problem being well-defined and differentiable in the usual way. Right now the manuscript treats this as routine, when it is actually a delicate point. At minimum the authors need to clarify whether they intend signed weights, whether the objective is only a moment-estimation device rather than a bona fide least-squares loss, and under what conditions the minimizer exists.

3. **There is a substantial gap between the population-moment derivation and the actual neural-network training procedure.**  
   The theoretical argument is built around exact population equalities in **Equation (4)** and rate assumptions in **Theorem 1**. The implemented method, however, optimizes a nonconvex neural objective
   \[
   \mathcal{L}=\mathcal{L}_{\mathrm{wls}}+\lambda_1\mathcal{L}_{\mathrm{ce}}+\lambda_2\mathcal{L}_{\mathrm{const}}
   \]
   with soft penalties and slack variables, as described on **Pages 5 to 6**. There is no argument in the main paper that minimizing this objective actually yields nuisance estimators satisfying the relevant moment conditions at the needed rates, or even approximately enough for the asymptotic conclusion to plausibly transfer.  
   In other words, the theorem is about an estimator under assumptions, but the paper often reads as if the architecture itself is what guarantees those assumptions. That implication is not established. The distinction between “we assume the rates” and “our training procedure delivers the rates” needs to be made much sharper.

4. **The main robustness story still leans heavily on correct propensity-score specification, and the empirical stress test for this is too weak.**  
   The central claim is robustness to misspecified outcome regressions, but **Theorem 1** on **Page 6** requires the propensity model to be correctly specified and estimated faster than $n^{-1/4}$. In practice, this is not a benign assumption. Propensity scores can be quite fragile in observational settings, especially under covariate shift, overlap issues, or when treatment assignment is driven by variables only weakly represented in the learned $\Phi(X)$.  
   The sensitivity analysis in **Table 6** is not really a convincing test of model misspecification. Injecting Gaussian noise into the *true* propensity score is a perturbation experiment, not a misspecified-model experiment. A wrong functional form, omitted confounders, representation misspecification, or poor overlap would be more relevant failure modes. Since the theorem depends critically on the propensity model, this is not a side issue, it is one of the paper’s key practical bottlenecks.

5. **The empirical evaluation of the relative-error estimator is narrower than the paper’s framing suggests.**  
   The main text evaluates pairwise comparisons among just three candidate HTE estimators, TARNet, Causal Forest, and X-Learner. That is enough for a proof-of-concept, but it is still a fairly small slice of the estimator landscape, especially given that **Table 1** already includes a much larger baseline set for downstream HTE estimation.  
   Also, **Figure 2** is more mixed than the text suggests. The method does look strong for some pairs, but selection accuracy varies noticeably by dataset and by estimator pair. On IHDP, at least one pair appears much less convincing than the strongest case, so the paper’s wording that it “provide[s] trustworthy advice” across pairs feels a bit too broad. A more granular analysis of when relative-error comparison is easy or hard would make the empirical story more credible.

6. **Section 5, the “enhanced estimation of HTE,” feels much less grounded than the evaluation framework, and it risks overselling a heuristic.**  
   The aggregation rule on **Page 7**
   \[
   \hat{\tau}(x)=\frac{2}{|\mathcal{K}|(|\mathcal{K}|-1)}\sum_{k,k'\in\mathcal{K}}
   \hat{\mu}_1(x;\hat{\tau}_k,\hat{\tau}_{k'})-\hat{\mu}_0(x;\hat{\tau}_k,\hat{\tau}_{k'})
   \]
   is introduced with very limited justification. There is no theory for why averaging over all pairs should improve HTE estimation, no comparison to straightforward alternatives such as averaging the candidate $\hat{\tau}_k$ directly, rank-based pruning, weighted ensembling, or stacking, and no analysis of whether low-quality pairs can poison the aggregate.  
   **Table 1** shows strong results, but because this section adds a second contribution beyond evaluation, the evidentiary bar should be higher. Right now the paper goes from “we can estimate pairwise relative error” to “surprisingly, our pairwise aggregate is excellent,” which is interesting but still somewhat heuristic.

7. **Presentation quality is uneven, especially in tables and notation, and this hurts reproducibility and trust.**  
   Some tables have formatting or symbol corruption. For instance, **Table 5** contains entries like “√εH2PE” and “εu4ZE,” which are clearly broken renderings of the intended metrics. There are also multiple reference and text errors, such as “Assumption 2” on **Page 4** where the paper appears to mean Condition 2, and several malformed reference entries in the bibliography.  
   These may sound minor, but in a paper that asks the reader to trust a delicate asymptotic argument and a custom training objective, these accumulated slips reduce confidence. The manuscript needs a serious proofreading pass.

## Questions
1. **Can the authors clarify the exact optimization role of $\mathcal{L}_{\mathrm{wls}}$ in Section 4.2?**  
   Since the factor $(\check{\tau}_1(X_i)-\check{\tau}_2(X_i))$ can be negative, is this really intended as a weighted least-squares loss in the optimization sense? If yes, please state conditions under which the objective is bounded below and the minimizer exists. If not, please present it as a moment-based estimating objective rather than WLS.

2. **Please provide a cleaned-up, notation-consistent version of the Taylor expansion and theorem statements in Section 4.1 to 4.4.**  
   In particular, what are the exact expansion point and the exact definitions of $\hat{\gamma}, \check{\gamma}, \bar{\gamma}$ and their outcome-model analogues? A line-by-line correction of **Equation (3)**, **Equation (4)**, **Theorem 1**, and **Proposition 2** would materially increase my confidence.

3. **What empirical behavior do you observe under genuine propensity-model misspecification, rather than noisy perturbations of the true propensity score?**  
   For example, what happens if the treatment head is intentionally underparameterized, if key treatment predictors are omitted from $\Phi(X)$, or if the propensity model class is wrong? This would directly test the most important assumption in the theory.

4. **Can you compare the Section 5 aggregate HTE estimator to simpler ensemble baselines?**  
   Obvious baselines would include: direct averaging of the candidate $\hat{\tau}_k$, selecting the top-ranked estimator by relative error and using only that one, weighted averaging based on pairwise relative-error scores, or standard stacking. If the pairwise aggregation still wins, that would strengthen the second contribution considerably.

5. **How are hyperparameters tuned without leaking information from the test set used for evaluation of relative error and HTE performance?**  
   The main paper says tuning details are in the appendix, but the setup would benefit from one explicit sentence in the main text clarifying the validation protocol, especially because the evaluation framework itself operates on the test dataset.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the submission. The paper uses standard benchmark datasets and methodological evaluation in causal inference. Any downstream deployment concerns would be the usual ones for HTE systems in high-stakes settings, but the paper itself is methodological and does not raise a specific ethics red flag.

## Soundness Rating
3: good. The core direction is technically meaningful and supported by a combination of theory and experiments, but the main theorem-to-method connection and several mathematical details need clearer and more careful presentation.

## Presentation Rating
2: fair. The paper is readable at a high level, but the notation inconsistencies, equation issues, and table-formatting errors are substantial enough that they interfere with careful verification.

## Contribution Rating
3: good. The paper addresses an important evaluation problem for HTE, offers a meaningful relaxation relative to prior relative-error inference, and includes a potentially useful neural nuisance-learning framework, although the second contribution on HTE aggregation is less convincing than the first.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The problem is important, the main idea is interesting, and the empirical results are promising enough that I can see this being useful to the community. However, the paper needs a tighter mathematical presentation, a more careful treatment of the weighted loss, and stronger evidence around propensity-model misspecification and the Section 5 aggregation claim.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main mathematical and empirical claims carefully, although the notation issues make some proof details harder to verify than they should be.