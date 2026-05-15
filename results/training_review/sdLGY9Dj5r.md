Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes ZO-PoG, a framework for black-box prompt learning that *alternates* between two optimization stages: policy-gradient-based discrete prompt optimization (using Gumbel-Softmax reparameterization) and zeroth-order continuous prompt optimization in a low-dimensional subspace. The core claim is that jointly optimizing both the discrete token initialization and the continuous embedding perturbation yields better task adaptation than optimizing either alone. The paper provides a convergence analysis showing sub-linear rate and reports experiments on five GLUE tasks with three backbone models (RoBERTa-large, GPT2-XL, Llama3).

---

## Strengths

1. **Novel problem framing — first joint discrete-continuous optimization for black-box PTMs.**  
   Prior black-box methods either optimize discrete tokens (BDPL) or continuous embeddings (BBT, SSPT) in isolation. The paper's alternating framework is a natural and well-motivated synthesis, and the paper appears to be the first to formalize and evaluate this combination. This is a genuine conceptual contribution.

2. **Consistent empirical advantage across models and tasks.**  
   Despite concerns about variance reporting (see below), the reported *means* show ZO-PoG outperforming all baselines (BBT, BDPL, SSPT, Manual Prompt) on nearly all 30 model–task–length combinations in Tables 1–3. The improvements are often non-trivial (e.g., +5.17% on WNLI with RoBERTa-large, +3.84% on MNLI with GPT2-XL). The ablation study (Figure 3) further confirms that removing either the discrete or continuous optimization component degrades performance across all backbone models, supporting the claim that the joint design is responsible for the gains.

3. **First convergence analysis for this joint setting.**  
   The paper provides a formal convergence guarantee (Theorem 1) establishing that ZO-PoG achieves an ε-stationary point with query complexity O(√(nκ)/ε³) under standard block-wise smoothness and bounded-variance assumptions. While the rate itself is standard for ZO methods, the analysis is the first to cover the combined discrete-PG + continuous-ZO alternating framework and includes variance bounds for the policy gradient estimator (Proposition 1).

4. **Ablation studies isolate both design choices.**  
   Figure 2 (Gumbel-Softmax vs. direct policy gradient) and Figure 3 (complete method vs. removing each component) provide controlled evidence that both the Gumbel-Softmax reparameterization and the alternating optimization contribute to the reported improvements. These ablations are run across all three backbone models and both prompt lengths.

---

## Weaknesses

### Fatal
*None.* The paper's core claims are conceptually sound and supported by empirical trends. The issues below are major but fixable.

### Major

1. **Critical experimental hyperparameters are undisclosed, preventing reproducibility.**  
   Algorithm 1 lists as inputs: subspace dimension *d*, sample sizes *I₁, I₂*, mini-batch size *B*, learning rates *η_α, η_z*, smoothing parameter *μ*, and temperature *τ*. The Implementation Details section (lines 241–242) specifies only the GPU type, model sources, and few-shot setting — none of these hyperparameter values are reported anywhere in the paper. Without them, the reader cannot reproduce the experiments, assess whether the comparison to baselines is query-budget-fair, or determine the sensitivity of the method to these choices. This is a significant violation of experimental reporting standards.  

2. **Missing variance information undermines statistical assessment of empirical claims.**  
   The table captions read "(mean ± std)" but the accompanying text says "report the mean test accuracy over 3 random seeds" and the tables (embedded as images) appear to contain only single numerical values. 3 random seeds is already a thin basis for statistical confidence, but if standard deviations are genuinely absent from the table cells, then the reader has no way to assess whether improvements of 0.5–2% (common across several tasks) reflect real gains or random variation. The ablation figures (2 and 3) also lack error bars. This directly weakens the paper's central empirical claim. *(Note: I cannot view the table images directly from the text extraction; this assessment is based on the textual description. If standard deviations are indeed present in the original submission, this weakness should be downgraded.)*

### Minor

1. **No sensitivity analysis on key hyperparameters.**  
   The paper does not study how performance varies with subspace dimension *d*, temperature *τ*, or sample sizes *I₁, I₂* — all of which are known to significantly affect discrete prompt optimization and ZO gradient estimation. A sensitivity analysis would strengthen the practical guidance for users.

2. **No analysis of learned discrete prompts.**  
   The paper claims the discrete prompt provides "task-specific alignment," but offers no qualitative analysis (e.g., case studies of learned tokens) to support this interpretation. What tokens does the policy gradient select? Do they form interpretable patterns? This would substantiate the motivation for discrete optimization.

