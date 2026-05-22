Now I have enough information for calibration. Let me compile the final review.

**Calibration Summary:**

Round 1 bracketing established the paper is above 3.5 (better than the weak inventory/bandit papers scoring 2.5-3.33) and well below 8.0 (those anchors are completely unrelated topics). The plausible range is 5.0–7.5.

Round 2 narrows this to 6.0–7.0. The paper is stronger than the 5.33 anchor (Reusable Resource Allocation, Rejected) and comparable to or slightly stronger than the 6.0 anchors (Discounted OCO, Online DFL, Controlling LDS — all Accepted Poster). Key differentiators: this paper has **both** a novel problem reduction (OIO→SOCO via two-stage projection) **and** a matching lower bound resolving an open question, which are stronger contributions than the incremental algorithmic improvements in the 6.0 anchors. The lack of experiments is acceptable for pure theory.

---

## Summary

This paper studies Online Inventory Optimization (OIO) under adversarial, non-stationary demand. The authors propose a two-stage projection strategy that decouples the carryover-stock constraint from learning, proving that OIO regret can be bounded by the regret of a Smoothed OCO (SOCO) base learner with switching costs proportional to \(L_{\max}\). By combining this reduction with a doubling trick for unknown \(L_{\max}\) and existing SOCO algorithms (OGD/SOGD), they obtain the first near-optimal dynamic regret bound \(\tilde{\mathcal{O}}(\sqrt{L_{\max}(1+P_T)T})\) and a static regret bound \(\mathcal{O}(\sqrt{L_{\max}T})\) that improves on prior work by \(\sqrt{L_{\max}}\). A matching lower bound \(\Omega(\sqrt{L_{\max}T})\) resolves the open question from Hihat et al. (2023).

## Strengths

1. **First near-optimal dynamic regret for OIO.** Theorem 1 (informal) and Theorems 3–4 provide the first dynamic regret guarantees for this setting. Table 1 confirms no prior work gives any dynamic regret bound for OIO.

2. **Novel reduction from OIO to SOCO via two-stage projection.** Lemma 1 (Section 4.1) is the core technical insight: it bounds the projection error by a switching-cost term proportional to \(L_{\max}\), transforming the challenging carryover-stock constraint into a standard SOCO problem. Remark 4 explicitly states this eliminates the difficulty of dynamic carryover constraints.

3. **Matching lower bound resolves an open question.** Theorem 5 proves \(\Omega(\sqrt{L_{\max}T})\) for static regret, showing the \(\sqrt{L_{\max}}\) factor is unavoidable. The paper explicitly notes this resolves the open question raised by Hihat et al. (2023).

4. **\(\sqrt{L_{\max}}\) improvement in static regret.** Table 1 shows the static regret improves from \(\mathcal{O}(L_{\max}\sqrt{T})\) (Hihat et al., 2023) to \(\mathcal{O}(\sqrt{L_{\max}T})\) — a \(\sqrt{L_{\max}}\) improvement — while extending to multi-item settings with convex losses under adversarial demand.

5. **Clean separation of concerns in algorithm design.** Algorithm 2 feeds subgradients to a SOCO base learner that is completely agnostic to the carryover constraint, then projects the output onto \(\mathcal{C}(x_{t+1})\). This simple architecture is the key enabler of the dynamic regret result and is clearly explained.

## Weaknesses

### Fatal
None.

### Major
None that are verifiable from the paper as written.

### Minor

1. **Theorem 2's assumptions may not align cleanly with the concrete base learners.** Theorem 2 assumes the switching cost satisfies \(\|\hat{y}_t - \hat{y}_{t+1}\|_1 \le O(L^{-\beta})\) where the bound depends only on \(L\). For the OGD base learner used in Theorem 3, the switching cost \(\eta\|g_t\|_1\) depends on both \(L\) (through \(\eta \propto 1/\sqrt{\sqrt{N}L+1/2}\)) and \(T\) (through \(\eta \propto 1/\sqrt{T}\)). The paper presents Theorems 3 and 4 as direct bounds for the combined system, so the main results do not actually depend on Theorem 2's assumption holding perfectly. However, the exposition in Section 4.2 presents Theorem 2 as a general framework and the subsequent subsections as instantiations, without clarifying whether Theorems 3–4 follow from Theorem 2 or are proven independently. This creates an unjustified impression of modularity and could confuse readers. The authors should clarify the logical dependency (or lack thereof) between Theorem 2 and the concrete bounds.

2. **Corollary 1's justification is logically valid but stated too tersely.** The argument — that a SOCO algorithm with \(o(\sqrt{LT})\) regret would, when plugged into Algorithm 2, violate the OIO lower bound — is a standard reduction argument and is logically sound. However, the one-sentence justification ("if there were an algorithm that can be improved upon, it can break the lower bound") is too brief and risks misleading readers who expect an explicit SOCO instance construction. Expanding this to a short paragraph would improve clarity and prevent misinterpretation.

