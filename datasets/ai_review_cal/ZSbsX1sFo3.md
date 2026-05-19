- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3
I have thoroughly verified all claims against the paper. Let me now produce the consolidated review.

## Summary

This paper proposes UNA (UNified Alignment), a framework that handles pairwise, binary, and scalar-score feedback by minimizing the difference between an implicit reward (derived from the policy as β log(π_θ/π_ref)) and an explicit reward (from human labels, reward models, or LLMs). The key claimed contributions are: (1) a "generalized implicit reward function" r(x,y)=β log(π_θ/π_ref)+f(x)+c that extends DPO's mapping, (2) unification of RLHF/PPO, DPO, and KTO into a supervised learning objective, and (3) experimental results showing improvements over baselines.

## Strengths

- **Simplification of RLHF via supervised learning (Section 3.3.4, Table 3–6)**: UNA replaces the PPO stage of RLHF with MSE minimization between implicit and explicit rewards, removing the value model. Training time drops from ~8 hours (RLHF) to ~3.5 hours (UNA) at equal batch sizes on 8×A100 GPUs (Section 4.2). This is a concrete, measurable efficiency gain over standard RLHF, and UNA also yields better or comparable leaderboard scores (e.g., avg 25.91 vs. 25.36 on the new leaderboard).

- **Unified handling of multiple feedback types (Sections 3.3.1–3.3.3)**: The paper explicitly derives loss functions for pairwise data, binary data, and continuous score data within a single conceptual framework: L_UNA = 𝔼[g(r_φ, r_θ)]. While the claim of "unifying" existing methods is overstated (see weaknesses), the framework's ability to accommodate three data types under one objective is a genuine practical contribution.

- **Competitive empirical results on standard benchmarks (Tables 1–2, 5)**: UNA-score (MSE) achieves 30.92 vs. DPO 28.53 and KTO 28.56 on the new Open LLM Leaderboard, and 6.72 vs. DPO 6.10 on MT-Bench. UNA-binary (MSE) also shows consistent improvements over KTO. While confounds exist (see weaknesses), the results are promising and suggest the approach merits further investigation.

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed novelty of the "generalized implicit reward" relative to DPO**: The paper presents r(x,y) = β log(π_θ/π_ref) + f(x) + c as a new theoretical contribution (line 31, contribution 1). But DPO's known mapping (Eq. 6, line 86) is r(x,y) = β log(π_θ/π_ref) + β log Z(x), where Z(x) is a prompt-dependent partition function. The term f(x)+c plays the same role as β log Z(x) + const — it is a reparameterization, not a fundamentally different result. The derivation in Section 3 introduces f(x) as an arbitrary additive term during algebraic manipulation (line 220), then pulls it out of the log-sum inequality. This is algebraically valid, but the claimed "generalization" is that f(x) is unconstrained relative to DPO's specific Z(x). However, the paper never leverages this "generality" — it immediately simplifies to f(x)=c=0 and uses only that simplified form throughout the experiments (Eq. 8, line 108–109). The special case f(x)=c=0, which drops the prompt-dependent normalization term, is presented without justification that it preserves optimality. This makes the framing misleading: the core contribution in practice is the simplified form r = β log(π_θ/π_ref), which is already implicit in DPO's derivation (up to the Z(x) term that cancels in DPO's pairwise loss).

- **Equivalence to DPO is not properly demonstrated (Section 3.3.1)**: The paper claims UNA is "mathematically equivalent to DPO" for pairwise data (lines 35, 162, 410). However, the defined UNA-pair loss (Eq. 14, line 157) is L = -𝔼[r_θ(y_w) - r_θ(y_l)], which is a linear difference. DPO's loss is -𝔼[log σ(r_θ(y_w) - r_θ(y_l))], a logistic loss. The paper then states the equivalence holds "as long as f(x)=log[σ(x)] is applied to the difference" (line 162) — but f(x) was previously defined as a prompt-dependent additive term in the reward function, so this is a notation overload that obscures the argument. The paper is essentially saying "if you replace the UNA-pair loss with the DPO loss, you recover DPO," which does not demonstrate that UNA-pair *as defined* is equivalent to DPO. This is a significant gap in a central claim.

