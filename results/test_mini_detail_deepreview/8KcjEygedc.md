Now I have sufficient calibration data. Let me write the final review.

**My round-1 bracket**: Based on comparison with the anchors, I initially bracketed this paper between 4.5 and 6.5. The lower anchor at ~3.0 (disentangling data pruning paper, rejected at 3.0) is clearly weaker — that paper had confused framing and no real theory. The upper anchor at 7.0 (severing spurious correlations paper) is more empirical and thus different in kind. The most comparable papers are the RMT synthetic data paper (5.50, accepted), the data selection theory paper (5.50, accepted), and the grokking linear estimator paper (5.50, accepted).

**Round-2 narrowing**: Reading the RMT paper (5.50) and grokking paper (5.50) in full confirmed strong similarity in both contribution type and reviewer concerns. Both had: (a) clean theory in a simple model, (b) gap between toy setting and claimed real-world relevance, (c) intuitive core insight. The paper under review is comparable in quality but has slightly broader experimental scope (ImageNet + model collapse). However, it also has more ambitious/overclaimed framing. Overall, 5.5 is the right anchor.

---

## Summary

This paper develops an exact theoretical framework for data curation in high-dimensional binary classification with Gaussian features. It derives closed-form scaling laws (Theorems 1–3) characterizing test error under two pruning rules — label-agnostic and label-aware — and obtains a precise phase transition (Theorem 2): when the generator is strong, "keep hard" is optimal; when weak, "keep easy" is optimal. The theory is validated through synthetic experiments, ImageNet experiments showing the crossover, model collapse mitigation results, and a qualitative interpretation of recent LLM reasoning results (LIMO, s1).

## Strengths

- **Exact theoretical framework for data curation.** Theorem 1 gives a closed-form expression for limiting test error under label-agnostic pruning, characterized entirely by four scalars (p, γ, β, β̃) that capture the pruning strategy's effect. The extension to label-aware curation (Theorem 3) broadens the framework's scope to match practical settings like label verification.

- **Clean phase transition result (Theorem 2).** The paper precisely characterizes when "less is more" vs. "more is more": when the generator is strong (ρ → 1) and the oracle excellent (ρ_* → 1), the "keep hard" strategy uniquely minimizes test error; when the generator is weak (ρ < 1) but the oracle excellent, "keep easy" is optimal. This is stated as a crisp mathematical theorem with a clear proof sketch, not just a heuristic claim.

- **Synthetic validation matching theory.** Figure 1 shows theoretical predictions and empirical simulations on the same model across four regimes (small/large n × strong/weak generator), with error bars. The match between theory and simulation is clean, and the predicted "less is more" regime (bottom-left quadrant, p ≪ 1 optimal under strong generator + large data) is clearly demonstrated.

- **ImageNet experiments demonstrating crossover.** Figure 2 shows that when the generator is trained on 160K examples (weak), "keep easy" outperforms "keep hard"; when trained on 1.2M examples (strong), "keep hard" becomes superior — precisely matching Theorem 2's qualitative prediction.

- **Model collapse mitigation.** Figure 3 demonstrates that over six rounds of iterative pseudo-labeling on ImageNet, training on all data degrades from ~30% to ~52% error, while the "keep hard" strategy maintains stable error near ~30%. This connects the theory to a practical failure mode and provides actionable insight.

## Weaknesses

### Major

- **The theory-practice gap for the LLM claims is unbridged.** Section 4.2 and the abstract claim the framework "provides a principled explanation" for LIMO/s1 results, but the connection is entirely qualitative. The theory analyzes a linear classifier with Gaussian features and binary labels; the "generator quality" ρ becomes in the LLM context an unspecified "proficiency on a specific slice of test data" with no measurement, no mapping, and no testable prediction derived from the theory. The paper says LLM results are "aggregated from existing literature" and used for interpretation — this is post-hoc storytelling, not scientific validation of the theory. The paper would be significantly stronger if it either (a) reframed the LLM connection as a qualitative analogy with clear disclaimers, or (b) provided any measurable connection (e.g., estimating ρ from LLM behavior on standard benchmarks).

- **Empirical validation outside the theoretical model is too thin to stand alone.** The ImageNet experiments (Figure 2) are described in only a few sentences: "We use a pre-trained model as both the generator (w_g) and pruner (w_o)" — with no architecture specification, no description of how difficulty scores are computed, no details on the pruning oracle implementation, and no error bars on the crossover point (only on individual points). The model collapse experiment (Figure 3) similarly lacks dataset size, architecture, and ablation (does any curation prevent collapse, or specifically the "keep hard" strategy?). The paper defers details to Appendix B (which is stripped in this version), but the main text alone does not provide enough information to evaluate these experiments. For a paper that claims empirical validation as a main contribution (bullet 3 of contributions), this is insufficient.

### Minor

- **Theorem 1 is a black box in the main text.** The key functions m, m̃, r are said to be "explicitly determined" by constants in Eqn (8) but are deferred entirely to the appendix. A reader cannot evaluate the main theoretical result without consulting the appendix. At minimum, a qualitative description of how test error depends on (p, γ, β, β̃) should appear in the main text.

- **The core qualitative insight is well-known from prior work.** The conclusion that strong models benefit from hard examples (hard-negative mining) and weak models benefit from easy examples (curriculum learning) is already the implicit understanding in the field, given extensive prior empirical work (Sorscher et al., 2022, and decades of work on active learning/curriculum learning). The paper's contribution is in formalizing this in a specific model class — which is valuable — but the novelty of the *insight itself* is limited.

- **The LLM interpretation (Section 4.2) does not test the theory's predictions.** The paper does not measure ρ, ρ_*, or any other theoretical parameter for the LLMs it discusses. The interpretation that "for average AIME performance, the base LLM is a strong generator" and "for hard AIME questions, it is a weak generator" is plausible but entirely unsupported by any evidence from the theory. This section would be more honest as "analogy" rather than "explanation."

