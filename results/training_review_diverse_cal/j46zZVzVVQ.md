Now I have a thorough understanding of the paper and the reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes Preference Control RL (PCRL), a framework for training a single meta-policy conditioned on user preferences to achieve controllable trade-offs on the Pareto front of multi-objective RL problems. The main methodological contribution is the PreCo algorithm, which integrates a novel similarity function (Definition 4.1) into a min-norm gradient manipulation step to produce update directions that simultaneously ascend toward Pareto optimality and align with user-specified preferences. Experiments across discrete (Fruit-Tree, MO-Reacher) and continuous (MO-Ant, MO-Hopper) environments demonstrate that PCRL with PreCo outperforms baselines (LS, EPO, CAGrad, SDMGrad) on both Hypervolume (Pareto coverage) and Cosine Similarity (controllability), especially as the number of objectives increases.

## Strengths

1. **Novelty of the similarity-based preference control approach**: The paper introduces a custom similarity function Ψ(p, v) = –½‖max_i(v_i/p_i) p – v‖² (Definition 4.1) whose gradient directs optimization toward the least-satisfied objectives relative to the preference. This is a principled departure from linear scalarization, and the paper's analysis explains why LS fails for preference control even on convex Pareto fronts (Figure 1). The value is empirically demonstrated: PreCo maintains HV=1.00 and CS=0.83 at 6 objectives in Fruit-Tree, while LS collapses to HV=0.00 and CS=0.33 (Table 1).

2. **Clear empirical demonstration of preference-specific controllability**: The MO-Reacher experiment (Figures 7–8) provides a compelling visual and quantitative verification that PreCo and EPO learn genuinely preference-conditioned policies — their state-coverage heatmaps shift smoothly as the input preference changes — whereas LS, SDMGrad, and CAGrad produce identical coverage regardless of preference input, performing no better than a random agent on CS. This directly validates the core claim that a single meta-policy can produce user-directed trade-offs.

3. **Versatility across RL frameworks and action spaces**: The paper demonstrates PCRL with TD3 (continuous control, MO-Ant, MO-Hopper) and PPO-clip (discrete actions, Fruit-Tree, MO-Reacher), showing the scheme is not tied to a specific RL algorithm and supporting its claim of broad applicability (Section 3.1, Section 5).

4. **Practical design choice for min-norm computation**: Solving the min-norm problem at the policy level (∇_{π_p} v̂^{π_p}, size m×B) rather than the parameter level (∇_θ v̂^{π_p}, size m×M where M ≫ B) is a sensible efficiency consideration for scaling to large models (Section 3.2). While no runtime benchmarks are provided, the reasoning is sound.

## Weaknesses

### Fatal
None.

### Major

1. **The PreCo algorithm is underspecified for exact reproducibility.** The core update equation (Equation 6) states w* ∈ argmin_w ‖d‖ with d ≜ ∇_{π_p}^T v̂^{π_p} w + λ ∇_{π_p} Ψ(p, v̂^{π_p}), but the paper does not state:
   - What constraints (if any) are imposed on w. MGDA-style min-norm problems typically require w to lie on the simplex (w_i ≥ 0, Σ w_i = 1), but this is never specified.
   - How d* is applied to update the policy parameters (e.g., θ ← θ + η·d*? Through a surrogate loss?).
   - A step-by-step pseudocode (Algorithm 1 is referenced but not present in the visible main text).
   While an expert in MOO may infer the intended procedure, the lack of precision is a barrier to reproducibility and independent verification. This is the single most important issue to fix.

2. **The λ hyperparameter (similarity gradient weight) is never discussed.** λ controls the trade-off between the Pareto-ascent direction (∇_{π_p}^T v̂^{π_p} w) and the similarity-seeking direction (∇_{π_p} Ψ). The paper never states how λ is set — whether it is tuned per environment, held constant across all experiments, or annealed during training. This is a critical design choice that directly affects the behavior of PreCo and should be documented.

### Minor

