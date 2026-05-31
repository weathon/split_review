Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper develops a deep α-stable kernel process (Dα-KP) arising as the infinite-width limit of Bayesian neural networks with infinite-variance (elliptical α-stable) priors on weights at every layer. The core theoretical contribution (Theorem 1) extends Cho & Saul's recursive kernel formula to the infinite-variance regime, showing that the conditionally-Gaussian covariance kernels relate layer-wise in closed form. This enables posterior inference in kernel space rather than feature space, avoiding the exponential \(O(n^{I+2})\) complexity of prior work (Loria & Bhadra) and extending stable processes to multi-layer architectures for the first time. Experiments on discontinuous functions and UCI benchmarks show competitive or superior predictive performance.

## Strengths

1. **Recursive kernel formula for deep infinite-variance architectures (Theorem 1).** The paper derives a layer-wise recursion for the conditional covariance kernel under elliptical α-stable priors, generalizing Cho & Saul (2009) to the infinite-variance setting. This is a genuine theoretical advance that enables the entire subsequent framework. (Section 2, Theorem 1)

2. **Elimination of exponential computational bottleneck.** By working in kernel space rather than feature space, the method avoids the \(O(n^{I+2})\) enumeration required by Loria & Bhadra, making posterior inference feasible in higher dimensions (e.g., 10D in Table 1) where the prior method simply cannot run. This is the clearest practical contribution.

3. **Competitive predictive performance on discontinuous functions and UCI benchmarks.** On discontinuous truth functions (Table 1), Dα-KP substantially outperforms all Gaussian-process-based methods and closely matches the (much more expensive) Stable method in 1D/2D, while being the only stable-process method that scales to 10D. On UCI data (Table 2), Dα-KP is best on Energy and Yacht, and essentially ties GP Bayes on Boston. (Table 1, Table 2)

4. **Demonstrated feature learning for \(\alpha<2\).** Proposition 2 analytically shows that the posterior features depend on the data when \(\alpha<2\) (unlike the deterministic-kernel GP limit). The paper confirms this empirically with heavy-tailed posterior feature distributions (Figure 2 in the submission — Feature learning figure), validating the mechanism for representation learning. (Proposition 2, Section 4.2)

## Weaknesses

### Fatal
None. The core theoretical development is sound, the computational advantage over prior work is clear, and the experimental results support the main claims.

### Major
1. **Depth does not empirically improve predictions, weakening the "deep" framing.** Table 3 shows that increasing depth from \(L=3\) to \(L=16\) yields no meaningful improvement on any of the three test functions. The paper acknowledges this and conjectures that the stable process is "rich enough" with one hidden layer, but this raises the question: what does depth add beyond the shallow case? If the method's primary novelty over Loria & Bhadra is computational scaling (kernel space vs. feature space) — which is a real and important contribution — the paper should either (a) demonstrate a scenario where depth matters, or (b) honestly de-emphasize depth and reframe the contribution. As it stands, the title and contributions highlight "deep" but the evidence does not yet support depth as an advantage.

### Minor
1. **Runtime comparison with variational alternatives is deferred to supplementary material.** The paper claims the method is "computationally viable" relative to DIWP (which uses 8000 variational steps) but only reports timing in the supplementary section. Including a summary runtime table in the main paper would substantiate this claim without requiring readers to consult the supplement. This is easily fixable.

2. **The feature learning demonstration is qualitative and not directly linked to prediction quality.** Figure 2 shows that posterior features are non-Gaussian (heavy-tailed), confirming the stochastic kernel is at work. However, the paper does not connect this to improved prediction or interpretable representations. While the existence of feature learning is a genuine point of differentiation from GPs, the practical value would be strengthened by showing, e.g., that learned features correlate with meaningful structure in the data.

3. **Mutual information analysis (Figure 1) is not connected to predictive performance.** The finding that conditional mutual information decays more slowly for smaller \(\alpha\) is theoretically interesting, but the paper does not verify that this translates to better long-range dependency capture in a prediction task. This is a missed opportunity to strengthen the narrative.

### Trivial
- The 2D test function definition on line 132 appears to have a typo: both terms use \(\xi_1\) rather than \(\xi_1\) and \(\xi_2\).
- Algorithm 1 references sub-algorithms (alg:s_given_s, alg:s_given_y) that are deferred to the appendix. While the appendix exists in the original submission, the main text could provide a brief sketch of the MH proposals for self-containedness.

