Now let me run calibration searches to anchor the score.Now I have sufficient grounding for the final review. Let me compose it.

---

## Summary

RoPE++ proposes to reintroduce the imaginary component of the complex-valued attention dot product that standard RoPE discards. The core observation is elegant: the imaginary term equals standard RoPE applied to a query vector pre-rotated by −π/2, and its characteristic curve is sine-based (vs. cosine-based for real attention), causing it to assign comparatively higher weight to distant tokens. Two architectural variants are proposed: RoPE++_EC (equal KV cache, doubled Q-heads, doubled W_O) and RoPE++_EH (equal head count, halved QKV parameters and KV cache). Both are evaluated at 376M and 776M parameter scales on RULER, BABILong, and a suite of short-context benchmarks, with a noise-injection experiment providing mechanistic evidence for the functional role of imaginary heads.

---

## Strengths

- **Elegant, verifiable mathematical insight.** Equation 4 shows concisely that imaginary attention is equivalent to applying a −π/2 rotation to q_t before standard RoPE. This is computationally free and preserves the absolute/relative position decomposition of standard RoPE. The insight is non-trivial and directly actionable.

- **Well-motivated characteristic curve analysis.** Equation 5 derives the imaginary attention's characteristic function as a sine-integral, which decays more slowly than the cosine-based real characteristic curve. Figure 1 illustrates the contrast clearly. This provides a principled, mechanistically grounded reason to expect imaginary heads to aid long-range retrieval.

- **Strong noise-injection experiment (Section 5.2 / Figure 5).** Adding Gaussian noise to imaginary vs. real attention heads reveals a consistent ~5–8 point performance drop on RULER-4k when imaginary attention is corrupted, a gap that is parameter-independent and directly validates the claim that imaginary heads play a dominant functional role in long-context tasks. This is the paper's most convincing empirical evidence.

- **RoPE++_EC shows substantial long-context gains.** Table 2 shows RoPE++_EC outperforming vanilla RoPE on RULER by 6.2 points (376M) and on BABILong by 1.3 points (776M), and consistently dominating at 64k context length across both benchmarks.

- **Compatibility with Linear PI and YaRN (Table 3).** RoPE++_EC retains its advantage when combined with existing interpolation schemes, confirming generality and plug-and-play usability.

---

## Weaknesses

### Fatal
None.

### Major

- **W_O is doubled in RoPE++_EC but no parameter-matched ablation is provided.** Section 3.3 explicitly states: "W_o in RoPE++_EC is double-sized." This means RoPE++_EC has strictly more capacity in its output projection than vanilla RoPE. The paper frames the main comparison as "equal KV cache," which is a valid inference-efficiency framing, but does not control for the extra W_O parameters. A "RoPE-2xQ" baseline — doubling W_Q and W_O without adding imaginary attention — is necessary to attribute the RULER/BABILong gains to the mathematical structure rather than to additional capacity. Without it, the headline empirical claim (e.g., 376M RULER avg 25.0 for EC vs. 18.8 for RoPE) cannot cleanly be attributed to imaginary attention. This is the central gap in the empirical argument.

- **RoPE++_EH underperforms vanilla RoPE on BABILong at 776M, but this is not acknowledged.** Table 2 shows RoPE++_EH at 776M averaging 19.4 on BABILong vs. RoPE's 22.8 — a 3.4-point deficit across all context lengths in that benchmark. The abstract, introduction (line "RoPE++_EH achieves comparable performance"), and Section 4.3 do not acknowledge this divergence. The EH variant is the parameter-fair comparison (no W_O increase), so this underperformance directly weakens the "efficiency without loss" claim. The paper should honestly report this limitation and, ideally, discuss why imaginary attention may underperform on BABILong-style multi-fact reasoning relative to RULER-style single-fact retrieval.

### Minor

- **GPQA outlier at 776M Short is unreported.** Table 1 shows RoPE++_EH at 776M Short achieving a GPQA score of 15.8 versus RoPE's 25.8 — a ~10-point gap that is not mentioned anywhere in the text. Average scores (42.5 vs. 42.0) hide this substantial per-task divergence. The paper should flag this outlier and investigate whether it reflects instability, benchmark sensitivity, or a structural limitation of halving QK parameters.

- **Distributional assumptions in characteristic curve derivation are implicit.** The expectation E_{qk}[A^Im] ≈ K·c_Im(Δt) in Equation 5 requires that q and k be approximately isotropic and zero-mean so that cross-terms vanish. This assumption is non-trivial for trained representations and is never stated. The analysis is reasonable as intuition and is partially supported by Figure 5, but the gap between the theoretical model and the actual behavior of trained heads deserves an explicit caveat.

### Trivial

- The paper's framing of "irreversible information loss" in the abstract/introduction is technically accurate but slightly imprecise: the real attention already contains both sin- and cos-modulated terms (Equation 1), so "discarding the imaginary component" does not remove all phase information, only the sine-dominant characteristic curve.

---

## Nice-to-Haves

- A parameter summary table comparing W_Q, W_K, W_V, W_O, and KV cache sizes across RoPE, RoPE++_EH, and RoPE++_EC would make the fairness of each comparison immediately legible (the information is scattered across Section 3.3).
- Experiments at a larger scale (e.g., 3B+) would increase confidence that the gains are not scale-artifact.
- Discussion of why imaginary attention may help or hurt on multi-fact vs. single-fact long-context tasks (motivating the BABILong vs. RULER divergence) would substantially deepen the analytical contribution.
- Variance across seeds for short-context tasks (Table 1), where margins are often sub-1 point, would strengthen confidence in the claims.
- Addressing whether a standard RoPE model with a sufficiently expressive W_Q could learn the −π/2 rotation implicitly (and why the explicit mechanism provides inductive bias that training alone does not) would sharpen the theoretical contribution.

