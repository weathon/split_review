## Summary

This paper addresses online inventory optimization (OIO) in non-stationary environments. It proposes the first algorithm with near-optimal dynamic regret guarantees for OIO, achieving \(\tilde{\mathcal{O}}(\sqrt{L_{\max}T(1+P_T)})\) dynamic regret and \(\mathcal{O}(\sqrt{L_{\max}T})\) static regret — improving the prior state-of-the-art by a \(\sqrt{L_{\max}}\) factor. The key technical insight is a two-stage projection that connects OIO to Smoothed Online Convex Optimization (SOCO), transforming the carryover stock constraint into a time-varying switching cost. The paper also provides a matching \(\Omega(\sqrt{L_{\max}T})\) lower bound, establishing near-optimality and resolving an open question from Hihat et al. (2023).

## Strengths

- **First dynamic regret guarantee for OIO**: The paper presents the first algorithm with a \(\tilde{\mathcal{O}}(\sqrt{L_{\max}(1+P_T)T})\) dynamic regret bound (Theorems 1 and 4), addressing a critical gap where prior work only analyzed static regret. The motivating example in Section 1 (fluctuating demand \(d_t = Dt/T\)) concretely demonstrates why static comparators fail and why dynamic regret matters.

- **Improved static regret with matching lower bound**: The static regret bound of \(\mathcal{O}(\sqrt{L_{\max}T})\) improves over the \(\mathcal{O}(L_{\max}\sqrt{T})\) of existing OIO algorithms (Table 1). Theorem 5 establishes an \(\Omega(\sqrt{L_{\max}T})\) lower bound, proving the \(\sqrt{L_{\max}}\) factor is essential and resolving the open question raised by Hihat et al. (2023).

- **Elegant reduction from OIO to SOCO**: Lemma 1 is the paper's central technical contribution — it shows that under the two-stage projection, the regret gap \(\sum\langle g_t, y_t - \hat{y}_t\rangle\) is bounded by a switching cost term \(2GL_t^*\|\hat{y}_t - \hat{y}_{t+1}\|_1\). This insight transforms the complicated carryover constraint into a manageable SOCO instance and is genuinely novel.

- **Practical adaptivity with doubling trick**: The algorithm (Alg. 2) handles unknown \(L_{\max}\) via a doubling trick that restarts the base learner when the observed cycle length exceeds the current estimate, requiring only \(\mathcal{O}(\log L_{\max})\) restarts (Theorem 2). The SOGD-based variant (Theorem 4) further adapts to unknown comparator path-length \(P_T\).

- **Byproduct SOCO lower bound**: Corollary 1 provides a new \(\Omega(\sqrt{LT})\) lower bound for smoothed online convex optimization, consolidating the relationship between the two problem settings.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Linear capacity constraint vs. general convex**: The paper assumes a linear warehouse capacity constraint \(\sum_i y_t^i \leq D\) (Eq. 3), while Hihat et al. (2023) handles general convex constraints. The authors acknowledge this limitation in the conclusion and note it is critical for Lemmas 5–6. The linear case is practically relevant (the authors argue it covers weighted-sum capacities), but the improvement over Hihat et al. is achieved under a more restricted constraint class. This does not invalidate the contribution — even under linear constraints, no prior work achieved dynamic regret — but it tempers the comparison slightly.

- **Condition on horizon length**: Theorems 3 and 4 require \(T\) to be sufficiently large relative to \(L_{\max}\) (e.g., \(T \geq \sqrt{L_{\max}(\log_2 T + e)}\) for Theorem 4). While the authors note this holds broadly (e.g., \(T > L_{\max}\log^2 L_{\max}\)), the condition means the bounds are not fully unconditional and may not apply in the very-short-horizon regime.

### Trivial

- The precise tracking of \(\max\mathcal{L}_t\) (Eq. 9) and the restart condition in lines 7–9 of Algorithm 2 could be described more explicitly for implementation clarity.

## Nice-to-Haves

- A small synthetic simulation on the motivating example (\(d_t = Dt/T\)) would illustrate the practical gap between static-regret baselines and the proposed dynamic-regret algorithm, strengthening the narrative.
- A brief discussion of whether the \(\log T\) overhead from the SOGD meta-algorithm (Theorem 4) could be removed via more recent meta-learning advances would be informative.
- Some intuition about the prospects and obstacles for extending the approach to general convex capacity constraints would enrich the limitations discussion.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's concern about Lemma 1 proof being in the appendix**: The paper states "All omitted proofs are given in the appendix" — this is standard practice in CS theory papers. The appendix exists in the original submission but is stripped by the parser. Per policy, criticisms about missing proofs in appendix must be removed.

