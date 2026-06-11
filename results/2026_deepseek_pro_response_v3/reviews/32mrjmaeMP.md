Now I have all the data I need. Let me synthesize the final review.

**Anchor comparison summary:**

| Anchor | Score | Comparison to TAK |
|--------|-------|-------------------|
| τ-Jp (1VwWi6zbxs) | 6.00 | TAK directly solves τ-Jp's key limitation (data dependency) while matching/exceeding performance; TAK is stronger |
| TATR (q3ztjJRQuJ) | 5.75 | TAK has stronger theoretical contribution and more thorough experiments |
| Submodule Linearity (irPcM6X5FV) | 6.00 | TAK has more novel insight and more comprehensive evaluation; TAK is stronger |
| Attn-Only FT (dj0TktJcVI) | 6.25 | Both address weight disentanglement; TAK has comparable quality with a cleaner theoretical bridge to optimization literature |
| CAMEx (nT2u0M0nf8) | 6.67 | Comparable — both use curvature approximations (KFAC/Fisher); TAK has similar strengths and scope limitations |
| Partial Linearization (iynRvVVAmH) | 7.00 | Both solid papers with good ideas and evaluations; Partial Linearization has slightly more consistent reviewer endorsement and cleaner contribution |

TAK fits at **6.5**: clearly above the 6.0 cluster (solves a key limitation those papers had), comparable to CAMEx at 6.67, and not quite at the 7.0 level given the uncharacterized merging heuristic and narrower non-linear scope than framing suggests.

---

## Summary

This paper proposes TAK (Task Arithmetic with KFAC regularization), a dataless regularizer for weight disentanglement in task arithmetic. The core insight is that under linearized fine-tuning, representation drift regularization — originally data-dependent — simplifies to a quadratic form involving the Jacobian Gram matrix (a generalized Gauss-Newton matrix) evaluated only at the pre-trained weights. This eliminates the need for external task data after a one-time KFAC pre-computation. The paper introduces a Kronecker-factor merging heuristic yielding O(1) complexity in the number of tasks. TAK matches or exceeds the data-dependent τ-Jp baseline across three CLIP ViT scales, achieves state-of-the-art task negation, and exhibits strong robustness to task vector rescaling coefficients.

## Strengths

- **Clean theoretical connection between representation drift and curvature approximation (Section 3.1, Eq. 3):** Under linearized fine-tuning, the data-dependent representation drift penalty collapses into α²τᵀG(θ₀)τ where G is the Jacobian Gram matrix evaluated at θ₀ only. This is a non-obvious derivation that bridges two previously disconnected literatures — task arithmetic and second-order optimization — and immediately motivates the use of KFAC and other well-studied curvature approximations in a new context.

- **Strong empirical results in the linearized regime matching a data-dependent baseline while being dataless (Table 1):** TAK at α=1 achieves 85.8/97.6 (Abs/Norm) on ViT-B/32, matching τ-Jp's 85.0/97.4 despite τ-Jp requiring access to other tasks' training data. On ViT-L/14, TAK reaches 91.6/99.3, exceeding all baselines including τ-Jp (91.1/98.5). Results hold across all three CLIP ViT scales tested.

- **State-of-the-art task negation while being dataless (Table 2):** TAK achieves the lowest target accuracy (3.4 on ViT-B/32, 3.4 on ViT-B/16, 3.5 on ViT-L/14) while preserving the highest control accuracy, beating τ-Jp (6.7/4.7/3.7 target). The dataless property is particularly valuable for unlearning applications where control datasets like ImageNet are large and costly to share.

- **Convincing α-robustness eliminating held-out tuning (Figure 4a):** TAK with simple task arithmetic maintains near-peak accuracy across α ∈ [0, 2], while unregularized TA and post-hoc methods (TIES, TSV, ISO) exhibit sharp peaks followed by rapid degradation. This is a genuine practical advantage for settings where validation data is unavailable.

- **Mechanistic validation via task localization (Figure 5):** Histograms of ||J_θ f(x, θ₀) τ_t||² show that under TAK, outlier scores are pushed toward zero while unregularized linear FT shows broad, overlapping distributions. This directly connects empirical performance back to the theoretical mechanism in Section 3.1.

- **Thorough efficiency and ablation studies (Figures 6-8, Table 3):** KFAC pre-computation takes ~4 minutes with MC=1; compression via block-diagonalization reduces storage by 87% (~550→70 MB) with ~1 point accuracy loss; the regularizer remains effective when applied every 16 steps. The Diagonal GGN ablation in Table 1 quantifies the benefit of KFAC's intra-layer correlation capture over cruder approximations (85.8 vs 80.1 on ViT-B/32 at α=1).

- **O(1) aggregation validated across architectures (Table 3):** The accumulated regularizer incurs marginal gaps versus the idealized O(T) formulation — on ViT-B/16 and T5-base the accumulated version edges out the naïve version; on ViT-B/32 a small gap (~0.6–0.8 points) exists but accumulated still substantially outperforms all non-τ-Jp baselines.

## Weaknesses

### Fatal

None.

### Major

- **The Kronecker merging heuristic (Eq. 8) lacks analytical characterization and its failure modes are unexplored.** The proposed aggregation replaces Σ_t λ_t (B_t ⊗ A_t) with (Σ_t B_t) ⊗ (Σ_t λ_t A_t), which is not a mathematical identity — Kronecker products do not distribute over summation. The paper acknowledges this is a heuristic and validates it empirically in Table 3 across three model configurations (ViT-B/32, ViT-B/16, T5-base), but provides no analysis of when or why the approximation degrades. On ViT-B/32, the gap between the O(T) and O(1) formulations is ~0.6–0.8 absolute accuracy points. Since the O(1) complexity claim is one of the paper's two stated contributions, the absence of any characterization (analytical bounds on approximation error, dependence on task similarity or number of tasks) leaves practitioners without guidance on when the heuristic is safe beyond the tested settings.

