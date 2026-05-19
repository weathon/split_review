- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 3
Now I have all the information I need to write the consolidated review.

## Summary

This paper proposes GLIDE, a causal discovery framework that identifies causal graphs by testing whether the conditional distribution \(P(X\mid Z)\) remains invariant across datasets resampled to induce different priors over source variables. The insight is that only the true parent set of \(X\) yields an invariant conditional. The framework combines this invariance test with a Markov-blanket-based graph search that reduces candidate parent enumeration to a maximal-clique problem, achieving \(O(md^2)\) overall complexity. Experiments on synthetic and real-world data (including a 1041-variable network) show substantial runtime improvements (up to 25×) and better or comparable accuracy relative to NOTEARS, PC, FCI, GIES, SCORE, and DAS.

## Strengths

- **Novel invariance principle with theoretical grounding**: Theorem 1 formalizes a principled causal test — \(P(X\mid Z)\) has non-zero variance across changes in source priors only if \(Z\) is not the true parent set of \(X\). The paper further provides supporting theory: the relationship between basis sets and sources (Theorems 2–3), the optimal downsampling procedure (Theorems 4–5), and the convex subspace of admissible priors (Theorem 6). This gives the method a firmer foundation than purely heuristic score-based approaches.

- **Provably quadratic complexity with sparsity**: Section 4.1D and Section 4.3 derive an end-to-end complexity of \(O(m d^2 + m|D| + m|B|)\), breaking down the costs of Markov blanket identification (via Edera et al., 2014), maximal-clique enumeration (empirically \(O(d)\) per variable with degeneracy \(p\leq13\)), and augmented dataset construction. The complexity analysis is clear and well-justified.

- **Consistent and large empirical gains across diverse settings**: On synthetic continuous data (Figures 2–3), GLIDE achieves the best SHD and spurious rate in the extreme L-G setting and is competitive in nL-nG while running 9.6×–25.52× faster than NOTEARS/MLP-NOTEARS. On 7 real-world categorical datasets (Table 2), it achieves best SHD on all 7 and best spurious rate on 5/7, including a 1.8% spurious rate on the 1041-variable Munin graph versus GIES's 42.36%. The runtime and accuracy improvements are large and well-documented.

- **Comprehensive evaluation covering multiple data types and scales**: The experiments span synthetic continuous (linear-Gaussian and non-linear non-Gaussian), synthetic categorical, and 7 real-world benchmark datasets. The 95% confidence intervals over 10 runs add statistical rigor. The use of SHD, spurious rate, and runtime gives a multi-faceted picture of performance.

## Weaknesses

### Fatal
None.

### Major
- **No analysis of Markov blanket estimation quality or error propagation**: The entire candidate enumeration (Section 4.3) depends on Markov blankets estimated by an external algorithm (Edera et al., 2014). If these blankets are inaccurate — missing true parents or including spurious variables — the candidate clique set may not contain the true parent set, or may be polluted with false candidates. The paper provides no analysis (oracle experiment, sensitivity study, or diagnostic) of how blanket estimation errors affect the final graph, nor any evaluation of blanket accuracy on the test datasets. This is a structural gap: a failure in the upstream component could negate the invariance test's advantages, and the reader cannot assess how serious this risk is.

- **Continuous-data binning is used without any sensitivity analysis**: The downsampling and prior-manipulation procedure (Section 4.2.2) requires categorical data; for continuous data, the paper simply states that "binning with fixed bin width" is used (line 157). No ablation or sensitivity study of bin width is provided. This matters because (i) discretization can destroy the invariance property of the true continuous conditional, (ii) the choice of bin width is a free parameter that could affect results, and (iii) several baselines (NOTEARS, SCORE) operate natively on continuous data, so any advantage or disadvantage could partly reflect discretization rather than the invariance principle itself.

### Minor
- **Theoretical clarity of the invariance test could be sharpened**: Theorem 1 states the one-directional implication (variance\>0 ⇒ Z≠Pa[X]), which is sound. However, the practical parent-finding criterion (Eq. 3) uses argmin of finite-sample variance, implicitly relying on the converse (near-zero variance ⇒ Z=Pa[X]) for finite \(m\). The paper acknowledges this is not guaranteed (line 88: "might not be perfect but remains highly accurate"), but does not analyze the conditions under which the converse approximately holds or characterize when the test could select a superset \(Z\) containing the true parents plus conditionally independent extra variables. A brief discussion or formal characterization of what "sufficiently large and diversified" \(m\) means would strengthen the paper.

- **No recall or missing-edge metrics reported**: SHD and spurious rate (a false-discovery proportion analog) are informative, but without recall (or F₁) the reader cannot tell whether a low spurious rate is achieved by simply being conservative (predicting few edges). On the real-world data, GLIDE achieves very low SHD and spurious rate, which partially mitigates this concern, but explicit recall values would be more informative, especially for comparisons where SHD differences are small.

