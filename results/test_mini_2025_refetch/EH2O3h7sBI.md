Now I have a good calibration. Let me produce the final consolidated review.

## Summary
This paper proposes Prompt Gradient Projection (PGP), combining prompt-tuning with gradient projection for continual learning. The key idea is to derive orthogonal conditions that prompt gradients must satisfy to prevent forgetting (Eq. 9: x_t Δp^T = 0 and p_t Δp^T = 0), then realize these conditions by performing SVD on an element-wise sum of the input and prompt spaces. PGP is evaluated on L2P, DualPrompt, and CLIP baselines across class-incremental, online class-incremental, and task-incremental settings.

## Strengths
1. **First principled analysis of anti-forgetting conditions for prompt-based continual learning.** The paper derives explicit orthogonal conditions (Eq. 9) that prompt gradients must satisfy to prevent forgetting, linking the self-attention mechanism to the gradient-projection framework. This goes beyond existing prompt-based methods that lack such formal treatment (Section 3.1).
2. **Consistent empirical improvements across diverse settings without task identifiers.** Across 10/20-Split-CIFAR100, 10-Split-ImageNet-R, and online benchmarks, PGP improves both accuracy and forgetting over L2P and DualPrompt (Tables 1 and 3). These gains are achieved without the task identifiers that prior gradient-projection methods (GPM, TRGP) require — a genuine advantage enabled by the prompt-tuning paradigm (Section 1).
3. **Systematic ablation study validates design choices.** Table 4 compares projection on prompt gradients only, key gradients only, and both, confirming that projecting both (l2p-pk) yields the strongest anti-forgetting. Task-by-task curves (Fig. 4) further show PGP variants consistently below baselines in forgetting across all tasks.
4. **Stability-plasticity analysis via threshold ε.** Section 3.3 and Fig. 5 demonstrate that adjusting ε directly trades off forgetting (stability) against new-task accuracy (plasticity), providing a principled control knob adapted from prior gradient-projection work to the prompt space.

## Weaknesses

### Fatal
None. The core empirical approach is functional and produces consistent results.

### Major
1. **The derivation conflates a single sum-space constraint with two independent constraints (Section 3.1, Eq. 14 → Eq. 9).** The paper claims (lines 183–185): conducting SVD on `s_t = x_t + p_t` to satisfy `s_t Δp^T = 0` "equals to `x_t Δp^T = 0` and `p_t Δp^T = 0`." This is mathematically incorrect. `s_t Δp^T = (x_t + p_t)Δp^T = x_t Δp^T + p_t Δp^T = 0` is a single linear constraint on the sum; it does not factor into two independent constraints without additional assumptions about orthogonality between `x_t` and `p_t` that the paper never establishes. This error directly undermines the paper's central claim of a "rigorous theoretical guarantee" (Section 1, contribution (1)). The method may still work empirically as a heuristic, but the theoretical argument as presented is unsound.

2. **The classifier head is not addressed in the theoretical analysis.** Proposition 1 (Eq. 2) considers the full model output `f_θ(p, x)`, but the derivation focuses exclusively on the self-attention matrix of the transformer, implicitly assuming that preserving the transformer output is sufficient. However, the classifier head (which is trainable in L2P/DualPrompt) is not discussed — even if the transformer's output for old tasks is perfectly preserved, a changed classifier can still cause forgetting. This gap means the analysis does not fully account for forgetting at the classification level, which is what the evaluation metrics (accuracy, forgetting) measure.

3. **No variance or statistical significance is reported.** Across all tables and figures, only point estimates are given. The improvements (e.g., +0.42% accuracy on 10-Split-CIFAR100 for DualPrompt-PGP) are modest enough that standard errors could place them within the noise floor. Without multiple seeds or confidence intervals, it is impossible to assess whether the gains are reliable. This is a standard expectation in empirical ML papers, particularly when the reported improvements are small.

### Minor
1. **The element-wise sum operation `s_t = x_t + p_t` is underspecified (Eq. 14).** The paper does not define how matrices of potentially different dimensions (input feature sequence vs. prompt tokens) are summed. This is a reproducibility concern that should be clarified (e.g., broadcasting or padding strategy).

2. **The ablation on ε (Fig. 5) reports new-task accuracy and forgetting but not final average accuracy across all tasks.** This makes it difficult to assess the overall practical impact of the ε trade-off on the full benchmark — average accuracy across all tasks is the standard metric used in Table 1 and should be included here.

3. **The comparison to L2P-R (rehearsal) is interesting but L2P-R is not a standard published method.** The implementation details are not described, and the training time advantage (0.787h vs. 0.756h, a 4% reduction) is negligible. The data memory comparison (1.12 GB vs. ≤1 MB) is expected since L2P-R stores images — this does not demonstrate a novel advantage of PGP over standard rehearsal-free prompt methods.

