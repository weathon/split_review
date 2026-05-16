Here is my consolidated review after cross-checking every claim against the paper.

---

## Summary

ActSafe proposes a model-based RL algorithm for safe exploration that combines pessimistic safety evaluation (using epistemic uncertainty to define a safe policy set) with optimistic intrinsic exploration (using model uncertainty as a reward bonus). The paper proves safety and finite-sample complexity guarantees under RKHS assumptions (Theorem 1) and presents a practical variant that scales to high-dimensional visual control tasks using RSSM dynamics models with ensemble uncertainty. Experiments cover GP-based state tasks and vision-based Safety Gym / Real World RL benchmarks.

## Strengths

1. **First finite-sample safety and optimality guarantees for model-based safe RL in continuous state-action spaces.** Theorem 1 proves that ActSafe (the idealized version) is safe throughout learning and converges to an $\epsilon$-optimal policy in finite episodes. The paper carefully scopes this claim to *model-based* RL, distinguishing it from prior model-free safe-BO approaches (Sukhija et al., Hübotter et al.) that operate on low-dimensional policy parameters — these are properly cited and discussed in §2.

2. **Intuitive and well-motivated two-stage design with empirical support.** The two-stage framework (intrinsic exploration for safe-set expansion, then extrinsic exploitation) is clearly motivated by the exploration–expansion dilemma (§4.1). The GP experiments (§5.1) demonstrate that the pessimism component is necessary for safety, and the hard-exploration experiments (§5.2, Figures 5–6) show that intrinsic exploration is necessary for reaching good policies — together validating both design choices.

3. **Practical instantiation that bridges theory and deep RL.** The paper identifies three key principles from the theory (§4.4: intrinsic rewards for expansion, pessimism for safety, restricted policy selection) and maps them to a tractable constrained optimization problem solvable via LBSGD. This is a non-trivial engineering bridge, and the results on visual control tasks show meaningful progress toward scaling safe exploration.

## Weaknesses

### Fatal
None.

### Major

1. **The main vision-based experiments confound algorithmic contribution with offline-data initialization.** The paper states (§5.2, p. 11) that ActSafe is initialized with "offline-collected data of 200K environment steps, collected with a random policy" and that learning curves start at 200K steps. The baselines (LAMBDA, BSRP-Lag, CPO) are not described as also receiving this data, and the paper's learning curves (Figure 3) do not separate the effect of the warm-start from the effect of the proposed algorithm. Since the paper's central empirical claim is that ActSafe "significantly reduces constraint violation" in visual control, this confound weakens the interpretability of the main results. The paper does reference additional experiments "without offline data" in the appendix, but these are not part of the main comparison. The authors should either match the baselines' initialization or run ActSafe from scratch.

