## Summary

This paper introduces $RW_p$, a family of translation-invariant Wasserstein distances defined on the quotient space $\mathcal{P}_p(\mathbb{R}^n)/\sim$ (modulo translation). For the quadratic case $p=2$, the paper proves a decomposition theorem showing that the ROT optimization decouples into independent sub-problems (the coupling is determined by classical OT, and the optimal translation is simply the difference of means), yielding a Pythagorean relationship $W_2^2 = \|\bar{\mu}-\bar{\nu}\|_2^2 + RW_2^2$. This insight motivates the $RW_2$ Sinkhorn algorithm (center-then-Sinkhorn), which improves numerical stability and computational efficiency when mean shifts are large. Experiments on synthetic data, MNIST, and a large-scale thunderstorm dataset demonstrate the behavior of $RW_2$.

## Strengths

1. **Clean theoretical decomposition (Theorem 3)** — The proof that the quadratic ROT optimization decouples into two independent problems — a standard OT problem determining the coupling $P$ and a simple quadratic minimization for the translation $s$ with closed-form $s = \bar{\nu} - \bar{\mu}$ — is the paper's strongest contribution. This is non-trivial because the squared norm expansion introduces cross-terms that must be shown to decouple.

2. **Pythagorean relationship (Corollary 5)** — The decomposition $W_2^2(\mu,\nu) = \|\bar{\mu}-\bar{\nu}\|_2^2 + RW_2^2(\mu,\nu)$ provides an interpretable factorization of the total squared Wasserstein distance into a mean-difference term and a shape term. This is geometrically elegant and enables the bias-variance analogy.

3. **Principled numerical stability analysis (Section 4.3)** — The paper formalizes stability via $g(K)=\prod_{i,j}K_{ij}$ and proves that choosing $s=\bar{y}-\bar{x}$ maximizes this quantity, pushing $K$ entries away from zero. This is a more principled justification than a heuristic claim about centering.

4. **Large-scale real-world deployment** — The thunderstorm experiment uses 205,848 radar images spanning eight years. The scale and practical motivation (shape-similarity detection regardless of spatial location) are genuinely impressive.

## Weaknesses

### Fatal
None.

### Major
1. **Thunderstorm experiment is purely qualitative.** Despite 205,848 images, the evaluation consists of showing a handful of side-by-side comparisons with the subjective claim that "$RW_2$ focuses more on shape similarity." No quantitative metrics (precision@k, retrieval accuracy, clustering evaluation, temporal proximity correlation) are reported. For a paper whose headline real-world application is thunderstorm pattern detection, the lack of any quantitative evidence is a significant evidential gap. The qualitative results are suggestive but do not constitute validation of the method.

### Minor
2. **Bias-variance framing is stated but not developed.** The paper lists this as a contribution (contribution c) and spends roughly two sentences on the analogy (lines 171-172). The connection to the classical statistical bias-variance decomposition is analogical, not formal — no theoretical link to learning theory, no experiments on regression or prediction tasks, and no discussion of when this decomposition provides actionable insight. The claim is oversold relative to what is actually shown.

3. **Digit recognition experiment tests only the favorable regime.** $RW_2$ outperforms non-invariant distances ($L_1, L_2, W_1, W_2$) under large translations, which is expected by construction since $RW_2$ is explicitly translation-invariant. The experiment would be more informative if it also tested a setting where translation carries signal (e.g., training on centered digits and testing on translated digits), demonstrating when invariance is a limitation. Acknowledging failure modes builds trust.

4. **Numerical validation (Experiment 1) tests only identical distributions.** The Gaussian and uniform experiments use $\mu = \nu$ before translation, so $RW_2 = 0$. This is the most favorable case for demonstrating the numerical benefits of centering. Testing with genuinely different shapes would strengthen the claim that the algorithm is broadly useful for computing $W_2$, not just in the identity-shape limit.

### Trivial
5. **Title and abstract slightly overframe the contribution.** The paper presents itself as introducing a "family of $RW_p$ distances" but all analysis, algorithm, and experiments are confined to $p=2$. The main text is clear about this focus (line 93: "We will then focus on the quadratic $RW_2$ case"), and this is not harmful to the paper's correctness, but a title or abstract emphasizing $RW_2$ would better match the paper's actual content.

## Nice-to-Haves
- A quantitative evaluation protocol for the thunderstorm experiment (even a small human-annotated subset or temporal proximity as a weak signal) would significantly strengthen the real-world validation.
- An experiment showing when translation-invariance is detrimental (where location matters) would provide a more balanced picture.

## Removed Points
These points were flagged by reviewers but are removed per filtering rules:

1. *"Algorithm is just centering + Sinkhorn"* — The paper transparently presents the algorithm as a direct consequence of the decomposition theorem (line 210: "key idea of this algorithm involves precomputing the difference between the means"). The contribution is the theoretical insight plus the resulting analysis, not a claim of fundamentally new computation. Removing as this mischaracterizes what the paper asserts.

2. *"Missing proof of Theorem 2 (general $p$)"* — Falls under the hard rule: the parser strips appendices; proofs exist in the original submission. The paper is also transparent about focusing on $p=2$ after introducing the general definition.

3. *"Distribution shift motivation conflates different things"* — The paper's two examples (weather patterns, sensor calibration/sim2real) are clear and reasonable. Criticizing them requires demanding the paper address shifts outside its stated scope.

4. *"Missing related works comparison"* — Hard rule prohibits raising missing related works without external verification. The paper already cites sliced Wasserstein and Gromov-Wasserstein.

5. *"Center-then-W2 missing baseline"* — The paper's algorithm IS centering + Sinkhorn; comparing against this would be self-comparison. The existing baselines ($L_1, L_2, W_1, W_2$) are appropriate for the robustness experiment.

6. *"Claim about time complexity relies only on $\|C\|_\infty^3$ term"* — The paper uses the Altschuler et al. bound as motivation and validates empirically. This is standard practice; the bound is a sufficient (not necessary) complexity guarantee.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add a quantitative evaluation for the thunderstorm experiment — even correlation with temporal/geographic proximity or a small annotated retrieval set would move this from anecdotal to evidential.
2. Dial back the bias-variance claim to what is actually shown (the geometric Pythagorean decomposition) unless the connection is developed further with formal links or experiments.
3. Add one experiment where translation is informative (e.g., digit classification without random translation on test data) to show when $RW_2$ underperforms, providing a more complete picture.
4. Consider retitling to emphasize $RW_2$ rather than the general $RW_p$ family, to match the paper's actual scope.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>