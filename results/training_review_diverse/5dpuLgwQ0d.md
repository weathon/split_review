Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper addresses the problem of determining the number of clusters $k$ in a graph under the eigen-gap heuristic. It proposes a randomized algorithm that runs in $\widetilde{O}(m)$ time by combining three components: (1) cluster-preserving sparsification (Sun & Zanetti, 2019) to reduce the graph to $\widetilde{O}(n)$ edges, (2) Chebyshev polynomial expansions with Hutchinson's stochastic trace estimator to count eigenvalues in a given interval, and (3) a binary-search-like procedure over geometrically scaled intervals to locate the eigenvalue gap. The main theoretical claim is that under the condition $\Upsilon_G(k) \ge C\cdot k$ (the same condition used in prior spectral clustering analyses), the algorithm returns $k$ with high probability in nearly-linear time.

## Strengths

- **First nearly-linear time algorithm for a well-motivated problem.** The paper addresses a genuine bottleneck in spectral clustering — determining $k$ typically requires computing all eigenvalues, while spectral clustering itself runs in nearly-linear time. The idea of combining sparsification with spectral density estimation (SDE) techniques to solve this specific problem is novel, and the paper explicitly claims and argues for this novelty (end of Section 1, Theorem 6).

- **Works under the same condition as state-of-the-art spectral clustering analyses.** Remark 1 correctly notes that $\Upsilon_G(k)=\Omega(k)$ is the same condition used in prior work to guarantee spectral clustering performance (Macgregor & Sun, 2022). The paper thus shows that determining $k$ requires no stronger condition than what is already needed to trust the clustering result itself.

- **Modular and clean algorithmic design.** The three-component design (sparsification → CountEigenvalues → search over intervals) is clear, and the CountEigenvalues subroutine is a well-structured integration of Chebyshev expansions and Hutchinson estimation that avoids explicit matrix polynomial construction.

- **Theoretical connections to SDE literature.** The CountEigenvalues analysis builds on known SDE techniques (Braverman et al., 2022), and Lemma 8 provides a clean closed-form computation of Chebyshev coefficients for the indicator function. Lemma 9's Hutchinson bound and Lemma 11's Wasserstein-1 analysis set up a formal framework for the eigenvalue counting guarantee.

## Weaknesses

### Major

- **Circular dependency in the sparsification step (Section 3.1).** The sampling probabilities for the cluster-preserving sparsifier are defined as $p_u(v) = \min\{C\cdot \frac{\log n}{1-\lambda_{k+1}(N_G)}\cdot \frac{w_G(u,v)}{\deg_G(u)}, 1\}$, which requires *knowledge of $\lambda_{k+1}(N_G)$* — the very quantity the overall algorithm is designed to uncover. The paper does not explain how to set these probabilities from the input graph alone. The assumption $\Upsilon_G(k) \ge C\cdot k$ relates $1-\lambda_{k+1}(N_G)$ to $\rho_G(k)$, but $\rho_G(k)$ is also unknown. While the paper cites Sun & Zanetti (2019) for the sparsification algorithm, it does not clarify whether that prior work provides a procedure that avoids this circularity or how a user would actually implement this step. As presented, the sparsification component is not evidently implementable.

- **Wasserstein-1 analysis assumes $q$ is a probability measure without justification (Lemma 11 and surrounding text).** The paper defines a spectral density $s(x) = \frac1n \sum_{i=1}^n \delta(x-\lambda_i)$ (a valid probability measure) and an approximate function $q$ implicitly via $\langle q,\overline{T}_k\rangle = \frac1n H_\ell(\overline{T}_k(M))$. The Kantorovich–Rubinstein dual formulation of $W_1$ requires both arguments to be probability measures; $q$ as defined is **not verified** to integrate to 1, be non-negative, or even be a proper distribution. The proof chain $W_1(s,q) \le 38/N$ lacks a rigorous foundation because it treats $q$ as a probability measure without construction or post-processing. The reference Braverman et al. (2022) handles this via careful density construction, but the present paper makes no mention of such a step. This is a genuine gap in the theoretical proof.

- **Main algorithm's correctness argument is underspecified (Section 3.3).** The search procedure runs CountEigenvalues$(M, 1-(\beta/2)^i/n^2, 1)$ for geometrically increasing $i$ and terminates "when any two [consecutive] executions return the same value." The paper provides no proof that two consecutive equal counts imply the interval includes exactly $\lambda_1,\dots,\lambda_k$ but excludes $\lambda_{k+1}$. CountEigenvalues has additive error $\epsilon$ per invocation, and the analysis does not bound how many interval steps are needed to guarantee the count stabilizes at the true $k$, nor does it handle the possibility that estimation noise could produce the same wrong count twice. The claimed guarantee does not follow from the presented analysis. Additionally, the analysis states the algorithm runs $O(\log n)$ times of CountEigenvalues without a rigorous bound on how the number of iterations depends on the spectral gap and the error parameter $\epsilon$.

### Minor

- **No experimental comparison to baseline methods.** The experiments test only synthetic SBM graphs (with $n$ up to 5000, $k$ up to 8) and small sklearn datasets (500 vertices). There is no comparison to any baseline — not even a simple method like computing the top $k+1$ eigenvalues via Lanczos and applying the eigengap heuristic. The paper claims that determining $k$ is the main computational bottleneck in spectral clustering but never measures the actual runtime of a standard eigengap computation on the same graphs. Even a coarse baseline would meaningfully strengthen the empirical claims.