2. **The claimed inclusion $\widehat{\gS}_n \subseteq \gS_n$ is not rigorously justified, though the practical algorithm's safety does not depend on it.** In §4.4, the paper writes "Note that $\widehat{\gS}_n \subseteq \gS_n$, making it a conservative estimate of $\gS_n$." The theoretical safe set $\mathcal{S}_n$ (Definition 3) is defined recursively via an expansion operator that requires proximity to an already-safe policy, whereas $\widehat{\gS}_n$ is defined purely by a direct pessimistic cost bound. The claim that every policy satisfying $\max_{f'\in Q_n} J_c(\pi, f') \leq d$ is necessarily in $\mathcal{S}_n$ does not obviously follow from the definitions and is not argued. **However**, this does **not** invalidate the practical algorithm's safety guarantee: the constraint in the practical optimization problem (Eq. 9) directly enforces $\max_{f'\in Q_n} J_c(\pi, f') \leq d$, and since $f^* \in Q_n$ with high probability (well-calibrated model), $J_c(\pi, f^*) \leq d$ follows directly. The issue is a presentation/justification gap, not a safety flaw. The paper should either prove the inclusion or drop the claim and make the direct safety argument explicit for the practical variant.

### Minor

1. **The criterion for $n^*$ (when to switch from intrinsic to extrinsic exploration) is not specified in the main paper.** The vertical dashed line in Figure 3 is not explained, and it is unclear whether $n^*$ is derived from the theoretical bound (which depends on unknown constants) or set heuristically. The paper should state the criterion used.

2. **The Greedy baseline's model class is underspecified.** In the hard-exploration experiments (§5.2), the Greedy baseline "collects trajectories only based on the sparse extrinsic reward" — it is not stated whether this uses the same learned dynamics model (without the intrinsic term) or a different method. This matters for interpreting whether the gap is due to the intrinsic reward or the model class.

3. **Unknown Lipschitz constants in the theoretical safe set are not discussed as a limitation.** The theoretical expansion operator $D(\pi,\pi')$ depends on $L_c$ and $L_f$ (Assumption 1), which are generally unknown in practice. The practical variant sidesteps this, but the paper does not acknowledge this gap between the theoretical and practical algorithms.

### Trivial

- The bound in Equation (5) involves $T^6$ scaling and a term $\sigma_0$ that is not explicitly defined in the main text (the reader must infer it is the prior GP variance from context). The bound's extreme pessimism is not discussed.

## Nice-to-Haves

- Running the vision baselines with the same 200K-step offline initialization, or running ActSafe without offline data as a standalone ablation, would significantly strengthen the empirical contribution.
- A brief discussion of why $\widehat{\gS}_n$ policies are safe (via the well-calibrated model property directly) would cleanly resolve the safe-set justification gap without needing to prove $\widehat{\gS}_n \subseteq \gS_n$.

## Removed Points

These points are flagged to be removed from the review; treat them with caution:

1. **Critic's claim that the safe-set mismatch is a "structural issue" invalidating the practical algorithm's safety guarantee.** *Removed because it is factually wrong: the practical algorithm has a direct safety argument via the well-calibrated model ($f^* \in Q_n \Rightarrow$ satisfying $\max_{f'\in Q_n} J_c(\pi, f') \leq d$ implies $J_c(\pi, f^*) \leq d$), independent of the $\widehat{\gS}_n \subseteq \gS_n$ claim.*

2. **Critic's claim that the "first to show" claim conflicts with Sukhija et al. and Hübotter et al.** *Removed because the paper explicitly scopes its claim to "model-based RL" and describes the cited works as model-free safe-BO methods operating on low-dimensional policy parameters (§2). The distinction is present in the paper.*

3. **Complaint that the MOPO implementation details (ensemble size, etc.) are missing.** *Removed because these details belong in the appendix, which the parser strips.*

4. **Complaint that zero cost in GP experiments is implausible.** *Removed because the cost measures constraint violations (e.g., leaving a safe region), not process noise. A safety-respecting policy can incur zero cost.*

5. **Strength Finder's generic strengths that lack specificity or conflict with verified weaknesses.** *The Strength Finder's strength #4 ("theoretically grounded safe-set expansion that maps to a tractable constrained optimization problem") is partially weakened by the $\widehat{\gS}_n \subseteq \gS_n$ justification gap. However, the general direction remains valid — the paper correctly identifies the key principle that safe-set expansion can be replaced with a direct pessimistic constraint, even if the subset claim is not fully justified.*

## Novel Insights

The most interesting structural observation from this review is that the theoretical safe set (defined via recursive expansion) and the practical safe set (defined via direct pessimistic cost bound) serve different roles: the former is needed for the *proof* of the sample-complexity bound, while the latter is sufficient for the *safety guarantee* in practice because the well-calibrated model directly bounds the true cost. The paper conflates these two through the unjustified $\widehat{\gS}_n \subseteq \gS_n$ claim, but the practical algorithm's safety is actually more straightforward than the paper makes it seem. This suggests that the key to scaling safe exploration is not in faithfully implementing the recursive safe-set expansion, but in maintaining a well-calibrated uncertainty model — a point the paper makes implicitly but could emphasize more strongly.

## Suggestions

1. **In the main paper, explicitly state whether baselines receive the same offline initialization.** If they do not, add an experiment controlling for this (either run ActSafe without offline data, or give baselines the same warm-start). This is critical for the paper's main empirical claim.

2. **Either prove $\widehat{\gS}_n \subseteq \gS_n$ or drop the claim and instead make the direct safety argument:** because $f^* \in Q_n$, any $\pi$ satisfying $\max_{f'\in Q_n} J_c(\pi, f') \leq d$ is safe. This is simpler and doesn't require the recursive safe set.

3. **Specify $n^*$ and the criterion used** (heuristic or theory-based) for all experiments, ideally in the main text.

4. **Clarify the Greedy baseline's model class** — is it the same learned dynamics model without the intrinsic term, or a different approach?

## Score and Decision

The paper presents a well-motivated approach to safe exploration with a clean theoretical contribution and a practical instantiation that shows promise. However, the main empirical evidence for the scalable variant is weakened by an uncontrolled confound (offline-data initialization), which prevents attributing the observed safety gains to the algorithm itself. The safe-set justification gap is a presentational issue rather than a fatal flaw. The paper's strengths — the theoretical guarantees for model-based safe RL, the clear two-stage design, and the non-trivial engineering bridge to deep RL — are real, but the empirical evidence needs strengthening to fully support the claims.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>