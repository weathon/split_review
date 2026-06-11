Now I have a thorough calibration. Let me compile the final review with score.

**Calibration summary:**

Round 1 bracket: **5.5–7.5** based on comparison with QFgbJOYJSE (5.75) and n7n8McETXw (6.50).

Round 2 narrowed: comparing against jwsPS8yRe4 (6.00, solid but less novel), aKJr5NnN8U (6.50, similar structure with gating mechanism and theory-experiment gap), and n7n8McETXw (6.50, very similar in spirit — first training dynamics analysis, one-layer, orthogonality, synthetic experiments). Our paper matches or slightly exceeds the 6.50 anchors due to the SSM-specific novelty, the explicit mechanism analysis (Corollaries 1-2), and honest experimental validation including position sensitivity.

**Final score: 6.5 | Decision: Accept**

---

## Summary
This paper provides the first theoretical analysis of training dynamics and ICL generalization for one-layer Mamba models on binary classification tasks with additive outliers. The key technical insight is a reduction (Equation 3) showing one-layer Mamba decomposes into linear attention multiplied by a sigmoid-based gating factor. The authors prove training converges under explicit conditions (Theorem 1), that the trained model generalizes to test prompts with distribution-shifted unseen outlier patterns (Theorem 2), and provide a mechanism analysis showing linear attention selects same-pattern examples while gating suppresses outliers and induces exponential positional decay (Corollaries 1-2). A controlled comparison with linear Transformers isolates the gating as the source of Mamba's robustness advantage: Transformers converge under milder conditions but break at α > 1/2, while Mamba tolerates outlier fractions approaching 100%.

## Strengths
- **First theoretical analysis of Mamba training dynamics for ICL (Theorems 1-2):** Prior theoretical work on Mamba (Li et al., 2024b; 2025b; Bondaschi et al., 2025) analyzed loss landscapes or expressivity but did not address whether SGD training converges to ICL-capable models. Theorem 1 provides explicit sufficient conditions — on batch size, outlier magnitude, prompt length, and iteration count — under which SGD-trained Mamba converges. Theorem 2 extends this to distribution-shifted test-time outliers.

- **Clean architectural reduction enabling unified analysis (Equation 3):** The derivation showing one-layer Mamba reduces to linear attention multiplied by a position-dependent sigmoid gating factor cleanly separates the two mechanisms, making the comparison with linear Transformers (which set G=1) both rigorous and simple.

- **Precise non-asymptotic outlier-robustness bound (Theorem 2):** The bound α < min(1, p_a·l_tr/l_ts) provides an explicit interplay between training outlier proportion, training prompt length, and test prompt length. When p_a·l_tr/l_ts ≥ 1, Mamba provably tolerates outlier fractions approaching 100%.

- **Mechanistic explanation with experimental validation (Corollaries 1-2, Figures 3-4):** Corollary 1 proves attention concentrates on same-pattern examples (≥ Θ(1)); Corollary 2 proves gating suppresses outliers (O(poly(M₁)⁻¹)) and imposes exponential positional decay (≥ Θ(1/2^{j-1})). Figures 3-4 confirm these patterns in 3-layer Mamba.

- **Controlled comparison isolating the gating effect (Theorems 3-4):** By analyzing the linear Transformer under identical data and training, the comparison cleanly shows the tradeoff: Transformers are easier to train (Theorem 3) but break at α > 1/2 (Theorem 4), while Mamba is harder to train but far more robust. Confirmed in Figure 2.

- **Honest empirical findings on position sensitivity (Table 1):** When outliers are positioned close to the query (CQ), Mamba's accuracy drops to 82.73% — a vulnerability the position-agnostic Transformer avoids. This enriches the theory by revealing a tension in the gating mechanism.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Theory-experiment gap on the α bound is unaddressed:** With p_a=0.6 and l_tr=l_ts=20, Theorem 2 guarantees robustness only for α < 0.6, yet Figure 2 shows Mamba maintaining error below 10⁻² at α ≈ 0.8 (Section 4.1). The paper claims consistency with Remark 5 without acknowledging this numerical discrepancy. While theory bounds are typically loose (sufficient, not necessary), the absence of discussion weakens the theory-experiment alignment the paper otherwise presents carefully.

- **The positivity condition on test-time outliers warrants more explicit qualification in the abstract/introduction:** Theorem 2 condition (a) restricts test outliers to positive-linear-combinations of training patterns (Σλ_i ≥ L > 0). While P1 (Section 3.1) and Remark 3 state this condition explicitly, the abstract presents robustness without this nuance. Outlier negations (e.g., -v₁^*) fall outside the guarantee, representing a meaningful restriction that would benefit from upfront acknowledgment.