- **Only Erdős–Rényi graphs reported for continuous synthetic experiments**: The paper mentions generating bipartite and scale-free graphs (line 221) but omits results due to space. Since graph topology affects Markov blanket structure and clique enumeration, showing results on at least one additional topology (or confirming similar behavior) would strengthen the evidence.

- **Selection of \(m\) (number of augmented datasets) and the \(K\)-means clustering for prior sampling are not justified or ablated**: Section 4.2.4 describes sampling 10⁴ Dirichlet vectors and clustering into \(m\) centroids, but the paper neither reports the value of \(m\) used in experiments nor tests sensitivity to it. Since \(m\) directly enters the complexity as a multiplicative factor and affects test reliability, this is a missing design-space exploration.

### Trivial
- The runtime numbers (Figures 2–3) compare total wall-clock times, but the paper does not report the breakdown between Markov blanket estimation, clique enumeration, and invariance testing. A breakdown would help identify the actual computational bottleneck.

## Nice-to-Haves
- A dedicated limitations section (the paper ends abruptly after the conclusion) discussing the reliance on Markov blanket quality, the binning approximation, causal sufficiency, and the finite-\(m\) approximation would improve reproducibility and credibility.
- Specification of the independence test used to compute \(\Phi(X)\) (e.g., Fisher's \(z\), mutual information) and the significance threshold are implementation details that should be reported.
- An oracle experiment where true Markov blankets are substituted for estimated ones would cleanly isolate the contribution of blanket accuracy.

## Removed Points
- **Theorem 1 claimed "unconditional and therefore misleading" with a specific counterexample**: The critic argued that a superset Z containing conditionally independent extra variables would also have invariant \(P(X|Z)\), making the test unreliable. However, Theorem 1 as stated is one-directional (variance>0 ⇒ Z≠Pa[X]); the critic's counterexample does not contradict this direction. The paper explicitly notes the reverse direction holds only as \(m\to\infty\) (line 88). The concern about practical argmin selection is valid but is already captured in the Minor weakness about theoretical sharpness above. The specific mathematical objection against Theorem 1 is removed as it misreads the theorem's scope.
- **"Appendix not available" and "missing proofs"**: The parser strips appendix content from all papers; these exist in the original submission. Removed per instructions.
- **Claim that PC/FCI can scale to hundreds of nodes with "practical runtimes"**: This is a generic opinion about baselines, not a specific weakness of the paper. The paper's runtime comparisons (Figures 2–4) speak for themselves. Removed.
- **Formatting, grammar, and typographical nitpicks**: The critic noted "in in" (line 238) as a typo, but this is a parser artifact. Removed per instructions.
- **"Could not be independently verified" / reproducibility concerns about cited entities**: Removed per hard rules.

## Novel Insights

The harsh critic and strength finder together surface a revealing tension: the paper's core **conceptual innovation** — using distributional invariance across manipulated priors as a causal test — is genuinely novel and well-motivated, and the empirical results are compelling. Yet the **practical execution** has two blind spots (no analysis of Markov blanket error propagation, no binning sensitivity study) that, while individually addressable, collectively weaken the claim that the method works *because of* the invariance principle rather than in spite of approximations in its implementation. The strength finder correctly identifies the theoretical scaffolding (basis sets, optimal downsampling, convex prior subspace) as above-average for an empirical paper. The harsh critic's demand for an oracle Markov blanket experiment is the most actionable insight: it would directly test whether the invariance test by itself is reliable or whether the current results depend on the specific blanket estimator working well on these benchmarks.

## Suggestions

1. **Add an oracle Markov blanket experiment**: Run GLIDE with ground-truth Markov blankets (from the known synthetic graphs) alongside the estimated-blanket version. This isolates the error introduced by blanket estimation and quantifies how much accuracy is lost (or gained) by the upstream component.
2. **Add a bin-width sensitivity study**: On 2–3 continuous synthetic datasets, vary the bin width substantially (e.g., 0.5×, 1×, 2× the default) and report SHD, spurious rate, and runtime. Show that results are not artifacts of a particular discretization.
3. **Report recall or F₁ alongside SHD and spurious rate** for at least the main synthetic experiments, so readers can assess whether the method is missing many true edges.
4. **Report the value of \(m\) used** and test one or two alternatives (e.g., \(m=10, 20, 50\)) to demonstrate robustness to this hyperparameter.
5. **Add a limitations subsection** that honestly discusses the reliance on Markov blanket estimation accuracy, the binning approximation, causal sufficiency, and the finite-\(m\) approximation.
