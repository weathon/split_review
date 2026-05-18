Now I have a thorough understanding of the paper and all the claims. Let me synthesize the final review.

## Summary

The paper introduces "reward adaptation" (RA), where pre-learned source behaviors (with their Q* and Q^μ values) are leveraged to speed up target-task learning under a reward function that is a polynomial of source rewards. The proposed method, Q-Manipulation, derives upper/lower bound proxies for the target Q-values from source Q-values, applies reward shaping to tighten these bounds, then prunes actions whose upper bound falls below another action's lower bound before target learning begins. Theorem 2 formally claims that optimal actions are never pruned. Experiments on grid-world and synthetic domains show faster convergence versus Q-learning, Q-Decomposition, and reward-shaping baselines.

## Strengths

1. **Novel problem framing and practical motivation**: Reward adaptation formalizes a realistic setting — reuse pre-trained source behaviors (e.g., "drive fast" and "drive safe") for a combined target (e.g., "drive fast and safe") without re-accessing source domains. This cleanly separates the problem from standard transfer learning and Q-Decomposition.

2. **Guaranteed optimality preservation (under correct bounds)**: Theorem 2's proof logic is sound *if* the bounds in Theorem 1 hold: pruning only occurs when a computed lower bound exceeds another action's computed upper bound, and the proof shows this cannot happen for an optimal action (Lines 154–178). The formal guarantee is stronger than heuristic pruning methods.

3. **Handles non-linear target reward functions**: Unlike Q-Decomposition (restricted to linear combinations), Q-Manipulation handles polynomial combinations (e.g., 𝒟=R₁⁴+R₂³) via Lemmas 2–3 and Theorem 1. Fig. 4 shows substantial speedups on a non-linear target where Q-Decomposition is inapplicable, directly demonstrating the method's distinctive advantage.

4. **Consistent empirical speedups across diverse domains**: Q-M outperforms baselines in all five tested domains, with 7.8%–42.7% action pruning (Table 1) and corresponding faster convergence. The correlation between pruning rate and speedup (e.g., only 7.8% pruning in Frozen Lake yields the smallest improvement) supports the core mechanism.

5. **Reward-shaping formulation to increase pruning**: Lemma 5 and the LP formulation (Eq. 11) provide a principled way to tighten bounds without violating optimality, moving the upper and lower bounds in opposite directions.

## Weaknesses

### Fatal
None. The paper's core claims are not invalidated; however, a significant theoretical gap exists (see Major).

### Major

1. **Lemma 2 (and consequently Theorem 1) is not proven for general stochastic MDPs as presented.**  
   The paper defines the MDP with stochastic transitions $T: S\times A\times S\rightarrow[0,1]$ (Line 28) and assumes only that "the influence of discounting can be safely ignored, e.g., when MDPs with absorbing states are considered" (Line 73). The reviewer provides a valid counterexample for a **stochastic** 1-step MDP with $\gamma=1$: action A yields reward 10 (prob 0.1) or 0 (prob 0.9); action B yields 1 deterministically. Then $Q_R^* = 1$, $(Q_R^*)^2 = 1$, but $Q_{R^2}^* = 10$, violating $Q_R^{*m} \ge Q_{R^m}^*$.  

   **Verification**: The inequality *does* hold for **deterministic** MDPs with non-negative rewards (by the binomial expansion: $(\sum r_i)^m \ge \sum r_i^m$ for $r_i \ge 0$, and the optimal trajectory under $R^m$ cannot exceed the optimal total under $R$ raised to $m$). However, the paper does *not* state a determinism assumption, and its general MDP formalism (Line 28) permits stochasticity. This means Lemma 2 and Theorem 1 are overclaimed.  

   **Impact**: This is a real gap, but not fatal, because (a) all experimental domains where the nonlinear bounds are used (Dollar-Euro for $\mathcal{R}=R_1^4+R_2^3$, and the auto-generated domains) either are deterministic or use only linear combinations (Lemma 4, which is always valid for $a,b>0$), so the empirical results are not undermined; (b) the gap can be closed by explicitly assuming deterministic transitions (or a related structural condition) in the theoretical development. The paper must clarify this limitation.

2. **No direct verification that optimal actions are never pruned in practice.**  
   The experiments compare convergence curves, but the paper does not report diagnostics such as: how often are the computed bounds violated? Are any optimal actions ever pruned? The heat maps (Fig. 2) show *how many* actions are pruned per state, but not *which* actions — specifically, whether any pruned action was optimal under the true target reward. Without this check, the empirical results cannot confirm the core theoretical claim (Theorem 2) and leave open the possibility that the bounds are accidentally violated but the pruning still "works" by luck.

### Minor

1. **Computational cost of $Q^\mu$ ($Q_{-R}^*$) is understated.**  
   The paper notes that $Q^\mu$ (via $Q_{-R}^*$) "doubles" the source learning cost and argues it is acceptable because source domains are "less expensive while accessible" (Sec. 5). However, the paper never quantifies this cost or compares total (source + target) sample complexity against learning from scratch. For practitioners, the question of whether the upfront investment pays off is critical. A concrete analysis — even rough — would strengthen the practical argument.