- **The one-layer reduction collapses per-channel gating without discussion of what is lost:** Equation (3) simplifies to a single scalar gating function controlled by w = w_{d_0}, collapsing the full Mamba's per-channel selective scan (where each dimension j has its own Δ_{j,i}). The paper does not discuss which properties of the full Mamba architecture survive this reduction and which do not, though this is partially understandable given the one-layer scope is standard in the theoretical ICL literature.

### Trivial
None.

## Nice-to-Haves
- A brief speculative remark on what changes when the orthogonality assumption across patterns is relaxed.
- A note on whether the hinge-loss results are expected to carry over to cross-entropy.
- A brief theoretical bridge for why one-layer mechanism patterns propagate to the 3-layer experiments in Section 4.2.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **HC: Appendix E.1 derivation is inaccessible:** Removed per hard rule — the parser strips appendices from all papers; the derivation exists in the original submission.
- **HC: Notation poly(M₁^{κ_a}) is unusual:** Removed as notation nitpick — κ_a is a scalar constant (set to 2 in experiments), making this unusual but mathematically well-defined.
- **HC: A = -I_m is a further simplification beyond Gu & Dao's Theorem 1:** The paper explicitly states this is "for simplicity of analysis" — standard practice in theoretical work, not an error.
- **HC: Remark 5 "overstates" the α → 1 claim:** Verifiably incorrect. Remark 5 says "Mamba can remain robust when α goes to 1 (Condition (c))" — Condition (c) is α < min(1, p_a·l_tr/l_ts), which does approach 1 when p_a·l_tr/l_ts ≥ 1. Mathematically precise.
- **SF: Generic strengths about "addressing an important problem":** Removed as not concrete or paper-specific.
- **HC: Request for compute time analysis, testing on larger datasets, using larger models:** Removed — generic criticisms that could apply to virtually any paper.
- **HC: Concern about missing discussion of what happens when orthogonality is violated:** Moved to Nice-to-Haves — asking the paper to address what happens outside its stated assumptions is outside its scope.

## Novel Insights
Beyond the paper's own contributions, the review process surfaces an interesting tension: Mamba's sigmoid gating plays a dual role — suppressing outliers AND imposing exponential positional decay — which means the same mechanism that provides robustness also creates vulnerability to outlier placement near the query (Table 1, CQ at 82.73%). This is not a weakness of the theory but a nuanced prediction: Mamba's robustness advantage over Transformers is not uniform but distribution-dependent, richer than the headline "Mamba is more robust" suggests.

## Suggestions
- In Section 4.1, explicitly discuss the theory-experiment gap for α (bound at 0.6 vs. experiment showing good performance at 0.8), noting whether it reflects bound looseness or a more interesting generalization phenomenon.
- Add a brief paragraph in Section 2 or 3.3 discussing which properties of full Mamba (per-channel gating, selective scan) survive in the one-layer reduction and which do not, to help readers assess the scope of the architectural insights.
- In the abstract, add "positive-combination" before "outliers" (or equivalent) to match the precision of Theorem 2 condition (a).

---

## Anchor Comparison

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| 52XG8eexal | 4.00 | R1 | SSM+ICL construction; our paper adds training dynamics analysis and mechanism validation, clearly stronger |
| QFgbJOYJSE | 5.75 | R1 | SSM vs Transformer expressivity; our paper adds training dynamics analysis and experimental mechanism validation, stronger |
| jwsPS8yRe4 | 6.00 | R1/R2 | Transformer ICL classification theory; our paper adds SSM novelty, outlier analysis, and mechanism experiments, stronger |
| n7n8McETXw | 6.50 | R1/R2 | First training dynamics for CoT, similar structure/limitations (one-layer, orthogonality); comparable quality |
| aKJr5NnN8U | 6.50 | R1/R2 | Gating mechanism for ICL vs IWL, theory + experiments; similar weakness profile, comparable quality |
| ikwEDva1JZ | 6.50 | R1/R2 | ICL with representations; our paper has more explicit mechanism analysis and SSM-specific contribution, comparable |

**Round 1 bracket:** 5.5–7.5. Round 2 narrowed to 6.5 by direct comparison with the 6.50 anchors, which share similar scope, structure, and weakness profiles. The paper is comparable in quality to n7n8McETXw and aKJr5NnN8U, with the additional novelty of being the first such analysis for Mamba/SSM architectures.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>