- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8
Now I have a thorough understanding of the paper. Let me synthesize the final review after carefully cross-checking all claims against the paper text.

---

## Summary

This paper investigates the connection between flatness of the reward landscape in policy parameter space and robustness in reinforcement learning. The authors define ℰ-flat reward maxima, state Proposition 1 linking flatness to action robustness (Δ* ≤ ∥J(θ*)∥ℰ + O(ℰ²)), and provide informal intuition for why flatness should also confer robustness to transition and reward perturbations. Empirically, they augment PPO with Sharpness-Aware Minimization (SAM+PPO) and evaluate it against standard PPO and robust RL baselines (RARL, RNAC) across action noise, mass/friction variations, and reward noise in three MuJoCo environments.

## Strengths

- **Comprehensive evaluation across multiple perturbation types.** The paper tests three distinct forms of robustness — action noise (§5.2, Figure 3), transition dynamics perturbations via mass/friction variations (§5.3, Figures 4–6), and reward noise during training (§5.4, Table 2) — across three continuous control environments. This breadth is a genuine advance over prior work that considered only one type of perturbation.

- **Direct comparison with dedicated robust RL methods.** SAM+PPO is compared with RARL and RNAC (Figures 4–6, Table 1) under the same evaluation protocol. SAM+PPO matches or outperforms these specialized algorithms in several settings, demonstrating that flat-reward optimization can be a competitive alternative to adversarial training approaches.

- **Quantitative flatness metrics.** Table 3 reports the maximum Hessian eigenvalue λ_max and LPF flatness measure for PPO and SAM+PPO, providing numerical evidence that SAM+PPO indeed converges to flatter regions. This goes beyond earlier work that relied solely on visualizations.

## Weaknesses

### Major

- **Proposition 1 is stated without proof and the inequality direction is suspect for a central theoretical claim.** The paper presents Proposition 1 (lines 145–151) as its main theoretical result — arguing that if θ* is an ℰ-flat reward maximum, the policy is Δ*-action robust with Δ* ≤ ∥J(θ*)∥ℰ + O(ℰ²). No derivation is given in the paper body, and the paper does not cite an appendix containing one (grep for "Appendix" and "proof" returns no matches). Moreover, the inequality is an *upper bound* on the action robustness radius. To guarantee that flatness *implies* robustness, what matters is a *lower bound* — the paper should show that the policy is guaranteed to be robust to action perturbations of at least some positive radius. An upper bound only says the robustness radius cannot exceed ∥J∥ℰ, which is the wrong direction to support the paper's thesis. The intended reasoning appears to be that an action perturbation δ corresponds to a parameter perturbation ε ≈ J⁺δ (via the Jacobian pseudo-inverse), yielding a robustness guarantee Δ* ≥ ℰ/∥J⁺∥, which would be a lower bound — this is different from what the paper writes.

- **Definition 1 (ℰ-flat reward maxima) is impractically strong.** It requires the expected return to be *exactly* r* for *all* parameter perturbations within an ℰ-ball. For any non-constant reward function in continuous parameter space, this is essentially impossible unless ℰ=0. The paper later measures flatness via Hessian eigenvalues and LPF metrics, which capture *approximate* flatness, but the theory never bridges this gap. A tolerance-based definition (return within ε of r*) would be more realistic and would connect naturally to the empirical measurements.

- **The SAM perturbation radius ρ, a critical hyperparameter, is not reported.** The perturbation radius ρ in the SAM objective (lines 112–115, 171–173) determines how aggressively flatness is pursued. The paper states that PPO and SAM+PPO use "identical hyperparameters" (line 183) but never discloses the value of ρ for any environment or how it was selected. This makes the experiments fundamentally irreproducible. Without this information, the reader cannot assess whether the reported benefits stem from principled flatness-seeking or from fortunate tuning.

- **No error bars, confidence intervals, or measures of variability anywhere in the results.** Figures 3–6 and Tables 1–3 report only point estimates. While the paper mentions 5 independent trials and 100 evaluation runs per trial (line 183), none of the plots or tables show standard deviations, standard errors, or individual trial data. It is impossible to judge whether any reported difference between methods is statistically significant or within the noise of the estimator.

- **Causality is not established: observed robustness may come from SAM's optimization details, not from flatness per se.** The paper attributes robustness to "flatness" but only compares SAM+PPO (an algorithm that pursues flatness) against standard PPO. SAM modifies the gradient computation (double-backprop through the surrogate objective), which could confer robustness through other mechanisms — implicit regularization, altered effective batch size, or optimization dynamics unrelated to the flatness of the converged solution. Control experiments that vary flatness within a *single* algorithm family (e.g., PPO with varying weight decay, varying SAM ρ, or SWA) are absent. Without such controls, the evidence supports "SAM+PPO is more robust than PPO" but not "flatness causes robustness."

### Minor

- **The transition dynamics experiments (§5.3) test large-scale parameter changes (0.5x to 1.5x mass/friction) rather than small local perturbations.** The theory (Definition 1) concerns local flatness in parameter space, but the mass and friction variations are substantial global changes to the environment dynamics. The paper does not discuss this mismatch or argue why the local theory should extend to such large perturbations. This weakens the claimed connection between theory and experiments, though it also shows the method's practical generalization beyond the theory's strict scope.

