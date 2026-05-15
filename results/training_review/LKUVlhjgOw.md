Here is my final consolidated review:

---

## Summary

This paper proposes a safety filtering framework for PDE boundary control when the underlying PDE dynamics are unknown. The approach combines a neural boundary control barrier function (BCBF) with a neural operator that maps boundary control input trajectories to boundary output trajectories. By differentiating through the neural operator, the BCBF condition becomes affine in the control derivative, enabling a quadratic-programming-based safety filter for pre-trained model-free RL controllers. Experiments on hyperbolic, parabolic, and Navier-Stokes PDE environments show improvements in feasible rate and average feasible steps over vanilla RL baselines.

## Strengths

- **Problem framing fills a clear gap.** The paper correctly identifies that safe PDE boundary control with unknown dynamics is an important and underexplored problem. Existing safe PDE control methods (backstepping-based) require analytical knowledge of the PDE, while ODE CBF methods do not transfer due to the non-Markovian nature of PDE boundary dynamics. The introduction of "boundary feasibility" (Definition 2.1) as a trajectory-wise finite-time constraint is a principled adaptation of forward invariance to the PDE setting.

- **Novel use of neural operators as transfer functions for safety filtering.** Rather than using neural operators to approximate PDE solutions, the paper uses them to directly model the mapping from boundary input trajectory to boundary output trajectory. The derivation showing that $d\mathcal{G}_\theta(U)(t)/dt = \Lambda_\theta(t)\dot{U}(t) + \mu_\theta(t)$ (Equation 11) is non-trivial and enables the QP-based safety filter. This is a genuinely novel technical contribution.

- **Consistent empirical improvements across diverse PDE environments.** The method is evaluated on three distinct PDE types (1D hyperbolic, 1D parabolic, 2D Navier-Stokes) with two RL baselines (PPO, SAC), and results across 100-episode evaluations consistently show improved feasible rates and feasible steps. Ablation studies on the threshold $\eta$, finite-time vs. asymptotic convergence, and different neural operator architectures (FNO vs. MNO) provide practical insight into design choices.

## Weaknesses

### Fatal
None.

### Major

- **The "Guaranteed" framing overpromises relative to what is delivered.** The paper's title and abstract claim a "guaranteed" framework. Theorem 3.2 provides a guarantee only under the assumption of *no model mismatch* between the neural operator and the true PDE dynamics. The experiments explicitly use a threshold $\eta>0$ as a "workaround" for model mismatch, acknowledge that "the safety filter is disabled when $\eta=0$," and report feasible rates well below 100%. The paper is transparent about this limitation (Section 3.3, line 142, and Conclusion), but the title and abstract do not reflect this caveat, creating a misleading first impression. This is a framing problem that should be corrected (e.g., "Data-Driven Neural PDE Boundary Control with Neural Barrier Function" or "Toward Guaranteed...").

- **The neural operator's predictive accuracy is never evaluated.** The entire pipeline rests on the neural operator $\mathcal{G}_\theta$ providing a reasonable approximation of the true PDE input-output mapping — the QP filter uses the operator's predicted $Y(t)$ and its derivative to decide whether an action is safe. The paper reports no quantitative measure of the operator's prediction error (e.g., MSE or relative $L_2$ error on held-out test trajectories) for any environment. Without this, it is unclear whether the improvements in feasible rate come from the framework working as intended or from some incidental correlation (e.g., the QP simply constraining $\dot{U}$ to small values). This is a significant evidential gap that weakens the interpretation of the experimental results. At minimum, a table of prediction errors should be reported, and a trajectory-level visualization of predicted vs. true $Y(t)$ would help attribute successes and failures.

### Minor

- **The acausal nature of the neural operator is not adequately addressed.** The neural operator defined in Equation (5) integrates over the full temporal domain $\mathcal{T}=[0,T]$, meaning $v_{l+1}(t)$ depends on $v_l(s)$ for *all* $s\in\mathcal{T}$. Consequently, the terms $\mu_\theta(t)$ in Equation (11) (which involve $\int_{\mathcal{T}}\partial\kappa^{(l)}(t,s)/\partial t\cdot v_l(s)ds$) depend on the full input trajectory, including future times. The paper describes iterative filtering at each time step, but does not explain how these acausal integrals are computed when future inputs are yet to be filtered. The paper acknowledges that "the computation of QP is not yet real-time" (line 142), which clarifies this is an offline trajectory-level procedure. However, the exposition in Section 3.3 and Algorithm 1 is insufficiently precise about how the full-trajectory dependency is resolved during iterative filtering. A clearer explanation is needed: does the algorithm use the unfiltered nominal trajectory $U_{\text{nominal}}(s)$ for $s>t$ as a placeholder during the integral computation, or is the entire procedure performed as a single optimization over the full horizon?

