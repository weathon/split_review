Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes the first dynamic regret guarantee for online inventory optimization (OIO) under adversarial demands. The key technical insight is a two-stage projection strategy that connects OIO to Smoothed Online Convex Optimization (SOCO), converting the carryover stock constraint into a switching cost. The algorithm achieves \(\tilde{\mathcal{O}}(\sqrt{L_{\max}T(1+P_T)})\) dynamic regret and \(\mathcal{O}(\sqrt{L_{\max}T})\) static regret — the latter improving over the prior best (Hihat et al., 2023) by a factor of \(\sqrt{L_{\max}}\). A matching \(\Omega(\sqrt{L_{\max}T})\) static lower bound is also provided, showing near-optimality up to logarithmic factors.

## Strengths

1. **First dynamic regret guarantee for OIO with adversarial demands.** The paper resolves an open question from Hihat et al. (2023) by providing — for the first time — a sublinear dynamic regret bound for OIO. The bound \(\tilde{\mathcal{O}}(\sqrt{L_{\max}T(1+P_T)})\) is clean and includes dependence on both the sell-out period \(L_{\max}\) and the comparator path-length \(P_T\), which captures problem difficulty in non-stationary environments.

2. **Elegant conceptual connection between OIO and SOCO.** Lemma 1 shows that OIO's dynamic regret reduces to a SOCO regret with switching costs proportional to \(L_{\max}\). This reduction is the main technical novelty — it cleanly sidesteps the difficulty posed by the dynamic carryover stock constraint, which had prevented standard two-layer OCO approaches from working.

3. **Matching static lower bound and near-optimality.** Theorem 5 provides the first \(\Omega(\sqrt{L_{\max}T})\) lower bound for OIO static regret, matching the upper bound up to logarithmic factors. The paper also gives a clean argument (Corollary 1) showing that this lower bound carries over to SOCO, a well-studied setting.

4. **Doubling trick for unknown \(L_{\max}\).** The algorithm handles the unknown switching cost coefficient via a restart-based doubling trick (Theorem 2), incurring only logarithmic overhead. This makes the main bound (Theorem 4) adaptive, not requiring \(L_{\max}\) as input.

5. **Clear and rigorous presentation.** The problem motivation (fluctuating demand example in §1) is compelling. The proofs are structured logically (projection lemma → doubling trick → base learner instantiation), and the regret bounds are summarized transparently in Table 1.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core technical claims are sound, and its contributions (first dynamic regret for OIO, matching lower bound) are clearly substantive.

### Minor

1. **The "improvement over existing studies" claim in the abstract could be more precise.** The abstract states "an improvement of \(\sqrt{L_{\max}}\) for the static regret upper bound in existing studies." Most existing works in Table 1 assume i.i.d. demands, while the paper operates under adversarial demands with linear-sum capacity constraints. The directly comparable work under non-i.i.d. demands (Hihat et al., 2023) uses general convex constraints. The paper acknowledges the constraint difference (Remark 2), but the abstract's phrasing could mislead readers into thinking the improvement holds across all existing studies under equivalent settings. A small rewording would clarify this.

2. **Algorithm assumes knowledge of the total horizon \(T\).** Algorithm 5 (SOGD base learner) uses \(T\) to set the number of combiners \(K\) and the learning rates. The paper does not discuss how to extend the approach to an anytime setting where \(T\) is unknown. While knowledge of \(T\) is common in OCO theory, this limits direct applicability to real inventory systems where the horizon is typically not known in advance. A brief discussion of an anytime extension (e.g., a standard online doubling trick over \(T\)) would address this.

3. **The lower bound argument for dynamic regret is incomplete.** Theorem 5 provides a *static* regret lower bound. To claim near-optimality of the *dynamic* regret bound, the paper combines this \(\sqrt{L_{\max}}\) factor with the \(\sqrt{1+P_T}\) OCO lower bound from Zhang et al. (2018b). This suggests rather than proves a joint \(\Omega(\sqrt{L_{\max}(1+P_T)T})\) dynamic lower bound for OIO — the OCO lower bound was derived for a fixed feasible set, not the time-varying constrained OIO setting. The paper appropriately hedges ("matches this lower bound up to a logarithmic factor"), but a dedicated OIO dynamic lower bound would strengthen the optimality claim.

4. **Definition of \(L_{\max}\) uses an artificial terminal demand.** Definition 1 extends the interval to \(T+1\) with \(d_{T+1}^i = D\). This boundary handling is technically sound but unusual; a brief justification would help readers understand why this does not affect the regret analysis.

### Trivial

- Theorem 3 requires knowing \(P_T\) a priori, which the paper correctly notes as a limitation before presenting the parameter-free Algorithm 5. This is by design, not a flaw.
- Some minor notation: the informal Theorem 1 could reference the formal theorem numbers (Theorems 3 and 4) directly.

