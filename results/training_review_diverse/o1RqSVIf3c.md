Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper proposes a framework (Bayesian PR) for personalizing algorithmic recourse via preference elicitation. It uses pairwise comparison queries to learn an individual's Mahalanobis cost weighting matrix $\tilde{A}$, modeled with a Wishart prior. The framework has three components: (1) analytical mutual information maximization for question selection (Theorem 3.2 provides a closed-form expression using hypergeometric functions), (2) a projected gradient descent posterior update after each response, and (3) a graph-based recourse recommendation minimizing expected cost under the posterior, formulated as a binary linear program. Experiments on synthetic and three real-world datasets compare against FACE, Wachter, and DiCE.

## Strengths

- **Analytical mutual information for efficient question selection**: Proposition 3.1 derives the asymptotic ($\kappa \to \infty$) mutual information as a binary entropy, and Theorem 3.2 provides a closed-form expression for $\mathbb{P}(\Delta_{ij}(\tilde{A}) \leq 0)$ using hypergeometric functions. The paper shows this reduces complexity from $O(L d^2)$ (sampling-based) to $O(d^2)$ (analytical), which is a genuine computational contribution.

- **Projected gradient descent posterior update with convergence guarantees**: The posterior update problem (3) is reduced to optimizing over $\Sigma$ for fixed integer $m$, compactified (Proposition 4.3), and shown to be strongly convex with Lipschitz gradient (Lemma 4.5), yielding linear convergence of Algorithm 1. This provides a principled, tractable method for refining the posterior after each response.

- **Graph-based recourse as a binary linear program**: The recourse problem (7a) minimizes expected cost under the Wishart posterior. Using $\mathbb{E}[A] = m_T \Sigma_T$, the problem simplifies to a deterministic binary linear program (7b) solvable with off-the-shelf solvers — a clean and practical formulation.

- **Empirical results across multiple datasets show the pipeline works as a whole**: Tables 1–2 and Figure 2 demonstrate that Bayesian PR achieves lower or competitive path costs across synthetic, German, Bank, and Student datasets under both correct (Mahalanobis) and misspecified ($\ell_1$) cost structures. The mean rank trend in Figure 2 shows the posterior mean approaching the ground truth as $T$ increases.

## Weaknesses

### Fatal

None.

### Major

- **The linear approximation $\Phi(v) \approx v$ in the posterior update is crude and poorly justified.** In Section 4.1, the response likelihood $\int \Phi(\kappa R \Delta(S)) f_P(S)\,dS$ is approximated by $\kappa \mathbb{E}_P[R \langle M, \tilde{A} \rangle]$ via $\Phi(v) \approx v$. The logistic function $\Phi(v) = 1/(1+e^{-v})$ is bounded in $[0,1]$ and equals 0.5 at $v=0$, while the linear approximation is unbounded and maps $0 \to 0$. For large $|\kappa \Delta|$ — which can occur when $\kappa$ is moderately large or cost differences are substantial — the approximation is quantitatively and even qualitatively wrong (sign and scale both off). No error bound, variational justification, or empirical validation of this approximation is provided. Because this step is the basis for the entire posterior update, the resulting procedure is not a proper Bayesian update of the BTL model. **This does not make the resulting optimization meaningless** — the objective $\min \mathrm{KL}(\mathbb{P}\|\mathbb{P}_{t-1}) + \tau\kappa \mathbb{E}_P[R\langle M,\tilde{A}\rangle]$ can be viewed as a regularized learning objective — but the paper's framing as a Bayesian posterior derived from the BTL likelihood is misleading, and the gap between the approximation and the true likelihood is unexamined.

- **The experiments lack key statistical and methodological details, making the empirical claims difficult to verify.** Tables 1 and 2 report cost and validity without any measure of variability (no standard deviations, confidence intervals, or number of independent runs). Figure 2 shows mean rank trends over $T$ without error bars. The paper does not specify: (a) how many subjects/users $x_0$ were evaluated per dataset, (b) what value of $\kappa$ was used to simulate user responses under the BTL model (only the product $\tau\kappa = 1$ is reported, leaving both $\tau$ and $\kappa$ individually unspecified), and (c) whether results are averaged over multiple random seeds for ground truth $A_0$ generation. Without these details, it is impossible to determine whether the reported differences between methods are systematic or within noise.

