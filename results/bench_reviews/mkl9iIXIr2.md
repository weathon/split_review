Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper studies Online Inventory Optimization (OIO) in non-stationary environments and provides the first dynamic regret guarantee for this setting. The key technical contribution is a two-stage projection strategy (Lemma 1) that connects OIO to Smoothed Online Convex Optimization (SOCO), enabling the use of existing SOCO algorithms as base learners. The paper also provides a matching lower bound \(\Omega(\sqrt{L_{\max}T})\), resolving an open question from prior work, and achieves an overall dynamic regret of \(\tilde{\mathcal{O}}(\sqrt{L_{\max}T(1+P_T)})\).

## Strengths

- **First dynamic regret bound for OIO with carryover stock.** The paper proves (Theorem 4) that its algorithm achieves \(\tilde{\mathcal{O}}(\sqrt{L_{\max}T(1+P_T)})\) dynamic regret, whereas existing work [Hihat et al. 2023] only provided static regret guarantees. The motivating example (fluctuating demand) convincingly demonstrates why static regret is insufficient for non-stationary environments.

- **Novel theoretical connection between OIO and SOCO.** Lemma 1 is the paper's technical linchpin: it shows that the OIO regret decomposes into a SOCO regret with switching cost proportional to \(L_{\max}\), thereby eliminating the difficult carryover stock constraint. This connection (Remark 4) is clean and enables the use of existing SOCO algorithms, which is a genuinely novel reduction.

- **Matching lower bound resolving an open question.** Theorem 5 provides a \(\Omega(GD\sqrt{L_{\max}T})\) static lower bound, and Table 1 shows this matches the static upper bound up to constants. This resolves the open question raised by Hihat et al. (2023). Corollary 1 extends the lower bound to SOCO, which is an interesting cross-domain implication.

- **Adaptivity to unknown parameters.** Algorithm 2 uses a doubling trick to handle unknown \(L_{\max}\), while the SOGD base learner adapts to unknown path-length \(P_T\). The algorithm does not require these parameters a priori, which is practically meaningful.

## Weaknesses

### Major
- **The "near-optimal dynamic regret" claim is not fully supported by a matching dynamic lower bound.** The paper claims near-optimality for dynamic regret (abstract, Theorem 1) but only proves a *static* lower bound (Theorem 5). While the paper cites the known OCO dynamic lower bound \(\Omega(\sqrt{(1+P_T)T})\) from Zhang et al. (2018b), the combination with the \(L_{\max}\) factor has not been proven optimal for the *OIO-specific* dynamic setting. The bound could in principle have a worse dependence on \(L_{\max}\) in the dynamic case than the static case. This is not a fatal flaw — many theory papers claim near-optimality based on partial matching — but the claim should be softened to reflect what is actually proven.

- **The claimed "improvement of \(\sqrt{L_{\max}}\)" over prior static regret is not an apples-to-apples comparison.** The abstract and Table 1 present an improvement from \(\mathcal{O}(L_{\max}\sqrt{T})\) (Hihat et al. 2023) to \(\mathcal{O}(\sqrt{L_{\max}T})\). However, as Remark 2 honestly acknowledges, Hihat et al. assume general convex capacity constraints while this paper assumes a linear-sum constraint. The improvement is therefore partly attributable to the relaxed constraint, not solely to the algorithm. This qualification belongs in the abstract and the contribution summary, not just in a remark. The paper should be more transparent about this comparison.

### Minor
- **The SOCO base learner (SOGD) is not independently verified within the paper's setting.** Algorithm 5 (SOGD) is adapted from Zhang et al. (2022a), and Theorem 4 states its regret guarantee under an OIO-specific condition (\(T \geq \sqrt{L_{\max}(\log_2 T + e)}\)). However, no proof or derivation is given showing that SOGD indeed achieves the claimed bound with the specific parameters (Eq. 11, the erf/inverse-erf combiner) under the paper's OIO assumptions (ℓ₁-norm switching cost, subgradient bound \(G\), capacity \(D\)). While citing prior work for sub-components is standard practice, the paper's central guarantee depends on this sub-component, and a proof sketch or explicit verification would strengthen the paper's self-containedness.

- **The paper provides no experimental validation.** As a pure theory paper, this is not disqualifying, but simulations on synthetic non-stationary demand sequences (e.g., with trends, seasonality, or abrupt changes) would demonstrate that the dynamic regret bound translates into practical gains over static-regret baselines like MaxCOSD. This limits the paper's impact.

- **The dependence on the number of items \(N\) is not analyzed.** The regret bounds include \(N\) (through \(\|g_t\|_1 \leq \sqrt{N}G\)), but its impact on the lower bound and the algorithm's scaling is not discussed. For a multi-item setting, understanding how \(N\) affects the bounds would be useful.