---

## Removed Points

*These points were considered but removed — treat with caution.*

- **Harsh critic's structural concern about W_Q doubling**: The critic claimed W_Q doubles in RoPE++_EC. This is incorrect: the paper explicitly states "Both RoPE++_EH and RoPE++_EC share W_q between the real and imaginary attention" (Section 3.3). The imaginary attention reuses W_Q via a parameter-free rotation. Only W_O doubles in EC. The W_Q part of this criticism is factually wrong and removed; the W_O part is retained above as a Major weakness.

- **Strength: "parameter-free augmentation"** — The Strength Finder claimed RoPE++ is "parameter-free." This is inaccurate for RoPE++_EC, where W_O doubles. Removed as partially misleading.

- **Strength: "superior empirical performance on long-context benchmarks" (EH)** — Conflicts with the verified BABILong 776M underperformance of EH. Removed for EC-only framing; retained more narrowly in Strengths as an EC result.

- **Harsh critic's concern that "RoPE-2xQ is missing"** — Partially mislabeled, since W_Q is shared; reframed as the actual missing control being RoPE with doubled W_O.

- **Harsh critic's concern about "should the model learn imaginary rotation implicitly"** — Speculation about what training could discover is not a verifiable weakness from the paper as written. Moved to Nice-to-Haves as a theoretical clarification suggestion.

---

## Novel Insights

The paper's most genuinely novel contribution, beyond the headline method, is the characteristic curve framework applied to the imaginary component (Equation 5 / Figure 1). The observation that the imaginary term has a sine-integral characteristic that decays substantially more slowly than the cosine characteristic of real attention is a clean, verifiable, and underexplored mathematical fact. Paired with the noise-injection diagnostic (which provides model-internal mechanistic evidence independent of parameter counts), this constitutes a principled case that real and imaginary heads specialize functionally — real heads prioritizing semantic locality, imaginary heads prioritizing global retrieval. This functional specialization picture could generalize to other architectural designs beyond RoPE.

---

## Suggestions

1. **Add a "RoPE-2xW_O" control** that doubles only the output projection without imaginary attention, trained under the same conditions. If RoPE++_EC outperforms it, the imaginary mechanism is confirmed as the source of the gain.
2. **Explicitly acknowledge and investigate the BABILong 776M gap for RoPE++_EH** (19.4 vs. 22.8), including a hypothesis about whether multi-fact reasoning tasks require local attention patterns that EH's halved K-heads cannot sustain.
3. **Comment on the GPQA outlier** at 776M Short for EH (15.8 vs. 25.8) — check if it is variance or a structural effect.
4. **Add a parameter count table** in Section 3.3 for clarity.
5. **State distributional assumptions** underlying Equation 5 explicitly.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| jp4pxKqCRW.md (Long-context extrapolation via periodic extension) | 2.50 | 1 (weak) | Weaker: modifies RoPE interpolation without pre-training scale or mechanistic analysis |
| 5dDYhvt6dY.md (Reinforced position embedding) | 3.00 | 1 (weak) | Much weaker: small-scale translation task, no LLM evaluation |
| OhauMUNW8T.md (Wavelet-based positional representation) | 5.25 | 1 (mid) | Comparable in scope, weaker in mechanistic validation and engineering design |
| t717joHHSc.md (Mitigate position bias) | 4.75 | 1 (mid) | Lower contribution: inference-time scaling trick without pre-training study |
| eoln5WgrPx.md (STRING - Shifted RoPE) | 6.50 | 1 (mid) | Comparable: also modifies RoPE for long context, but inference-only, no pre-training |
| Us1RXG1Ji2.md (TAPE - contextualized equivariant PE) | 6.00 | 1 (mid) | Comparable novelty but less focused mechanistic evaluation |
| GtvuNrk58a.md (Round and Round - RoPE internals) | 6.20 | 2 (narrow) | Most comparable: analyzes RoPE internals and proposes modification; uses larger model (7B) but has proof errors and narrower evaluation |
| JO7k0SJ5V6.md (Scaling Laws of RoPE extrapolation) | 5.00 | 2 (narrow) | Weaker: more empirical scaling study, less mechanistic insight |
| VkqqZcofEu.md (Controlled study on long-context extension) | 5.75 | 2 (narrow) | Weaker contribution: controlled comparison study without novel method |
| 1Iq1qIsc2s.md (Revisiting positional info - Flash Attention PE) | 6.33 | 2 (narrow) | Comparable: practical PE-with-flash-attention design paper, rejected due to novelty questions |

**Round 1 bracket:** 5.0–6.5

**Round 2 narrowing:** The most topically similar anchors are "Round and Round" (6.20, accepted) and "Scaling Laws of RoPE" (5.00, accepted). The paper under review is:
- **Stronger than** the Scaling Laws paper (5.00): more mechanism, more engineering design, fresh pre-training experiments
- **Comparable to** "Round and Round" (6.20): both analyze RoPE internals with mathematical rigor and propose modifications validated empirically; RoPE++ adds two engineering variants and the noise-injection experiment; "Round and Round" uses a larger model but has proof errors and narrower evaluation
- **Slightly below** "Round and Round" due to the unresolved W_O parameter confound in the headline EC result and the inconsistently framed EH BABILong gap

The paper makes a genuine, clean contribution: the imaginary-as-rotation insight is novel and actionable, the pre-training study is solid, and the mechanistic noise-injection experiment is a clear empirical plus. The two Major weaknesses (W_O ablation gap, EH BABILong misframing) are meaningful but fixable without requiring new conceptual work. Final score: **5.5**, borderline accept.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>