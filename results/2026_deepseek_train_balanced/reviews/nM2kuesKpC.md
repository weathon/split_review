Here is the consolidated final review.

---

## Summary

The paper proposes D2P2-SGD, a differentially private optimizer that combines (i) a dynamic (time-decaying) noise variance mechanism with automatic gradient clipping and (ii) random projection of gradients into a lower-dimensional subspace. The authors claim provably tighter error bounds than DPSGD and empirically demonstrate improved accuracy on two datasets. The core idea — integrating dynamic DP with random projection — is novel, but the paper's execution has significant issues that prevent it from being accepted in its current form.

## Strengths

- **First integration of dynamic DP with random projection for SGD.** Table 1 systematically compares existing methods and shows D2P2-SGD as the first to combine both dynamic (time-varying) privacy noise and gradient compression via random projection. Section 4.1 further positions D2P2-SGD as a unifying framework that subsumes prior methods (D2P-SGD, DP2-SGD/PrivSGD) as special cases — a concrete architectural claim.

- **Algorithmic simplification over PrivSGD.** Unlike Kasiviswanathan (2021), which requires a separate optimization to lift low-dimensional gradients back to the original space, D2P2-SGD simply multiplies by \(A_k\) (Section 4.1, line 87), reducing implementation complexity. This is a verifiable improvement.

- **Systematic ablation on the projection dimension \(p\).** Figure 5b identifies an optimal 30% reduction rate and reports that privacy loss is empirically independent of \(p\) — a non-obvious practical insight not previously reported in projected-DP works.

## Weaknesses

### Fatal

None. The core idea is not invalid; the issues are in the evaluation and presentation.

### Major

1. **Empirical comparison at mismatched privacy budgets confounds the central accuracy claim.** In Figures 1–2, D2P2-SGD operates at \(\varepsilon \approx 2.45\)–\(2.75\) while the static DP baselines operate at \(\varepsilon \approx 0.95\)–\(1.06\) — a factor of \(\sim\)2.5–3 difference in privacy budget. The paper then claims D2P2-SGD "significantly enhances accuracy while maintaining privacy" (abstract), yet higher accuracy at a higher \(\varepsilon\) is not evidence of a superior method. A meaningful comparison would fix \(\varepsilon\) across methods (or plot a Pareto frontier). The paper acknowledges the tradeoff but does not control for it, so the headline empirical claim is not supportable from the evidence provided.

2. **Theoretical "main results" (Theorems 1–3) are absent from the main paper.** Section 4 is titled "ALGORITHM AND MAIN RESULTS" but contains only the algorithmic description (Section 4.1). No theorem statements, assumptions, or convergence rates appear in the body. The paper references Theorem 1 (lines 104, 111), Theorem 2 (line 111), and Theorem 3 (lines 104, 109) repeatedly in the experiments section, yet a reader cannot evaluate whether the claimed bounds are tighter, under what assumptions, or how the rates compare to DPSGD. For a paper whose central contribution includes "provably tighter error bounds" (abstract), this is a structural omission.

3. **Privacy accounting is unspecified and the reported \(\varepsilon\) values are not reproducible.** The paper never states how \(\varepsilon\) is computed. It references Opacus but gives no accounting details (moments accountant, Rényi DP, or any composition method). No \(\delta\) value is reported for the experiments. The only bound for \(\varepsilon\) given in the main text is \(\varepsilon \le C_1 B^2 K / n^2\) with \(C_1 \ge 314\) (line 111), which is qualitatively different from standard DP-SGD accounting and would yield very loose bounds for the reported parameters. It is unclear whether the \(\varepsilon\) values in Figures 1–2 (2.45, 2.75, 0.95, 1.06) come from this bound, from Opacus, or from another mechanism. This makes the privacy claims — central to the paper's identity — unverifiable from the main text.

### Minor

4. **Tension between the paper's motivation for random projection and the empirical finding about privacy loss.** The paper motivates projection as "reducing the dimension of additive noise and mitigating the increase in privacy loss" (line 20), yet Figure 5b shows that privacy loss is "independent of the dimension change" (line 113). If privacy loss is independent of \(p\), the privacy benefit of projection is unclear, and the motivation should be reconciled with this finding.

5. **Limited experimental scope.** The empirical evaluation uses only two datasets (FashionMNIST, SVHN) and one model architecture (4-layer CNN). This is narrow for a paper claiming broad improvements to DP optimization, especially given that the paper scopes out scalability to larger models (line 26) but does not provide counterbalancing breadth on the tasks it does consider.

6. **Automatic clipping claim is stated without supporting evidence in the main text.** The paper asserts that "for any \(\gamma > 0\), the gradient norm will converge to a neighborhood at the same asymptotic rate such that common deep learning optimizers are insensitive to the choice of \(\gamma\)" (lines 51–52) but provides no proof, citation, or experimental validation for this claim in the main body.

### Trivial

None.

## Nice-to-Haves

- Compare all methods at the same \(\varepsilon\) (or plot accuracy vs. \(\varepsilon\) Pareto curves) to demonstrate that the accuracy improvement is not simply a byproduct of a higher privacy budget.
- Include at least one higher-dimensional dataset (e.g., CIFAR-10) to broaden the empirical claims.
- Isolate the effect of automatic clipping via an ablation that replaces it with standard per-sample clipping.
- Report wall-clock time or FLOPs to substantiate the claimed computational efficiency improvement.

## Removed Points

These points were flagged by reviewers but are excluded after verification:

- *"Comparison between dynamic and static DP is not at fixed total privacy budget"* — duplicates Major Weakness #1, which already captures the core concern.
- *"No wall-clock time or FLOPs comparison"* — a nice-to-have, not a core weakness.
- *"Random projection subspace changing every iteration is problematic"* — this is an explicit design choice, not an error.
- *"Hyperparameter choices not reported with enough specificity"* — standard for venues where code is expected (the code link is provided in the original submission).
- *"Claims about lazy region are wrong"* — not central to the paper's contribution; removed to avoid distraction.

## Novel Insights

The core combination of dynamic DP with random projection is novel and the finding that privacy loss is empirically independent of the projection dimension (Figure 5b) is a non-obvious result worth further study. However, these strengths are overshadowed by the confounded empirical evaluation and the absence of the main theoretical results from the paper body, so the overall contribution cannot be properly assessed without substantial revision.

## Suggestions

1. Move the statements of Theorems 1–3 (with their assumptions and bounds) into the main text — Section 4 is incomplete without them.
2. Add an experiment comparing all methods at the same \(\varepsilon\), or plot accuracy vs. \(\varepsilon\) across a range of \(\sigma_\varepsilon\) values for each method.
3. Specify the privacy accounting mechanism (moments accountant, Rényi DP, etc.) and the \(\delta\) value used. Clarify how the reported \(\varepsilon\) values relate to the theoretical bound \(\varepsilon \le C_1 B^2 K / n^2\).
4. Address the tension between the projection motivation ("mitigating the increase in privacy loss") and the finding that privacy loss is independent of \(p\).
5. Broaden the empirical evaluation to include at least one additional dataset (e.g., CIFAR-10).

## Score and Decision

The paper introduces a novel integration of dynamic DP with random projection, but the empirical evaluation is confounded by mismatched privacy budgets, the theoretical results are absent from the main text, and the privacy accounting is unspecified. These are major, not fatal, issues — the core idea is sound — but they prevent the paper from meeting the acceptance bar for a top venue in its current form.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>