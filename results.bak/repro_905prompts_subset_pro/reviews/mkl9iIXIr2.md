Now I have a thorough understanding of the paper and the calibration landscape. Let me write the final consolidated review.

---

## Summary

This paper addresses online inventory optimization (OIO) in non-stationary environments. The core contribution is a two-stage projection algorithm that reduces OIO to smoothed online convex optimization (SOCO) by bounding the gap between feasible decisions and base-learner decisions via switching costs proportional to the cycle length (Lemma 1). This yields the first dynamic regret guarantee for OIO, Õ(√(L_max·(1+P_T)·T)), and improves the static regret bound by a √L_max factor over prior work. A matching lower bound of Ω(GD√(L_max·T)) (Theorem 5) establishes near-optimality of the L_max and T dependence, resolving an open question from Hihat et al. (2023).

## Strengths

- **Elegant reduction from OIO to SOCO (Lemma 1)**: The two-stage projection strategy bounds the gap ⟨g_t, y_t − ŷ_t⟩ by switching costs proportional to the cycle length L_t^i, explicitly linking the carryover-constrained OIO setting to SOCO with time-varying switching-cost coefficients. This is the paper's central technical insight and is genuinely novel.

- **First dynamic regret guarantee for OIO (Theorem 4)**: The algorithm achieves Õ(√(L_max·(1+P_T)·T)) dynamic regret by combining the reduction with SOGD as the base learner and a doubling trick, without requiring prior knowledge of L_max or P_T. No prior work had established any dynamic regret bound for this setting.

- **First lower bound for OIO resolving an open question (Theorem 5)**: The Ω(GD√(L_max·T)) lower bound matches the upper bound's dependence on L_max and T up to logarithmic factors, establishing near-optimality of the √L_max factor. This resolves the open question raised by Hihat et al. (2023). Corollary 1 further provides a lower bound for SOCO as a byproduct.

- **Parameter-free operation via doubling trick (Theorem 2)**: The algorithm handles unknown L_max by restarting the base learner when observed cycle lengths exceed the current estimate. Theorem 2 provides a generic bound on the overhead, making the method practical without sacrificing guarantees.

- **Clear positioning against prior work (Table 1)**: The paper concisely summarizes static regret bounds from eight prior studies, making the √L_max improvement and the extension to dynamic regret immediately visible.

## Weaknesses

### Fatal

None.

### Major

- **N-dependence gap between upper and lower bounds is not discussed**: The lower bound (Theorem 5) is Ω(GD√(L_max·T)) and contains no dependence on the number of items N. The upper bounds (Theorems 3 and 4), however, carry implicit √N factors through the ℓ₁/ℓ₂ norm conversion (line 130: "‖g_t‖₁ ≤ √N‖g_t‖₂ ≤ √NG") and an N^(1/4) factor in the SOGD bit signal (Eq. 11). The paper claims the upper and lower bounds "establish that Õ(√(L_max·T)) is nearly optimal" without qualifying that the lower bound's construction appears to be for N=1 while the upper bound's N-dependence is not claimed optimal. This weakens the tightness claim — the optimality of the N-dependence remains unresolved. The core contribution (L_max and T dependence) is unaffected, but the claim of near-optimality should be scoped explicitly.

### Minor

- **SOGD description is heavily compressed and reliant on external references**: Section 4.3 presents Algorithms 4 and 5 with minimal explanation of how the combiner's discounting and bit signal (Eq. 11) adapt to the OIO-specific switching-cost structure. The reader must consult Zhang et al. (2022a) to assess whether the adaptation is faithful. A paragraph summarizing the key inherited property would substantially improve self-containedness.

- **No proof sketches for central lemmas in the main text**: Lemma 1 (the critical bridge from OIO to SOCO) and Lemma 2 (cycle length bounded by L_max) are stated without any proof sketch. The paper notes "All omitted proofs are given in the appendix" (footnote 6), but the main text would benefit from a brief intuitive explanation — particularly why the cycle length appears as a multiplier on the switching cost in Eq. (7). This does not affect correctness but limits accessibility.

- **Linear capacity constraint is a restriction from prior work**: As the paper acknowledges (Section 6), the analysis relies on the linear capacity constraint ∑_i y_t^i ≤ D, whereas Hihat et al. (2023) handled general convex constraints. The paper argues the linear case is practically common and that the reduction via rescaling handles weighted sums, but the restriction is real and worth noting.

### Trivial

None beyond formatting artifacts attributable to the parser.

## Nice-to-Haves

- A minimal simulation with a simple non-stationary demand pattern (e.g., time-varying Newsvendor) comparing the algorithm against MaxCOSD or a static baseline would illustrate the practical benefit of dynamic regret and strengthen motivation. This is optional for a theory paper.

- A brief discussion of when the √L_max improvement is practically large (e.g., L_max ≫ 1) and the regime of T relative to L_max would contextualize the gain.

- Clarifying the norm used in the projection Π_{C(x_{t+1})} (presumably Euclidean) and any needed contraction properties would remove ambiguity.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Theorem 3 requires knowing P_T, which is unrealistic"** — REMOVED. The paper itself acknowledges this on lines 255–257: "To obtain the optimal regret order, we must know P_T a priori when setting the learning rate η. This parameter depends on the characteristics of the future demands and is sometimes difficult to determine in advance." Theorem 3 is explicitly presented as an illustration, with Theorem 4 removing this requirement. The critic's point is already addressed by the paper.

