- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes BreZOSBA, a fully single-loop zeroth-order algorithm that uses Bregman distance to solve nonsmooth stochastic black-box bilevel optimization problems. The main theoretical contribution is a non-asymptotic convergence guarantee with query complexity \(\mathcal{O}(d_1(d_1+d_2)^2\epsilon^{-2})\) to reach an \(\epsilon\)-stationary point measured by \(\frac1T\sum\mathbb{E}\|\mathcal{G}^t\|^2 \le \epsilon\). This is the first convergence result for the nonsmooth black-box bilevel setting and improves on prior smooth-only bounds. Experiments on data hyper-cleaning and hyper-representation learning show BreZOSBA achieves higher test accuracy than two baselines (ZDSBA, HOZOG).

## Strengths

1. **First complexity result for nonsmooth black-box bilevel optimization**: Theorem 1 and Remark 2 derive a total query complexity of \(\mathcal{O}(d_1(d_1+d_2)^2\epsilon^{-2})\). This is the first non-asymptotic guarantee for the nonsmooth setting and improves over the smooth-only bound of \(\tilde{\mathcal{O}}((d_1+d_2)^4\epsilon^{-3})\) from Aghasi & Ghadimi (2024).

2. **Fully single-loop zeroth-order framework**: Algorithm 1 updates \(\mathbf{x},\mathbf{y},\mathbf{z}\) simultaneously without inner iterations for lower-level solving or Hessian-inverse approximation, unlike prior black-box bilevel methods that require inner loops (Section 4.1). This design is the key enabler for query reduction.

3. **Handling nonsmooth \(h(\mathbf{x})\) via Bregman distance**: The paper extends zeroth-order bilevel optimization to problems with a convex nonsmooth regularizer by incorporating mirror descent with Bregman distance (Eqn. 19, Section 4.2), a setting prior work could not address.

4. **Rigorous non-asymptotic analysis with explicit variance bounds**: Lemma 3 characterizes the bounded variance of the zeroth-order gradient estimators with explicit dependence on \(d_1,d_2\) (Remark 1). Lemmas 4–6 establish descent properties for the lower-level and auxiliary variables, and Theorem 1 assembles them into a complete convergence result.

5. **Consistent empirical accuracy improvement**: Tables 2 and 3 show BreZOSBA achieves higher test accuracy than ZDSBA and HOZOG across MNIST, FashionMNIST, CIFAR-10, and SVHN in both application tasks (e.g., MNIST: 89.31% vs 85.76% and 82.79% in Table 2).

## Weaknesses

### Fatal
None.

### Major

1. **Experimental protocol does not cleanly support the query-efficiency claim.** The experiments impose a wall-time cutoff (600s for data hyper-cleaning, 3600s for hyper-representation learning). Because the baselines (ZDSBA, HOZOG) have inner loops that make each outer iteration slower than BreZOSBA's single-loop design, the time limit may restrict how many queries the baselines can execute. Figures 1 and 2 plot accuracy vs. queries, but the baselines' curves may be truncated by the time limit — there is no evidence from these curves that the baselines would not continue to improve if given the same query budget under a fixed-query protocol. The paper conflates two distinct resources (time and queries). This weakens the central claim of practical query efficiency.

2. **The complexity comparison with prior work uses different stationarity measures.** The paper states its \(\mathcal{O}(d_1(d_1+d_2)^2\epsilon^{-2})\) bound in terms of \(\frac1T\sum\mathbb{E}\|\mathcal{G}^t\|^2\) (where \(\mathcal{G}^t = \frac1\alpha(\mathbf{x}^{t+1}-\mathbf{x}^t)\)), while comparing against Aghasi & Ghadimi (2024)'s \(\tilde{\mathcal{O}}((d_1+d_2)^4\epsilon^{-3})\) bound for \(\|\nabla F(\mathbf{x})\|^2\). The paper acknowledges these are different metrics in Table 1, but the text claims to "surpass the performance of existing methods" (abstract, conclusion) without a bridging argument. The paper does not bound the gap between the smoothed composite stationarity condition and the original problem's stationarity. This makes the headline complexity improvement less directly comparable than it appears.

3. **No ablation isolating the Bregman distance component.** The paper's title and methodology emphasize Bregman distance for handling nonsmooth regularization, but the experiments never compare against a variant that replaces the mirror descent step with standard Euclidean proximal gradient (which Section 4.2 notes is a special case when \(\psi(\mathbf{x}) = \frac12\|\mathbf{x}\|^2\)). Since the baselines cannot handle nonsmooth \(h(\mathbf{x})\) at all, any improvement could stem from the ability to accommodate nonsmoothness generally, the fully single-loop structure, or the Bregman choice specifically. Without this ablation, the claim that Bregman distance is specifically the enabler for query efficiency in the nonsmooth setting is empirically unsupported.

