Now I have thoroughly read the paper and verified all claims against the actual content. Let me produce the final consolidated review.

---

## Summary

This paper proposes **Dig-DEC**, a new model-free decision-estimation coefficient that removes the optimism principle used in prior work (FGQ+23) and instead drives exploration via two information-gain terms (KL regularization plus a flexible divergence). The framework generalizes the AIR framework of XZ23/LWZ25, provides a new analysis that avoids restrictive minimax theorems, and improves the online function-estimation procedure. The result is a unified framework yielding improved regret bounds in stochastic settings and — notably — the first model-free regret bounds for hybrid MDPs (stochastic transitions, adversarial rewards) with bandit feedback, resolving an open problem from LWZ25.

## Strengths

- **Dig-DEC is never larger than optimistic DEC and can be arbitrarily better**: Theorem 13 proves $\text{dig-dec}_\eta^{\Phi,\overline{D}} \leq \text{o-dec}_\eta^{\Phi,\overline{D}} + \eta$ for any $\overline{D}$, showing Dig-DEC is always competitive. Theorem 14 exhibits a 3-armed bandit instance where optimistic DEC suffers $\Omega(\sqrt{T})$ regret while Dig-DEC achieves $O(1)$ regret, demonstrating improvement can be arbitrarily large.

- **First model-free regret bounds for hybrid MDPs with bandit feedback, resolving an open problem**: The paper establishes the first model-free regret bounds for hybrid MDPs with bandit feedback under linear rewards and general transition structures (Table 2), resolving the main open problem from LWZ25 who could only handle full-information feedback in the model-free setting.

- **Sharper regret bounds via improved online function estimation**: For squared estimation error in Bellman-complete MDPs, the two-timescale procedure is redesigned (Section 4.2.2), improving regret from $T^{5/6}$ to $\sqrt{T}$ — the first time a DEC-based method matches optimism-based approaches in Bellman-complete MDPs.

- **Flexible framework with simpler analysis**: The new analysis (Section 4) connects regret decomposition to mirror descent, avoiding the restrictive "constructive minimax theorem" of prior work. This allows handling a general divergence $D$ and even simplifies the recovery of prior results (Appendix C notes that the framework removes the need for a two-level algorithm in the full-information hybrid case).

- **Coverage of multiple canonical MDP classes under a unified complexity measure**: Tables 1 and 2 provide Dig-DEC bounds for bilinear classes (on/off-policy), MDPs with bounded Bellman-Eluder dimension (Q-type and V-type), and coverable MDPs — in both stochastic and hybrid settings.

## Weaknesses

### Fatal
None.

### Major

1. **Abstract's numerical claims are inconsistent with the main results and contain an arithmetic error.** The abstract states: "improving their regret bounds from $T^{3/4}$ to $T^{3/5}$ (on-policy) and from $T^{5/6}$ to $T^{7/8}$ (off-policy)." However, Table 1 shows the paper's own regret bounds for the corresponding bilinear classes (on-policy with $\overline{D}_{\text{av}}$) as $O(T^{2/3})$, not $T^{3/5}$. Moreover, $T^{7/8} > T^{5/6}$ for $T>1$, so the claimed "improvement" from $T^{5/6}$ to $T^{7/8}$ is actually a regression. The introduction (line 39) further muddies the picture with yet another set of exponents ($T^{3/2}/T^{5/8}$ to $T^{3/2}/T^{5/6}$). The paper must reconcile these numbers, map each abstract claim to a specific row in a table, and verify the arithmetic. This does not appear to be a fundamental flaw — the technical results in the tables are likely correct — but as presented, it undermines reader confidence in the paper's quantitative claims.

### Minor

2. **"Improves the rate of Est from $\sqrt{T}$ to $T^{1/2}$" (line 219) is vacuous as written.** Both $\sqrt{T}$ and $T^{1/2}$ are $T^{0.5}$ — identical rates. The sentence reads as an error (possibly the constant factor improves, or a different exponent was intended). The paper should clarify what is actually being improved.

3. **Computational tractability of Algorithm 1 is not discussed.** The core algorithm requires solving a saddle-point optimization over $\Delta(\Pi)$ and $\Delta(\Psi)$ at every round, where $\Psi$ is the union of all infosets. While the paper is a theoretical contribution and can reasonably abstract away computation, a brief acknowledgment of the tractability challenge would help readers understand the nature of the contribution (information-theoretic rather than algorithmic).

4. **Assumption 5's stationarity condition needs clarification.** The assumption requires $\mathbb{E}^{\pi,M_t}[\ell_h(\phi; o_h)] = \mathbb{E}^{\pi,M_{t'}}[\ell_h(\phi; o_h)]$ for all $t,t'$ — a stationarity restriction that is not automatically implied by the hybrid environment definition (where rewards change arbitrarily). The paper should state explicitly how restrictive this is and when it holds naturally.

### Trivial

None.

## Nice-to-Haves

