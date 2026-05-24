Now I have a comprehensive understanding of the paper and the calibration anchors. Let me synthesize the final review.

**My analysis of the harsh critic's points against the paper:**

1. **β missing from main text**: The paper introduces β in Eq. (7) and mentions it controls regularization strength. The value is likely in the stripped appendix. Per the rules, I should remove criticisms based on missing appendix content. However, the point that β should ideally be mentioned in the main text is a valid minor presentation concern.

2. **Kronecker accumulation heuristic**: Valid concern about theoretical justification, but the paper provides empirical validation on 14 tasks (8 vision + 6 language) showing minimal gap. The harsh critic overstates the issue — the gap is 0.6 on ViT-B/32, and on ViT-B/16 and T5-base, TAK actually slightly outperforms the naïve version.

3. **Method tied to linearized/attention-only FT**: The paper explicitly acknowledges this limitation. The non-linear results (Table 1) show TAK + attention-only FT works effectively. The critic's point is not wrong but is already addressed.

4. **ISO degradation**: A 0.2 point drop (84.4→84.2) is negligible noise. The paper's characterization is accurate. Remove this.

5. **MC sample deterioration**: The paper acknowledges this as "surprising" and offers speculation. Valid minor point.

6. **λ_t weighting**: Minor point about design choice explanation.

Now let me write the final review.## Summary

This paper proposes TAK (Task Arithmetic with KFAC regularization), a dataless regularizer for task arithmetic that penalizes representation drift without requiring access to other tasks' training data. The key insight is that under a linearized model, representation drift simplifies to a quadratic form involving the network Jacobian's Gramian (an instance of the generalized Gauss-Newton matrix). By approximating this with Kronecker-factored approximate curvature (KFAC) and proposing a Kronecker-factor merging scheme that yields constant complexity in the number of tasks, the authors obtain a practical regularizer. Experiments on CLIP vision benchmarks (ViT-B/32, B/16, L/14) and T5-base language tasks show TAK matches or exceeds data-dependent baselines like τ-Jp while being dataless, and exhibits strong robustness to the task-vector scaling coefficient α.

## Strengths

**1. Dataless regularization that matches or exceeds data-dependent methods.** TAK achieves state-of-the-art results on the 8 Vision benchmark for task addition (Table 1) and task negation (Table 2) without using any external task data. For ViT-B/32 task addition, TAK reaches 86.0% absolute accuracy vs. 85.6% for τ-Jp (which requires data); for negation, TAK drives target accuracy to 3.4% (better forgetting) while τ-Jp only reaches 6.7%.

**2. Constant-complexity scaling via Kronecker-factor merging.** The accumulation heuristic (Eq. 8) reduces storage and computation from O(T) to O(1) with negligible performance loss across all tested settings. Table 3 shows the accumulated regularizer closely matches the naïve multi-task formulation (ViT-B/16: 88.3 vs. 88.1; T5-base: 78.7 vs. 78.5).

**3. Robustness to task-vector rescaling eliminates held-out tuning.** TAK maintains stable accuracy across a wide α range (α ∈ [0, 2]) while competing methods peak sharply then degrade (Figure 4a). Even with α=1 (no tuning), TAK rivals or exceeds the best tuned α of other methods (Table 1).

**4. Principled connection between representation drift and curvature matrices.** The paper derives the drift regularizer as a quadratic form of the Jacobian Gramian (Eq. 3) and identifies it as a GGN matrix, enabling use of established KFAC approximations (Sections 3.1–3.3). This theoretical link is novel in the task arithmetic context.

**5. Efficient and thoroughly analyzed curvature estimation.** KFAC matrices can be estimated with 128–256 examples and 1 MC sample per datum, requiring only ~4 minutes total for all 8 vision tasks (Figure 6b). Compression analysis (Figure 7b) shows KFAC storage can be reduced by 87% with only ~1 point accuracy drop.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

**1. The Kronecker-factor accumulation heuristic (Eq. 8) lacks theoretical analysis of its approximation error.** The approximation Σ_t B_t ⊗ A_t ≈ (Σ_t B_t) ⊗ (Σ_t λ_t A_t) is justified only by empirical validation on 8 vision + 6 language tasks. The paper does not provide error bounds, discuss conditions under which the approximation succeeds or fails, or analyze whether the gap might grow with more tasks. While the empirical results are encouraging (the gap is 0.6 points on ViT-B/32 and negligible or even slightly positive on ViT-B/16 and T5-base), a core contribution of the paper — constant-complexity scaling — would benefit from a stronger foundation.

**2. The method's theoretical correctness is tied to linearized or approximately-linear (attention-only) fine-tuning.** The regularizer derivation relies on the linearized model (Eq. 1–3), and the non-linear results are obtained by coupling TAK with attention-only fine-tuning. Many practical settings (full fine-tuning, LoRA, prompt tuning) are not covered. The paper acknowledges this limitation in the conclusion, but it does constrain the method's generality. The non-linear results (Table 1, bottom half) do show that TAK + attention-only FT is effective, but the scope of applicability remains narrower than competing methods like τ-Jp that work with arbitrary fine-tuning regimes.

**3. The Monte Carlo sample ablation (Figure 7a) shows a counter-intuitive pattern that is noted but not investigated.** Performance deteriorates when the number of MC samples exceeds 1–2, with the paper speculating about "variance across seeds." Since the exact GGN approximation is a better approximation in theory, this result warrants deeper analysis — or at minimum a more thorough discussion — to rule out implementation-specific artifacts.

**4. The task weighting scheme λ_t (Eq. 7) is set to dataset-size ratios without justification or sensitivity analysis.** The paper states λ_t = |D_{t'}| / Σ_{t≠t'}|D_t| but does not explain why this is a principled choice, nor does it test alternative weighting schemes or report sensitivity to this design decision.