3. **The capacity constraint difference is acknowledged but could be more prominent.** Remark 2 correctly notes that Hihat et al. (2023) assumes a general convex constraint while this paper uses a linear-sum constraint. When the paper claims a "\(\sqrt{L_{\max}}\) improvement over existing works" (Section 1.1), it would be more accurate to state this more precisely: the improvement is achieved under a linear capacity constraint, which is a special case of the convex constraint studied by Hihat et al. This is not a flaw — the paper is transparent about the difference — but the phrasing in the narrative slightly overclaims.

### Trivial

- The paper provides sketch-level descriptions of Lemma 1 and the cycle construction but defers all proofs to the appendix. While acceptable for a theory paper at a conference, including a proof sketch for Lemma 1 in the main text would improve readability.
- The computational overhead analysis (\(\mathcal{O}(T\log T)\) per round) is mentioned briefly; a more explicit statement about the total cost including doubling-trick restarts would aid practitioners.

## Nice-to-Haves

- A brief illustrative example (e.g., the linear-trend demand from the introduction) showing how the cycle lengths behave and how the doubling trick adapts would help build intuition without requiring experiments.
- The paper assumes known horizon \(T\); a note on extending to unknown \(T\) via a standard doubling trick for \(T\) would be a useful addition.

## Removed Points

- **Switching-cost assumption is "fatal" or "structural":** The harsh critic characterized Issue 1 as potentially breaking the central regret bound. This is overblown: Theorems 3 and 4 provide direct bounds for the combined system without relying on Theorem 2's specific decomposition. The critic acknowledges "the proof details are in the appendix (which I cannot check) — this gap may be a correctable exposition issue." This is at most a minor exposition concern, not a fatal flaw. **Moved to Minor #1.**

- **Corollary 1 is unsubstantiated / non sequitur:** The reduction argument is logically valid. A SOCO algorithm with \(o(\sqrt{LT})\) regret would, via Algorithm 2 with overhead \(L_{\max}\log L_{\max} = o(\sqrt{L_{\max}T})\) for large \(T\), violate Theorem 5. This is a standard lower-bound transfer via reduction. The critic's claim that "a reduction from OIO to SOCO yields an upper bound for OIO; it does not embed the OIO lower bound into SOCO" is technically wrong — lower bounds can be transferred via reductions. **Removed.** (The expanded version appears as Minor #2 since the exposition is indeed too brief.)

- **Comparison with existing bounds should acknowledge capacity constraint difference:** This is already done in Remark 2 and the Table 1 caption. The critic's concern is that the narrative phrasing in Section 1.1 could be more precise. **Moved to Minor #3.**

- **Missing related works, missing appendix, formatting/style nitpicks:** Removed per hard rules.

- **Generic strengths** from the Strength Finder (e.g., "realistic subgradient observation," "extension to high-probability bounds," "reasonable computational overhead"): These are not core contributions and are dropped.

## Novel Insights

The paper's key observation — that the carryover-stock constraint in OIO can be reinterpreted as a switching cost in a SOCO problem — is the genuinely novel insight. The two-stage projection strategy (Algorithm 2, lines 10–11) is elegantly simple once stated but non-obvious: the base learner operates in a relaxed feasible set \(\mathcal{C}(0)\) that ignores carryover stock, and the projection onto \(\mathcal{C}(x_{t+1})\) introduces a regret penalty that Lemma 1 bounds using cycle lengths. This connects two previously separate literatures (inventory management and smoothed OCO) in a way that is both theoretically productive and algorithmically clean.

## Suggestions

1. Clarify the relationship between Theorem 2 and Theorems 3–4: state explicitly whether the concrete bounds follow from Theorem 2 or are proved independently, and if the latter, acknowledge that Theorem 2 serves only as a conceptual framework.
2. Expand the argument for Corollary 1 to a short paragraph with precise statements about the overhead and the contradiction.
3. In the narrative of Section 1.1, when claiming the \(\sqrt{L_{\max}}\) improvement, add a parenthetical noting that the comparison is to Hihat et al.'s result for convex constraints while the current paper assumes a linear constraint (already stated in Remark 2 but worth flagging earlier).

## Score and Decision

### Round 1 bracket
Weak anchors (topics similar to OIO/inventory): 2.50–3.33 → paper is clearly above these.
Middle anchors (OCO/dynamic regret/resource allocation): 4.00–6.00 → paper sits in or above this band.
Strong anchors (7.5+): all unrelated topics → no useful comparison.

**Initial bracket:** [5.5, 7.0]

### Round 2 narrowing
Compared against anchors at 5.33 (Online Reusable Resource Allocation, Rejected), 6.00 (Discounted OCO, Poster; Online DFL, Poster; Controlling LDS, Poster), and 6.50 (Online RL Sample Complexity, Poster).

The paper is stronger than the 5.33 anchor (which was rejected due to unclear contributions and presentation issues). It is comparable to or slightly stronger than the 6.0 anchors: it has a more novel problem formulation (first dynamic regret for OIO, matching lower bound) than the 6.0 papers, which primarily extend existing techniques to new sub-problems. The pure-theory nature without experiments is acceptable for this kind of contribution. The paper sits slightly above the median 6.0 anchor papers.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>