4. **The paper defers key details to appendices** (task-incremental results, prefix-tuning derivation, detailed experiment settings) that were stripped. While this is a formatting issue, the main paper would benefit from including at least a summary of the TIL results and a clearer description of the SVD accumulation mechanism across tasks.

### Trivial
None worth noting.

## Nice-to-Haves
- Provide error bars (multiple seeds) for all main results to establish statistical significance.
- Extend the gradient projection to cover the classifier head, or provide theoretical/empirical justification that preserving transformer outputs is sufficient given the classifier's learning dynamics.
- Compare with more recent prompt-based methods (Coda-Prompt, HiDe-Prompt) to demonstrate generality beyond L2P and DualPrompt.

## Removed Points
- *Criticism about ignoring Δp Δp^T as a high-order infinitesimal:* This is a standard approximation in gradient-based optimization; the update Δp is O(η) for learning rate η, so Δp Δp^T is O(η²). The approximation is well-justified for small learning rates.
- *Criticism about the paper only comparing to two baselines and lacking comparisons to Coda-Prompt/DyTox:* This is a reasonable request but more of a nice-to-have; the paper's aim is to show improvement over the base methods it builds on. However, to strengthen the paper, including such comparisons would be valuable.
- *Criticism about "missing related works":* I do not have external sources to confirm the existence of unmentioned works.
- *Criticism about training time advantage being tiny and expected:* While the training time difference is small, the memory comparison is valid and relevant. This criticism was partially merged into minor weakness 3.
- *Pure formatting/style nitpicks, typos, grammar:* Removed as parser artifacts.
- *Complaint about Table 2 showing advantage that "does not demonstrate a novel advantage of PGP":* The table shows PGP is competitive without exemplars, which is a meaningful comparison point.

## Novel Insights
None beyond the paper's own contributions. The reviews surface the mathematical flaw in the derivation but do not contribute a novel theoretical or practical observation about the CL setting that the paper itself does not provide.

## Suggestions
1. **Fix the theoretical derivation.** Either (a) reformulate to directly enforce both constraints (e.g., by constructing a combined matrix [x_t; p_t] and taking its nullspace), or (b) drop the claim of equivalence and instead provide an empirical justification that projecting onto the nullspace of s_t works well in practice despite not guaranteeing both constraints individually. Remove or qualify the claim of "rigorous theoretical guarantee."
2. **Address the classifier head.** Apply the same gradient projection to the classifier gradients, or provide an argument and supporting experiment showing that transformer output preservation is sufficient given the specific classifier design.
3. **Report variance.** Run experiments with at least 3 seeds and report mean ± std for all main results.
4. **Clarify the element-wise sum operation** and the SVD accumulation mechanism over tasks.

## Score and Decision

**Calibration:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Maintaining Adversarial Robustness in CL (sr0My6yDNu) | 3.25 | R1 | Weaker paper with gradient projection for robustness; had theoretical issues and poor presentation. This paper is better structured and more coherent. |
| Knowledge Accumulating Contrastive Prompt (Hf54sNeeBM) | 4.75 | R1 | Similar prompt-based CL paper with marginal improvements; rejected mainly for incremental gains and missing baselines. This paper has a more principled approach but a more serious theoretical flaw. |
| TIPS: Two-Level Prompt (QYgtZRTv3e) | 4.50 | R1 | Prompt-based CL paper with marginal gains; withdrawn/rejected. Comparable overall quality, but this paper has the theoretical flaw. |
| OVOR (FbuyDzZTPt) | 6.00 | R2 | Accepted prompt-based CL paper. Clear contribution, solid results, no fundamental theoretical issues. This paper is weaker. |
| MISA (V6uxd8MEqw) | 6.50 | R2 | Strong accepted CL paper with large improvements. Well above this paper. |

**Round 1 bracket:** 3.0 – 5.0. The paper sits above the weakest rejected papers (~2–3) but below the stronger rejected ones (~4.75) due to the mathematical flaw.

**Round 2 narrowing:** Compared to "Knowledge Accumulating Contrastive Prompt" (4.75, rejected), this paper has a more fundamental theoretical problem (incorrect equivalence claim) and similarly marginal gains. Compared to OVOR (6.0, accepted), this paper lacks both theoretical soundness and the strong empirical story needed to compensate.

**Final calibration:** The paper is below the "Knowledge Accumulating Contrastive Prompt" anchor (4.75) because that paper's weaknesses were about marginal improvements and missing baselines — not about a core mathematical error. This paper's theoretical flaw is more central to its contribution claim.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>