- **Uncontrolled hyperparameter differences confound experimental comparisons**: In the main comparison (Tables 1–2), UNA-score uses a learning rate of 3×10⁻⁵ while DPO and KTO use 5×10⁻⁶ — a 6× difference (lines 267–268). The paper provides no ablation, grid search, or justification showing this choice is fair or that UNA's advantage holds at matched learning rates. For the RLHF comparison (Section 4.2), RLHF uses β=0.05 while UNA uses β=0.03 (line 269), and a *different base model* (Qwen2-1.5B vs. Mistral-7B used in the main experiments) with a *different reward model* (GRM-Gemma-2B). The paper states this is due to "computation availability and LoRA is not supported in PPOv2" (line 269), but this breaks comparability across experimental sections. Without controlled hyperparameters, observed improvements (e.g., 25.91 vs. 25.36 on new leaderboard) could partially reflect optimization tuning rather than algorithmic advantage.

- **Missing score-aware baselines for the score-feedback experiments**: UNA-score uses continuous scores from HelpSteer2 (combined human scores ranging 0–4 normalized to [0,1], line 276). DPO and KTO, used as baselines, only see pairwise preference information from the same dataset and do not have access to these scores. The paper therefore compares a method with *strictly more information* (continuous scores) against methods with *less information* (pairwise preferences). The claimed improvement (30.92 vs. 28.53) is expected and does not demonstrate the superiority of the UNA framework specifically. A proper comparison would include a score-aware baseline such as weighted DPO (where scores serve as weights in the preference loss) or soft-label DPO.

- **No variance, confidence intervals, or statistical significance reported**: All leaderboard results (Tables 1–6) are single point estimates with no error bars, standard deviations over multiple seeds, or statistical tests. Given the modest improvements in many comparisons (e.g., UNA-binary (BCE) 28.93 vs. KTO 28.56 on new leaderboard; UNA 25.91 vs. RLHF 25.36), it is impossible to determine whether these differences are meaningful or within the noise of the evaluation. This is particularly important because leaderboard evaluations are known to have non-trivial variance.

### Minor

- **The "unification" claim is broader than what is demonstrated**: The paper states UNA "unifies RLHF/PPO, DPO and KTO" (abstract, line 6). What UNA provides is a general loss family (minimize difference between implicit and explicit rewards) that can be instantiated differently for each data type. This is a valid unifying *perspective*, but the paper does not show a *single loss function* that recovers DPO and KTO as special cases. For binary data, UNA proposes MSE and BCE losses (Eqs. 15–16) that differ from KTO's reference-point formulation; the paper claims "improvement over KTO" but does not show UNA subsumes KTO's loss as a special case. The unification is conceptual (all methods compare implicit and explicit rewards) rather than mathematical.

- **RLHF comparison uses different, smaller-scale models (Section 4.2)**: The RLHF experiment uses Qwen2-1.5B instead of Mistral-7B (used in the main DPO/KTO comparison). The paper acknowledges this but does not discuss how the "alignment tax" (mentioned in Section 6) might affect the relative performance differently at different scales. Generalizing "UNA outperforms RLHF" from 1.5B-parameter models to the 7B+ scale of the main experiments is unsupported.

- **Derivation's finiteness condition for $f(x)$ is introduced without justification (Section 3)**: On line 259, the paper states $f(x) > \max[r(x,y)]$ is needed for finiteness of $\sum_y \pi_{\text{ref}}(y|x) e^{\frac{1}{\beta}(r(x,y)-f(x))}$. This condition is stated without proof and is tangential to the main derivation. While not invalidating the core result, it reflects a lack of rigor in the theoretical presentation.

