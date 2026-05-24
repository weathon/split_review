Now I have a thorough understanding of the paper. Let me compose the final review.

## Summary

This paper addresses Online Inventory Optimization (OIO), an extension of Online Convex Optimization (OCO) with carryover stock constraints. The key contributions are: (1) a two-stage projection strategy that reduces OIO to Smoothed Online Convex Optimization (SOCO), enabling the first dynamic regret guarantee for OIO: $\tilde{\mathcal{O}}(\sqrt{L_{\max}T(1+P_T)})$; (2) a $\sqrt{L_{\max}}$ improvement in static regret from $\mathcal{O}(L_{\max}\sqrt{T})$ to $\mathcal{O}(\sqrt{L_{\max}T})$; and (3) a matching $\Omega(\sqrt{L_{\max}T})$ lower bound, establishing near-optimality.

## Strengths

- **First dynamic regret algorithm for OIO.** Theorem 1 and Theorem 4 provide the first dynamic regret guarantee for the OIO setting. Prior work (Hihat et al., 2023) only achieved static regret, which the paper shows can be $\Omega(T)$ under demand fluctuations (Section 1 example). The paper clearly motivates why the dynamic carryover stock constraint prevents straightforward application of standard two-layer meta-algorithms.

- **Near-optimality established via matching lower bound.** Theorem 5 gives $\Omega(\sqrt{L_{\max}T})$ for static regret, and the algorithm's upper bound in Theorem 4 ($\tilde{\mathcal{O}}(\sqrt{L_{\max}(1+P_T)T})$) matches this up to logarithmic factors. This resolves the open question raised by Hihat et al. (2023).

- **Clean conceptual reduction from OIO to SOCO.** Lemma 1 shows that, under the two-stage projection (Algorithm 2), the OIO regret decomposes into the base learner's regret plus a switching-cost term proportional to cycle lengths. Remark 4 explicitly articulates this connection. This framing is non-obvious and lets the paper leverage existing SOCO theory rather than building a specialized algorithm from scratch.

- **Adaptivity to unknown problem parameters.** Algorithm 2 uses a doubling trick (lines 7–9) that does not require prior knowledge of $L_{\max}$ or $P_T$, and Theorem 4 shows the regret bound holds without these parameters. The SOGD base learner (Algorithm 5) removes the need to know $P_T$ a priori, which was required by the OGD version (Theorem 3).

- **Cross-connection lower bound for SOCO.** Corollary 1 derives an $\Omega(\sqrt{LT})$ lower bound for SOCO as a consequence of the OIO lower bound, providing an interesting two-way connection between the problem settings.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No proof intuition for Lemma 1 in the main text.** Lemma 1 is the paper's core technical lemma — it bounds the projection error via switching costs and cycle lengths — yet the main text simply states it (lines 201–205) and moves on. There is no sketch, outline, or intuition for why the inequality holds, how the cycles relate to the projection, or how the derivation works. The paper says "All omitted proofs are given in the appendix" (line 221), but providing a 1–2 paragraph proof sketch for the central lemma would significantly improve reader trust and accessibility. This is especially important because the inequality's form (linking the projection error $\langle g_t, y_t - \hat{y}_t\rangle$ to switching costs $\|\hat{y}_t - \hat{y}_{t+1}\|_1$ weighted by cycle lengths) is non-trivial.

- **The SOGD base learner (Algorithms 4, 5) is described without adequate intuition.** The paper reproduces a complex meta-algorithm from Zhang et al. (2022a) involving combiners, Discounted-Normal-Predictor, conservative updating, and bit sequences (Eq. 11). The description is precise but dense, and no high-level explanation is given for why the architecture achieves the claimed bound or how the components work together. A reader unfamiliar with Zhang et al. (2022a) cannot follow the logic from the text alone.

### Trivial

- **Lemma 2 ("The cycle length is upper bounded by $L_{\max}$") is stated without any justification.** While the reasoning likely follows from Definition 1 (sell-out period), a brief sentence explaining the connection would help.

## Nice-to-Haves

- **A small synthetic simulation** illustrating the algorithm's empirical behavior (e.g., on periodic or piecewise-constant demand) would increase confidence in the practical viability of the approach. This is not required for a theoretical paper, and the absence is not a weakness, but a numerical illustration would strengthen the submission's impact.
- **A brief speculation on extending the linear capacity constraint to convex constraints**, building on the remark in Section 6, would be helpful for future work.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism about missing proofs in the appendix / inability to verify lemmas without the appendix.** The paper states (line 221) that all proofs are in the appendix; the appendix was stripped by the parser. Per policy, this cannot be held against the paper.
- **Criticism about the lower bound being stated without proof sketch.** Same reason — the proof is in the appendix.
- **Criticism about the doubling trick possibly restarting prematurely.** This is speculative; the paper's analysis (Theorem 2) provides formal guarantees for the doubling-trick mechanism, so the concern is not a verified flaw.
- **Criticism about no experimental validation.** Moved to Nice-to-Haves (theoretical paper, not required).
- **Strength: "this paper addressed an important problem"** — generic/superficial; removed.
- **Strength: "the problem is well-motivated"** — generic praise without a specific anchor to unique content; removed.

## Novel Insights

None beyond the paper's own contributions. The reviews affirm the core technical claims without uncovering a hidden tension or unstated implication beyond what the paper already articulates.

## Suggestions

- Add a 1–2 paragraph proof sketch after Lemma 1 in the main text, showing how the projection error accumulates over a cycle and why it relates to the switching cost. This would make the paper self-contained and significantly improve readability.
- Provide a brief high-level intuition for Algorithms 4–5: explain why a meta-algorithm with multiple experts and combiners is needed, and how the Discounted-Normal-Predictor adaptively weights experts to handle unknown $P_T$.
- Consider adding a brief justification for Lemma 2 immediately after its statement, connecting cycle lengths to the sell-out period definition.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>