- **The threshold $\eta$ ablation is only shown for one environment.** Figure 2 (ablation on $\eta$) is presented only for the hyperbolic PDE with PPO. Since the trade-off between constraint satisfaction and reward likely varies across PDE types, showing similar analysis for the parabolic and Navier-Stokes environments would strengthen the work.

- **No training/validation split information is reported.** The paper states 50k trajectory pairs are collected, but does not specify how these are split into training, validation, and test sets, nor whether hyperparameters were selected based on validation performance.

### Trivial
- The paper would benefit from more prominently stating that the current implementation is offline (not real-time), to avoid misleading readers about the deployment setting.

## Nice-to-Haves
- A confusion matrix showing whether BCBF condition violations correspond to actual feasibility failures would help diagnose how well-calibrated the BCBF is.
- A robustness experiment where neural operator accuracy is artificially degraded (e.g., by training on less data) and the impact on feasible rate is measured would directly test whether the framework's performance depends on operator quality.

## Removed Points

These points were removed from the review because they are factually incorrect, misread the paper, or are pure formatting/style nitpicks. They are documented here for completeness but should be treated with caution:

1. **C_α,T inconsistency claim (Harsh Critic, item under "Several critical details are missing"):** The critic claimed that $C_{\alpha,T}=0.02$ with $\alpha=10^{-5}, T=50$ is mathematically impossible and would require $\alpha\approx0.04$. This is factually wrong. Verifying: $C = 10^{-5}/(e^{0.0005}-1) \approx 0.00001/0.000500125 \approx 0.02$. The paper's math is correct. **Removed per hard rule (factually wrong criticism).**

2. **Claim that the QP filter "cannot be executed" and is "infeasible" (Harsh Critic, Critical Issue 1):** The critic argued that the acausal neural operator makes the QP filter infeasible. The paper explicitly states the QP is not real-time and uses an offline iterative filtering procedure where the full trajectory is available. While the paper should explain the acausality handling more clearly, calling the method "infeasible" is an overstatement. **Removed per hard rule (misunderstands the paper — the method is feasible as an offline filter; the paper acknowledges the non-real-time nature).**

3. **Feasible rate numbers (58%, 42%) cited by the Harsh Critic:** The critic claimed Table 1 shows PPO+φ(t,Y) achieves 58% and SAC+φ(t,Y) achieves 42% feasible rate. These numbers do not match the paper's narrative and could not be verified from the parseable text. **Removed as unverifiable and likely misread.**

4. **Formatting/style nitpicks:** Any critiques about typos, grammar, or formatting artifacts. **Removed per hard rule (parser artifacts, not author errors).**

5. **Criticism that the paper ignores existing backstepping methods with neural operators (Bhan et al. 2023; Krstić et al. 2024):** The paper explicitly cites these works and distinguishes its contribution (safety filtering via learned transfer function vs. learning backstepping kernels). **Removed per hard rule (strawman — the paper already addressed this).**

6. **Missing related work complaints:** Per instructions, missing related works should not be mentioned as we cannot independently verify their existence.

## Novel Insights

Beyond the paper's own contributions, the reviewers' debate surfaces an important tension: the paper uses acausal neural operators (standard FNO/MNO architectures with global integral kernels) for what is fundamentally a time-sequential decision-making problem. The reviewers correctly identify that the integral over the full temporal domain creates a dependency on future inputs, but this does not necessarily invalidate the method — it means the filtering must operate on full trajectories, not in an online Markovian fashion. This trade-off between expressiveness (global integral kernels capture long-range dependencies) and causality (online deployment) is inherent in the approach. A genuinely causal variant (e.g., causal temporal convolution or recurrent neural operator) would limit the model's ability to capture the non-Markovian structure that motivates the use of neural operators in the first place. This suggests that the fundamental challenge is not just building a safety filter for PDEs, but designing neural operator architectures that are both causally evaluable and expressive enough for safe control — a direction the paper could explore in future work.

## Suggestions

1. **Revise the title and abstract** to reflect that the theoretical guarantee assumes no model mismatch, and the empirical implementation is a relaxed heuristic. Even a small change (e.g., "Toward Guaranteed...") would resolve the mismatch between the rhetoric and the experimental results.

2. **Report neural operator prediction error** (MSE, relative $L_2$) on held-out test trajectories for all three environments, along with trajectory-level visualizations of predicted vs. true $Y(t)$ for both successful and failed episodes.

3. **Add a clear explanation of how the acausal integral** $\int_{\mathcal{T}} \partial\kappa^{(l)}(t,s)/\partial t \cdot v_l(s) ds$ is computed during iterative filtering. If the nominal (unfiltered) trajectory is used as a placeholder for future time steps, state this explicitly in Algorithm 1.

4. **Include an ablation of $\eta$ for the parabolic and Navier-Stokes environments**, or at minimum justify why the hyperbolic case suffices to establish the trend.

5. **Add clear notation** that $\Lambda_\theta(t)$ and $\mu_\theta(t)$ depend on the entire input trajectory $U$, not just time $t$, to avoid misleading readers.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>