### Trivial
None.

## Nice-to-Haves

- An ablation study matching learning rates and β values across methods would substantially strengthen the experimental claims.
- Adding a score-aware baseline (e.g., weighted DPO) for the score-feedback experiments would isolate the benefit of the MSE-minimization objective from the benefit of using continuous scores.
- Reporting results over multiple seeds with standard deviations would clarify whether performance differences are significant.
- Clarifying the relationship between UNA's derivation and DPO's known mapping (including how f(x)+c relates to β log Z(x)) would improve the paper's theoretical framing.

## Removed Points

These points from the inputs were removed with justification:

- **"The mathematical proof contains a non-rigorous step that invalidates the claimed optimality condition"**: The derivation is algebraically valid — introducing f(x) as (r-f)+f and applying the log-sum inequality is standard. The equality condition follows correctly. The critic's claim of "invalidation" is too strong; the issue is overclaimed novelty, not mathematical error.
- **"f(x)=c=0 is not a natural or constrained version" / "drops the necessary prompt-dependent term"**: The paper presents f=c=0 as a "simplification," not a derived consequence. This is a valid critique of framing but does not make the derivation incorrect. It belongs under "overclaimed novelty" above.
- **Claims about missing appendix, incomplete proofs, or formatting artifacts**: Parser issues; these exist in the original submission.
- **"The paper does not compare UNA-RLHF to DPO in the online setting"**: This is out of scope for an RLHF-simplification claim; DPO is an offline method.
- **Generic nitpicks about "undisclosed hyperparameters" beyond what is reported**: The paper reports learning rates, β, LoRA rank, and model choices. Minor implementation details not disclosed do not invalidate results.
- **"UNA-pair loss being 'equivalent to DPO' claim is contradictory"**: While the claim is poorly justified (kept as a major weakness above), it is not contradictory per se — the paper attempts to claim that a transformed version of the UNA loss recovers DPO. The core issue is lack of clarity, not impossibility.
- **Strength Finder's claim that equivalence to DPO is "mathematically proven"**: The paper attempts this but does so unclearly. The strength is dropped because it conflicts with the verified weakness.
- **Strength Finder's claim about the "generalized implicit reward derivation" being a "self-contained proof"**: The derivation is indeed self-contained but the novelty is overstated relative to DPO. This strength is weakened to reflect the overclaim.

## Novel Insights

None beyond the paper's own contributions. The key insight — that LLM alignment with different feedback types can be cast as minimizing the difference between an implicit reward (derived from policy ratios) and an explicit reward — is a useful organizational perspective, but both the reward mapping (derived from the KL-constrained RLHF objective) and the supervised learning simplification (replacing PPO with a regression loss) are well-precedented in the DPO and related literature. The paper's main novel claim — that its derivation strictly generalizes DPO's — does not withstand close scrutiny, as f(x)+c is a reparameterization of DPO's β log Z(x).

## Suggestions

1. **Reframe the theoretical contribution honestly**: Acknowledge that the "generalized" implicit reward r = β log(π_θ/π_ref) + f(x) + c is structurally equivalent to DPO's mapping (with f(x)+c playing the role of β log Z(x)), and that the contribution lies in using this reward formulation in a supervised regression framework rather than claiming it is a fundamentally new mapping.

2. **Run controlled ablations**: Match learning rates and β across UNA and baselines, or provide a grid search showing the advantage is robust. For the score-based experiments, include weighted DPO or a similarly informed baseline.

3. **Clarify the DPO equivalence**: Either drop the claim that UNA-pair is equivalent to DPO (it is a different loss), or show the precise g function in the general UNA framework that recovers DPO's logistic loss, with clear notation.

4. **Report variance**: Add results over multiple seeds (at least 3) with standard deviations for all leaderboard metrics, or justify why single runs are sufficient.
