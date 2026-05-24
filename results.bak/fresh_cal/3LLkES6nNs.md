Here is my final consolidated review:

## Summary

This paper establishes the Neural Network Gaussian Process (NNGP) correspondence for Neural ODEs by viewing them as infinite-depth ResNets with shared weights. The authors prove that: (1) the limiting covariance of a finite-depth ResNet approximation exists and satisfies the NNGP property, (2) the depth and width limits commute via random matrix theory, yielding the NNGP correspondence for the Neural ODE itself, and (3) the resulting kernel is strictly positive definite for non-polynomial Lipschitz activations. The paper also provides a dynamic programming algorithm for computing the covariance matrix and supports the theory with experiments.

## Strengths

- **Novel NNGP correspondence for Neural ODEs with shared weights (Theorem 4.5)**: The paper is the first to establish that wide Neural ODEs converge to Gaussian processes, overcoming the key obstacle that shared weights prevent standard SDE-based arguments. The explicit closed-form limiting covariances for both shared-weight (autonomous) and independent-weight (non-autonomous) cases are derived, revealing a genuine architectural distinction — the independent-weight case collapses to a shallow two-layer kernel while the shared-weight case yields a richer integral form.

- **Strict positive definiteness of the limiting kernel (Theorem 4.8)**: The paper proves that the limiting NNGP kernel \(\Sigma^*\) restricted to the unit sphere is strictly positive definite for any non-polynomial Lipschitz activation, even in the autonomous shared-weight case. This property is essential for global convergence guarantees of gradient-based methods and for benign overfitting theory, and the result extends the finite-depth analysis to the infinite-depth limit.

- **Approximation bound for ResNet→Neural ODE (Proposition 4.1)**: The paper provides an explicit \(O(T/L)\) error bound (holding almost surely) for the Euler discretization of the Neural ODE, establishing that the finite-depth ResNet faithfully approximates the continuous-depth model. This bound is the quantitative foundation for the entire analysis.

- **Efficient DP algorithm for covariance computation (Section 4.5)**: The \(O(L^2 N^2)\) dynamic programming algorithm addresses a computational challenge unique to the shared-weight ResNet setting, where skip connections couple all previous layers — a problem absent in previous NNGP works on feed-forward, convolutional, or recurrent networks.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Proof sketch for Lemma 4.1 (limit interchange) is very brief in the main text.** The central technical step — showing that the depth and width limits commute via uniform convergence derived from RMT — is described in only two sentences (lines 177–178), referring to "Lemma A.3 or A.2" without any explanation in the main text of how the RMT result applies or why the relevant random quantities satisfy its conditions. While full proofs are standardly deferred to the appendix in conference papers, the main text provides too little reasoning for a reader to assess the plausibility of the key argument without consulting the (separate) appendix. This is an exposition concern rather than a correctness concern, but for a theory paper built around this lemma, a slightly expanded sketch would substantially improve accessibility.

- **The function \(V_\phi\) in the DP algorithm is not defined in the main text.** Algorithm 1 and the recurrence (line 242) use \(V_\phi(\cdot,\cdot,\cdot)\) but the main text provides no definition. From context this appears to be a function that computes bivariate Gaussian expectations \(\mathbb{E}[\phi(z_1)\phi(z_2)]\) given covariance terms — a standard construction in the NNGP literature — but the paper should state this explicitly. As it stands, the algorithm description is incomplete without consulting the appendix.

- **Constants \(C_1, C_2\) in Proposition 4.1 are left unspecified.** The bound \(\|h^L(x)-h(x,T)\| \leq (A/B)(e^{BT}-1)\beta\) contains constants \(C_1, C_2\) that are never resolved. The \(O(T/L)\) rate is clear, which is the important part, but the statement is somewhat imprecise as presented in the main text.

### Trivial
- **Experimental details are sparse.** Hyperparameters, dataset splits, number of runs, and error bars are not reported for the MNIST experiment (Figure 3). The figures are described but the actual images cannot be verified from the text alone. These are minor concerns for a primarily theoretical paper but should be tightened for publication.

