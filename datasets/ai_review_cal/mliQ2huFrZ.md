- Decision: Accept
- Avg Score: 7.25
- Scores: 5, 8, 8, 8
Now I have all the information needed to synthesize the final review. Let me compose it.

## Summary

This paper introduces Class Probability Matching (CPM), a novel framework for label shift adaptation that estimates the class probability ratio \(w^* = q(y)/p(y)\) by matching probabilities on the label variable \(Y\) rather than the feature variable \(X\). The key theoretical contribution (Theorem 3.1) proves equivalence between matching on \(Y\) and matching on \(X\), while reducing the matching problem from high-dimensional feature space to \(K\) scalar equations. The proposed algorithm CPMCN uses calibrated neural networks (BCTS) to estimate \(p(y|x)\) and solves the matching via BFGS with \(O(n_q K^2)\) per-iteration complexity. The paper provides identifiability guarantees, weight estimation error bounds, and generalization bounds. Experiments on CIFAR100 show CPMCN outperforming existing matching and EM-based methods, and runtime comparisons demonstrate dramatic computational advantages over feature-matching approaches.

## Strengths

- **Novel equivalent matching framework on the label variable.** Theorem 3.1 proves that matching on the one-dimensional label \(Y\) (Eq. 8) is equivalent to matching on the \(d\)-dimensional feature \(X\) (Eq. 5) under the label shift assumption. This provides the same theoretical guarantee as feature-probability matching while reducing the matching problem from high-dimensional distributions to \(K\) scalar equations — a genuine algorithmic insight.

- **Dramatic computational improvement over feature-matching methods.** The algorithm solves Eq. 11 with BFGS at \(O(n_q K^2)\) per iteration. Figure 4 shows that on CIFAR100, CPMCN completes in under 10 seconds, while KMM does not finish after 10,000 seconds and LTF takes over 1,000 seconds. This directly validates the efficiency claim made in the introduction.

- **Identifiability and generalization guarantees.** Theorem 5.3 establishes that \(w^*\) is the unique solution to the CPM equations under linear independence of class-conditional densities. Theorems 5.4 and 5.5 provide finite-sample bounds on weight estimation error and target-domain excess risk, giving rigorous theoretical support to the algorithm.

- **Empirical evidence for calibration's importance.** Figure 3 directly compares CPMCN without calibration vs. with three calibration methods (VS, NBVS, BCTS), showing substantially lower MSE and higher ACC for all calibrated variants. This provides concrete experimental support for the claim that calibration improves ratio estimation.

- **Convergence validation.** Figure 1 demonstrates that the objective function and the MSE weight-estimation error decrease monotonically to near zero, confirming that the BFGS optimization effectively recovers the true ratio.

## Weaknesses

### Fatal
None.

### Major
- **Experimental evidence in the main text covers only CIFAR100.** The paper states it evaluates on MNIST, CIFAR10, and CIFAR100 with two shift types (Dirichlet and tweak-one), but Table 1 — the only quantitative results table in the main text — shows only CIFAR100 under Dirichlet shift. The remaining configurations (MNIST, CIFAR10, and tweak-one shift on CIFAR100) are described in the experimental setup but no main-text tables report their results. The paper makes the broad claim that "CPMCN outperforms existing matching methods and EM-based algorithms" for "all datasets," but a reader of the main text alone cannot verify this for any dataset other than CIFAR100 under one shift type. (Note: Additional results may reside in the appendix, which was stripped by the parser. However, the main text should be self-contained for its central empirical claims.)

- **The strong claim of "outperforming existing methods" is under-supported by what is shown.** While CPMCN does achieve the best results across all \(\alpha\) values in Table 1 (CIFAR100 Dirichlet), the margins over EM are sometimes small (e.g., ACC 77.42 vs 76.24 for \(\alpha=0.1\)). Without seeing results for MNIST, CIFAR10, and the tweak-one shift, the generality and consistency of the claimed improvement cannot be assessed from the main text alone.