- **The constants in Theorem 2 (\(C(\alpha)\), \(\Delta(L_{\max},\beta)\)) are not specified**, making it hard to verify the final regret bounds without cross-referencing the appendix.

### Trivial
- The erf/inverse-erf combiner (Algorithm 4) is described without implementation guidance; a brief note on numerical stability would be helpful.

## Nice-to-Haves
- A diagram illustrating the two-stage projection and the definition of cycles (using a simple two-item example) would help readers understand Lemma 1 and the doubling trick.
- Extending the analysis to general convex capacity constraints (as in Hihat et al., 2023) would unify the static and dynamic regret results, but this is clearly scoped as future work.

## Removed Points
- Criticisms about missing proofs in the appendix (Lemma 2, Lemma 1 proof) — the parser strips appendix content; these proofs exist in the original submission.
- Criticism that the erf/inverse-erf combiner "may be numerically unstable" — this is speculative without evidence.
- Criticism that the gap between demand-based \(L_{\max}\) and cycle-length-based tracking is "not fully explained" — this is addressed in the omitted appendix.
- Any formatting, typo, grammar, or stylistic nitpicks — these are parser artifacts.
- Strength Finder points that are generic ("addressed an important problem") — filtered out.
- Criticisms about missing related works — cannot be verified externally.

## Novel Insights

Beyond the paper's own contributions, the most interesting insight to emerge from the reviews is that the OIO-to-SOCO reduction provides a template for handling stateful constraints in online learning more broadly. The carryover stock constraint creates a feasibility gap between the learner's decisions and the comparator that is normally fatal for dynamic regret. The paper resolves this by showing that the gap manifests as a switching cost on the base learner's decisions, which SOCO is designed to handle. This suggests that other online problems with similar "memory" constraints (e.g., perishable inventory, reusable resources) might benefit from a similar reduction, making Lemma 1 potentially more widely applicable than just the OIO setting.

## Suggestions
1. **Tone down the optimality claims.** Replace "near-optimal dynamic regret" with "dynamic regret guarantee" and explicitly note that optimality is only established for the static case. Qualify the \(\sqrt{L_{\max}}\) improvement in the abstract with a brief note about the different capacity constraints.
2. **Add a proof sketch for the SOGD base learner** showing how Theorem 4 follows from Zhang et al. (2022a) under the paper's specific parameter ranges, or explicitly state the required modifications.
3. **Include simulations** on at least synthetic non-stationary demand sequences (trends, seasonality, abrupt changes) to demonstrate that the theoretical dynamic regret translates to empirical gains over static-regret baselines.
4. **Discuss the \(N\)-dependence** in the regret bounds and whether the lower bound also scales with \(\sqrt{N}\).

## Score and Decision

**Calibration anchors (from batch retrieval):**

| Anchor Paper | Avg Score | Comparison |
|---|---|---|
| Discounted OCO (65iFtHZ8Cu.md) | 6.00 (Accept Poster) | Similar theoretical structure (algorithm + analysis + reliance on prior sub-components). Current paper is theoretically stronger (novel OIO-SOCO connection + lower bound) but lacks experiments. Comparable overall. |
| Online Decision-Focused Learning (FJhtHBphCt.md) | 6.00 (Accept Poster) | Similar scope (first provable guarantees for a new setting). Current paper has cleaner theory but fewer experiments. Comparable. |
| Proving Limited Scalability (0KXI6lDM9C.md) | 5.50 (Accept Poster) | Similar style (purely theoretical with lower bounds). Current paper has a broader contribution (algorithm + reduction + lower bound) but some overclaims. Comparable. |
| Online Reusable Resource Allocation (nR984mi6zD.md) | 5.33 (Reject) | Had unresolved technical issues with proofs. Current paper does not have similar proof issues. Stronger than this anchor. |
| Perishable Inventory Control (YlDHsGqjCO.md) | 4.40 (Reject) | Had limited novelty and heavy assumptions. Current paper has a cleaner, more novel theoretical contribution. Stronger. |
| Decentralized OCO Compressed (QTh3aRcbTt.md) | 3.00 (Reject) | Lacked algorithmic novelty. Current paper has a genuinely new reduction. Significantly stronger. |

Relative to the anchors, this paper sits firmly in the Accept (Poster) band. Its core theoretical contributions — the OIO-to-SOCO reduction and the matching lower bound — are genuinely novel and technically sound. The main weaknesses are about presentation overclaims and missing details, not about flawed methodology. The paper is comparable in quality to the 5.5–6.0 accepted anchors and clearly stronger than the rejected ones in the 3–5 range.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept (Poster)</orange>