## Nice-to-Haves
- Adding a brief sketch in the main text of how the RMT lemma (A.3/A.2) is applied to obtain uniform-in-width convergence of depth would strengthen the exposition.
- Defining \(V_\phi\) explicitly in the main text or the algorithm caption would improve reproducibility.
- Reporting the exact values from the MNIST experiment (test accuracy numbers) rather than only showing a small figure curve would be helpful.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "Lemma 4.1's proof is insufficient to the point of being non-verifiable in the main text / 'if the appendix does not fully justify the interchange, the entire NNGP correspondence collapses.'"** — This is speculative about appendix content. The parser strips appendix sections from all papers; the full proof exists in the original submission. The criticism about the main text being too brief is retained as a Minor weakness above, but the assertion that the proof is potentially invalid is removed as unverifiable.

- **Harsh Critic: "Proposition 4.1 bound depends on random matrix norms only indirectly... unclear how they incorporate the operator norm of random weight matrices."** — The bound is stated to hold "a.s." (almost surely), which is the standard way to handle random quantities in this literature. The constants subsume Lipschitz constants and norm bounds that follow from standard random matrix concentration. This is a misunderstanding of standard practice.

- **Harsh Critic: "The experiments are not rigorous... do not compensate for the lack of clarity in the theoretical core."** — The criticism about experimental rigor is partly valid but is evaluated in context (theory paper). The claim that experiments must compensate for theoretical clarity is a framing issue, not a separate weakness.

- **Strength Finder: All six listed strengths are retained** as they are specific, concrete, and supported by evidence in the paper. None are generic, and none conflict with verified weaknesses.

## Novel Insights

The two-reviewer synthesis surfaces a key tension that the paper does not fully resolve in the main text: the central claim (NNGP for Neural ODEs) depends on Lemma 4.1 (limit interchange via RMT), yet the main text's treatment of this lemma is thinner than one would expect for the paper's most technically novel step. This is partly an artifact of page constraints and appendix deferral, but it creates an uncomfortable gap between what the paper promises and what a reader can verify from the main body alone. The paper's genuine contribution — showing that shared-weight infinite-depth ResNets converge to a GP distinct from the independent-weight case — is conceptually important and fills a genuine gap in the literature, but its exposition currently asks theorists to trust that the RMT machinery works without giving them enough reasoning to see why.

## Suggestions

- Expand the proof sketch for Lemma 4.1 in the main text by adding 3–5 sentences that explain how the RMT result (Lemma A.3/A.2) implies uniform convergence of \(\hat{\Sigma}_n^L\) in the depth index, and why the Moore–Osgood theorem then gives limit interchange. A high-level equation or diagram showing the dependency structure would help.
- Define \(V_\phi\) explicitly in Section 4.5, even briefly (e.g., "\(V_\phi(\mathbf{A},\mathbf{B},\mathbf{C})\) computes \(\mathbb{E}_{(z_1,z_2)}\phi(z_1)\phi(z_2)\) where \((z_1,z_2)\) has covariance determined by its arguments").
- Add a brief remark in Proposition 4.1 clarifying that the constants depend on the Lipschitz constant of \(\phi\) and follow from Grönwall's inequality applied to the discretized ODE — this would address the concern about "unspecified" constants.
- Include test accuracy numbers and basic experimental setup (dataset split, optimizer, number of runs) in the main text or a clear table.

## Score and Decision

The paper makes a genuinely novel theoretical contribution by extending the NNGP correspondence to Neural ODEs — a non-trivial extension because shared weights break the standard SDE arguments used for prior architectures. The high-level approach (discretize → prove NNGP for finite depth → swap limits via RMT → prove positive definiteness) is coherent and the results are significant for the field. The weaknesses are primarily expository (thin main-text proof sketch, undefined notation in the algorithm, unspecified constants) rather than foundational. None of the verified weaknesses threaten the paper's core claims.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>