- **No sensitivity analysis for oracle quality (ρ_*).** Theorem 2 assumes ρ_* → 1 (near-perfect oracle). In practice, oracles are imperfect. How does the optimal strategy degrade as ρ_* decreases? The paper does not analyze this, limiting practical applicability.

### Trivial

- The random baseline is described as using an orthogonal pruner (ρ_* = ρ_g = 0) rather than true random subsampling. With isotropic Gaussian features this is equivalent, but the connection should be explicitly justified.

## Nice-to-Haves

- Include explicit formulas or at least a qualitative characterization of m, m̃, r in the main paper so Theorem 1 is self-contained.
- Compare to alternative data selection strategies (uncertainty sampling, diversity sampling, error-based pruning).
- Add finite-sample analysis or at least discuss how the φ → 0, λ → 0 limit used in Theorem 2 relates to finite-sample behavior.
- Provide confidence intervals or replication information for the ImageNet crossover point.

## Removed Points

These points were raised by the reviewers but are removed after verification with the paper:

1. **"Random" baseline is a strawman** (from Harsh Critic). REMOVED — The orthogonal pruner (ρ_* = ρ_g = 0) with isotropic Gaussian features selects examples based on a direction independent of the labeling functions, which IS effectively random selection. The criticism misunderstands the setting.

2. **Missing comparison to alternative data selection methods** (from Harsh Critic). REMOVED — This is scope creep: the paper's contribution is a theoretical framework for specific pruning rules, not a comprehensive benchmark of data selection methods.

3. **No error bars on crossover point in Figure 2** (from Harsh Critic). REMOVED — Error bars are shown on individual points, and the crossover is derived from the full curves; requesting error bars on a derived crossover point is not standard practice.

4. **Missing statistical significance** (from Harsh Critic). REMOVED — Single-run evaluation with error bars is standard in this setting.

5. **Criticism about missing Appendix content** (from Harsh Critic). REMOVED — The parser strips the appendix; it exists in the original submission.

6. **Assumption 1 is too restrictive** (from Harsh Critic). REMOVED — The paper explicitly acknowledges this and notes that the two main strategies (keep easy/keep hard) are symmetric, so the assumption is appropriate for the paper's scope.

7. Several generic strengths from the Strength Finder (e.g., "this paper addresses an important problem"). REMOVED — These are superficial and lack specific content.

## Novel Insights

None beyond the paper's own contributions. The calibration search did not surface a reviewer observation about this paper that the authors themselves do not already acknowledge in their limitations section.

## Suggestions

1. **Reframe the LLM connection.** Move the LLM discussion (Section 4.2) from "reconciliation/explanation" to "qualitative analogy / speculation" with a clear disclaimer that the theory does not apply to transformer-based reasoning but offers a useful conceptual lens. This would eliminate the most significant overclaim without removing any actual content.

2. **Expand the ImageNet and model collapse experimental descriptions** in the main text. Provide architecture details, difficulty score computation, pruning oracle implementation, and at minimum one sentence about experimental setup per figure. If these details are already in the appendix (which is stripped here), add a brief summary to the main text.

3. **Make Theorem 1 slightly less of a black box.** Even a sentence like "The test error depends monotonically on p (pruning ratio) and γ (second moment of retained features), with the Stieltjes transform m capturing the spectral deformation due to pruning" would help readers who do not go to the appendix.

## Score and Decision

The paper makes a clean theoretical contribution to understanding data curation in a tractable model class. The exact formulas and clear phase transition (Theorem 2) are valuable. However, the paper overclaims the practical reach of its results, particularly the LLM connection, and the empirical validation outside the toy setting is thin. In quality it is comparable to other accepted theory papers in the calibration set (e.g., the RMT synthetic data paper at 5.50, the grokking linear estimator paper at 5.50) — similar technical quality, similar gap between toy setting and real-world claims.

**Anchors used across rounds:**

*Round 1 (Bracketing):*
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EOPLy80bBm.md` — avg 3.00, Reject. Data pruning for fine-tuning, purely empirical with confused framing. Clearly weaker than the paper under review.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/I9Dsq0cVo9.md` — avg 5.50, Accept. RMT-based theory for synthetic data + pruning in linear models. Very similar technical approach and scope. Reviewer concerns about Gaussian assumptions and theory-practice gap mirror those in this review. Comparable quality.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/HhfcNgQn6p.md` — avg 5.50, Accept. Data selection theory with both low/high-dim analysis. Similar theoretical contribution with concerns about toy setting vs. real claims. Comparable quality.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Bk13Qfu8Ru.md` — avg 7.00, Accept. More empirical paper on data pruning for spurious correlations. Different type of contribution (empirical, not theory), less directly comparable.

*Round 2 (Narrowing):*
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GH2LYb9XV0.md` — avg 5.50, Accept. Grokking in linear estimators. Same pattern: clean theory in toy model, gap between model and claimed real phenomenon, accepted despite concerns. Very similar quality level and reviewer criticism profile.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4vzGQcVUG8.md` — avg 6.50, Accept. Weak-to-strong generalization theory with Gaussian covariates. Slightly cleaner theoretical framing and less overclaiming. The paper under review is slightly weaker due to more ambitious claims without supporting evidence.

The paper sits within the 5.0–6.0 range, anchored at 5.5 by the most comparable accepted papers. It is stronger than the rejected 3.0 anchor, comparable to the accepted 5.5 anchors, and slightly weaker than the 6.5 anchor (which had cleaner framing). For ICLR, this is a marginal accept — the theoretical core is solid and publishable, but the framing needs adjustment.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>