Now I'll produce the final consolidated review.

---

## Summary

This paper proposes FourierShap, a two-stage method for computing SHAP values. In the first stage, the target function is approximated by a sparse Fourier (Walsh-Hadamard) representation — exact for tree ensembles (via recursion) and approximate for neural networks (via sparse WHT exploiting spectral bias). In the second stage, a newly derived closed-form expression for the SHAP values of individual Fourier basis functions (Lemma 1) is used to compute attributions in Θ(n·|𝒟|·k) time, bypassing the exponential coalition sum. The first stage is computed once and amortized across queries. Experiments on four tabular datasets report speedups of 10–10,000× over LinRegShap and competitive accuracy against FastShap and DeepLift.

## Strengths

1. **Novel closed-form expression for SHAP values of Fourier basis functions.** Lemma 1 and Theorem 1 provide an analytic formula that eliminates the exponential coalition sum for any function expressed in the Fourier basis. This is the paper's core theoretical contribution and is both clean and non-trivial. The resulting expression is structurally simple, summing over frequencies and background points rather than coalitions, which is the key enabler of the speedups.

2. **Principled amortization architecture.** The separation into a one-time function-approximation stage followed by a cheap per-query SHAP computation is well-motivated. Unlike KernelShap (which solves a per-instance optimization) and unlike FastShap (which trains an end-to-end explainer on the full SHAP pipeline), FourierShap's first stage only needs to approximate the function, and the second stage is a lightweight analytic evaluation.

3. **Fine-grained, continuous speed–accuracy trade-off via sparsity parameter k.** The ability to control the number of Fourier coefficients (k) smoothly trades approximation quality against runtime. This is a genuine practical advantage over black-box methods like KernelShap (where accuracy depends on stochastic convergence) and FastShap (where accuracy depends on the capacity of a separately trained MLP, which the paper shows can behave unpredictably).

4. **Exactness guarantee for tree ensembles.** When the Fourier decomposition of a tree ensemble is exact (obtained via the recursive algorithm), the SHAP values from FourierShap are identical to those from TreeSHAP, providing a correctness guarantee not shared by approximate methods.

## Weaknesses

### Fatal

None.

### Major

1. **Speedup comparisons omit the first-stage cost, making the headline claims difficult to verify.** The paper reports speedups (Figures 2 and 5) solely for the second stage of FourierShap relative to the full per-instance runtime of baselines like KernelShap, LinRegShap, and TreeSHAP. The first-stage cost — computing the sparse Fourier representation via sparse WHT (black-box) or recursive transform (tree setting) — is shown separately in Figure 1 but never combined into an end-to-end comparison. The paper acknowledges (line 199) that the first stage is "typically the most expensive part," yet no amortization break-even analysis is provided. For a practitioner explaining a moderate number of instances, the total wall-clock time could be *worse* than existing methods. The claim of "orders of magnitude faster" is accurate only for the per-query marginal cost after the first stage is fully amortized, and the reader cannot assess when this regime is reached.

2. **Ground-truth SHAP values lack convergence documentation.** Accuracy of FourierShap (and all baselines) is measured against "ground truth" obtained from KernelShap with convergence checked by "sampl[ing] more and more" (line 247). The number of coalitions sampled, the convergence criterion, and any measure of Monte Carlo error are not reported. Since KernelShap itself is an approximate method, the uncertainty in the reference values propagates into all reported R² accuracy numbers. This is especially concerning for the largest dataset (avGFP, n=236), where exact SHAP computation is prohibitively expensive and the quality of the converged estimate is unknown.

3. **The tree-setting Fourier extraction cost is unquantified.** For the white-box tree experiments (Figure 5), the paper states that the Fourier representation "can be efficiently computed" (line 259) via Equation (4), but provides no runtime breakdown or complexity analysis of this first stage. The diminishing speedups at larger depths may in part reflect this hidden cost, but the presentation does not allow the reader to separate it from the second-stage evaluation cost. An honest comparison would report the full pipeline runtime.

### Minor

1. **Function approximation R² measured on uniform Boolean inputs, not on the data distribution.** The paper evaluates the quality of the Fourier function approximation (Figure 1) using R² on uniformly sampled points from {0,1}^n (line 211). A network that fits well on uniformly sampled points may mis-approximate the function on the sparse manifold of real data, and this discrepancy could affect the downstream SHAP accuracy in unknown ways. A validation-set-based evaluation would be more informative.

2. **Complexity bound analysis is incomplete.** Theorem 1 states Θ(n·|𝒟|·k) flops, but the expression requires computing the set A = {j ∈ [n] | x_j ≠ x*_j, j ≠ i, f_j = 1} for each background point, each frequency, and each feature. The cost of this set construction and the associated modular arithmetic is not accounted for in the stated bound; a more careful analysis would clarify whether the practical runtime matches the asymptotic claim.

3. **Limited dataset scope.** The four datasets are all protein-fitness or GPU-tuning tasks with binary/categorical features. While this is consistent with the paper's stated scope, the evaluation would benefit from experiments on datasets with continuous features that have been discretized, to test whether the discretization step introduces meaningful bias in SHAP values.

