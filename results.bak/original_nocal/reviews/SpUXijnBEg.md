Now I have all the information needed to write the consolidated review.

---

## Summary

This paper proposes Direct Optimal Action Learning (DOAL), a framework for policy extraction from Q-value functions in offline RL. Instead of backpropagating through the policy's iterative sampling chain (which is expensive for diffusion/flow models), DOAL computes a target action by taking a batch-normalized gradient step from the data action using ∇_a Q(s,a), then trains the policy to imitate this target using efficient behavior-clone losses native to the policy's distribution (e.g., flow matching). DOAL is tested across three Q-value functions (IQL, Q-learning, regularized Q-learning) and three policy classes (Gaussian, flow, diffusion) on OGBench and D4RL Adroit tasks.

## Strengths

1. **Clean, computationally motivated core idea.** Proposition 1 shows that the BRAC policy gradient can be rewritten as the gradient of a squared-error loss w.r.t. a target action, providing a principled connection. DOAL avoids expensive backpropagation through iterative sampling chains by constructing the target action directly. This is a sensible design choice for diffusion/flow policies where BPTT is costly (Figure 2 shows DMFQL requires 18 NN calls vs. 37 for MFQL-BPTT).

2. **Time complexity analysis is thorough and favorable.** Figure 2 (left table) quantifies the exact number of forward/backward calls for each method, and the regression plot shows a clean linear relationship between NN calls and wall-clock time. DOAL variants add minimal overhead (e.g., DMFQL: 18 calls, 37 min vs. MFQL-BPTT: 37 calls, 61 min on antmaze-large).

3. **Versatility across value functions and policy classes.** The paper tests DOAL with IQL, Q-learning, and ReBRAC, combined with Gaussian, flow, and diffusion policies — a broad evaluation that supports the claim of generality. Tables 1 and 2 cover 15 tasks across these combinations.

4. **Identification of n_sample as a critical hyperparameter for MaxQ sampling.** Section 4 formalizes the overestimation bias from large n_sample (Proposition 3) and uses this insight to tune it, yielding strong baselines (e.g., IFQL 329 vs. IQL* 218 on OGBench). This is a practical contribution even though Proposition 3 is a known statistical property.

5. **The batch-normalizing optimizer provides a principled reinterpretation of α.** The δ parameter in Proposition 2 directly controls the expected update magnitude and Table 3 shows δ varies across a narrower range (0.03–0.1) than α (10–1000) on OGBench, making δ easier to search.

## Weaknesses

### Fatal
None.

### Major

1. **Experimental evidence for DOAL's effectiveness is mixed and modest.** The paper's own admission (line 226: "up on closer examination, we find that those [gains] are due to one or two tasks") confirms that the aggregated OGBench improvements in Table 1 (IFQL 329 → DIFQL 359; TrigFlow 361 → DTrigFlow 368) are driven by a handful of tasks, with many individual tasks showing overlapping performance within large standard deviations (often ±20–28 points). On D4RL Adroit tasks, DOAL shows essentially no improvement under IQL (Table 1 totals: IFQL 592, DIFQL 584) or standard Q-learning (Table 2: MFQL 623, DMFQL 614). Improvement is observed only with ReBRAC (MFReBRAC 425 → DMFReBRAC 466 on OGBench). The paper also does not provide statistical significance tests. Given that the paper's central claim is that DOAL is "effective," this evidence is weaker than one would hope.

2. **The hyperparameter simplification claim is overstated.** The DOAL objective (Eq. 16) still contains the α coefficient: L_DOAL(θ) = α · E[BCLoss(π_θ(s), a^{target})]. While the paper mentions in passing that an ablation (Appendix F) finds α=1 works, the main experiments tune α per task (following FQL values from Park et al., 2025c). So in practice, DOAL introduces δ on top of α, not instead of it. Meanwhile, δ still requires per-dataset tuning (δ∈{0.03,0.1,0.3} for OGBench, δ∈{0.0003,0.001,0.003} for D4RL). The claim that δ is "shared" (line 41) is technically across algorithms within the same task, not across tasks. While δ does vary less than α (Table 3), the actual hyperparameter burden is not reduced — it adds a second hyperparameter.

3. **No experimental comparison with strong concurrent methods.** The Related Work (Section 6) discusses FAC, DAC, and BDPO as contemporary methods, but none are included in the experiments. Since the baselines are already strong (tuned n_sample versions of FQL), a direct comparison with these state-of-the-art methods would be needed to establish DOAL's competitiveness.

### Minor

