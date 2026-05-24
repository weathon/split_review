Now I have a thorough understanding of the paper and can cross-check all reviewer claims. Let me produce the consolidated review.

## Summary

This paper introduces "Reward Adaptation" (RA) — reusing pre-trained source behaviors (Q* and Q-min from source reward functions) to speed up learning of a target behavior under a different reward function on the same MDP. The proposed method, Q-Manipulation, derives upper/lower bounds on the target's expected return from source Q-functions, tightens those bounds via reward shaping (solved via LP), and prunes provably suboptimal actions before target learning begins. The paper claims optimality guarantees (pruning never removes an optimal action) and shows empirical pruning rates of 7.8%–42.7% with faster convergence on several small discrete domains.

---

## Strengths

1. **Novel problem framing and creative use of Q-min.** The idea of maintaining both Q* and Q-min (via Q*_{-R}) for source behaviors and using them to compute bounds on a target polynomial reward is original. This departs from standard Q-Decomposition (which learns from scratch) and provides a principled way to reuse prior knowledge.

2. **Optimality guarantee for the linear case.** Theorem 2's proof structure is sound *if* the bounds it relies on are correct. For linear reward combinations (Lemma 4), the bound Q*_{aR_i+bR_j} ≤ aQ*_{R_i}+bQ*_{R_j} follows from the subadditivity of the max operator and is correct. The optimality guarantee therefore holds for linear targets, which is a nontrivial contribution.

3. **Reward shaping to tighten bounds (Section 2.3).** The insight that shaping shifts Q* and Q^μ in opposite directions (Lemma 5), and the LP formulation to minimize the bound gap while preserving optimality, is a clever and principled mechanism for increasing pruning beyond raw bounds.

4. **Empirical pruning across diverse domains.** The paper reports pruning rates of 7.8%–42.7% across six domains (Dollar-Euro, Frozen Lake, Race Track, three auto-generated MDPs). Faster convergence is visually demonstrated relative to standard Q-learning and reward-shaping baselines.

---

## Weaknesses

### Fatal

**1. Lemmas 2 and 3 are stated without proof, and the claimed inequality direction is not obviously correct — this invalidates the theoretical support for non-linear reward combinations.**

Lemma 2 asserts that for $\mathcal{R}=R^m$ with positive $R$: $Q_R^{*\,m} \ge Q_{R^m}^{*}$. That is, $(\max_\pi \mathbb{E}[\sum \gamma^t r_t])^m \ge \max_\pi \mathbb{E}[\sum \gamma^t (r_t)^m]$. No proof is given. For a fixed policy, comparing $(\mathbb{E}[G])^m$ and $\mathbb{E}[G^m]$ (where $G=\sum\gamma^t r_t$) involves Jensen's inequality ($\mathbb{E}[G^m] \ge (\mathbb{E}[G])^m$ for convex $x^m$), while the per-trajectory inequality $G^m \ge \sum (r_t)^m$ goes in the opposite direction (cross terms are non-negative). The net direction is ambiguous without additional assumptions about the MDP's stochasticity, and the paper's vague statement that "the influence of discounting can be safely ignored, e.g., when MDPs with absorbing states are considered" does not resolve this. The same concern applies to Lemma 3 (multiplicative case). Because Theorem 1 aggregates these lemmas and Theorem 2 (optimality) depends on the bounds being correct, **the paper provides no valid theoretical basis for applying Q-Manipulation to any non-linear target reward function.** The experiments using non-linear targets (e.g., $R_1^4 + R_2^3$) are therefore uninterpretable with respect to the claimed guarantees.

### Major

**1. Non-linear experiments lack a valid foundation.** The experiments with non-linear targets (Figure 4, auto-generated domains with non-linear $\mathcal{R}$) purport to demonstrate generalizability, but because the bounds that underpin the method for these cases are unproven (see Fatal issue above), these results cannot be interpreted as supporting the paper's claims. The observed pruning and convergence improvements may stem from the method accidentally pruning actions based on invalid bounds, and the paper provides no verification (e.g., by computing the true optimal policy and checking whether pruned actions were actually suboptimal).

**2. No error bars, variance reporting, or statistical significance on convergence curves.** All convergence plots (Figures 2–5) show only the mean over 20 runs with no error bars, shaded regions, or confidence intervals. Given the inherent variance in RL, it is impossible to assess whether the claimed improvements are statistically significant or whether the apparent advantage over baselines could be within the noise.

