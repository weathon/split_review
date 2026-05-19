- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8
Now I have a thorough picture of the paper and all claims. Let me synthesize the final review.

## Summary

The paper introduces **general graph random features (g-GRFs)**, a random-walk-based algorithm that extends prior Graph Random Features (GRFs) from a handful of specific kernels to the broad class of functions expressible as a power series $\sum \alpha_k \mathbf{W}^k$ of the weighted adjacency matrix. The key innovation is a *modulation function* $f$ that weights walker contributions by walk length, satisfying a convolution condition ($\alpha = f_1 * f_2$) for unbiasedness. The paper also introduces *neural modulation functions* — a small neural network parameterizing $f$ — enabling scalable implicit kernel learning, and provides closed-form $f$ for common kernels (regularized Laplacian, random walk, diffusion), Rademacher complexity bounds, and experiments on kernel estimation, ODE solving, clustering, and mesh regression.

## Strengths

1. **Clean theoretical generalization of GRFs to power-series kernels.** Theorem 1 proves that any kernel of the form $\mathbf{K}_\alpha(\mathbf{W}) = \sum \alpha_k \mathbf{W}^k$ admits an unbiased random feature approximation via the convolution condition $\alpha = f_1 * f_2$. This is a nontrivial extension beyond the original GRF, which covered only the 2-regularized Laplacian and asymptotically unbiased diffusion kernel. The iterative formula (Eq. 6) for symmetric modulation functions provides an efficient computational route.

2. **Neural modulation functions enable scalable implicit kernel learning.** By parameterizing $f$ with a 1-hidden-layer network and training on a downstream loss (Frobenius error or angular prediction error) on a small graph, the learned kernel generalizes across larger, topologically different graphs (Tables 3 and 4). The learned $f^{(N)}$ consistently outperforms unbiased fixed kernels — notably, this is done without ever computing the exact kernel, which would be $\mathcal{O}(N^3)$.

3. **Subquadratic time complexity is clearly articulated.** Algorithm 1 and footnote 1 make explicit that the method avoids $\mathcal{O}(N^3)$ exact evaluation, costing $\mathcal{O}(N^2)$ per matrix-vector product with a precomputed batch of modulation values of size scaling only logarithmically in the number of walks.

4. **Closed-form modulation functions for three popular kernels** (Table 2: $d$-regularized Laplacian, $p$-step random walk, diffusion) plus the iterative formula for cases without closed forms. This makes deployment for common cases trivial.

5. **Broad experimental validation across diverse tasks:** unbiased estimation of multiple kernels on 8 graphs (Fig. 1), ODE simulation on real graphs, kernelized $k$-means clustering on graphs up to 3300 nodes with low error ($E_c \leq 0.16$), learned modulation for improved estimation, and implicit kernel learning on triangular meshes up to 21K nodes.

6. **Rademacher complexity bound (Theorem 2)** provides theoretical support for generalization of the learnable kernel class, linking complexity to the spectral radius of $\mathbf{W}$ and maximum Taylor coefficients — a theoretical component absent in the original GRF work.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaim of "arbitrary" functions.** The abstract, introduction, and conclusion repeatedly claim g-GRFs estimate "arbitrary functions of a weighted adjacency matrix" (lines 4, 22, 24, 320). The actual class is functions with a convergent power-series expansion $\sum \alpha_k \mathbf{W}^k$ (Eq. 1). While this includes many kernels (exponential, cosine, regularized Laplacian, etc.), it excludes element-wise nonlinearities, functions defined via eigendecomposition without power-series representations, and non-analytic functions. The paper should qualify this claim precisely — "arbitrary" is materially misleading.

2. **No comparison to other scalable graph kernel approximations.** The paper claims scalability as a central advantage but does not compare against any other scalable approach such as Nyström methods, Lanczos iteration, or spectral sparsification. The experiments compare only against exact kernels (which is natural as a correctness check) and against the *unbiased* g-GRF itself. Without any comparison to alternative approximations, the reader cannot judge whether g-GRFs are merely viable or actually competitive in terms of speed-accuracy trade-offs. Adding at least one baseline (e.g., Nyström with a comparable budget) for the ODE or clustering tasks would substantially strengthen the empirical contribution.

### Minor