### Minor

- **The scope of non-linear regime results is narrower than the framing could suggest, though the paper is transparent about the coupling.** The paper pairs TAK with Attention-Only Fine-Tuning in the non-linear regime, explicitly noting (line 227) that this "induces approximately linear fine-tuning dynamics" and that "our regularization is not theoretically exact in the non-linear regime." The rows in Table 1 are clearly labeled. However, the abstract's claim of "state-of-the-art results in task addition and negation" and the general discussion of "non-linear regime" could mislead a casual reader into thinking TAK has been shown to work with arbitrary non-linear fine-tuning, when in fact standard non-linear FT with TAK performs worse than random (Tab. 1, α=1).

- **The λ_t task-weighting scheme is stated without justification or ablation.** λ_t is set proportional to dataset size (line 145) with no justification for why dataset size should determine the importance of preserving a task's representations. Alternative schemes (uniform, inverse-frequency, learned) are not explored or discussed.

- **The β hyperparameter is underspecified.** β is introduced in Eq. (7) as controlling overall regularization strength, but the paper never reports what value(s) were used or whether results are sensitive to this choice. Given that β directly controls the trade-off between task performance and weight disentanglement, this is a gap in experimental reporting.

- **τ-Jp outperforms TAK on language tasks with only a post-hoc explanation.** On T5-base (Table 3a), τ-Jp achieves 81.3/100 vs TAK's 78.7/98.9. The paper attributes this to "textual domains may still benefit from even more accurate curvature estimation" (line 231), which is post-hoc. A more systematic investigation of whether this is a domain effect or a model-architecture effect would strengthen the analysis.

### Trivial

- **The conclusion lacks a discussion of limitations.** The paper's closing paragraph is forward-looking but does not acknowledge the heuristic nature of the merging scheme, the reliance on linearization for theoretical guarantees, or the quadratic memory scaling of KFAC factors with layer width.

- **The TaLoS comparison relies on numbers from the original paper (marked with †).** Different training protocols, hyperparameters, or data splits could explain part of the performance gap. This does not affect the paper's main comparisons (against Linear FT, τ-Jp, Diag. GGN), which are self-run.

## Nice-to-Haves

- **Variance estimates for main results:** Several comparisons in Tables 1–3 involve margins under one percentage point (e.g., TAK vs. τ-Jp on ViT-B/16 at α=1: 88.3 vs. 88.2). Reporting standard deviations across 3–5 seeds would strengthen confidence in close comparisons. However, single-run evaluation is standard practice in large-scale vision benchmarks of this type.

- **Characterize the merging approximation analytically:** A study of how ||Σ_t λ_t (B_t ⊗ A_t) – (Σ_t B_t) ⊗ (Σ_t λ_t A_t)|| behaves as a function of task count, task similarity, and layer type would illuminate when the heuristic is safe. Even a simple synthetic study or diagnostic measurements on the actual KFAC factors would be valuable.

- **Test on at least one larger model (e.g., ViT-H or T5-large):** The quadratic memory scaling with layer width is acknowledged and tested with compression on ViT-B/16, but scaling to larger architectures would further validate the method's practicality.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"No statistical significance or variance is reported"** — moved to Nice-to-Haves because single-run evaluation is standard in large-scale vision benchmarks of this type; demanding confidence intervals is not standard practice in this subfield (see soft rule on methodological practices not standard in the field).

- **"The abstract claims constant complexity but KFAC pre-computation is O(T)"** — the abstract's claim is about the multi-task regularization/aggregation step, not pre-computation. The introduction explicitly clarifies this distinction (line 31: "The per-task regularizers induce memory and computational costs that grow linearly... we propose an aggregation scheme... yielding constant complexity"). The harsh critic's objection is overly pedantic given this clear distinction; KFAC pre-computation is obviously O(T) since you must compute factors for each task.

- **"The Kronecker merging heuristic is mathematically unjustified"** — the paper never claims mathematical justification; it explicitly calls this a "heuristic" (line 151) and validates it empirically. The concern about limited validation scope is retained in the Major weakness above, but the framing of "mathematically unjustified" is misleading since the paper is transparent about the heuristic nature.

## Novel Insights

The paper's most novel contribution is the connection between representation drift regularization and curvature matrix approximation (Section 3.1). Under linearized fine-tuning, the data-dependent representation drift penalty simplifies to a quadratic form of the Jacobian Gramian evaluated at pre-trained weights only. This is a crisp, non-obvious derivation that bridges two previously disconnected literatures — task arithmetic and second-order optimization — and immediately motivates the use of KFAC and other well-studied curvature approximations in a new context. The insight that what was previously a data-access problem can be reframed as a curvature-estimation problem (for which a mature approximation toolkit already exists) is genuinely elegant.

## Suggestions

- Add an analysis (even a simple one) of the Kronecker merging heuristic's approximation quality: measure ||Σ_t λ_t (B_t ⊗ A_t) – (Σ_t B_t) ⊗ (Σ_t λ_t A_t)|| as a function of task count on the actual KFAC factors. This would transform the heuristic from a pure empirical claim into a better-understood approximation.

- Report the β values used and add a brief sensitivity experiment (e.g., a small sweep over β on one model) or at minimum state the chosen value and note that results are not highly sensitive to it.

- Add a brief limitations paragraph to the conclusion acknowledging the heuristic nature of the merging scheme and the reliance on approximately linear fine-tuning dynamics in the non-linear regime.

- In the abstract, consider qualifying "constant complexity" as applying to the multi-task regularization step specifically, to match the precision already present in the introduction.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>