- **Remark 1.1 is largely definitional.** It states that the Δ*-action robust policy satisfies the max-min objective for perturbation radius Δ*. This follows directly from Definition 2 and does not provide new insight. It does not connect the flatness-induced robustness to a *fixed, a priori* perturbation radius as in standard Action Robust MDP formulations, because Δ* itself depends on the policy parameters.

- **The reward-robustness experiment (§5.4) only compares PPO vs. SAM+PPO, omitting RARL and RNAC.** Table 2 would be more informative with all four methods under reward noise. The inclusion of two of the three baselines is inconsistent across experiments.

- **Hessian eigenvalue and LPF flatness metrics (Table 3) are reported without variance or across multiple runs.** The Hessian's maximum eigenvalue is known to be unstable in high dimensions. Reporting a single number without any measure of variability or confirmation across seeds provides weak evidence.

### Trivial

- Figure 7 (reward surface visualizations) plots surfaces along two random directions in a high-dimensional space — a known partial view. The claim that the SAM+PPO surface "is noticeably flatter" is subjective and not quantified in the figure.

## Nice-to-Haves

- **Statistical rigor:** Adding shaded regions (e.g., ±1 standard error) to Figures 3–6 and standard deviations to Tables 1–3 would substantially strengthen the empirical claims. Using more than 5 random seeds (10+ is standard for RL benchmarks) would also help.
- **A control experiment that varies flatness within the same algorithm:** For example, training PPO with explicit flatness regularization (e.g., varying ρ in SAM or using SWA) and then measuring whether flatness metrics predicted robustness across policies from the *same* algorithm family. This would directly support the causal claim.
- **A discussion of limitations:** When might flatness *hurt* performance? Tasks requiring precise, brittle actions (e.g., fine manipulation) could suffer from overly flat policies.
- **Deriving the proposition correctly:** A corrected Proposition 1 should provide a *lower bound* on the guaranteed action robustness radius in terms of ℰ and the minimum singular value of J (or a Lipschitz constant of the return w.r.t. parameters), not an upper bound.

## Removed Points

These points were raised in the reviews but removed or downgraded for the reasons given:

- *"Remark 1.2 only provides informal intuition"* — The paper explicitly labels Remark 1.2 as informal. Criticizing it for being informal when it is described as such is not a valid weakness.
- *"The 2D navigation example only illustrates correlation, not proof"* — This example is presented as an intuitive illustration in the introduction, not as a proof. The criticism misreads the rhetorical purpose.
- *"Definition 1 requires exact equality which is impossible"* — Kept as Major, not removed. It is a valid weakness: the definition is impractically strong. However, the claim that it's "impossible unless ℰ=0" is too strong since trivial constant return functions would satisfy it; but for any realistic RL setting it is indeed unrealistic. This is a genuine issue.
- *"The Jacobian of mean action may not capture stochastic policy effects"* — This is technically true but the paper's framework focuses on deterministic components of the action; stochastic policies are common in RL and this limitation deserves acknowledgment. Kept within the broader Major weakness about the theory's gap.
- *"Missing related works"* — Removed per instructions: I cannot verify existence of external sources.
- *"Reproducibility nitpicks about undisclosed hyperparameters"* — The SAM ρ is not a trivial hyperparameter; it is central to the method. Kept as Major.
- *"The reward noise experiment trains under noisy rewards, not test-time robustness"* — The paper explicitly acknowledges this design choice (lines 232–233). The criticism is noted but does not rise to a weakness since the paper is transparent about what the experiment measures.
- *"Missing appendix/proofs"* — The paper body does not reference an appendix, and the proof is simply absent from the submission as provided. This is not a parser-stripping issue but a genuine gap in the paper itself. Kept within the Major weakness about Proposition 1.
- *"The claim that SAM+PPO outperforms PPO on HalfCheetah action noise is overstated"* — Looking at Figure 3(a), the lines do appear close, but without error bars this cannot be evaluated. The underlying criticism about overclaiming without statistical support is valid and is captured in the error-bars weakness.

## Novel Insights

None beyond the paper's own contributions. The idea that flat reward landscapes may connect to robustness in RL is interesting and the paper offers preliminary evidence, but the reviews do not surface any insight that the authors themselves did not already articulate.

## Suggestions

1. **Reformulate the theory with a practical definition of flatness.** Replace Definition 1's exact equality with a tolerance-based condition (e.g., |E[return] - r*| ≤ ε for all ∥δθ∥ ≤ ℰ). Provide a complete proof, and state the correct inequality — a lower bound on the guaranteed action robustness radius in terms of ℰ and appropriate Jacobian/Lipschitz constants. Connect this to measurable quantities like the Hessian's maximum eigenvalue.

2. **Report the SAM perturbation radius ρ** for each environment and describe the tuning procedure. This is essential for reproducibility.

3. **Add error bars** to all figures and tables. Even simple ±1 standard error bars would dramatically improve the paper's credibility.

4. **Include control experiments** that isolate flatness from the SAM optimizer. For instance, train PPO with explicit flatness regularization (varying SAM ρ, or using SWA) and measure whether flatness metric values predict robustness within that single algorithm family.

5. **Acknowledge the limitations** of the theory and experiments — the theory uses an idealized definition that does not match the experimental setup, and the experiments test large global changes while the theory considers local perturbations.