### Minor
- **The theoretical argument linking calibration to bias reduction is imprecisely framed.** The discussion following Theorem 5.4 argues that calibration "significantly reduces the bias error term" (\(\inf_{f\in\mathcal{F}} \mathcal{R}_p(f) - \mathcal{R}_p^*\)). Strictly speaking, the bias term is the approximation error of the function class \(\mathcal{F}\); adding calibration parameters (BCTS adds a layer with \(2K\) parameters) expands \(\mathcal{F}\) to a superset, so the infimum over the expanded class is at most the infimum over the original class. The claim of *significant* bias reduction is not formally justified from this alone — the practical benefit comes from the fact that calibration procedures correct systematic miscalibration in probability estimates, which is critical for the matching equations. The paper would benefit from reframing this argument in terms of probability estimation consistency rather than approximation error reduction.

- **No confidence intervals or statistical significance tests.** The paper reports medians and standard deviations over 100 repetitions but does not provide confidence intervals or statistical tests (e.g., paired comparisons). Given the modest margins in Table 1 (e.g., \(\alpha=0.1\), ACC 77.42 vs 76.24), significance testing would strengthen confidence in the claimed improvements.

- **The comparison with KMM is rhetorically weak.** KMM is included only for running time ("does not produce any results even after running for over 10,000 seconds"), which supports the efficiency claim but does not provide an accuracy comparison. This is understandable since KMM is not designed for this setting, but the paper should be upfront about this limitation rather than treating it as a full comparison.

### Trivial
- Minor formatting and notation inconsistencies (e.g., "CIFAR1oO" line 233, inconsistent use of "ŵ" vs "\widehat{w}").
- Figure 3 and Figure 4 share a single caption (line 243), which appears to be a formatting error.

## Nice-to-Haves
- Include a synthetic experiment that isolates the effect of calibration on the matching equations to visually separate the calibration benefit from other algorithmic components.
- Discuss potential failure modes for large \(K\) (the algorithm scales with \(K^2\) per iteration; CIFAR100 uses 100 classes but the Dirichlet shift only uses 10 active classes).
- Provide a brief proof sketch of Theorem 3.1 in the main text to strengthen the presentation of the core theoretical contribution.

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **Harsh critic's claim that the theoretical bounds are "standard and not novel":** This is a subjective judgment about novelty rather than a specific weakness. The bounds are appropriate for the paper's contribution and serve the purpose of connecting calibration to the matching framework.

2. **Harsh critic's claim that the paper "lacks a discussion of potential failure modes":** This is a suggestion for improvement, not a weakness. The paper scopes itself to standard label shift settings.

3. **Strength Finder's characterization of "state-of-the-art experimental results on large datasets":** This strength is overstated given that only one dataset/shift combination is shown in the main text. Downgraded to reflect the actual evidence presented.

4. **Strength Finder's claim that the generalization bound "explicitly explains the benefit of calibrated networks":** The bound's connection to calibration is less direct than claimed — it applies to the function class \(\mathcal{F}\) of calibrated networks, but the theoretical argument about "bias reduction" is imprecise (see Minor weakness above).

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs largely recapitulate the paper's content without introducing orthogonal observations. The one noteworthy perspective is the framing of the calibration argument: the harsh critic correctly identifies that the paper conflates calibration (confidence correction) with approximation error reduction. This distinction — that calibration improves probability estimation fidelity rather than discriminative power — is a genuinely useful refinement to the paper's narrative.

## Suggestions
- Add a comprehensive results table (or tables) covering all three datasets (MNIST, CIFAR10, CIFAR100) and both shift types (Dirichlet and tweak-one) to the main text. A combined summary table with means/standard deviations across all settings would allow readers to assess the generality of the claimed improvement.
- Reframe the theoretical discussion of calibration's role: instead of claiming calibration reduces the approximation error (which adds at most marginal expressive power), explain that the matching equation (Eq. 8) requires accurate *probability estimates* of \(p(y|x)\), and calibration ensures these estimates are well-calibrated, reducing systematic bias in the expectation computation.
- Add statistical significance indicators (e.g., bold for best, underline for second-best with significance tests) to the results tables.