2. **No comparison against Q-value transfer initialization.**  
   A natural baseline would be to initialize the target Q-table with the best source Q-function (or a combination thereof) and continue Q-learning on the target — a simpler reuse strategy. This baseline would isolate whether the benefit comes from the pruning itself or simply from leveraging source knowledge. The absence weakens the claim that pruning specifically drives gains.

3. **The reward-shaping LP does not directly maximize pruning.**  
   The paper acknowledges (Line 150) that minimizing bound distances (Eq. 11) only indirectly relates to pruning count. This is honest but leaves the shaping step somewhat ad-hoc. A more direct objective (e.g., maximize number of pruned actions subject to the no-optimal-pruning constraint) would be technically cleaner, though likely harder to solve.

4. **Brittleness to target reward approximation error.**  
   Fig. 5 shows that Q-M degrades substantially at just 4% noise when the target must be approximated from sources. The paper acknowledges this (Line 222) and attributes it to linear regression limitations, but the sensitivity is concerning for practical use where exact polynomial relationships are rarely known.

### Trivial
None.

## Nice-to-Haves
- A diagnostic experiment checking whether the bounds $(Q_R^*)^m$ and $-|Q_{-R}^*|^m$ ever violate the true $Q_{R^m}^*$ and $Q_{R^m}^\mu$ on held-out states in the tested domains.
- A cost-benefit analysis comparing total (source + target) sample complexity of Q-M vs. learning from scratch.
- Comparison against the simpler baseline of using source Q-functions as initialization for target Q-learning.

## Removed Points

- **"Lemma 2 is unsound, invalidating the entire approach"** — Kept as Major but downgraded from Fatal. The inequality fails for stochastic MDPs but holds for deterministic MDPs (which the experiments use). The paper needs to add the determinism assumption; the approach is not fundamentally broken.
- **"Reward adaptation is just transfer learning"** — Removed because the paper itself explicitly states this framing ("RA may also be viewed as a special form of transfer learning," Line 12). This is the authors' own characterization, not a criticism.
- **"Missing appendix/proofs"** — Removed per instructions (parser strips appendices; they exist in the original submission).
- **"The core theoretical bounds are unsound" / "any proof must contain an error"** — Partially removed. The reviewer's claim of categorical unsoundness overstates the issue. The bounds hold for deterministic MDPs with non-negative rewards, which covers all experimental setups. The real problem is insufficiently specified assumptions, not an irreparable flaw.
- **"The Q-min function is not clearly motivated"** — Removed. The motivation is explicit: a lower bound is needed for the pruning condition, and Q^μ provides it via Lemma 1 (Line 34–48). The paper explains this clearly.
- **"Source domains being less expensive is never justified"** — The paper states this as an assumption (Sec. 5), not a derived claim. Criticizing an assumption for being assumed is circular.
- **"Global minimum not well-defined"** — Removed. For finite MDPs, the min over a finite set of deterministic policies is well-defined; for stochastic policies, it's a standard RL problem with negated rewards. This is well-understood in the literature.
- **Generic strengths from Strength Finder that are superficial** — Strengths kept; all five are substantive and backed by evidence. No generic filler strengths were included.

## Novel Insights

The most interesting observation emerging from the reviews is that the core theoretical gap (Lemma 2 requiring deterministic dynamics) creates an inverted relationship between the paper's claimed generality and its actual strength. The paper presents itself as broadly applicable (any MDP with absorbing states), but its formal guarantees actually rely on a much stronger implicit condition. Paradoxically, this gap may not affect the practical utility of the method at all — many interesting RA applications (grid-worlds, deterministic discrete control) satisfy the missing condition. The real question the paper should address is whether stochastic dynamics actually matter for the bound to hold, or whether a more careful proof (e.g., using Jensen's inequality in the opposite direction or decomposing along trajectories) could recover the result in full generality. The paper's current framing hides this interesting nuance.

## Suggestions

1. **State the determinism assumption explicitly** in Lemma 2 and Theorem 1, or provide a corrected proof that handles stochastic transitions. If determinism is required, note it clearly as a limitation.
2. **Add a direct diagnostic** showing that actions pruned by Q-M are indeed suboptimal under the true target reward (e.g., by computing the true $Q_{\mathcal{R}}^*$ via exhaustive policy evaluation on small domains and checking the pruning decisions).
3. **Quantify the cost of learning $Q_{-R}^*$** for each source domain and provide a total sample complexity comparison (source pre-training + target learning) against learning the target from scratch.
4. **Add a Q-value transfer baseline** where source Q-values initialize the target Q-table, to isolate pruning's contribution to speedup.
5. **Discuss the conditions under which Lemma 2 actually holds** (the paper's current "ignoring discounting" assumption is insufficient — it needs to address stochasticity in the transition dynamics).

## Score and Decision

**Originality**: Good — reward adaptation is a clean new problem framing, and the bound-based pruning mechanism is novel.  
**Importance**: Moderate — useful for settings where pre-trained source policies are available, but the polynomial-target assumption restricts applicability.  
**Claims support**: Weak in theory (unspecified assumptions in Lemma 2), good in experiments (consistent speedups, though missing diagnostic checks).  
**Soundness**: Moderate — the theoretical guarantee is narrower than claimed; experiments support effectiveness on the tested (mostly deterministic) domains.  
**Clarity**: Good — well-structured, though the key assumption gap is not discussed.  
**Value**: Moderate — the core idea is useful and empirically promising; with a corrected theoretical framing it would be a solid contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>