## Nice-to-Haves
- A sensitivity analysis for \(\alpha\) (e.g., \(\alpha \in \{0.5, 1.0, 1.5\}\)) on the synthetic functions would help readers understand the role of the stability index.
- A synthetic example where depth *does* matter (e.g., a compositional function) would substantially strengthen the "deep" claim.
- Reporting whether DIWP kernel hyperparameters were tuned per dataset would address a natural reviewer question.

## Removed Points

These points were considered but removed with justification:

- **"Baseline comparisons lack hyperparameter tuning"** (Harsh Critic, Issue 2): This criticism states that "no hyperparameter search is conducted for any method." However, GP Bayes (via the `tgp` package) uses MCMC to integrate over kernel hyperparameters, and GP MLE (via `mlegp`) optimizes them by maximum likelihood — both are standard packages that handle tuning internally. For DIWP and NNGP, the paper explicitly uses the original settings from Aitchison et al. (2021), which is standard practice. The GP methods on Energy and Yacht show substantial-margin improvements for Dα-KP that tuning is unlikely to erase; on Boston the methods are essentially tied, and this is honestly reported. The criticism as framed is factually incorrect for the GP methods and overstated for DIWP/NNGP.

- **"Theorem 1 proof not fully provided"** (Harsh Critic): The paper provides the characteristic function form and the conditionally-Gaussian representation. For a conference paper, this level of detail is standard. The derivation follows from known properties of elliptical α-stable vectors and the Cho & Saul recursion; a full measure-theoretic proof would be appropriate for a journal but is not required here.

- **"Algorithm underspecified"** (Harsh Critic): Steps reference sub-algorithms in the appendix. The parser strips the appendix from all papers; the original submission contains these details. This is not an author error.

- **Multiple generic or speculative criticisms** (e.g., "could the metric be measuring a proxy?", concerns about the "Stable method may have tuned α differently" without evidence): These lack a concrete anchor in the paper and are removed as per the filtering guidelines.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the combined reviews is the tension between the technical generality of the recursion (which holds for any depth) and the empirical finding that depth has no effect on the test functions studied. This suggests that the infinite-variance limit may saturate representational capacity at one hidden layer for simple discontinuous functions, but could matter for more structured data (e.g., compositional or hierarchical targets). This points to a specific future direction — identifying the function classes where depth in α-stable processes is necessary — that would sharpen the paper's contribution.

## Suggestions

1. **Address the depth issue directly** by either (a) finding a test function where depth demonstrably helps (e.g., a compositional function), or (b) reframing the paper's contributions to de-emphasize depth as an advantage and instead highlight the computational breakthrough (kernel space → polynomial complexity) plus the extension to multi-layer architectures as a technical contribution that future work can build on. Either approach would resolve the paper's biggest weakness.

2. **Add a runtime summary to the main paper.** A single sentence or a small table showing total runtimes for Dα-KP vs. DIWP on the UCI datasets would substantiate the "computationally viable" claim without requiring the supplement.

3. **Clarify hyperparameter handling for all baselines** in the experimental setup, noting that the GP packages tune internally and that DIWP/NNGP use the original paper's settings.

## Score and Decision

**Originality:** 7/10 — Extending Cho & Saul's recursion to infinite-variance priors is a novel and non-obvious step. The kernel-space approach to stable processes is original.  
**Importance of research question:** 7/10 — Enabling inference in heavy-tailed prior processes and overcoming the exponential bottleneck of Loria & Bhadra is a meaningful problem.  
**Claims well-supported:** 7/10 — Core claims are supported, but the "deep" advantage is not empirically validated.  
**Soundness of experiments:** 7/10 — Experiments are well-designed with 20 train/test splits and standard deviations. The main gap is the tuning concern (which is partially addressed by standard GP packages) and the lack of a runtime table.  
**Clarity of writing:** 8/10 — Well-structured, clear motivation, honest about limitations. The algorithm section is clear given the appendix context.  
**Value to research community:** 8/10 — The kernel-space recursion opens up a family of methods for stable-process posteriors that prior work could not address.

MY FINAL SCORE: <score>7.5</score>  
MY FINAL DECISION: <decision>Accept</decision>