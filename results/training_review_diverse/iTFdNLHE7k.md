Now I have a thorough understanding of the paper and all review claims. Let me write the final consolidated review.

## Summary

This paper introduces Ferumal flows, which replace the neural-network-based scaling and translation functions in affine coupling layers (RealNVP, Glow) with kernel expansions. The authors motivate this from parameter efficiency—kernelised flows use up to 93% fewer parameters than neural counterparts—and from the need for better low-data generalization. They provide a representer-theorem-style argument to justify the kernelised objective and introduce auxiliary points for scalability. Empirical results on tabular density-estimation benchmarks show competitive or superior log-likelihoods versus neural coupling-layer baselines and significantly outperform FFJORD in low-data regimes.

## Strengths

- **Parameter efficiency is convincingly demonstrated.** Table~4 (Parameter count) shows dramatic reductions: e.g., FF-RealNVP on Power uses 16K vs 228K parameters (93% reduction), and similar reductions hold across all five datasets. This directly validates the paper's central thesis.

- **Strong empirical performance on full datasets.** FF-Glow achieves the best coupling-layer log-likelihoods on 4 of 5 benchmarks (Power 0.35, Gas 10.75, Hepmass −17.11, Miniboone −10.76) and is competitive with more expensive autoregressive and continuous methods on BSDS300. This makes the parameter-efficiency claim meaningful—reduction does not come at the cost of degraded performance.

- **Clear low-data advantage over strong baselines.** On 500-example subsets, Ferumal flows outperform FFJORD across all five benchmarks (e.g., BSDS300: 121.22 vs 100.32 nats) while using 1–2 orders of magnitude fewer parameters. This supports the key promise that kernelised flows are especially attractive in data-sparse settings.

- **Novel methodology with broad applicability.** Kernelising coupling-layer functions is a clean idea that can be applied as a drop-in replacement in many coupling-layer architectures (RealNVP, Glow, and potentially neural spline flows, invertible attention, etc.). The auxiliary-points trick for scalability is a sensible adaptation of sparse GP techniques.

## Weaknesses

### Fatal

None.

### Major

- **The representer-theorem proof (Proposition 1) has a compositional dependency gap.** The proof projects each layer's RKHS element onto the span of $\{\phi(u_{\ell,i}^1)\}_{i=1}^n$ independently, using the premise that only inner products with $\phi(u_{\ell,i}^1)$ appear in the objective. However, the inputs $u_{\ell,i}^1$ to layer $\ell$ depend on the parameters $V_1,\dots,V_{\ell-1}$ of earlier layers. When $V_1$ is replaced by its projected version $V_1^*$, the inputs to layer 2 change, which means the span used for projecting $V_2$ in the proof may not be the correct one for the new $V_1^*$. The proof does not address this interdependence. This does **not** invalidate the method—the kernel expansion is a valid direct parametrisation of $s_\ell$ and $t_\ell$—but it means the theoretical framing ("a principled reduction justified by a representer theorem") is unsupported as written. The paper would be stronger if it presented the kernelised parametrisation directly and appealed to kernel universality for expressiveness rather than claiming an equivalence guarantee.

### Minor

- **Low-data comparison is incomplete.** The 500-example experiment (Table 3) compares only against FFJORD. The paper states that RealNVP and Glow "struggled to generalise in low-data regimes" citing the Gaussianisation Flows paper, but does not report their actual test log-likelihoods under the same conditions. Including these direct neural counterparts would strengthen the claim that kernelisation specifically improves low-data robustness over the same architecture family.

- **Convergence claim lacks quantitative support.** Section 5.3 claims faster convergence based on learning curves (Figure~\ref{fig:nats}), but provides no quantitative measure (e.g., iterations or wall time to reach a given log-likelihood threshold). A visual learning curve is suggestive but not sufficient for a comparative claim of this kind.

- **No explicit statement of number of runs or random seeds in the main text.** The paper references an appendix table for error bars (Table~\ref{tab:error bars}), which is standard practice, but the main text should state how many independent runs were performed and how the reported numbers were obtained (mean, median, etc.). Without this, the reader cannot assess the stability of the reported single-number results.

### Trivial

- Table 2's caption notes that results marked * are taken from existing literature, but the table itself does not mark any entries with asterisks. The formatting appears inconsistent.

## Nice-to-Haves

- **Ablation on the number of auxiliary points $N$.** The paper fixes $N=150$ in most experiments without analysis of how performance or training time varies with $N$. Since auxiliary points are central to scalability, even a small ablation (e.g., $N\in\{50,150,500\}$ on one dataset) would be informative.
- **Comparison against a neural net with matched parameter count.** The paper shows parameter reduction, but does not test whether a comparably small neural network would perform as poorly as implied. Such an experiment would clarify whether the gains come from kernelisation per se or simply from having fewer parameters.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Error bars promised but absent, Table~\ref{tab:error bars} missing"** — Removed per hard rules. The paper references this table; it was in the appendix and was stripped by the parser. The original submission contains it.
- **"Missing training details, hyperparameter disclosure"** — Removed per hard rules (generic reproducibility nitpick). The paper provides kernel type, optimizer settings, learning rate schedules, batch sizes, and number of auxiliary points—a reasonable level of detail for a conference paper.
- **"Missing appendix / missing proofs"** — Removed per hard rules. Parser artifact.
- **"Should compare against more methods / broader evaluation"** — Scope-creep criticism. The paper already compares against RealNVP, Glow, MAF, MADE, FFJORD, and three Gaussianisation methods, which is a thorough evaluation for its category.

## Novel Insights

The reviews surface an interesting tension: the paper's representer-theorem framing claims a principled equivalence guarantee, but the compositional dependency gap means the actual status of the theorem is unclear. The most productive insight from the reviews is that the paper would be *stronger* by abandoning the flawed theorem framing and instead positioning the kernel expansion as a direct, valid parametrisation of $s_\ell$ and $t_\ell$. This would remove a theoretical weak point without requiring any changes to the method or experiments, and allow the paper to focus on its genuine empirical contributions. The auxiliary-points trick for coupling layers is a technically interesting adaptation of inducing-point methods from GPs, and the strong low-data results suggest this direction is worth pursuing beyond the current scope.

## Suggestions

1. **Drop or repair the representer-theorem framing.** Either fix the proof by addressing the compositional dependency (which may require an inductive argument with careful tracking of how projected parameters affect later-layer inputs), or simply present $s_\ell(u) = \sum_i k(u_{\ell,i}^1, u) A_{\ell,i}$ as a direct parametrisation and appeal to the universality of Gaussian/Matérn kernels for expressiveness. The latter is cleaner and avoids the theoretical vulnerability.

2. **Report the low-data performance of RealNVP and Glow** under the same 500-example conditions to directly demonstrate that kernelisation improves low-data generalization over the same architecture family, rather than citing external work.

3. **Add a quantitative convergence metric** (e.g., iterations to 95% of final test log-likelihood) to support the faster-convergence claim beyond a visual curve.

4. **State the number of independent runs explicitly** in the main text and clarify how the reported numbers relate to the appendix error-bar table (means? medians? best runs?).

## Score and Decision

This paper presents a genuinely novel idea—kernelising coupling-layer functions in normalising flows—with compelling empirical evidence for parameter efficiency (up to 93% reduction) and strong low-data performance. The core contribution is valuable and the empirical results are credible. The main weaknesses are the flawed representer-theorem proof (which can be removed without harming the method) and some gaps in experimental reporting. These are addressable in revision. I recommend acceptance with the expectation that the theoretical framing is corrected and the experimental gaps are filled.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>