- **Harsh critic's concern about the doubling trick proof**: Same as above — appendix-deferred. Removed.

- **Strength Finder's generic framing**: No strengths were removed; all six are concrete and grounded in specific theorems, lemmas, and sections of the paper.

- **Demand for confidence intervals, user studies, or empirical validation in a theory paper**: These are not standard expectations for a theory contribution. Removed.

## Novel Insights

The paper's reduction of OIO to SOCO via the two-stage projection (Lemma 1) is genuinely novel and may have broader implications. By showing that the carryover constraint produces a switching cost whose coefficient is bounded by the sell-out period \(L_{\max}\), the paper opens the door to applying the rich SOCO toolkit to inventory problems. The observation that this connection runs in both directions — the OIO lower bound directly implies a new SOCO lower bound (Corollary 1) — is elegant and suggests the two problems share deeper structural commonalities than previously recognized.

## Suggestions

- Consider adding a proof sketch of Lemma 1 in the main body (even 4–5 lines of key inequalities) to make the paper more self-contained without depending on the appendix for the central insight.
- Clarify in the main text how \(\max\mathcal{L}_t\) is maintained incrementally with \(\mathcal{O}(N)\) memory, since the paper mentions this only briefly.
- In the comparison with Hihat et al. (2023), explicitly note the constraint-class difference (linear vs. convex) when discussing the \(\sqrt{L_{\max}}\) improvement.

## Score and Decision

**Round 1 bracketing**: The three queries returned weak anchors (3.00), middle anchors (4.50–6.50), and strong anchors (8.00). The paper clearly sits above the middle band — it is stronger than the 4.50 and 5.25 anchors (which had incremental contributions and unclear novelty) and comparable to or above the 6.25–6.50 anchors. **Initial bracket: 6.5–8.0**.

**Round 2 narrowing**: Anchors in (6.0, 7.5) included iZgECfyHXF (6.50, online nonconvex optimization with matching lower bounds), RR70yWYenC (6.25, continual finite-sum minimization), and wISvONp3Kq (7.33, sparse GLMs with varying observations). Anchors in (6.5, 8.0) included FCMpUOZkxi (6.75, contextual bandits with knapsacks) and jeMZi2Z9xe (6.75, adversarial bandits).

The paper is clearly stronger than iZgECfyHXF (6.50): both provide matching lower bounds and optimal algorithms, but this paper additionally connects two problem domains (OIO ↔ SOCO) and resolves an explicitly stated open question. The paper is comparable to wISvONp3Kq (7.33): that paper has both theory and real experiments with a novel methodology; this paper is pure theory but has matching lower bounds and a deeper structural insight. The paper is stronger than FCMpUOZkxi (6.75), which had more limited novelty per reviewers.

Anchor comparison summary:
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| J7hbPeOZ39 | 3.00 | 1 | Much weaker — different problem, limited contribution |
| Rdb0HxGJa3 | 4.50 | 1 | Weaker — incremental contribution, unclear motivation |
| WIerHtNyKr | 5.25 | 1 | Weaker — modular but incremental, limited novelty |
| RR70yWYenC | 6.25 | 2 | Weaker — narrower problem, no matching lower bound |
| iZgECfyHXF | 6.50 | 1,2 | Comparable but this paper is stronger: connects two domains, resolves open problem |
| cUN8lJB4rD | 6.50 | 2 | Weaker — narrower scope, more specialized |
| FCMpUOZkxi | 6.75 | 2 | Weaker — more limited novelty per reviewers |
| wISvONp3Kq | 7.33 | 2 | Comparable: that paper has experiments + theory; this paper has matching lower bound + deeper structural insight |
| 5t57omGVMw | 8.00 | 1 | Stronger — more novel application, cleaner results |

The paper sits between the 6.50–6.75 anchors (clearly stronger) and the 8.00 anchor (clearly not at that level). It is comparable to wISvONp3Kq (7.33) but slightly weaker due to being theory-only with a linear constraint limitation. **Final score: 7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>