### Minor

1. **Bregman function \(\psi_t\) used in experiments not specified.** Section 4.2 discusses several possibilities (Euclidean, adaptive matrix like Adam, etc.), but the experimental section (Section 6) never states which Bregman function was actually used. This makes the core methodological choice opaque.

2. **No sensitivity analysis on smoothing parameters \(\eta, \mu\).** The theory sets these as functions of \(\epsilon\) (Remark 1), but the experiments fix \(\eta_1 = \eta_2 = \mu_1 = \mu_2 = 10^{-4}\) for all tasks without showing robustness or providing tuning guidance. The ablation studies only vary \(B'\) and \(r_\mathbf{z}\).

3. **Very low test accuracy on CIFAR-10 and SVHN not discussed.** The reported accuracies are ~20% and ~14% respectively (Tables 2, 3). The paper does not acknowledge this limitation or explain whether the tasks (data hyper-cleaning / hyper-representation learning with random features or LeNet-5) are well-posed for these datasets.

### Trivial
None.

## Nice-to-Haves
- A fixed-query comparison (all methods run to the same query budget, no time limit) would cleanly validate the query-efficiency claim.
- A comparison where the baseline methods are also extended to handle nonsmooth \(h(\mathbf{x})\) (e.g., via a proximal variant) would isolate the contribution of the fully single-loop design from the ability to handle nonsmoothness.
- An explicit bridging lemma relating \(\frac1T\sum\mathbb{E}\|\mathcal{G}^t\|^2\) to \(\|\nabla\Phi(\mathbf{x})\|^2\) (the original problem's stationarity) would make the complexity comparison with prior work fully self-contained.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- "HOZOG is from 2021; check for newer black-box bilevel methods" — REMOVED: Speculative; the critic does not name any specific newer method that the authors failed to cite. Per Hard Rules, criticisms that question the existence of references are removed.
- "The main text alone does not allow independent verification" — REMOVED: Per Hard Rules, criticisms about missing appendix content are removed (appendix is stripped by the PDF parser).
- "Computational cost beyond queries (memory/per-iteration cost) not analyzed" — REMOVED: The paper's stated scope is query efficiency for black-box problems, not computational analysis of the zeroth-order estimators.
- "Theoretical presentation too terse" — REMOVED: This conflates a presentation style preference with a substantive weakness and overlaps with the removed appendix concern.

## Novel Insights

The most interesting observation from synthesizing the reviews is a tension in the paper's contribution structure: the theoretical advance (first nonsmooth black-box bilevel bound, improved complexity, fully single-loop design) is strong and could stand on its own, but the experimental evaluation tries to carry the weight of three distinct claims simultaneously — (i) query efficiency, (ii) Bregman-distance-specific benefit, and (iii) practical accuracy improvement — without the controls needed to disentangle them. The experiments succeed in showing the method works better overall but fail to attribute the improvement to the specific methodological innovation (Bregman distance) that the paper foregrounds. This is a typical gap between a "new method" paper and a "new architecture/component" paper: the paper positions itself as the former but the critic evaluates it as the latter.

## Suggestions
1. **For the experiments**: Add a fixed-query-budget comparison (run all methods to the same number of queries, no time limit). This directly tests the query-efficiency claim. The current results can be retained as a secondary "practical speed" comparison.
2. **For the Bregman claim**: Add an ablation that replaces the mirror descent step with Euclidean proximal gradient (\(\psi(\mathbf{x}) = \frac12\|\mathbf{x}\|^2\)) while keeping everything else identical. Show that the general Bregman version outperforms this special case on problems with nonsmooth \(h\) (e.g., \(\ell_1\) regularization).
3. **For the theory**: Add a brief remark or lemma bounding \(\|\nabla\Phi(\mathbf{x})\|^2\) (the original problem's stationarity) in terms of \(\|\mathcal{G}^t\|^2\) and the smoothing parameters. This makes the complexity comparison with prior work self-contained.
4. **Clarify in the experiments**: State explicitly which Bregman function \(\psi_t\) was used in the experiments.
5. **Acknowledge limitations**: Discuss the low accuracy on CIFAR-10/SVHN and whether this reflects task difficulty or method limitations.
