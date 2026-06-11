Now let me finalize the review with the calibration results.

**Round 1 — Bracketing:** The paper sits above the middle-band anchors:
- TaLoS (5.50): TAK has stronger theory, broader experiments
- τ-Jp (6.00): TAK addresses its main limitation (data dependence) while matching performance
- Attention-Only FT (6.25): TAK is more principled and comprehensive

The strong band (>7.5) returned unrelated papers. **Initial bracket: 6.5–8.0.**

**Round 2 — Narrowing:**
- CAMEx (6.67): TAK is stronger — cleaner theory, stronger empirical results
- Parameter-Efficient Partial Linearization (7.00): TAK is stronger — more novel, better results
- Second-Order Model Compositionality (7.50): Most comparable paper. Both use curvature/second-order methods for model composition. The 7.50 paper has deeper theory but narrower experiments and some questionable assumptions. TAK has broader experiments, more practical impact (dataless, compression, α-robustness).

TAK is comparable to the 7.50 anchor but with a slightly different strength profile — less theoretical depth on the compositionality side but more practical breadth and cleaner empirical validation. **Final score: 7.0, Accept.**

## Summary

TAK proposes a dataless regularizer for task arithmetic that promotes weight disentanglement by penalizing a KFAC-approximated quadratic form of the Jacobian Gram matrix. Under linearized fine-tuning, representation drift regularization—previously requiring external task data—reduces to τ⊤G_t τ where G_t is a curvature matrix (GGN) that can be pre-computed and shared without data. A Kronecker-factor merging heuristic further reduces complexity from O(T) to O(1) in the number of tasks. The method matches or exceeds data-dependent baselines on task addition and negation across vision and language benchmarks while remaining robust to the scaling coefficient α.

## Strengths

- **Elegant theoretical reduction (Section 3.1, Eq. 3):** Under linearized fine-tuning, representation drift collapses exactly to a quadratic form involving the Jacobian Gram matrix, which is shown to be an instance of the GGN when the criterion is squared loss. The derivation is clean, exact under the stated assumption, and factors out data dependence entirely into a pre-computable curvature matrix.
- **State-of-the-art task addition results that match data-dependent methods while being dataless (Table 1, linearized regime):** TAK achieves 85.8/88.3/91.6 on ViT-B/32, ViT-B/16, and ViT-L/14 at α=1.0, essentially matching τ-Jp (85.0/88.2/90.9) which requires external task data, while substantially outperforming the diagonal GGN baseline (80.1/82.9/87.9).
- **Superior task negation with minimal collateral damage (Table 2):** TAK drives target-task accuracy down to 3.4–3.5% across all three ViT backbones while preserving control-task accuracy at or above the pre-trained level, outperforming τ-Jp and TaLoS on both axes.
- **Robustness to the scaling coefficient α (Figure 4a):** TAK maintains a flat, high accuracy profile across the full [0, 2] α range, in stark contrast to post-hoc merging methods and unregularized linear FT, which exhibit sharp peaks followed by rapid degradation. This eliminates the need for held-out α tuning.
- **Compelling task-localization evidence (Figure 5):** The distribution of ||J_θ f(x,θ_0)τ_t||² is sharply concentrated near zero for out-of-distribution inputs under TAK, while remaining spread for in-distribution inputs, providing direct evidence that the regularizer achieves its stated goal.
- **Practical efficiency demonstrated:** KFAC estimation requires only 128 examples and a single MC sample per task (~4 minutes total for 8 Vision tasks, Figure 6b). Block-diagonal compression achieves 87% storage reduction with only ~1 point accuracy loss (Figure 7b). The merged regularizer keeps training cost at O(1) in number of tasks (Table 3).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The KFAC merging heuristic (Eq. 8) lacks theoretical justification.** The approximation (∑ λ_t B_t ⊗ A_t) ≈ (∑ B_t) ⊗ (∑ λ_t A_t) is acknowledged as a heuristic with no derivation or error bounds. Table 3 shows the gap between the O(T) idealized formulation and the O(1) merged version is small for ViT-B/16 and T5-base (within 0.2 points) but larger for ViT-B/32 (0.7 point drop), suggesting architecture-dependent approximation quality. Providing even an empirical characterization of when this heuristic holds would strengthen the paper's central complexity claim.