3. **Limited discussion of the convergence analysis's practical limitations.**  
   The theory assumes block-wise Lipschitz smoothness and bounded variance, which are standard but unverified for LLM loss landscapes. The query complexity bound O(√(nκ)/ε³) is standard and does not yield actionable hyperparameter guidance. The paper could benefit from acknowledging these limitations more explicitly.

### Trivial
- The "m" in "selecting *m* instances for each class" (line 241) is later revealed to be 16-shot, but this is never explicitly stated in the Implementation Details section.

---

## Nice-to-Haves
- **Control for query budget:** Compare ZO-PoG to baselines with roughly equal numbers of forward passes, and report total queries per method.
- **Convergence curves** (accuracy vs. iteration/query count) for at least one dataset, to illustrate optimization speed.
- **Comparison to a simpler baseline:** random discrete initialization + ZO optimization (BBT's setting but with ZO gradient instead of CMA-ES), to isolate the benefit of optimizing discrete prompts versus random initialization alone.

---

## Removed Points
These points were raised by reviewers but are removed or downgraded after verification:

- *"The Gumbel-Softmax motivation is unclear and the contribution relative to prior work is overstated."* — The paper's claim is that Gumbel-Softmax "has a positive impact on the overall optimization in ZO-PoG." The ablation (Figure 2) directly tests this by comparing ZO-PoG with vs. without Gumbel-Softmax and shows degradation when removed. This is a valid ablation supporting the stated claim. The reviewer's critique conflates mechanism analysis (why it helps) with the empirical question (whether it helps), which the ablation answers. **Downgraded from major to removed (overstated criticism).**

- *"No comparison to white-box prompt tuning methods."* — Scope creep. The paper explicitly addresses black-box settings. **Removed.**

- *"The convergence analysis does not connect to practice / assumptions not verified for LLMs."* — These limitations are inherent to virtually all theoretical ML work on non-convex optimization. The paper uses standard assumptions. **Downgraded from major to minor (see Minor #3).**

- *"The proof sketch for Proposition 1 is missing."* — Not verifiable from this text extraction; proofs are typically in an appendix that may have been stripped. **Removed per hard rules.**

- *"Does not discuss related work on discrete prompt optimization for white-box settings."* — The reviewer already acknowledges this is "fine given the black-box focus." **Removed.**

- *"3 seeds insufficient for robust conclusions."* — This is subsumed by the missing std weakness above. **Merged.**

- *"Missing comparison to more recent black-box methods."* — The method compared against include SSPT (2024), which is recent. This is a plausible but unsubstantiated complaint without naming specific missing methods. **Removed.**

---

## Novel Insights
None beyond the paper's own contributions. The key observation — that the alternating discrete-continuous optimization yields consistent improvements over optimizing either modality alone — is already the paper's central empirical finding and is well-supported by its ablation studies.

---

## Suggestions
1. **Disclose all experimental hyperparameters** in a dedicated table: subspace dimension *d*, *I₁*, *I₂*, *B*, *η_α*, *η_z*, *μ*, *τ*, the total query budget per method, and the number of optimization iterations *T*.
2. **Add standard deviations** to all result tables (if they are genuinely missing), or clarify in the caption if they are already present in the image-based tables. Report results over at least 5 random seeds.
3. **Add a sensitivity analysis** for at least 2–3 key hyperparameters (e.g., subspacedimension *d*, temperature *τ*, and discrete sample size *I₁*) on one representative dataset+model combination.
4. **Include qualitative examples** of learned discrete prompts to substantiate the "task-specific alignment" claim.

---

## Score and Decision

The paper proposes a well-motivated and novel framework for black-box prompt learning, provides a first-of-its-kind convergence guarantee, and demonstrates consistent empirical improvements across diverse settings. However, the experimental presentation has significant gaps: critical hyperparameters are omitted, variance information is likely absent from the main results, and the statistical basis for the empirical claims is thin. These issues are fixable but, in the current form, prevent reproducibility and full evaluation of the reported improvements.

**Originality:** Good — the alternating discrete-continuous formulation is a genuine novel contribution for the black-box setting.  
**Importance of research question:** High — improving prompt learning under black-box constraints is practically relevant.  
**Claims supported:** Partially — the trends are consistent but lack statistical grounding and reproducibility details.  
**Soundness of experiments:** Moderate — experiment design is reasonable but reporting is incomplete.  
**Clarity of writing:** Adequate — the method description is clear; the Implementation Details section is too sparse.  
**Value to community:** Moderate — the framework and convergence analysis are useful contributions, but the incomplete reporting limits immediate impact.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>