3. **ODE experiment graphs not named.** The paper (line 211) states "we consider diffusion on three real-world graphs" but never names them. The figure caption and text provide no identifying information, making this result unverifiable.

4. **Clustering experiment reports only an upper bound on $m$.** Table 2 (wrapped) states "$m \leq 80$" but gives no single exact value per graph. Since the error values depend on $m$, the reader cannot interpret these results precisely or reproduce them.

5. **Bias-variance decomposition of the learned modulation function is claimed but not shown.** Section 3.4 asserts the learned $f^{(N)}$ improves MSE by reducing variance at the cost of bias (line 248). Only the total Frobenius norm error is reported. Showing the decomposition explicitly on at least one graph would turn an interesting observation into a concrete insight and would clarify whether the bias introduced is indeed justified.

6. **Generalization bound is not connected to the experiments.** Theorem 2 provides a Rademacher complexity bound, but it is never referenced, evaluated, or discussed in the experimental sections. The paper says "this immediately yields generalization bounds" but does not develop this into any concrete statement or empirical check. The theoretical contribution and the experimental one sit side-by-side without integration.

### Trivial
None.

## Nice-to-Haves

- **Report wall-clock times** for g-GRFs vs. exact computation on small graphs and against other approximations on larger graphs. Since scalability is a central claim, concrete runtime numbers would make the efficiency argument more compelling.
- **Explicit discussion of memory footprint.** The output feature vectors are size $N$ per node; clarifying that they are stored implicitly (via the walk-based construction used in matrix-vector products) rather than as dense $N \times N$ arrays would preempt confusion.
- **Sensitivity to the neighbor-sampling distribution.** Algorithm 1 uses unweighted node degrees and uniform neighbor sampling. A brief discussion of when weighted degrees or non-uniform sampling would be preferable (e.g., highly skewed weight distributions) would strengthen the methodology section.

## Removed Points

These points are flagged to be removed — treat them with caution.

- *"No discussion of why those particular kernels were selected in Table 4"* — Removed. The three kernels (1-reg Laplacian, 2-reg Laplacian, diffusion) are the natural choices from the paper's own taxonomy (Table 1): they have closed-form modulation functions, are widely used in the literature, and are the comparison points established in the fixed-kernel experiments. No special justification is needed.
- *"Neural modulation function architecture not justified"* — Removed. The paper explicitly states "Bigger, more expressive architectures... can be used but this is found to be sufficient for our purposes" (line 246). This is a reasonable justification for a proof-of-concept experiment.
- *"Distributed claim not tested"* — Removed. The paper notes the algorithm "can also be trivially distributed across machines" (line 4). This is a structural observation about the algorithm's parallelizability (walks are independent), not an empirical claim requiring testing.
- *"Subquadratic memory not clarified"* — Moved to Nice-to-Haves. The paper's complexity analysis focuses on time, which is the primary bottleneck for the problems considered. Memory clarification would be useful but is not a flaw.

## Novel Insights

The reviews surface two meta-observations that go beyond the paper's own presentation. First, the paper's "arbitrary" claim is a recurring rhetorical choice that will predictably draw pushback — the actual contribution (power-series kernels) is already broad and interesting enough to stand on its own without the overclaim. Second, the gap between the Rademacher complexity bound (Theorem 2) and the experiments highlights a common pattern in ML papers where a theoretical result is presented for completeness but never operationalized. In this case, the bound could plausibly explain *why* the learned modulation function transfers across graphs with different spectral radii, yet this connection is left unmade. Fixing this would turn an isolated theorem into an integrated part of the paper's narrative.

## Suggestions

1. Replace every instance of "arbitrary functions" with qualified language: "functions with a convergent power-series expansion" or "analytic functions of the weighted adjacency matrix." This does not weaken the contribution — the class is still broad and includes the most popular graph kernels.
2. Add at least one baseline comparison to a non-random-feature scalable method (e.g., Nyström approximation with $m$ landmarks) for the clustering or ODE task. This would directly address the main empirical weakness.
3. Name the three real-world graphs used in the ODE experiment and provide the exact $m$ values used for each graph in the clustering table.
4. Include a small figure or table showing the bias-variance decomposition of the learned $f^{(N)}$ on the small ER graph — decompose the total MSE into squared bias and variance components for both the unbiased and learned estimators.