1. **The δ=0 ablation is claimed but not shown.** The paper states that DOAL subsumes the baseline by setting δ=0 (lines 228, 232), which would be a clean verification that the method does not accidentally harm performance. However, this experiment is not included. The paper instead says it "do[es] not include such choice to explicitly show that first order gradient-based policy extraction might not always work" (line 232-233) — this undermines the claim rather than supporting it.

2. **The connection between DOAL and the BRAC objective is heuristic rather than principled.** Proposition 1 derives the BRAC target, but DOAL substitutes the gradient evaluation point from π_θ(s) to the data action a. The paper honestly acknowledges they are "similar but different" (line 139) but provides no theoretical justification for why the DOAL target is preferable or when the approximation is reliable. The D4RL results where DOAL fails under IQL (attributed to "unreliability of IQL learned function gradient" without supporting analysis) underscore that this gap matters. No convergence guarantees, error bounds, or connections to pessimism/conservatism theory are provided.

3. **Proposition 3 (MaxQ sampling bias) is a standard statistical property.** The result that the maximum of noisy Gaussian estimates diverges with more samples is a basic fact about maxima of independent Gaussians. While it motivates tuning n_sample, the paper does not derive any practical heuristic for setting n_sample — it is simply tuned empirically. The proposition's inclusion as a formal result inflates its novelty.

### Trivial
- The paper's title formatting ("Direct Optimal Action Learning") renders inconsistently in the parser but is fine in the original.

## Nice-to-Haves
- Showing the δ=0 ablation run would cleanly verify that DOAL subsumes the baseline without negative side effects.
- Including a sensitivity analysis of δ across tasks (with/without batch normalization) would strengthen the hyperparameter simplicity claim.
- A gradient quality analysis (e.g., fraction of ∇_a Q steps that increase the true Q-value) could test the paper's speculation about IQL gradient reliability on D4RL.
- Testing DOAL with α=1 in the main experiments (not just in the appendix) would substantiate the simplification claim.

## Removed Points

- **"DIOL is a typo for DIQL"** — The paper intentionally names DOAL-IQL as "DIOL" (line 220: "DIOL, DIFQL, and DTrigflow"). This is not an error. REMOVED (factually wrong).

- **"The IQL(Gauss) baseline is too weak to make DIOL comparison informative"** — The DIOL vs. IQL(Gauss) comparison is within the same policy class (Gaussian) and fairly shows DOAL's effect on that class. The cross-policy comparisons (IFQL, TrigFlow) are separate. REMOVED (strawman).

- **"The batch-normalizing rescaling is trivially equivalent to a fixed step size"** — The paper itself acknowledges this (lines 158, 333): "We are not claiming that this batch normalized scheme can find better a^{target}... if the gradient statistics is stable, you can always get the same result by having g(s,a) = C·∇_a Q_φ(s,a)." The paper's claim is that δ varies less than a fixed step size C, not that batch normalization is fundamentally different. REMOVED (paper already addresses this).

- **"No convergence guarantees or error bounds"** — This is a generic demand applicable to most empirical offline RL papers and does not specifically threaten the paper's claims beyond what is already covered above. REMOVED (generic).

- **Strengths removed from Strength Finder:** The claim that DOAL "achieves improved or competitive results" is weakened by verified weaknesses about modest, concentrated gains — retained in modified form under verified results. The claim that "the paper subsumes baselines by setting δ=0" conflicts with the verified weakness that this ablation is not shown. The Strength Finder's "single most important piece of evidence" paragraph is acknowledged but tempered by the mixed results.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension: the core idea is clean and computationally motivated, but the experimental execution reveals a pattern of modest, task-concentrated gains that do not cleanly support the paper's effectiveness claims. No reviewer identified a problem or opportunity the authors had not already partially acknowledged.

## Suggestions

1. Run and report the δ=0 ablation across tasks to verify the claim that DOAL subsumes the baseline.
2. Either remove α from the DOAL objective (set α=1 as the ablation suggests it works) or reframe the hyperparameter contribution to honestly state that DOAL introduces a *second* hyperparameter (δ) that is easier to tune, rather than replacing α.
3. Include comparisons with FAC, DAC, or BDPO on OGBench to establish competitiveness with current state-of-the-art.
4. Add a simple analysis of gradient quality (e.g., correlation between ∇_a Q direction and improvement in true Q) to explain why DOAL fails on D4RL under IQL but works with ReBRAC.
5. Present individual per-task plots with confidence/credible intervals rather than just aggregated totals, to give readers a clearer picture of where DOAL helps and where it hurts.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>