## Nice-to-Haves

- **Empirical validation.** The paper is purely theoretical. While ICLR publishes theory papers (and the contribution stands on its own), a small simulation on synthetic demand sequences (e.g., sinusoidal, piecewise-constant) validating the regret rates and comparing against OGD baselines would significantly broaden the paper's impact.

- **An OIO-specific dynamic regret lower bound.** A dedicated lower bound that jointly lower bounds both the \(L_{\max}\) and \(P_T\) dependencies would cleanly close the optimality question.

- **Visualization of the sell-out period.** A plot illustrating how \(L_{\max}\) interacts with regret behavior (e.g., low vs. high demand fluctuation) would help readers build intuition.

## Removed Points

- *Criticism about the lack of experiments as a "methodological gap" weakening the paper's credibility* — This is a theory paper with novel algorithmic and lower-bound contributions. ICLR publishes theory papers without empirical validation (see accepted anchor papers such as "On the Hardness of Online Nonconvex Optimization with Single Oracle Feedback," avg score 6.5). Demanding experiments treats a scope choice as a flaw. Moved to Nice-to-Haves.
- *Criticism about the paper not discussing how the doubling trick's guarantee degrades when the restarted learner has fewer rounds left* — The base learner \(\mathcal{E}(2L, T)\) is initialized with the same \(T\) every restart; the regret bound for \(T\) rounds upper-bounds the regret for fewer remaining rounds by monotonicity. This is standard practice and the concern is addressed implicitly by the analysis structure.
- *Strength about "the paper identified a genuine difficulty"* — Generic/superficial, not specific to the paper's content.

## Novel Insights

The reviews reveal a subtle but interesting point: the paper's lower-bound argument for dynamic regret (combining a static OIO lower bound with an OCO dynamic lower bound from prior work) is the weakest link in the optimality narrative. This is not a fatal flaw — the static lower bound already shows that \(\sqrt{L_{\max}}\) is necessary, and the dynamic regret upper bound matches the standard OCO optimal rate in \(P_T\). But a reader who focuses on this gap will correctly note that no single information-theoretic argument proves that *both* factors are simultaneously unavoidable in OIO's dynamic regret. This tension between what is proven (static matching, dynamic upper bound) and what is claimed (dynamic near-optimality) is worth resolving in future work.

## Suggestions

1. **Reword the abstract's contribution claim** to specify that the \(\sqrt{L_{\max}}\) improvement is relative to the adversarial, non-i.i.d. setting (Hihat et al., 2023) and that comparisons to i.i.d. bounds serve as context.
2. **Add a brief discussion** of how to handle unknown \(T\) (e.g., an outer loop doubling the horizon estimate), even if only in the appendix.
3. **Acknowledge the limitation** in the lower bound section more explicitly: the dynamic regret is near-optimal *relative to* the proven static lower bound plus the OCO dynamic lower bound, rather than a proven joint lower bound.
4. **Add a synthetic experiment** (optional but recommended for impact). Even a simple plot of regret vs. \(T\) under adversarial demands with known ground truth would validate the theory and make the paper accessible to a broader audience.

## Score and Decision

**Calibration anchors (from retrieval):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `iZgECfyHXF` — Online Nonconvex Optimization | 6.50 (Accept) | Pure theory paper with matching bounds, no experiments. The current paper has similarly clean theory and a more applied motivation. Comparable quality. |
| `RR70yWYenC` — Continual Finite-Sum Minimization | 6.25 (Accept) | Theory paper with nearly tight bounds. The current paper has a similar profile: novel problem, tight bounds, clear writing. Slightly narrower scope. |
| `Rdb0HxGJa3` — OCO with Predictions | 4.50 (Reject) | Incremental contribution with unclear motivation. The current paper has a clearer contribution and stronger motivation. |
| `WIerHtNyKr` — Non-Stationary OCCO | 5.25 (Reject) | Had experiments but unclear contribution. The current paper has clearer theoretical contributions. |
| `lFzUHGebeb` — Online Linear Regression | 2.00 (Reject) | Poorly written, flawed theory. Not comparable. |
| `ze7DOLi394` — Feature Interaction Tensor | 7.50 (Accept) | Strong empirical + theoretical work. More broadly impactful but also a very different type of contribution. |

The current paper is cleanest compared to mid-to-high scoring theory papers (iZgECfyHXF at 6.5, RR70yWYenC at 6.25). It has a well-motivated problem, novel technical insight (OIO→SOCO connection), matching bounds, and clear writing. The weaknesses are presentation-level and do not threaten the core claims. It is clearly stronger than the rejected theory papers at ~4.5–5.25.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>