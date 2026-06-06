## Summary

PolicyFlow is an on-policy reinforcement learning algorithm that extends PPO-style optimization to continuous normalizing flow (CNF) policies. Its two technical contributions are: (1) an approximation of PPO importance ratios via velocity-field variations along a linear interpolation path, avoiding costly ODE simulation during training; and (2) a "Brownian Regularizer," a heuristic-but-principled entropy regularizer inspired by Brownian motion that shapes the velocity field to promote diverse exploration without explicit likelihood computation. The method is evaluated on MultiGoal, PointMaze, MuJoCo Playground, and IsaacLab.

---

## Strengths

- **Computationally efficient importance ratio approximation.** The key innovation (Eqs. 8–13) rewrites the importance ratio using the terminal shift $\delta_{\varphi_1}$, then approximates it via velocity-field differences $\delta_{v_t}$ evaluated along a linear interpolation path (Eq. 9–10). The result avoids ODE backpropagation during training entirely. Table 2 confirms this is practical: PolicyFlow adds less than 50% overhead over PPO for standard model sizes, and under 2× even for large embedding dimensions (H1, Go2 at 512-dim), validating the computational claim concretely.

- **Brownian Regularizer effectively mitigates mode collapse.** The regularizer (Eq. 15–16) leverages the rectified-flow score–velocity relationship (Eq. 14) to penalize collapse without explicit log-likelihood evaluation. In Fig. 2, the six-panel MultiGoal ablation provides clear evidence: PPO concentrates on a few goals; DPPO and FPO (without regularization) similarly collapse; PolicyFlow with only Gaussian entropy (e) covers more goals; and PolicyFlow with both the Brownian and Gaussian terms (f) achieves the most balanced six-goal coverage. This is strong controlled evidence for the regularizer's specific contribution.

- **Sensitivity analyses confirm theoretical predictions.** The clipping-range ablation (Fig. 4a) reproduces the expected trade-off: smaller $\epsilon$ reduces approximation error but slows learning, while $\epsilon = 0.2$ is a good practical balance — precisely as predicted by the O(ε) error bound in Eq. 11. The interpolation-path comparison (Table 3) shows robustness for locomotion and mild sensitivity on multimodal tasks, with the rectified-flow path performing best.

- **Clear and honest acknowledgment of heuristic design choices.** The paper explicitly states: *"The Brownian regularizer should not be regarded as a theoretically exact derivation"* (Section 4.1 remark), and notes that the score-velocity relationship is borrowed from rectified flows. This scientific transparency is commendable.

---

## Weaknesses

### Fatal
None.

### Major

- **Entropy regularization confound in the MuJoCo Playground comparison.** PolicyFlow is evaluated with both the Brownian regularizer ($w_b = 0.25$) and Gaussian entropy regularization ($w_g = 0.001$), while FPO and DPPO are run without any entropy regularization — a fact the paper itself acknowledges ("the original implementations of FPO and DPPO do not include explicit entropy regularization," Section 5.2). Entropy regularization is a well-established performance booster in RL. This makes it impossible to determine whether PolicyFlow's advantage in Fig. 3 stems from its CNF approximation mechanism or simply from having an additional entropy bonus that FPO and DPPO lack. Neither FPO+entropy nor DPPO+entropy ablation baselines are provided. The paper's conclusion that PolicyFlow is a superior on-policy generative policy algorithm may be correct, but the MuJoCo Playground experiments do not establish this — they only show that a CNF policy *with* an entropy regularizer beats alternatives that lack one. This is the most important gap in the empirical evidence.

- **Overclaiming in IsaacLab results.** Section 5.2 asserts that PolicyFlow "achieves asymptotic performance that consistently matches or surpasses PPO across all tasks." Table 1 shows this is not accurate: on H1, PPO achieves 29.3 ± 0.9 versus PolicyFlow's 27.3 ± 0.2 (p = 0.0069), which is a statistically *significant win for PPO*, not a "match." Similarly, 5 of 8 tasks have p-values between 0.26–0.41 (clearly not significant), meaning the "consistently surpasses" framing is unwarranted. PPO is numerically better in four of eight tasks (Open-Drawer, Quadcopter, H1, Go2). The language should be recalibrated to reflect the actual pattern: significant wins on 2–3 tasks, competitive but not significantly different on the rest, and a loss on H1.