**5. The β regularization strength is not stated in the main text.** While this detail likely resides in the appendix (which the PDF extraction strips), the main text should at minimum mention the chosen value or selection strategy. This is a minor presentation issue that does not affect the validity of the results.

### Trivial
None.

## Nice-to-Haves

- A bound (even loose) on the Kronecker accumulation approximation error, or a synthetic experiment with many (e.g., 50+) tasks to test whether the gap grows with task count.
- Experiments with full fine-tuning (even if the method is not theoretically exact) to characterize how performance degrades outside the linear regime, giving practitioners a clearer picture of when TAK can be applied.
- A sensitivity analysis or ablation on the λ_t weighting scheme.

## Removed Points

These points were raised by the reviewers but are removed or demoted for the following reasons:

- **"ISO achieves 84.4 without KFAC and 84.2 with KFAC — a small degradation that the paper does not remark on"**: The 0.2-point drop is negligible noise. The paper accurately notes that "ISO and TSV already perform competitively without it." Removed as a nitpick.
- **"The Kronecker accumulation heuristic is tested on only a small number of tasks (8 vision, 6 language)"**: 14 tasks across two modalities is a reasonable evaluation for this type of work. The criticism overstates the concern. Demoted to the general discussion; the substantive point about missing theoretical analysis is kept as a minor weakness above.
- **Criticisms about missing appendix content**: Per the rules, the parser strips appendix sections from all papers. Criticisms that presume information absent from the main text is missing from the submission entirely are invalid.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a theoretical or extensive empirical analysis of the Kronecker accumulation heuristic. Even a loose bound on the approximation error, or a simulation with many tasks, would significantly strengthen the "constant complexity" contribution.
2. Test TAK under standard (non-linearized) fine-tuning for a small number of steps, or with parameter-efficient methods like LoRA, to quantify the performance gap outside the linear regime and provide practical guidance.
3. Move the β value and selection strategy to the main text for reproducibility.

## Score and Decision

**Calibration report:**

All anchors retrieved across rounds:
- WM5G2NWSYC (avg 2.00, round 1, low band) — weak, not comparable
- HCCkCjClO0 (avg 3.00, round 1, low band) — weak, not comparable
- OW5Gf4cse1 (avg 3.00, round 1, low band) — weak, not comparable
- fUz6Qefe5z (avg 3.00, round 1, low band) — weak, not comparable
- **1VwWi6zbxs (avg 6.00, round 1, middle band)** — τ-Jp paper, directly comparable. This paper proposes a data-dependent regularizer for task arithmetic. Current paper is slightly stronger: dataless, more comprehensive experiments (vision + language), but has more constraints (linearization reliance).
- **dj0TktJcVI (avg 6.25, round 1, middle band)** — Attention-Only FT paper. Comparable contribution in task arithmetic space. Current paper has stronger theoretical grounding (curvature matrices) and more extensive ablations.
- yVGGtsOgc7 (avg 5.80, round 1, middle band) — Less directly comparable (disentangled representations, not task arithmetic).
- **q3ztjJRQuJ (avg 5.75, round 1, middle band)** — TATR paper, training-free merging. Current paper is more novel and thorough.
- STUGfUz8ob (avg 7.60, round 1, high band) — Not comparable (abstract reasoning in transformers).
- gc8QAQfXv6 (avg 9.00, round 1, high band) — Not comparable (function vectors for continual learning).
- nwDRD4AMoN (avg 9.00, round 1, high band) — Not comparable.
- hrqNOxpItr (avg 8.00, round 1, high band) — Not comparable.
- pAVJKp3Dvn (avg 5.67, round 2, middle band) — Not directly comparable (structured matrices).
- DwiwOcK1B7 (avg 6.33, round 2, middle band) — Not comparable.
- FT4gAPFsQd (avg 6.00, round 2, middle band) — Not comparable.
- irPcM6X5FV (avg 6.00, round 2, middle band) — Submodule Linearity paper. Directly relevant. Current paper is comparable in quality but addresses a different aspect of task arithmetic.
- LojXXo2xaf (avg 6.00, round 2, middle band) — Not comparable.
- GtpubstM1D (avg 5.71, round 2, middle band) — Not comparable.
- **iynRvVVAmH (avg 7.00, round 3, upper middle band)** — Partial Linearization paper. Higher-scoring but had significant novelty concerns from reviewers. Current paper's curvature-based approach has stronger novelty than that paper's adaptation of linearization to LoRA.

**Round 1 bracket**: I initially bracketed the paper between 5.5 and 7.5 based on the strong middle-band anchors (τ-Jp at 6.00, Attention-Only FT at 6.25).

**Round 2 narrowing**: Comparing against the directly comparable anchors (τ-Jp at 6.00, Attention-Only FT at 6.25, Submodule Linearity at 6.00, Partial Linearization at 7.00), the current paper sits solidly in the 6.0–6.5 range. It is stronger than τ-Jp (dataless advantage, broader experiments) and comparable to Attention-Only FT and Submodule Linearity. The Partial Linearization paper at 7.00 has some unresolved novelty concerns that make it an imperfect upper bound.

**Final score**: **6.0**. The paper makes a genuine contribution — the dataless curvature-based regularizer is well-motivated, the empirical validation is thorough, and the robustness to α is practically valuable. However, the Kronecker accumulation heuristic lacks theoretical backing, and the method's reliance on linearized/attention-only fine-tuning limits its scope relative to simpler alternatives. These limitations prevent the paper from reaching the 6.5–7.0 range but do not negate its clear merits.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>