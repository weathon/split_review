Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper formalizes visual offline RL as an ExoPOMDP and identifies, through an information-theoretic lens, why standard latent-dynamics models retain distraction-correlated "superfluous information" in their representations. The authors propose CLEAR, which learns two disentangled representations (agent-centric state and exogenous factors) using a joint ELBO objective with an adversarial inverse-dynamics regularization that encourages action-controllability of the state encoding while suppressing exogenous information. The method is evaluated on DeepMind Control Suite tasks with four levels of distraction, where CLEAR consistently achieves the best or near-best normalized scores and is the only latent-dynamics method that maintains performance invariance as distractions intensify.

## Strengths

- **Principled information-theoretic diagnosis of prior failures**: The paper identifies (Section 2.2) why standard SSM-based objectives (e.g., SLAC) necessarily retain superfluous information in the presence of exogenous variables, providing a clear theoretical motivation for a disentangled two-encoder approach that goes beyond "this is a known problem."

- **Consistent and highest empirical performance across diverse distractions**: CLEAR achieves the best or near-best normalized scores in nearly all environment–distraction combinations in Table 1 (e.g., Cheetah 2×2 Grid: 66.7 vs. next best 54.5; Walker 2×2 Grid: 94.4 vs. next best 60.5). It is the only latent-dynamics method that maintains performance invariance as distraction difficulty increases, directly supporting the claim of distraction-free representations.

- **Demonstration of successful disentanglement and the critical role of regularization**: Qualitative reconstruction results (Figure 4) show CLEAR cleanly separates agent from background, identifying the correct agent among four in the 2×2 Grid. The ablation study (Table 3, Figure 5) shows that without the inverse-dynamics regularization, the model converges to "flipped" or degenerate representations (normalized scores dropping from 95.5 to 38.2 and 59.6), validating the design.

- **Quantitative evidence that representations track ground-truth state**: The linear regression task (Table 2) shows CLEAR's frozen representations achieve low MSE in predicting the true state across environments and distractions (e.g., Cheetah 2×2: 0.34 vs. SLAC 0.67, Iso-Dream 0.51), confirming the state encoder captures control-relevant information without losing fidelity.

- **Thorough comparison against diverse baselines**: The paper evaluates nine baselines spanning latent-dynamics methods (SLAC, TiA, Iso-Dream, Den-MDP, RePo), multi-step inverse-dynamics methods (ACRO, InfoGating), and model-free methods (DrQ-v2), and discusses their specific limitations in Section 4.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Eq. (2) decomposition mixes ground-truth and learned variables without proper justification**. The equation writes I_{θ*}(Ŝ_{t-1}, A_{t-1}; O_t) = I(S_{t-1}, A_{t-1}; S_t) + I_{θ*}(Ŝ_{t-1}, A_{t-1}; O_t | S_t), where the first term uses the ground-truth state S (not the learned representation Ŝ) and does not involve θ. This is not a standard mutual information decomposition — it mixes variables from different spaces (learned and ground-truth) without showing how the two relate. The paper cites Federici et al. (2020) and says it "resembles" the supervised learning decomposition, but no formal connection is established. Since this decomposition is the key motivation for why "superfluous information" exists and why a new method is needed, it should be stated with mathematical precision. The actual method (Eq. 3 onward) does not rely on this equation, so the imprecision does not invalidate the empirical results, but it weakens the paper's theoretical framing.

- **Min-max optimization for J_InvDyn-E (Eq. 7) lacks analysis of training dynamics**. The objective trains an inverse-dynamics predictor q_ψ(a_t | ê_t, ê_{t+1}) to be accurate while the encoder θ tries to make it inaccurate — a sensible adversarial approach to minimize I_θ(A_t; Ê_t, Ê_{t+1}). However, the paper does not discuss optimization schedules (number of inner ψ updates per outer θ update), gradient clipping, learning-rate tuning specific to this term, or convergence behavior. The reconstruction loss in J_ELBO prevents collapse, but the interaction between objectives is unanalyzed. The paper states that implementation details are in Appendices G and H (stripped by the parser), so some specifics may exist, but the broader question of optimization robustness across environments remains unaddressed.

