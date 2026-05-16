Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper addresses subspace inference for Bayesian neural networks by proposing three complementary improvements: (1) a **block-averaging (BA) subspace construction** that partitions the SGD trajectory into blocks and uses their means for PCA, capturing full-trajectory variability at the same memory cost as tail-only methods; (2) **new subspace evaluation metrics** based on the Bayes factor and prior predictive (test-data evidence ratio); and (3) **RQMC-based importance sampling (RQMC-IS)** for efficient posterior predictive inference in the subspace. Experiments on synthetic data, UCI regression, and CIFAR classification show that BA subspaces closely approximate full-trajectory subspaces (angular distance ≈ 0°) while tail-only subspaces are nearly orthogonal (≈ 89°), and that BA+RQMC achieves better test log-likelihood than TT+ESS/VI on most datasets.

## Strengths

1. **Block-averaging closely approximates the full-trajectory subspace at the same memory cost as tail-only methods.** Table 1 shows an angular distance of 0.0±0.0 degrees between the BA subspace and the full-trajectory subspace, while the tail-only subspace is 88.8±1.3 degrees away — nearly orthogonal. Figures 1 and 2 visually confirm that BA preserves the full trajectory's structure. This directly addresses the known limitation that tail-only methods fail to capture the complete variability of the SGD trajectory.

2. **New quantitative evaluation framework for subspaces using Bayes factors and prior predictive checks.** Definitions 1–3 formalize subspace evidence, Bayes factor, and test-data evidence ratio, enabling direct comparison of subspace quality without relying on downstream task performance. Figure 3 and Table 3 demonstrate that these metrics discriminate between BA and TT subspaces (Bayes factors strongly favor BA), and the framework is principled (grounded in Bayesian model comparison). This fills a gap: prior work evaluated subspaces only indirectly via predictive performance.

3. **RQMC-IS achieves lower RMSE with fewer forward passes than MCMC/VI for subspace inference.** Table 2 shows RQMC-IS with 1,024 samples achieving RMSE 0.14, outperforming ESS (0.23), VI (0.40), and standard IS (0.22), while requiring far fewer forward passes (1k vs. 20k for ESS). Theorem 2 provides a theoretical convergence guarantee (O(N^{-1+ε}) RMSE). This is a practical contribution for making subspace inference computationally feasible.

4. **Consistent empirical gains across diverse benchmarks.** BA+RQMC achieves the highest test log-likelihood on 4/5 small UCI datasets and 6/6 large UCI datasets (Tables 4, 5). On CIFAR-10, BA+VI achieves 94.4% accuracy vs. TT+VI at 94.0% (Table 6). BA consistently outperforms TT under increasing corruption severity on CIFAR-10-C (Table 7). These results demonstrate generalization across regression and classification settings.

## Weaknesses

### Fatal
None.

### Major
1. **Missing control: BA vs. uniform subsampling without averaging.** The paper does not compare BA against a baseline that simply selects M uniformly-spaced checkpoints from the trajectory (without averaging within blocks). The angular distance between a uniformly-sampled subspace and the full trajectory should also be small simply because it covers the whole trajectory. Without this control, the paper cannot substantiate that *averaging* (as opposed to *covering the whole trajectory*) provides the benefit. The paper describes BA as "structured downsampling" (Section 4.1) but never isolates the effect of averaging from coverage. This does not invalidate BA — even uniform subsampling would be a useful alternative to TT — but it means the specific contribution of "block-averaging" is not rigorously disentangled from simply using the full trajectory at reduced resolution.

2. **Incomplete baseline grid prevents isolating subspace vs. inference contributions.** Tables 4 and 5 compare BA vs. TT using different inference methods (ESS, NUTS, VI, RQMC-IS), but the grid is incomplete: "BA + ESS" and "TT + RQMC" are missing. Without these crossed comparisons, the reader cannot tell whether BA+RQMC's advantage comes from the better subspace (BA) or the better inference method (RQMC), or both. For example, if TT+RQMC also outperforms BA+ESS, then the inference method is the dominant factor. This is a standard experimental design gap that should be filled for the results to cleanly support the paper's three-pronged narrative.

### Minor

1. **The main text does not sketch how the Bayes factor integrals are computed.** Definitions 1–3 define the integrals (subspace evidence, test-data evidence), but the main text gives no indication of how these high-dimensional integrals are evaluated (e.g., importance sampling, Laplace approximation, bridge sampling). The paper states that details are in Appendices B/C/D, which were stripped by the parser. Still, the main text should at least briefly describe the estimation approach (e.g., "we estimate these via self-normalized importance sampling with a Gaussian proposal") so that a reader can assess whether the numerical results in Table 3 and Figure 3 are reliable. Without this, the evaluation metrics contribution is incompletely specified in the main paper.

2. **The novelty claim about evaluation metrics is somewhat overstated.** The paper states "there are currently no metrics designed to directly evaluate how well the subspace represents the data-relevant portions of the full parameter space" (Section 1). While applying marginal likelihood and Bayes factors to subspace evaluation in BNNs is a useful contribution, these are standard Bayesian model comparison tools. The contribution is in the *application* to subspace quality assessment, not the invention of fundamentally new metrics. The framing should be adjusted to "adapting standard Bayesian model comparison to subspace evaluation" rather than claiming a gap that does not cleanly exist.

3. **Table 2 does not name the dataset/model used for the RMSE comparison.** The paper says "synthetic data regression example from Izmailov et al. (2020)" is used as a running example, but the text introducing Table 2 does not explicitly specify which dataset was used for the RMSE values. This should be stated.