- **"The deterministic condition on L_max is very strong"** — REMOVED. The paper discusses this in context: Remark 3 provides a high-probability extension, and the lower bound establishes that sublinear regret is impossible when L_max = Ω(T). The paper explicitly notes that "L_max does not primarily constrain the fluctuations in demand."

- **"Projection norm never defined"** — REMOVED. Euclidean projection is standard convention in the OCO/SOCO literature, and the Π notation is universally understood. Moved to Nice-to-Haves as an optional clarification.

- **"Missing experiments"** — REMOVED as a weakness. This is a theory paper. Moved to Nice-to-Haves as an optional suggestion.

- **"Demand for proof sketches of Lemma 1 and 2 for self-containedness"** — PARTIALLY RETAINED. Kept as Minor because the lack of any sketch does reduce accessibility. But the harsh critic's framing as a significant evidential gap was softened — the appendix contains proofs; this is about exposition, not correctness.

## Novel Insights

The paper's most striking conceptual contribution is the demonstration that the carryover-stock constraint in OIO — which initially appears to create path-dependency that resists standard OCO techniques — can be exactly characterized through the lens of switching costs in SOCO, with the cycle length L_max serving as the natural scaling factor. This connection is bidirectional: not only does it allow importing SOCO algorithms into OIO, but the lower bound (Theorem 5) also yields a new lower bound for SOCO itself (Corollary 1), showing that one problem's hardness can illuminate the other. This bidirectional constraint of lower bounds — where a construction for OIO proves optimality of SOCO algorithms — is a rare and elegant structural finding.

## Suggestions

- Add a sentence or footnote explicitly noting that the lower bound of Theorem 5 is constructed for N=1 (or single-item), clarifying that the N-dependence in the upper bounds is not claimed optimal. Re-scope "near-optimal" to refer specifically to the L_max and T dependence.

- Add a short paragraph after Lemma 1 giving intuition: why does the projection error ⟨g_t, y_t − ŷ_t⟩ get charged to switching costs, and why does the cycle length appear as a multiplier? A concrete single-item example walking through a cycle would make the concept immediately accessible.

- For Section 4.3, add a short paragraph summarizing the key guarantee inherited from Zhang et al. (2022a)'s SOGD and how the OIO-specific modifications (ℓ₁ norm switching cost, time-varying coefficient L_t^*) affect the analysis, to reduce reliance on external references.

## Score and Decision

**Calibration summary:**

*Round 1 bracketing*: Initial bracket [5.5, 8.0]. The paper is clearly above middle-band anchors like WIerHtNyKr (5.25, non-stationary OCCO with incremental novelty concerns) and below the 8.0 anchors. The paper's elegant reduction, matching lower bound, and resolution of an open question place it above the 5.25–5.57 range.

*Round 2 narrowing*: Within [5.5, 8.0], the closest anchors are iZgECfyHXF (6.50, online nonconvex optimization with matching bounds but restricted lower-bound family), FCMpUOZkxi (6.75, CBwK, first results without feasibility), and OvU9u6wS2J (7.00, trading-volume maximization with tight bounds). The paper is stronger than iZgECfyHXF (unrestricted lower bound, cleaner reduction) and comparable to OvU9u6wS2J (elegant reduction, tight bounds, new perspective, but techniques are standard). The N-dependence gap prevents scoring at 7.5+, but the core contribution is solid.

*Anchor comparison table*:
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| WIerHtNyKr | 5.25 | R1 | Our paper is stronger: cleaner reduction, matching lower bound, resolves open question |
| ZJ9LglIakj | 5.25 | R1 | Our paper is stronger: dynamic regret (not static), matching lower bound |
| Rdb0HxGJa3 | 4.50 | R1 | Our paper is stronger: more impactful contribution |
| GGZISiwgNt | 5.57 | R1 | Our paper is stronger: matching lower bound, cleaner theoretical story |
| iZgECfyHXF | 6.50 | R2 | Our paper is comparable-slightly-better: unrestricted lower bound, but similar structure |
| FCMpUOZkxi | 6.75 | R2 | Our paper is comparable: both first results, ours has matching lower bound |
| OvU9u6wS2J | 7.00 | R2 | Our paper is comparable: both have elegant reductions, tight bounds, new perspectives |
| wISvONp3Kq | 7.33 | R2 | Our paper is slightly weaker: less polish, N-dependence gap unaddressed |
| A3YUPeJTNR | 8.00 | R1 | Our paper is weaker: less practical impact, more compressed exposition |
| 5t57omGVMw | 8.00 | R1 | Our paper is weaker: less polished, but different subfield |

**Final assessment**: The paper makes a notable theoretical advance — the first dynamic regret guarantee for OIO, an elegant reduction connecting two problem classes, a matching lower bound that resolves an open question, and an improvement over prior static bounds. The main weaknesses (undiscussed N-dependence gap, compressed SOGD exposition, missing proof sketches) are addressable and do not undermine the core contribution. The paper is well-motivated, technically sound in its visible structure, and valuable to the online learning for operations research community.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>