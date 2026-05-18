Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes TV-HMM, a time-varying Hidden Markov Model for offline change point detection. The key idea is modeling change point locations via a time-varying Markov chain whose transition matrix \(\Pi_k\) is learned from data, with diagonal elements converging to 1 to automatically prune unnecessary change points. The paper develops a variational EM algorithm with stochastic approximation (reducing complexity from \(O(KN^2)\) to \(O(KS^2)\)), proves statistical consistency of location estimates (Theorem 1), and extends the model to a semi-parametric MMD-based version that avoids distributional assumptions.

## Strengths

- **Novel modeling approach**: Representing change point locations via a time-varying transition matrix whose size scales with sequence length \(N\) rather than state count \(K\) is a principled departure from standard HMM-based CPD. The ARD-inspired mechanism for automatically determining the number of change points by learning \(\Pi_k\) is conceptually interesting.

- **Theoretical consistency guarantee**: Theorem 1 provides a convergence rate analysis — proving that marginal probabilities for true change points converge to 1 at exponential rates while non-junction points decay — which is a level of theoretical analysis absent from most Bayesian CPD work. The prose explanation (Section 2.3, Remark) makes the intended claim clear: as \(N \to \infty\), MAP estimates recover the true unduplicated set of change points.

- **Computational efficiency**: The stochastic approximation scheme reduces per-iteration complexity from \(O(KN^2)\) to \(O(KS^2)\), and the paper notes convergence typically within 30 iterations. This is a practical improvement over MCMC-based alternatives.

- **Consistent parametric performance**: Table 1 (across three simulation models with varying dimensions and distribution families) shows TV-HMM ranks among the top methods in all settings, while competitors fluctuate. Table 2 demonstrates reasonable parameter estimation (MSE 0.1–0.2 for posterior means) with low variability.

- **Semi-parametric extension**: The MMD-based TV-HMM (Section 4) replaces the parametric likelihood with a kernel embedding, removing distributional assumptions. Results on three non-Gaussian sequences (Poisson, chi-squared, exponential) with Rand indices 0.9447, 0.8686, and 0.8911 suggest the approach has potential.

- **Robustness on real data**: On the Well-log dataset, TV-HMM correctly identifies regimes without mistaking outliers for change points and detects a change point at timestamp 1540 that the \(\mathcal{D}_m\)-BOCD baseline misses.

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 1 statement is poorly structured and hard to parse.** The formal mathematical statement (lines 138–144) mixes cases in a confusing multi-line expression where conditions and rates are interleaved in a way that makes it difficult to verify the precise claim without relying solely on the subsequent prose explanation (lines 146–147). While the prose conveys the gist — junction points' probabilities converge to 1 at exponential rate, non-junction points decay — a theorem that cannot be cleanly read as a formal statement undermines the paper's central theoretical contribution. Given that Theorem 1 is the paper's primary theoretical result, this is more than a presentation nitpick.

2. **Experimental results lack variability measures across all tables.** Table 1 (Rand indices) and Table 2 (MSE) report point estimates without standard deviations, confidence intervals, or any measure of uncertainty. The reader cannot assess whether the observed differences between TV-HMM and competing methods are statistically meaningful. The critic's concern that this is insufficient for rigorous validation is well-founded. (Note: the critic's claim of identical "0.921" values in Table 1 could not be verified from the extracted text and is removed from consideration.)

3. **Semi-parametric (MMD-TV-HMM) evaluation is too thin to validate the method.** Section 4 reports Rand indices for three non-Gaussian sequences (Poisson, chi-squared, exponential) with no comparisons to any nonparametric baseline (e.g., KCP, ECP3O), no variability measures, no details on sequence lengths, number of change points, or generative parameters. Three numbers in isolation, however "promising," do not constitute a convincing evaluation of a new method — especially one whose main selling point is robustness across distribution families.

4. **Real-world evaluation is purely qualitative.** The Well-log experiment (Section 3.3) compares TV-HMM against a single baseline (\(\mathcal{D}_m\)-BOCD) using only a visual comparison (Figure 3) and one qualitative observation about a missed change point. No quantitative detection metrics (precision/recall, F1 score, covering metric, detection delay) are reported. Without quantitative evaluation, claims of "comparative advantage" are unsupported.