### Minor

- **Theoretical gap: latent-conditional vs. marginal importance ratio.** The PPO surrogate (Eq. 7) uses the ratio $\pi(\mathbf{a}|\mathbf{z}, \mathbf{s})/\bar{\pi}(\mathbf{a}|\mathbf{z}, \mathbf{s})$, which is the likelihood ratio conditional on the sampled latent $\mathbf{z}$. Standard PPO requires the marginal ratio $\pi(\mathbf{a}|\mathbf{s})/\bar{\pi}(\mathbf{a}|\mathbf{s})$. The paper invokes the proxy objective framework of Frans et al. (2025) to justify that bounding divergence between $\pi^*$ and $\hat{\pi}$ suffices. However, the paper does not verify that clipping in the latent-conditional space actually constrains the marginal policy divergence — and because the flow is expressive (one marginal action $\mathbf{a}$ can come from many latents $\mathbf{z}$), the per-$z$ conditional ratio can in principle be a poor proxy for the marginal. This gap in the theoretical motivation is real, though empirical results suggest it does not cause instability in practice.

- **Computational comparison vs. FPO/DPPO is absent.** Table 2 reports only PolicyFlow vs. PPO per-iteration training time. One of the paper's stated motivations is efficiency relative to methods that require full ODE backpropagation (FPO, DPPO). The actual cost comparison against those alternatives — which is directly relevant to the "efficient alternative" framing — is not shown. The JAX vs. PyTorch implementation difference is offered as justification, but this limits the paper's ability to support its efficiency claims against its primary competitors.

### Trivial
None beyond the mentioned presentation adjustments.

---

## Nice-to-Haves

- **Ablation on approximate vs. ground-truth importance ratio.** A direct comparison between the approximate ratio $\rho$ (Eq. 13) and the true ratio (computed by running both ODEs) over training would empirically validate the O(ε) error bound and show how approximation quality evolves. This is strongly recommended as it would substantially sharpen the paper's mechanistic argument.

- **Quantitative MultiGoal coverage metric.** The six-panel heatmap in Fig. 2 is visually compelling, but a quantitative metric (e.g., fraction of trajectories reaching each goal within tolerance, or goal-distribution entropy) would make the mode-collapse comparison more rigorous and citable.

- **Sample-efficiency quantification.** Section 5.2 mentions that "PolicyFlow often converges faster," but no steps-to-threshold table or chart is provided. If faster convergence is genuine, a table of steps-to-fixed-performance would substantiate this claim.

- **Hyperparameter transfer analysis for the regularizer.** The paper notes that $w_b = 0.25$, $w_g = 0.001$ are used across environments, but does not report a sweep or sensitivity study. A brief analysis of how sensitive performance is to the Brownian weight would be practically useful.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **FPO bias characterization without comparative analysis.** The harsh critic argues that the paper critiques FPO's asymmetric bias without proving PolicyFlow does not have its own bias. This is technically true but is a standard practice in related-work framing; the paper does not claim PolicyFlow is bias-free, only that its approximation structure avoids the asymmetry. REMOVED as scope creep.

- **Approximation error not analyzed when velocity changes are non-uniform across t.** The critic suggests a direct numerical validation of the approximation. This is a nice-to-have (moved there) rather than a core weakness, since the appendix contains the formal bound and the clipping-range ablation provides empirical validation.

- **Missing appendix / proofs.** Several specific references to Appendix A (the O(ε) derivation) and Appendix C (hyperparameter tables). These sections are stripped by the parser; they exist in the original. REMOVED per hard rules.

- **Brownian regularizer hyperparameter transfer across environments.** The critic flags this as a weakness. The paper itself acknowledges the heuristic nature and the appendix configuration tables exist but are stripped. Moved to Nice-to-Haves.