- **Limited experimental scale and statistical rigor.** Only 5 data points are shown in Figure 1a for the scaling experiment ($n$ from 2000 to 5000). The accuracy claim "correctly determines $k$ for all tested instances" is stated without any statistical measures (e.g., success rate over multiple random trials, confidence intervals, or a plot showing accuracy as a function of $q$ as it approaches the theoretical threshold). The claim appears in the figure caption but is not backed by a dedicated accuracy plot. Given that the algorithm's guarantees depend on a strong spectral condition, experiments should probe where the condition starts to break down.

- **Pseudocode omits normalization in Chebyshev coefficients.** Algorithm 1's Step 10 references computing $\alpha_k$ from Lemma 8, but Lemma 8 computes $\langle h_{a,b}, w\cdot T_i\rangle$ while the algorithm needs $\alpha_i = \langle h_{a,b}, w\cdot \overline{T}_i\rangle = \langle h_{a,b}, w\cdot T_i\rangle / \sqrt{\langle T_i, w\cdot T_i\rangle}$. The normalization factor is missing from the pseudocode.

- **No discussion of rounding or error handling for CountEigenvalues outputs.** CountEigenvalues may return non-integer values due to estimation noise. The main algorithm's termination condition (comparing "the same value") doesn't specify how to handle fractional outputs or what tolerance to use. The paper does not address this.

- **No discussion of what happens when $\Upsilon_G(k) \ge C\cdot k$ does not hold.** In real-world graphs, the eigen-gap may be ambiguous or nonexistent. A practical algorithm should at least detect that the condition is violated and report failure rather than return a wrong value.

### Trivial

None. (The formatting artifacts and garbled equations noted by the critic are parser issues, not author errors.)

## Nice-to-Haves

- Larger-scale experiments (e.g., $n$ up to 50,000–100,000) to better demonstrate near-linear scaling.
- Experiments probing failure regimes (e.g., varying $q$ past the theoretical threshold for SBM until the algorithm breaks).
- A runtime comparison to computing the top $k+1$ eigenvalues using a standard iterative solver (e.g., scipy.sparse.linalg.eigsh).
- A brief comment on whether the sparsification circularity is resolved in the Sun & Zanetti (2019) algorithm, or a sketch of how one could estimate $1-\lambda_{k+1}(N_G)$ coarsely before sparsification.

## Removed Points

- **Criticism about "first nearly-linear time algorithm" not checking whether SDE methods apply directly.** This is kept in the Strengths (the paper does address the SDE literature in Related Work) but the critic's phrasing about "missing differentiation" is partially valid; however, the paper does cite relevant SDE references and distinguishes its task. The concern is more about exposition completeness than a factual error. I've subsumed the valid kernel of this into the Minor weakness about baseline comparisons.

- **Criticism about Lemma 3 appearing "garbled" —** acknowledged by the critic as a parser artifact. Removed.

- **Criticism about "executive" being ambiguous —** parser artifact (likely "consecutive" in the original). The substance (lack of rigorous termination argument) is preserved in the Major weakness.

- **Criticism that the paper claims novelty without checking "whether existing spectral density estimation methods... could be applied directly" —** This conflates missing differentiation with missing related work. The paper cites Lin et al. (2016), Jin et al. (2024), and Braverman et al. (2022). The differentiation is that the problem requires exact $k$ rather than density estimation. This point does not add new information beyond what the paper already addresses.

## Novel Insights

None beyond the paper's own contributions. The reviewer analysis does not uncover a novel interpretation of the paper's approach beyond what the authors state.

## Suggestions

1. **Resolve the sparsification circularity.** Either provide a self-contained procedure that estimates $1-\lambda_{k+1}$ coarsely (e.g., via a few Lanczos iterations or using a known spectral bound that depends only on $G$), or explain how the cited Sun & Zanetti (2019) algorithm circumvents this issue. This is the most critical fix.

2. **Repair the Wasserstein-1 analysis.** Explicitly construct $q$ as a valid probability measure (e.g., following the post-processing in Braverman et al., 2022) before applying the Kantorovich–Rubinstein dual, or switch to a discrepancy measure (such as maximum mean discrepancy) that does not require the estimator to be a proper density.

3. **Provide a rigorous termination argument for the main algorithm.** Define the intervals precisely, prove that under the gap condition there exist consecutive values of $i$ for which the eigenvalue count is exactly $k$ with high probability, and bound the number of iterations formally. Include discussion of how noise in CountEigenvalues is handled (e.g., rounding or probabilistic guarantees on the termination condition).

4. **Strengthen the experiments.** Add a baseline comparison (Lanczos eigengap computation), report accuracy rates over multiple random trials (not just correctness anecdotes), include a plot of accuracy vs. $q$ to probe the breakdown regime, and test on larger graphs to better demonstrate the near-linear scaling claim.

## Score and Decision

The paper tackles a well-motivated problem and sketches a plausible algorithmic framework. The core idea of combining cluster-preserving sparsification with SDE-based eigenvalue counting is genuinely novel, and working under the same condition as existing spectral clustering analyses is a clean contribution.

However, the paper in its current form has three significant issues that prevent acceptance: (1) the sparsification step contains a circular dependency that is not resolved in the presentation; (2) the Wasserstein-1 analysis of the eigenvalue counting subroutine relies on an unverified assumption about $q$ being a probability measure; and (3) the main algorithm's correctness argument is too vague to be accepted as a rigorous theoretical guarantee. While these issues are potentially fixable (the paper cites the right prior work for resolution of (1) and (2), and (3) requires additional analysis), they are substantive enough that the paper's central claims are not fully supported in this version. The experiments, while supportive, are too limited to compensate for the theoretical gaps.

I recommend rejection — a substantially revised version that addresses the sparsification dependency, repairs the Wasserstein-1 proof, and provides a rigorous termination analysis could be resubmitted.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>