- **Several baselines obtain very low or zero normalized scores** (e.g., Den-MDP, RePo, TiA on Hopper 2×2 Grid). While the paper explains why reward-based regularization methods struggle (Section 4), the dramatic underperformance compared to their established results in other settings raises a question about whether hyperparameters were specifically tuned for this setting. The paper states it used original hyperparameters where possible, which is standard practice, but a sensitivity analysis or additional tuning for these baselines would strengthen the claim that CLEAR's advantage is not partially an artifact of suboptimal baseline configurations.

- **No limitations section**. Important limitations worth acknowledging include: (a) the compositional decoder assumes agent and distraction occupy different spatial regions, which may fail for non-spatial distractions (e.g., color changes, lighting shifts); (b) CLEAR does not achieve full distraction robustness on Hopper, suggesting some types of distractions are harder to disentangle; (c) the method adds training complexity via the adversarial inverse-dynamics network.

### Trivial

- **KL weight values not reported in the main text**. The paper mentions (line 132) using two different constants for the two KL terms in J_ELBO, which "control the amount of information that passes through each encoder and improve performance," but does not report the values or sensitivity to them. These may be in the appendix (stripped by parser), but a brief mention in the main text would help.

## Nice-to-Haves

- The theoretical motivation for equating "superfluous information" with exogenous information could be tightened with a more explicit argument about how the residual term in a proper decomposition of I(Ŝ_{t-1}, A_{t-1}; O_t) relates to the exogenous-factor dynamics p^e(e_{t+1}|e_t).

- The qualitative disentanglement results (Figure 4) could be complemented with quantitative disentanglement metrics (e.g., DCI, MIG, or regression of ê_t onto ground-truth distraction variables) when ground-truth distraction factors are available.

- A brief discussion of why CLEAR's single-step adversarial approach might be preferable to multi-step inverse dynamics (beyond noting ill-posedness) would be helpful.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Consistency with ExoPOMDP" is not formally justified** (from Harsh Critic Critical Issue 1) — The paper uses "consistent with" to mean "structurally aligned with the ExoPOMDP's causal structure," not "provably recovers the true latent variables." The objective in Eq. (3) is derived to encourage the exact properties defined by the ExoPOMDP (independence, action-invariance of E, Markov property for S). This is standard usage and not an overclaim about identifiability. The reviewer reads a stronger technical meaning into "consistent" than the paper intends.

2. **Comparison with multi-step inverse dynamics methods is insufficient** (from Harsh Critic's "Missing Parts") — The paper already addresses this in Section 4 (lines 144-145), noting that multi-step inverse dynamics is "inherently ill-posed since there are multiple actions that can achieve the same transition" and positioning CLEAR's single-step adversarial approach as an alternative regularization. Criticism is already addressed.

## Novel Insights

None beyond the paper's own contributions. The reviews identify no new connection or implication that the paper itself does not already present.

## Suggestions

1. **Fix the mathematical imprecision in Eq. (2)**: Either re-derive the decomposition properly by establishing conditions under which I_{θ*}(Ŝ_{t-1}, A_{t-1}; O_t) can be related to I(S_{t-1}, A_{t-1}; S_t) (e.g., assuming Ŝ is a sufficient statistic), or replace the decomposition with a more qualitative motivation that does not mix ground-truth and learned variables in the same equation.

2. **Add analysis of the min-max optimization in Eq. (7)**: Report the inner/outer optimization schedule, any gradient clipping or learning-rate tuning specific to this term, and provide convergence curves for the adversarial loss across training. This is critical for reproducibility.

3. **Add a limitations section** discussing the spatial-decoder assumption, the Hopper failure case, and the added complexity of the adversarial training.

4. **Report the KL weight constants and their sensitivity** in the main text or explicitly reference the appendix section that contains them.

## Score and Decision

This paper presents a well-motivated method for an important problem in visual offline RL. The theoretical framing (ExoPOMDP + information-theoretic diagnosis of prior methods' failures) provides clear motivation, and the proposed CLEAR method is supported by strong empirical results across multiple environments and distraction types. The ablation study convincingly validates the design choices, and the qualitative analysis confirms the intended disentanglement. The main weaknesses are theoretical imprecision in the motivational decomposition, lack of optimization analysis for the adversarial component, and missing discussion of limitations — all addressable with revisions. These do not undermine the core contribution, which advances the state of the art in distraction-free representation learning for visual offline RL.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>