**3. Missing ablation of the reward-shaping step.** The paper does not separate how much pruning comes from the raw bounds (Sections 2.2) versus how much additional pruning the LP-based reward shaping (Section 2.3) provides. This makes it difficult to assess the marginal contribution of the shaping component, which is a nontrivial part of the method.

### Minor

**1. The "discounting can be safely ignored" justification is underspecified.** The paper states this without formal treatment. For the bounds in Lemmas 2–3, discounting interacts with the cross terms in nontrivial ways, and a proper justification or proof should address how $\gamma < 1$ affects the inequality direction.

**2. Heat map analysis is superficial.** Figures 2 and 4 show that pruning concentrates around initial and goal states, but the paper offers no analysis of why this occurs or whether it reflects the bounds being tighter in those regions (which would be expected behavior) or something else.

**3. Race Track domain has up to 49 states; auto-generated domains cap at 100 states.** The paper states it "analyzes scaling" but does not go to larger state spaces that would stress-test the LP bottleneck the authors themselves acknowledge in Section 5.

### Trivial

None of consequence. (Formatting artifacts in the PDF extraction are parser issues, not author errors.)

---

## Nice-to-Haves

- Compare Q-Manipulation against a baseline that also receives the source Q-functions (e.g., initializing the target Q-table as the sum of source Q* functions) to isolate the benefit of pruning from the benefit of extra information.
- Provide the solve time of the LP separately in Table 1, rather than bundled into the total time.
- Verify empirically (for at least one domain) that actions pruned by Q-Manipulation are indeed suboptimal under the true target optimal policy.

---

## Removed Points

- **"Unfair comparison (extra information only to Q-Manipulation)"** — demoted from the harsh critic's framing as a central issue. The paper acknowledges this asymmetry: "even though Q-M has access to additional information, we do not consider the extra costs... since they are assumed to be incurred before considering the task in hand." Comparing a method that uses prior information against methods that do not is a standard way to demonstrate the value of that information. It would be *better* to include a baseline that also uses source Q-functions, but its absence is not a flaw that invalidates the results. Moved to Nice-to-Haves.

- **"Q_R*^m is not even a valid Q-function for any policy"** — removed. An upper bound does not need to be a valid Q-function for any policy; it only needs to dominate the true optimal value. This criticism misunderstands what an upper bound is.

- **"Positivity assumption may not hold in Frozen Lake"** — removed. The paper explicitly states that for linear combinations (which Frozen Lake uses: $\mathcal{R}=R_1+R_2$), positivity is not required. For non-linear cases, the auto-generated domains use positive rewards. The paper is internally consistent on this point.

- **"Noise experiment shows fragility"** — removed. The paper itself presents and acknowledges this result ("the theoretical guarantee of optimality is lost in such an evaluation setting"). The critic's framing of it as a weakness is redundant.

- **"Missing related works"** — removed per instructions (cannot confirm existence of missing citations).

- **"No proofs in appendix"** — removed. The parser strips appendices; they exist in the original submission.

- **Several generic "strengths" from the Strength Finder** (e.g., "this paper addressed an important problem") — removed as superficial or generic.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same core tension: the paper's most novel claim (handling non-linear polynomial reward functions via Q-Raising) rests on unproven bounds, while the linear case, though correctly handled, is less surprising given the subadditivity of max.

---

## Suggestions

1. **Restrict the method's theoretical claims to linear reward combinations** (or provide rigorous proofs for Lemmas 2 and 3). If non-linear bounds cannot be proved, remove those claims and experimental results entirely.
2. **Add error bars or shaded regions** (e.g., standard deviation or standard error) to all convergence plots.
3. **Include an ablation study** showing pruning rates from raw bounds vs. after reward shaping.
4. **Add a baseline that uses the same source Q-function information** (e.g., target Q-table initialization from source Q* values) to better isolate the contribution of the pruning mechanism.
5. **Clarify the discounting assumption** formally: state exactly what condition (e.g., γ=1 with absorbing states, or deterministic MDPs, or some bound on variance) makes Lemmas 2–3 hold, and prove it.

---

## Score and Decision

The paper introduces a creative approach and a novel problem framing, with a sound theoretical core for the linear case. However, the paper overreaches by claiming the method works for general polynomial target functions without valid theoretical support for non-linear bounds. The non-linear experiments are uninterpretable under the claimed guarantees, and the lack of error bars further weakens the empirical evidence. The linear-case contribution is real but more incremental.

**Score: 5.0**

**Decision: Reject**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>