### Minor

1. **Overclaimed convergence guarantee.** The paper states that stochastic approximation "guarantees convergence to global optimal (Robbins & Monro, 1951)" (Section 2.2, line 113). Applying Robbins-Monro to a nonconvex variational EM objective with a subset sampling scheme is not a trivial extension, and the paper provides no argument or specific theorem justifying this claim. This overstates what is actually established.

2. **Automatic model selection not rigorously demonstrated.** The ARD analogy (Section 2.2) provides a heuristic explanation for why diagonal entries of \(\Pi_k\) converge to 1 for redundant regimes, and Figure 2 (right) shows a single converged transition matrix. But there is no systematic study of how reliably the pruning occurs across random initializations, varying amounts of over-specification (\(\tilde{K} \gg K\)), or under-specification (\(\tilde{K} < K\)). This is the paper's headline claim and should be more thoroughly validated.

3. **No runtime or convergence analysis.** The paper claims computational improvements from stochastic approximation but reports no actual runtimes, convergence curves, or ELBO traces. A simple plot of ELBO over iterations or a runtime comparison against baselines would strengthen the practical contribution.

### Trivial

- Equation 1 uses a product \(\prod_{t=j}^{i}\) where \(j \geq i\); while mathematically valid, this backward-indexed product is notationally confusing and would benefit from re-indexing.
- The paper does not report sensitivity to key hyperparameters (subset size \(S\), step size \(\eta\), initial \(\tilde{K}\)).

## Nice-to-Haves

- Ablation study on the reliability of automatic change point number selection across random seeds and varying \(\tilde{K}\).
- Comparison against nonparametric CPD methods (e.g., KCP, ECP3O) for the MMD-TV-HMM experiments.
- Quantitative detection metrics (F1, covering metric) for the Well-log dataset.
- Empirical runtime comparison and ELBO convergence curves.

## Removed Points

These points were flagged by reviewers but are removed after verification:

1. **"TV-HMM row shows identical values (0.921) across all three models"** — Table 1 is an image; the prose discussion (lines 184–185) describes different performance levels across models, which contradicts the claim of identical values. Removed as unverifiable and likely incorrect.
2. **"MMD-ELBO contains a sign error: \((m-n-1)\) should be \((n-m+1)\)"** — \((m-n-1) = -(n-m+1)\), which is consistent with the message function's \(-(n-m+1)/G\). The critic is factually wrong; the expression is internally consistent.
3. **"No theoretical argument—nor even a heuristic explanation for ARD mechanism"** — The paper explicitly discusses ARD (Neal, 2012) in Sections 2.1 and 2.2 and explains the mechanism (lines 65–66, 115–116, 167). This criticism misreads the paper.
4. **Various formatting/style nitpicks and claims about missing appendices/proofs** — these are parser artifacts or standard paper structure.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a tension between the paper's two main selling points. The theoretical consistency result (Theorem 1) is proven under a *parametric* Gaussian likelihood, while the semi-parametric MMD extension is the method's strongest argument for practical generality. The paper never bridges these: the theory does not cover the MMD version, and the MMD experiments are too thin to empirically substitute for that missing theory. This gap — between what is proven and what is claimed — is the deepest structural issue not fully articulated by either reviewer individually.

## Suggestions

1. Restructure the statement of Theorem 1 into a clean, readable form with explicit case notation (e.g., separate bullet points for junction vs. non-junction, with clear rate expressions). The prose explanation in the Remark is clear — bring that clarity into the theorem statement itself.
2. Add standard deviations or confidence intervals to all experimental tables (Tables 1 and 2).
3. Strengthen the MMD-TV-HMM evaluation by adding at least one nonparametric baseline comparison and reporting standard errors.
4. Add quantitative metrics (F1, covering metric) to the Well-log evaluation, and ideally compare against one or two additional baselines.
5. Provide a more measured statement about the stochastic approximation convergence guarantee, or add a justification for why Robbins-Monro applies to this setting.
6. Run a systematic study of the automatic model selection behavior: vary \(\tilde{K}\) in both directions, track the fraction of runs that correctly recover the true number of change points, and report results across random initializations.

## Score and Decision
MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>