- **MultiGoal experiment insufficient without FPO/DPPO+entropy baselines.** The MultiGoal experiment already includes PPO+entropy (Fig. 2a), PolicyFlow without regularizer (Fig. 2e), and PolicyFlow with noise injection (Fig. 2d). The comparison for the MultiGoal experiment is substantially more controlled than the MuJoCo Playground one — the heuristic strength finder claim about "extensive validation" is kept with this qualification.

- **Claim that FPO generally performs worse than PolicyFlow.** The strength finder states FPO performs worse, which is entangled with the entropy regularization confound. The strength is only partial and depends on resolving the confound — dropped from strengths accordingly.

---

## Novel Insights

PolicyFlow's most genuinely novel observation is the velocity-field shift decomposition: because the action distribution is a Gaussian centered at the flow terminal $\varphi_1(\mathbf{z}; \mathbf{s})$, importance ratios reduce to Gaussian ratios over the terminal shift $\delta_{\varphi_1}$, which can be approximated by the velocity-field variation $\delta_{v_t}$ along a cheap linear interpolation — never requiring ODE integration in the backward pass. This is an elegant observation that exploits the Gaussian noise injection (Eq. 5) as a structural bridge between flow-based and standard PPO objectives. The Brownian regularizer is an independently creative contribution: by recognizing that $v_t = -\nabla_x \log p_t$ recovers the heat equation, the authors turn a score-velocity algebraic identity (Eq. 14) into a penalty that can be computed purely from the velocity network without any likelihood evaluation.

---

## Suggestions

1. **Run FPO+entropy and DPPO+entropy baselines on MuJoCo Playground.** This is the single highest-impact fix. Add Gaussian entropy regularization ($w_g = 0.001$) to FPO and DPPO and re-run. If PolicyFlow still wins, the result is decisive and attributable to the CNF mechanism. If it does not, the paper should re-frame its contribution around the Brownian regularizer specifically, since that is what the MultiGoal experiment already strongly supports.

2. **Correct Table 1 language.** Replace "consistently matches or surpasses PPO across all tasks" with an accurate summary: "significantly outperforms PPO on Navigation and G1, and achieves competitive performance on most other tasks, though PPO retains a significant edge on H1."

3. **Add a scatter/error plot of the approximate vs. exact importance ratio.** Even on a single environment at convergence, plotting $\rho_\text{approx}$ vs. $\rho_\text{exact}$ (the latter from a one-time ODE solve) would directly validate the approximation and connect the theoretical O(ε) bound to practice.

4. **Expand computational comparison.** Report FPO and DPPO per-iteration wall-clock time on MuJoCo Playground (same framework if necessary), to support the efficiency claims relative to full-ODE methods.

---

## Score and Decision

**Originality:** The importance ratio approximation is creative and the Brownian regularizer is a novel heuristic with a principled motivation. Both are specific to this paper. Score: 4/5.

**Importance of research question:** Efficiently training expressive generative policies with PPO-style objectives is a meaningful open problem. Score: 4/5.

**Claims supported:** The efficiency claims and Brownian regularizer benefits are well-supported. The comparative performance claims against FPO/DPPO are confounded by entropy regularization, and the IsaacLab "consistently surpasses" claim is overstated. Score: 2/5.

**Soundness of experiments:** Good ablations (Sections 5.3–5.5), but the main comparison in MuJoCo Playground lacks the critical fairness control. Score: 3/5.

**Clarity of writing:** Generally clear, well-organized, and transparent about the method's limitations. Score: 4/5.

**Value to community:** A practical on-policy algorithm for CNF policies with a lightweight entropy mechanism would be broadly useful if the claims are validated. Score: 3/5.

The paper contains genuinely novel ideas and the MultiGoal evidence for the Brownian regularizer is strong. However, the primary comparative experiments (MuJoCo Playground against FPO/DPPO) are confounded, and IsaacLab results are overstated. The theoretical justification for the conditional importance ratio has an unresolved gap. These issues collectively weaken the paper's evidentiary support for its headline claims, though they are fixable with additional ablations.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>