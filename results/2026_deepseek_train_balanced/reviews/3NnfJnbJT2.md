## Summary

This paper presents GIO (Gradient Information Optimization), a task-agnostic data selection method that relaxes the discrete search over candidate training points into continuous gradient descent on KL divergence. The core idea is to find points that minimize the KL divergence between a target distribution $X$ (a small set of representative examples) and the selected training set $V \subseteq G$. Three optimizations make this tractable: (1) a "derivative trick" replacing exhaustive search with gradient descent, (2) a quantization-explosion scheme using K-means centroids, and (3) a k-NN estimator for continuous KL divergence. Experiments on WMT14 machine translation, spelling correction, and FashionMNIST show promising results.

---

## Strengths

1. **Novel relaxation of discrete data selection to continuous optimization.** The derivative trick (Eq. 9→10) reduces per-iteration complexity from $\mathcal{O}(|G| \cdot C)$ to $\mathcal{O}(S \cdot C)$, with an 80% wall-clock speedup verified on synthetic benchmarks (§3.5). This is a genuine algorithmic contribution.

2. **Negative consistency is cleanly demonstrated.** The 2D experiment (§4.2) shows GIO terminates without adding any points when $G$ is far from $X$ (centroids at (3,4) vs. (300,400)), a property that similarity-search methods requiring a fixed data size lack. This is a clear, well-illustrated advantage.

3. **Robustness across embedding models and quantization parameters is well-supported.** Changing from MPNet to MiniLM or varying K-means clusters (K=1000/1500/3000) yields <1% average BLEU difference (§4.2, Table 2). These experiments directly address concerns about brittleness and are the paper's strongest empirical contribution.

4. **Competitive against strong baselines in controlled comparisons.** In 10/12 MT evaluations, GIO outperforms BM25, data pruning, and submodular optimization when all methods are trained to the same data size and from the same initialization points — a fair, controlled setup.

---

## Weaknesses

### Major

1. **The headline claim of "surpassing the full model" compares against a cited number, not a reproduced baseline.** The full-model BLEU (41.8 EN-FR, 28.2 EN-DE) is footnoted as "From \citet{vaswani2017transformer}" (Table 1). The authors state they "replicate the setup" but do not report training the full model themselves under identical conditions (same Fairseq version, preprocessing, seeds, hardware). The claimed advantage is 0.4–0.5 BLEU — well within the ±0.5 to ±1.0 BLEU variation typical of uncontrolled reproduction. This directly weakens the paper's central claim. **This can be fixed by training the full model and reporting that BLEU**, but as submitted the evidence is insufficient.

2. **The spelling correction experiment evaluates a proxy metric, not task performance.** The main text reports only "% high quality data" (73% for GIO vs. 50–59% for baselines, Table 3). The claim of "set a new state of the art on the challenging BEA4660 spelling correction benchmark" (§4.3) is deferred entirely to the appendix (stripped by the parser). The proxy metric is not validated to correlate with actual spelling correction accuracy (WER/F1), and it is possible that GIO's selection leads to worse end-task performance despite selecting more "high quality" examples by the synthetic noising definition. The paper's main text should contain the actual task metric.

3. **No variance or uncertainty is reported for any experimental result.** Across all three tasks, results are reported as point estimates without standard deviations, confidence intervals, or number of runs (except FashionMNIST, footnoted as "averaged over 2 runs"). With only 2 runs, the 0.7% accuracy advantage on FashionMNIST (92.2% vs. 91.5%) could be within noise. The Spearman ρ = 0.83 between KL divergence and BLEU (median 1.0) — claimed as validation of the paper's core theoretical premise — is supported by very few data points per comparison group (5–6 per initialization/language pair), and the paper does not report confidence intervals or p-values.

4. **The KL divergence estimator has known biases and smoothness issues that are acknowledged but not addressed in the main paper.** The k-NN estimator (Eq. 10) has piecewise-constant gradients almost everywhere; the paper modifies it to "bypass 0 gradient problems" but defers the details to the appendix. On FashionMNIST, KL($X \parallel X$) is reported as 739 instead of 0 (Table 4, footnote), indicating substantial estimator bias. The paper explains this in the appendix, but the main text does not characterize how this bias affects the optimization or whether the estimated KL reliably distinguishes good from bad subsets.