### Trivial

- No dedicated limitations section appears in the main text (likely deferred to an appendix).

## Nice-to-Haves

- **End-to-end runtime analysis**: A single figure or table showing total (first stage + second stage) wall-clock time for varying numbers of query instances and varying k, with the break-even point marked relative to KernelShap and FastShap, would substantially strengthen the paper's practical claims.
- **Automatic k selection**: The trade-off parameter k is user-specified; a data-driven heuristic (e.g., based on held-out validation R²) would make the method easier to use.
- **Discretization sensitivity analysis**: Even one continuous-feature dataset with varying bin counts would help establish the practical robustness of the binary-input assumption.

## Removed Points

- **"No verification of the core closed-form expression"**: The critic claims Lemma 1 is presented without justification. The proof is deferred to the appendix (which was stripped by the parser). Per the hard rules, missing-appendix criticisms are removed — the derivation exists in the original submission.
- **"Method requires binary inputs; discretization impact not addressed"**: The paper explicitly scopes itself to binary/categorical features (line 75) and all tested datasets satisfy this. Criticizing the absence of continuous-feature evaluation is scope creep; the paper is transparent about its domain.
- **"FastShap trade-off comparison is not sharp"**: The paper explicitly argues (lines 256–257) that FastShap's accuracy depends on MLP capacity in an unpredictable way, while FourierShap's trade-off via k is reliable. This is a substantive counter-argument, not an omission.
- **"Spectral bias justification leap from infinite-width theory to finite-width networks"**: The paper cites empirical validation works (Lee et al., Gorji et al.) that carry these results to finite-width networks. This is standard practice, not a flaw.
- **Pure formatting/style nitpicks and parser artifacts**: Removed per the hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments do not surface an independent novel observation that the paper itself does not already make.

## Suggestions

1. **Add end-to-end runtime comparison.** Combine the first-stage cost (Figure 1) with the second-stage speedup (Figure 2) into a single table or figure that reports total time for varying numbers of query instances. Include the break-even point where amortization kicks in.
2. **Document KernelShap convergence.** Report the number of coalitions sampled, the convergence criterion used, and the standard error of the reference SHAP values for at least one dataset. If possible, use a tree ensemble + exact TreeSHAP to obtain a true ground truth for accuracy comparisons.
3. **For the tree setting, provide a runtime breakdown.** Separate the time to compute the Fourier representation from the tree ensemble vs. the time to evaluate Equation (15) for all query instances, across varying tree depths and ensemble sizes.
4. **Evaluate function approximation R² on a held-out validation split** from the actual data distribution, in addition to the uniform-Boolean evaluation, to verify that the Fourier approximation quality transfers to the data manifold.
5. **Make the k-selection practical.** Show a simple heuristic (e.g., choose the smallest k where held-out R² exceeds a threshold) and evaluate whether it yields consistent SHAP accuracy across datasets.

## Score and Decision

**Calibration anchors** (from the human-review corpus, all compared to the paper under review):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| /home/.../LiUfN9h0Lx.md (Distribution Compression, Accept) | 7.33 | Stronger paper: cleaner experiments, complete evaluation. Current paper has more novel theory but weaker empirical support. |
| /home/.../ky7vVlBQBY.md (InstaSHAP, Accept) | 6.67 | Comparable novelty level. InstaSHAP has more thorough experiments; current paper has more elegant theoretical contribution but experimental gaps lower its standing. |
| /home/.../eBVCZj3RZN.md (ViaSHAP, Reject) | 5.50 | Current paper has a stronger theoretical contribution (closed-form SHAP for Fourier bases) than ViaSHAP, but both have experimental weaknesses that prevent clear acceptance. |
| /home/.../mFHPoYVeqN.md (Q-SHAP, Reject) | 5.60 | Q-SHAP and current paper both propose polynomial-time SHAP variants for specific function classes. Current paper is broader (black-box + trees) and has a cleaner theoretical contribution. |
| /home/.../lLzeKG6t52.md (k-Additive SHAP, Reject) | 4.00 | Current paper is significantly stronger: the closed-form expression is a genuine theoretical advance, while k-additive is a heuristic with no guarantees. |
| /home/.../6zVElUoc6l.md (Ensemble Interpretability, Reject) | 5.60 | Different type of contribution (complexity theory), but similar overall quality tier. Current paper has more direct practical applicability. |
| /home/.../sTQC4TeYo1.md (GECo, Reject) | 2.00 | Current paper is far stronger: the closed-form SHAP expression is a real theoretical contribution, whereas GECo applies off-the-shelf community detection with limited novelty. |

Relative to these anchors, the current paper sits between the 5.5 and 6.67 clusters. The core theoretical contribution is genuinely novel — the closed-form SHAP expression for Fourier basis functions is a clean result that the community would find useful. However, the experimental evaluation has significant gaps (particularly the omission of first-stage costs from speedup comparisons and the weak ground-truth documentation) that prevent the paper from making a fully convincing case for its headline claims. A major revision that provides end-to-end runtime comparisons and tighter experimental methodology would position this paper for acceptance.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>