1. **Theoretical results are claimed but not stated in the main text.** Section 4 ("Theoretical Analysis") states that convergence to Pareto stationary points and convergence of the similarity will be proved, but no theorem, lemma, or convergence statement appears in the visible text. Even if proofs are deferred to an appendix (which the parser may have stripped), the main text should articulate what is actually proved — e.g., convergence rate, conditions on the similarity function, or the form of the stationary point. As it stands, the theoretical contribution is not accessible to the reader.

2. **Baseline implementations are described too briefly.** The descriptions of how EPO, CAGrad, and SDMGrad were adapted to the preference-conditioned setting are one sentence each. For example, CAGrad is described as "modif[ied] to be a common ascent direction not is not too far from the similarity gradient" — this is vague and contains a grammatical error. Without more detail (e.g., how similarity constraints are applied in the conditioned setting, how the two modes of EPO are balanced), it is difficult to assess whether the baselines were implemented correctly or were inadvertently disadvantaged.

3. **The computational efficiency argument is unvalidated.** The paper argues that solving the min-norm problem at the policy level (∇_{π_p}) is more efficient than at the parameter level (∇_θ), but provides no runtime, memory, or iteration-cost comparison. This remains a plausible but empirically unsubstantiated claim.

### Trivial

None.

## Nice-to-Haves

- The paper could benefit from ablating λ (similarity gradient weight) to show sensitivity. Even a single figure showing HV and CS across a range of λ values would substantially strengthen the understanding of the method.
- A runtime/memory comparison between policy-level and parameter-level min-norm solving would validate the efficiency claim.
- The MO-Reacher results attribute baseline failures to "high variance from conflicting gradients" but provide no direct evidence (e.g., gradient norm statistics). This explanation is plausible but speculative; supporting data would strengthen it.
- Comparison to envelope-based or distributional MORL methods that also learn single conditioned policies (e.g., Alegre et al. 2023, Xu et al. 2020) is suggested by the reviewer, but the paper's baseline set (LS, EPO, CAGrad, SDMGrad) is defensible and already covers the main MOO gradient-manipulation families. Adding more baselines would broaden but not invalidate the current results.

## Removed Points

- **"Table 1 shows only single numbers with no variance indicated"** — The paper states "We report the mean and standard deviation results of 5 seeds" (line 138). The table and figures are embedded images that the PDF parser cannot render; the original PDF likely contains the claimed statistics. The criticism is based on a parser artifact, not a paper flaw.
- **"Algorithm 1 is referenced but not shown"** — The algorithm was likely in a section that the parser stripped. This is a parser artifact.
- **"Missing appendix, proofs in appendix"** — The hard rule instructs that these should be assumed to exist in the original submission.
- **"Should compare to envelope-based or distributional MORL"** — This is scope creep. The paper's chosen baselines cover the main MOO gradient-manipulation families and are defensible.
- **"The choice of environment could be better motivated"** — The paper provides brief descriptions and the environments are from established MORL benchmarks (Felten et al. 2023). This is sufficient.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the familiar tension between a method paper that makes theoretical claims and a main text that defers those claims. The most novel observation from the reviews is that the similarity function Ψ(p, v) = –½‖max_i(v_i/p_i) p – v‖² naturally handles non-convex Pareto fronts where LS fails — this is a genuine insight that the paper itself articulates and the reviewers correctly recognize as the core contribution.

## Suggestions

1. **State the PreCo algorithm unambiguously**: Provide explicit constraints on w (e.g., w_i ≥ 0, Σ w_i = 1?), specify how d* updates policy parameters (θ ← θ + α·d*?), and include a clear pseudocode block in the main text.
2. **State the λ setting explicitly**: Report the value(s) of λ used in each experiment, and ideally include a sensitivity analysis.
3. **State the main theoretical claim as a theorem in the main text**: Even a one-sentence convergence result (e.g., "Under Assumptions A1–A3, PreCo with stochastic gradients converges to a Pareto stationary point at rate O(1/√T)") would make the theoretical contribution concrete and accessible.
4. **Provide more detail on baseline adaptations**: For each baseline, describe what adaptation was necessary for the preference-conditioned setting, and ideally reference publicly available code.
5. **Consider adding a runtime/memory comparison table** for the policy-level vs. parameter-level min-norm argument to validate the efficiency claim.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>