- A concrete example (beyond the 3-armed bandit of Theorem 14) illustrating why Dig-DEC succeeds in hybrid settings where optimism fails would strengthen the narrative.
- A brief discussion comparing the achieved hybrid rates ($T^{3/2}$, $T^{13/8}$) to known lower bounds or model-based rates would help contextualize the contribution.

## Removed Points
- **"log|Φ| vs log²|Φ| inconsistency in tables"** — removed because the tables correctly differentiate between settings: Table 1 shows $\log|\Phi|$ for the average-estimation-error cases and $\log^2|\Phi|$ where the squared-error case yields it through optimization. The critic misread the entries.
- **"Hybrid bounds are far from √T"** — partially removed because Table 2 row 4 (bilinear★ off-policy with completeness) actually achieves $T^{1/2}$, and the claim "first model-free bounds" is correctly qualified. The critic's concern is partially valid but overstated.
- **"Missing related works"** — removed per policy: I cannot verify which works are missing without external sources.
- **"Missing lower bounds discussion"** — weakened to nice-to-have; it is not standard for every theoretical paper to provide lower bounds for every setting.

## Novel Insights

The harsh critic and strength finder converge on a point that goes beyond what the paper explicitly states: the KL regularization term that replaces optimism simultaneously serves two distinct roles — (i) it regularizes the marginal distribution (making $\nu_\phi$ close to $\rho$), which avoids the need for the explicit $V_\phi(\pi_\phi)$ optimism term, and (ii) it provides an information-gain signal that captures distributional differences missed by mean-based divergences like bilinear divergence or squared Bellman error. The paper's decomposition of the KL into these two roles (Section 6) is insightful but buried. Making this decomposition more prominent would sharpen the paper's thesis: that information gain can do everything optimism does and more.

## Suggestions

1. **Fix the abstract's numerical claims.** Align them with Table 1. If $T^{3/5}$ and $T^{7/8}$ refer to specific sub-cases (perhaps shown in Appendix A), state this explicitly. Fix the regression error ($T^{7/8} > T^{5/6}$).
2. **Correct the vacuous "√T to $T^{1/2}$" claim** (line 219) to actually describe what rate or constant is improved.
3. **Add a one-paragraph note** on the computational character of Algorithm 1 (e.g., that the saddle-point can be solved via mirror descent, or that the contribution is information-theoretic).
4. **Clarify Assumption 5** to state the stationarity condition as an additional restriction on the adversary rather than part of the assumption about the existence of $\ell_h$.

---

## Score and Decision

### Round 1 (Bracketing)

**Queries used:**
- Weak band ($<3.5$): "model-free decision estimation coefficient DEC reinforcement learning theory regret bounds" — returned papers scoring 2.0–3.2, mostly unrelated or low-quality. The current paper is clearly well above this band.
- Middle band (3.5–7.5): "decision estimation coefficient reinforcement learning theory bounds" — returned anchors at 4.67, 5.50, 6.50, 7.00. The current paper fits in this band.
- Strong band ($>7.5$): "adversarial MDPs model-free regret bounds bilinear class" — returned anchors at 8.0 but on dissimilar topics (world models, quantum computing, etc.), not directly comparable.

**Initial bracket:** 5.0 – 7.0 (the paper is clearly above the weak-band papers but has notable presentation issues preventing it from reaching the 7+ level of the strongest anchors).

### Round 2 (Narrowing)

**Queries used:**
- "model-free decision estimation coefficient DEC" (4.5–6.5) — returned several anchors at 4.67–5.50, none closely related.
- "adversarial MDP regret bounds bilinear class theoretical paper" (6.0–8.0) — returned:
  - **QEcSLhfOoQ** (avg 6.50): Minimax Optimal Adversarial RL — similar theoretical contribution with computational concerns. The current paper has a broader framework but worse presentation issues.
  - **fE0RJto3Na** (avg 6.50): Q-Learning with Fine-Grained Gap-Dependent Regret — tabular RL theory, fixes prior flaws. Comparable quality.
  - **xCelVyUVO2** (avg 6.50): Multi-model RL perspective — incremental concerns noted by reviewers.

**Comparison with anchors:**
- vs QEcSLhfOoQ (6.50): The current paper's conceptual contribution (Dig-DEC as a new complexity measure) is more fundamental, but its presentation issues are more severe.
- vs fE0RJto3Na (6.50): Both fix flaws in prior work and extend to new settings. The current paper addresses a more general framework but has more presentation problems.
- vs vAU1fo1zRV (7.00): Decision calibration paper with very clean writing and clear results. The current paper has more significant contributions (open problem resolution) but less polished presentation.

**Final score: 6.0** — The paper's contributions are solid and its framework is conceptually clean, but the numerical inconsistencies in the abstract, the vacuous "improvement" claim, and the lack of discussion around computational tractability and Assumption 5's stationarity condition prevent it from reaching the polish level of the 6.5–7.0 anchors. These are fixable presentation issues, not fatal flaws. A revised version that resolves these would warrant a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>