- **The question selection strategy is not ablated.** The paper selects questions by maximizing asymptotic ($\kappa \to \infty$) mutual information but never compares against baselines such as random pair selection or exact MI via sampling. Since this is presented as a core contribution, the lack of an ablation makes it impossible to attribute any observed improvement to the query selection mechanism specifically — the posterior update and recourse formulation alone may be responsible.

### Minor

- **Graph construction is underspecified.** Section 5 describes the graph only as "inspired by FACE" and states that edges represent "feasible transitions." The edge connectivity criterion (e.g., $k$-NN with what $k$? distance threshold? density-based?), handling of low-density regions, and any graph regularization are not specified. This is a reproducibility concern for a paper whose recourse recommendation is graph-based.

- **The comparison to non-graph-based methods (Wachter, DiCE) is mentioned but not contextualized.** Line 266 states these methods are compared, but Tables 1–2 only show Bayesian PR vs. FACE (the tables are embedded as images, but the captions name only FACE and Bayesian PR). If Wachter/DiCE results are reported, their single-step counterfactual nature vs. the paper's sequential graph-based recourse makes the comparison apples-to-oranges; if they are not actually in the tables, the paper overstates its evaluation.

- **The strong parametric assumption (Mahalanobis cost + Wishart prior) is acknowledged but not studied.** The conclusion mentions this limitation, but the paper does not analyze how misspecification of the cost function form affects the elicitation (beyond the $\ell_1$ experiment in Table 2, which tests only the recourse outcome, not the elicitation quality).

### Trivial

None worth enumerating.

## Nice-to-Haves

- A comparison between the linearized posterior update and a sampling-based approach (e.g., importance sampling with the exact BTL likelihood) would address concerns about the approximation's validity.
- Reporting results over multiple random seeds (≥10) with standard deviations would substantially strengthen the empirical claims.
- An ablation comparing MI-based question selection to random selection would directly validate the contribution of Section 3.
- Specifying the graph construction parameters (edge criterion, $k$, thresholds) would improve reproducibility.
- Reporting the individual values of $\kappa$ and $\tau$ (not just their product) used in experiments.

## Removed Points

These points from the reviews were removed or downgraded:

1. **"The paper cannot be reproduced because models/data are unreleased"** — Removed. All cited models, datasets, and baselines (FACE, Wachter, DiCE) are published works; the paper uses standard benchmark datasets. This is a reviewer knowledge gap.

2. **"Missing related work on X"** — Removed per instructions: I cannot independently verify the existence of missing references.

3. **"Formatting/style nitpicks"** — Removed per instructions.

4. **"Reproducibility concerns about undisclosed hyperparameters beyond reasonable expectations"** — Some of the critic's reproducibility concerns about graph construction details are legitimate and kept; demands for complete training logs or exhaustive parameter sweeps are removed.

5. **"The posterior update searches over integer $m$ values, which is computationally expensive"** — This is noted in minor as a fair observation but not a significant weakness; the number of $m$ values is bounded by $d \leq m \leq m_{t-1}$ and $m_{t-1}$ decreases over rounds.

## Novel Insights

None beyond the paper's own contributions: the analytical MI formula (Theorem 3.2) and the binary LP recourse formulation (7b) are the paper's original technical contributions, and the review surface does not reveal deeper patterns or connections beyond what the authors already articulate.

## Suggestions

1. **Revisit the posterior update derivation.** Either (a) provide an error bound or variational justification for the linear approximation, (b) replace it with a more principled approximation (e.g., Laplace approximation, variational lower bound), or (c) reframe the update as a regularized optimization (KL + expected cost alignment) and drop the pretense of being a proper Bayesian posterior from the BTL model. Option (c) is the most practical.

2. **Add error bars and experimental methodology details.** Report results over at least 10 random seeds with standard deviations. Specify the number of subjects evaluated, the $\kappa$ value used in the BTL response simulation, and how ground truth $A_0$ varies across subjects/seeds.

3. **Ablate the question selection.** Add a random-selection baseline (uniform random pairs from $\mathcal{D}_1$) to demonstrate that MI-based selection provides a measurable benefit.

4. **Specify graph construction parameters** (edge connectivity metric, $k$ for $k$-NN or equivalent, treatment of low-density regions) for reproducibility.

5. **Clarify the role of Wachter/DiCE in the evaluation.** Either include them in the main tables with proper contextualization, or remove the claim of comparison if they are not actually benchmarked.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>