### Minor

1. **Stopping criterion is used inconsistently.** The paper highlights that GIO "provides a natural stopping criterion (KL divergence)" as an advantage over similarity-search methods. Yet in the FashionMNIST experiment, a fixed iteration count (250 iterations = ~25% of data) replaces the KL-based criterion without justification beyond "resource constraints" (§4.4). The spelling correction experiment (§4.3) also uses a custom two-phase scheme differing from the MT experiments. This inconsistency undermines the claimed advantage.

2. **GIO underperforms BM25 on EN-DE at 0% initialization (24.3 vs. 24.9 BLEU).** The paper acknowledges this (10/12 evaluations) but does not analyze why a bag-of-words retrieval method outperforms a distribution-matching method on this setting. Understanding this failure mode could reveal boundary conditions of the method.

3. **FMNIST setup is fundamentally different from MT and spelling correction.** Here $X = G$ (both are the training set), turning the problem from quality filtering into pure data compression. The result is a modest 0.7% gain over random with only 2 runs and no error bars. This experiment adds limited evidence for the method's effectiveness.

### Trivial

- The analytic checks (§3.5) use synthetic 2D similarity search without specifying the implementation details (k, distance metric), making the comparison suggestive but not fully reproducible.

---

## Nice-to-Haves

- Characterize the k-NN KL estimator's bias on synthetic data where ground-truth KL is known, so readers can assess how the bias propagates into the optimization.
- Analyze why BM25 outperforms GIO on EN-DE 0% initialization — this could reveal useful boundary conditions.
- Report the number of points selected after "explosion" from centroids back to full clusters; the paper currently gives only the centroid count, not the total selected data size per cluster.

---

## Removed Points

These points from the inputs were filtered; treat with caution:

- Harsh critic's point about "the derivative trick relaxation is a significant relaxation — no analysis of how the local-density assumption holds in practice" — Partially valid but the robustness experiments (varying K) provide indirect evidence that the approximation is reasonable. Demoted from Major.
- Harsh critic's point about "the method operates on centroids, not points — no analysis of how many points this corresponds to" — Valid but minor; the method's purpose is to select data, and the explosion step is clearly described. Demoted to Minor/Trivial.
- Strength Finder's claim that GIO "outperforms full-data training with substantially fewer examples" — Conflicts with verified weakness #1 (uncontrolled baseline). Stripped of the "outperforms" framing; what remains is that GIO achieves strong BLEU scores with fewer examples. Weakness wins.
- Harsh critic's claim about "similarity search implementation not described" — The 2D illustration in §3.5 is meant to be intuitive, not a rigorous benchmark. This criticism is disproportionate to the point being made. Removed.
- Harsh critic's claim that "makes no assumptions on the functions it can use" is misleading — The paper acknowledges in Limitations that any statistical distance can be used. This is a minor overclaim in Section 2 but not a substantive weakness. Removed.
- Various prose-level criticisms about placement of the limitations section, framing of results, etc. — These are organizational preferences, not evidential weaknesses. Removed.

---

## Novel Insights

None beyond the paper's own contributions. The key insight — relaxing discrete data selection to continuous KL gradient descent with quantization-explosion — is the paper's own. The reviews do not surface a fundamentally different interpretation of the work.

---

## Suggestions

1. Train the full Transformer Big model under your own setup (same Fairseq version, same hardware class, same preprocessing) and report that BLEU alongside the GIO results. If the reproduced number matches Vaswani et al. (41.8), the "surpasses full model" claim is validated; if not, the paper can still report the relative improvement.

2. Report actual task metrics (WER, F1, or BEA4660 accuracy) for the spelling correction experiment in the main paper, not just the appendix.

3. Add error bars (standard deviations over 3–5 seeds) to all main experimental tables. For the FMNIST experiment, increase the number of runs beyond 2.

4. Include a brief characterization of the k-NN KL estimator's bias in the main paper: e.g., show estimated vs. true KL on synthetic data, or discuss how the 739 value for KL($X\parallel X$) on FMNIST affects optimization.

5. In Table 1, add a column or footnote indicating the total number of data points selected after the explosion step, not just the centroid count.

---

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>