- **No statistical dispersion reported for main results.** Tables 1–3 and Figures 2–4 present point estimates without standard deviations or confidence intervals. While most key comparisons involve margins of several points and are unlikely to reverse under seed variance, a few comparisons (e.g., TAK 88.3 vs. τ-Jp 88.2 on ViT-B/16) involve sub-point margins where variance information would aid interpretation.

- **Missing ablation in the non-linear regime.** The non-linear experiments pair TAK with Attention-Only Fine-Tuning, justified by prior work showing attention-only FT induces approximately linear dynamics. While the comparison "Attn. Only FT + TAK" vs. "Attn. Only FT" does cleanly isolate TAK's effect within the attention-only setting, a non-linear full FT + TAK ablation (even if expected to perform poorly) would clarify whether TAK's benefit in the non-linear regime depends on the parameter subset restriction rather than the regularizer itself.

### Trivial

- The diagonal GGN baseline is described as "inspired by" Porrello et al. (2025), leaving some ambiguity about whether it exactly replicates their method or is a simplified adaptation. Given that this baseline serves as the key ablation establishing that KFAC's richer structure matters, a precise specification would be helpful.

## Nice-to-Haves

- A discussion of conditions under which the linearization assumption may break down (learning rate, fine-tuning duration, distance from pre-trained weights), which would provide practical guidance for users.
- An analysis or hypothesis for the counterintuitive finding that more MC samples degrade KFAC-based regularization performance (Figure 7a, line 318).
- An empirical characterization of the merging heuristic's approximation error (e.g., Frobenius norm error between the true sum of Kronecker products and the merged surrogate) as a function of architecture size and number of tasks.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim that non-linear experiments "conflate the choice of regularization with the choice of which parameters to fine-tune, making it impossible to isolate the contribution of TAK."** REMOVED because the paper does isolate TAK: Attn. Only FT + TAK is compared directly against Attn. Only FT (no TAK), holding the parameter subset constant. The missing full FT + TAK ablation is noted as a separate minor concern above.
- **Harsh Critic comment about T5-base table layout in Table 2 being confusing (negation headers over addition results).** REMOVED as a formatting artifact likely introduced by the parser, not a paper error.
- **Harsh Critic point that "the task localization analysis... the causal direction is ambiguous."** REMOVED because this is not actually a weakness: the paper's claim is precisely that the regularizer causes this separation. The paper does not claim a "deeper structural property" beyond what the regularizer enforces; it presents the histograms as evidence that the regularizer works as intended.
- **Strength Finder claim that "this paper addressed an important problem" / "this paper targeted an interesting question."** REMOVED as generic/superficial strengths that lack concrete anchoring.

## Novel Insights

None beyond the paper's own contributions. The core insight—connecting representation drift regularization in task arithmetic to the well-studied problem of curvature matrix approximation—is the paper's novel contribution and is clearly articulated.

## Suggestions

- Add standard deviations or confidence intervals to the main result tables (at minimum Tables 1–3); this is the single highest-impact improvement to evidential rigor.
- Add a brief analysis of the merging heuristic's approximation quality, even if purely empirical (e.g., Frobenius norm error vs. number of tasks).
- Report the non-linear full FT + TAK result, even if it performs poorly; this would cleanly delineate the scope of the method's applicability.

## Calibration Anchors

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| TaLoS (TDyE2iuvyc) | 5.50 | R1 | TAK has stronger theory, broader experiments, better results |
| τ-Jp (1VwWi6zbxs) | 6.00 | R1 | TAK addresses τ-Jp's main limitation (data dependence) while matching performance |
| Attention-Only FT (dj0TktJcVI) | 6.25 | R1 | TAK is more principled (curvature-based rather than heuristic subset selection) |
| CAMEx (nT2u0M0nf8) | 6.67 | R2 | TAK has cleaner theory-to-practice pipeline and stronger empirical results |
| Partial Linearization PEFT (iynRvVVAmH) | 7.00 | R2 | TAK is more novel (not just applying existing method to a new adapter) |
| Second-Order Compositionality (OZVTqoli2N) | 7.50 | R2 | Most comparable. Similar quality; TAK has broader experiments, this paper has deeper theory |

The paper sits between the 7.00 and 7.50 anchors. The Second-Order Compositionality paper (7.50) has deeper theoretical analysis but narrower experiments with questionable assumptions. TAK has a cleaner derivation, broader empirical validation (vision + language, addition + negation, compression, efficiency), and more immediate practical impact. However, TAK's merging heuristic lacks theoretical justification and error bars are absent. **Final score: 7.0.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>