4. **Cost comparison in Table 2 uses an incomplete metric.** Measuring cost by "number of forward passes on the training set" is reasonable for IS and RQMC-IS, but ignores that VI requires backpropagation (which is more expensive per iteration than forward passes) and ESS has a burn-in period that also incurs cost. A fair comparison should include wall-clock time or total likelihood evaluations inclusive of burn-in for MCMC methods.

5. **Subspace rank \(k\) is not reported for any experiment.** The paper never states what subspace dimensionality was used in Tables 3–7 and Figure 5. Without knowing whether \(k=2\), \(k=5\), or \(k=20\), the reader cannot assess whether the subspace is truly low-dimensional, nor can they reproduce the experiments.

6. **No ablation on the number of blocks \(M\) for BA.** Figure 3 shows Bayes factors vs. \(M\) for the full trajectory comparison, but there is no analysis of how BA's quality (angular distance, predictive performance) varies with \(M\). Is BA robust to \(M\)? Is there a trade-off?

7. **Missing full-space baselines for context.** The UCI experiments compare BA and TT subspaces but do not include full-space inference baselines (e.g., full-space HMC, SWAG, deep ensembles). Without these, the reader cannot assess whether subspace methods are competitive with full-space approximations at all, only that BA > TT.

8. **Figure 5 is qualitative.** The heat maps visually show BA has more dark-blue (low-loss) regions than TT, but the paper does not quantify this (e.g., percentage of points below a loss threshold). This weakens the evidence for "BA subspaces contain more high-likelihood points."

### Trivial
- The return line in Algorithm 1 (`P = V^T Σ / sqrt(M-1)`) could be clearer about the output dimensionality (\(d \times k\) vs. \(k \times d\)).
- The paper does not discuss potential failure modes of RQMC-IS when the posterior in the subspace is multimodal or heavily skewed.
- Minor: the paper uses "blocks" terminology but the online update in Algorithm 1 effectively computes block means — this could be described more intuitively as "running block mean."

## Nice-to-Haves
- A control experiment comparing BA, TT, and *equidistant subsampling without averaging* would cleanly separate the effect of trajectory coverage from the effect of averaging.
- Completing the crossed baseline grid (BA+ESS, TT+RQMC, BA+NUTS) would cleanly attribute gains to subspace vs. inference method.
- Quantifying Figure 5 (e.g., "% of subspace points with loss below threshold") would strengthen the qualitative visual evidence.
- A discussion of how the subspace rank \(k\) was selected (e.g., based on explained variance threshold) would improve reproducibility.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Criticism about Theorem 2 assumptions not being in the paper** (Harsh Critic Issue 3): The paper references "Assumption 3 and 4" which are defined in the appendix (stripped by the parser). Per the rules, weaknesses about missing appendix content are removed.
- **"The paper does not discuss whether centering tail deviations using the tail mean would fix the issue"** (Section 3.1 note): This is a speculative suggestion, not a weakness of the paper as written.
- **Criticism about BA sensitivity to M not being discussed** (from Missing Parts section): The paper already investigates varying M in Figure 3 (Bayes factor vs. M), though not specifically for BA's own properties — this is more of a nice-to-have than a weakness.
- **"The paper does not discuss the additional cost of storing block means"**: The paper explicitly states BA has "the same algorithmic complexity and memory cost as the TT construction" (Section 4.1), so this concern is already addressed.
- **"The high deviation values show tail construction is unstable"** (from Figure 3 discussion): The paper's own text already makes this point; it's not an unrecognized weakness.

## Novel Insights
None beyond the paper's own contributions. The reviews primarily identify experimental gaps (missing controls, incomplete baseline grid) rather than offering novel scientific observations about subspace inference.

## Suggestions

1. **Add the uniform-subsampling control.** Compare BA against equidistant subsampling (pick every \(n/M\)-th checkpoint without averaging) on angular distance to FT and on downstream predictive performance. This will reveal whether averaging contributes anything beyond trajectory coverage.

2. **Complete the baseline grid in Tables 4 and 5.** Add BA+ESS and TT+RQMC (and ideally BA+NUTS) to separate subspace quality from inference method quality. This is the cleanest way to support the claim that both BA and RQMC-IS are independently beneficial.

3. **Briefly describe the Bayes factor integral estimation method in the main text.** Even one sentence (e.g., "we estimate \(p(D\mid\mathcal{Z})\) via self-normalized importance sampling with a \(\mathcal{N}(0,I)\) proposal fitted to the projected trajectory points") would make the evaluation metrics contribution reproducible from the main paper.

4. **Report the subspace rank \(k\) used in each experiment** and briefly justify the choice (e.g., based on explained variance ratio).

5. **Specify the dataset used for Table 2 explicitly** and include wall-clock time or total likelihood evaluations (including burn-in for MCMC) as a complementary cost metric.

6. **Tone down the novelty claim** about evaluation metrics — frame it as "adapting standard Bayesian model comparison tools to subspace evaluation" rather than claiming no prior metrics exist.

## Score and Decision

This paper makes solid contributions: BA subspace construction is simple, well-motivated, and empirically effective; RQMC-IS offers practical efficiency gains; and the Bayes-factor evaluation framework is principled. The experimental results convincingly show BA > TT across multiple benchmarks. However, the paper has two significant experimental gaps (missing uniform-subsampling control and incomplete baseline grid) that prevent clean attribution of the claimed benefits. These are fixable but nontrivial. The remaining issues (missing details, overclaiming) are minor. The paper is clearly above the rejection threshold but needs focused revisions to justify its specific claims about the *averaging* contribution and to separate subspace from inference effects.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>