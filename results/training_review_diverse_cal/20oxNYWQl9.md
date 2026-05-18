Now I have a thorough understanding of the paper and can verify each reviewer claim. Let me write my consolidated review.

## Summary

This paper proposes a data selection algorithm that combines $(k,z)$-clustering (e.g., $k$-means) with sensitivity sampling to select a representative subset of training data. Under only Hölder continuity of the loss with respect to data embeddings — a weaker assumption than prior work — Theorem 5 guarantees that with $k$ queries to the loss function (at cluster centers) and $O(\varepsilon^{-2})$ additional samples, the weighted loss on the selected subset approximates the full dataset loss up to an additive-multiplicative error involving the clustering cost $\Phi_k$. The method is evaluated on linear regression (gas sensor data) and neural network benchmarks (CIFAR10, etc.) against uniform sampling and the $k$-center coreset method of Sener & Savarese (2018).

## Strengths

- **Weaker theoretical assumptions than prior work**: The analysis requires only Hölder continuity of the loss with respect to embeddings, which is more general than the Lipschitz assumption used in Sener & Savarese (2018) and avoids their strong assumptions on label distributions and training loss (Section 2.1, Theorem 5). This is a genuine theoretical advance for the data selection problem.

- **Robustness to outliers via $(k,z)$-clustering**: Replacing the $k$-center objective (which greedily picks farthest points) with $(k,z)$-clustering (e.g., $k$-means, $k$-median) yields a selection criterion that is provably less sensitive to outliers (Section 1.1). The paper correctly notes that smaller $z$ gives more outlier-robustness while large $z$ recovers the $k$-center objective.

- **Generality beyond classification**: The method and its theory apply to general Hölder-continuous loss functions, not just classification tasks. Section 4 further develops a dedicated analysis for linear regression (Assumption 8), broadening applicability relative to prior coreset-based active learning which was limited to classification.

- **Empirical performance and efficiency**: On neural network benchmarks, the loss-based and gradient-based variants consistently outperform both uniform sampling and the $k$-center coreset baseline (Figure 2), especially at small sample sizes. The loss-based algorithm is also fastest among the non-trivial methods. On linear regression, the clustering-based approach performs nearly on par with leverage score sampling while being "drastically faster" (Section 5.1), as $k$-medoids runs in linear time.

- **Adaptive multi-round extension**: Theorem 6 provides an $r$-round variant that trades off round complexity for tighter bounds, with error depending on $\Phi_{k\cdot i}(\mathcal{D})$ and reaching exactness when $r\cdot k = |\mathcal{D}|$.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between theory and experimental evaluation.** The theoretical framework (Definition 2, Theorem 5) addresses the problem of approximating the *current model's* loss sum $\sum_{e\in\mathcal{D}}\ell(e)$ using a small number of inferences. The experiments (Section 5.2), however, use the selected subset to *train a new model from scratch* (or fine-tune an initial checkpoint) and evaluate validation accuracy — not how well the sample approximates the initial model's loss. The paper acknowledges this gap (Section 2.1: "Our underlying assumption is that, if $S$ approximates the loss well, then it contains typical elements... and therefore updating the model based on $S$ should be similar") but provides no formal argument connecting the bound on $\Delta(S)$ to the performance of a retrained model. The claim that "proving a bound on $\Delta(S)$ implies the result of Sener & Savarese (2018)" is stated without proof. This disconnect means the theory speaks to a different quantity than what is experimentally measured.

2. **Narrow experimental comparison relative to the claims.** The paper claims in the abstract and introduction to "outperform state-of-the-art methods," yet the neural network experiments compare against only two baselines: uniform sampling (a very weak baseline) and the $k$-center coreset of Sener & Savarese (2018). Many well-established data selection / active learning strategies exist — margin sampling, entropy sampling, BALD, BADGE, and others — and are not included. On linear regression, only uniform and leverage-score sampling are compared, on a single dataset (gas sensor). Without a broader set of baselines, the claim of outperforming "state-of-the-art" is unsubstantiated. The experiments provide promising初步 evidence but are not comprehensive enough to support the strongest advertised claims.

### Minor

1. **Hyperparameters $\lambda$ and $z$ are not ablated.** The theory depends on the Hölder parameters $\lambda$ and $z$, and the practical algorithm uses $\lambda$ in the approximation $\tilde{\ell}(e) = \ell(A(e)) + \lambda\|e-A(e)\|_2^2$ (Section 5.2). No ablation study examines sensitivity to these choices, and the paper does not state how $\lambda$ is set in practice (it appears to default to 1). An ablation would be important for practitioners seeking to apply the method.

2. **Sample size accounting in the theorem vs. experiments.** Theorem 5 states the algorithm makes $k$ queries to $\ell$ (the cluster centers) and outputs a separate sample $S$ of size $O(\varepsilon^{-2})$. In the experiments (Section 5.2), the $k''$ cluster centers are part of the final training set and also count toward the total budget $k$, making the total sample size $k$ rather than $O(\varepsilon^{-2})$. The paper never clarifies whether the theorem's sample size bound includes or excludes the $k$ queried centers, creating ambiguity about what the theoretical guarantee actually promises in the experimental setting.

3. **Regression experiments deviate from the theory.** For the linear regression experiments (Section 5.1), the paper sets $\zeta \to \infty$, "which has the effect that we only look at distances and not losses." This means the regression experiments ignore the loss component at cluster centers entirely — a significant departure from Algorithm 2 and the theory in Section 4, which relies on computing the optimal regression at centers. The paper does not discuss why this simplification is justified or how it affects the theoretical guarantees.

### Trivial

- The algorithm (Algorithm 1) is described only in prose (Sections 3.2.1 and 5.2). A pseudocode box would resolve ambiguity about clustering computation, query strategy, and weight assignment, especially given the gap between the theoretical description and the experimental instantiation.

## Nice-to-Haves

- An ablation study on $\lambda$ and $z$, and on the number of clusters $k''$ relative to total budget $k$, would strengthen the practical guidance.
- A simple argument (or reference) linking the bound on $\Delta(S)$ for the current model to generalization guarantees for a model retrained on $S$ would bridge the theory-experiment gap.
- Additional regression datasets beyond gas sensor would increase confidence in the regression results.
- Inclusion of error bars (beyond standard deviation bands) and confidence intervals for the benchmark comparisons would improve statistical rigor.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Theorem 5 sample size is incorrect without sensitivity dependence" (Harsh Critic #1):** The critic argues the sample size $O(\varepsilon^{-2})$ must depend on the total sensitivity ratio $T/\mu$, which could be arbitrarily large. This overlooks the additive term $2\lambda\Phi_k$ in the error bound. By Hölder continuity, $\ell(c(e)) \leq \ell(e) + \lambda\|e-c(e)\|^z$, so $\sum(\ell(c(e)) + \lambda\|e-c(e)\|^z) \leq \sum\ell(e) + 2\lambda\Phi_k = \mu'$, giving $T/\mu' \leq 1$. The bound's structure accounts for the sensitivity ratio. **Removed** — factually incorrect, misunderstands the paper.

2. **"Theorem 4's role is unclear" (Harsh Critic #5):** The paper explicitly states in Section 3.2: "The lower bound on $\Delta(S)$ in theorem 4 shows is that one must sample more carefully if good guarantees are desired." The role — motivating adaptive sampling — is clear. **Removed** — misunderstands the paper.

3. **"Gradient-based variant lacks theoretical support" (Harsh Critic #7):** The paper presents the gradient-based variant as a heuristic instantiation of Algorithm 1 (Section 5.2) and never claims theoretical backing for it. The absence of theory for a heuristic is not a weakness. **Removed** — not a weakness the paper claims to address.

4. **"Missing proof sketch / appendix" (Harsh Critic, Missing Parts):** The appendix containing proofs was stripped by the PDF parser. Per policy, missing appendix content is a parser artifact, not an author error. **Removed**.

5. **"Missing related works"** — Not included as I cannot verify existence of unmentioned works.

6. **"Pure formatting/style nitpicks"** — None applicable from the harsh critic.

7. **"Strawman weaknesses" and "typos/grammar"** — None identified beyond those already removed above.

## Novel Insights

The most interesting tension exposed by the reviews is between the paper's two contributions: the theoretical analysis (bounding $\Delta(S)$ for a fixed model) and the experimental protocol (evaluating a retrained model's accuracy). This gap is not unique to this paper — it is endemic in coreset-based active learning. What makes this paper's situation distinctive is that the authors explicitly acknowledge the gap and claim their objective "implies" the stronger result of Sener & Savarese, but provide no formal bridge. A rigorous reader is left wondering whether the theory is a genuine contribution to data selection or merely a self-contained result about estimating weighted sums under Hölder continuity — the latter being a purely statistical estimation problem whose connection to learning is asserted but not proven. The paper would be stronger if it leaned into this distinction rather than claiming the implication without proof.

## Suggestions

1. **Bridge the theory-experiment gap formally or empirically.** Either provide a generalization argument showing that bounding $\Delta(S)$ for the current model implies the retrained model has low risk (perhaps via algorithmic stability or uniform convergence), or restructure the experiments to directly measure $\Delta(S)$ (e.g., compare the estimated weighted loss against the true total loss) and treat the retraining accuracy as a separate, heuristic sanity check.

2. **Expand the baseline comparison.** At minimum, add margin sampling, entropy sampling, and BADGE to the neural network benchmarks. This would not require new infrastructure — these methods are standard and easy to implement. Without them, claims of outperforming "state-of-the-art" are not credible.

3. **Add hyperparameter ablations.** Report how varying $\lambda$ (the coefficient on the distance penalty in $\tilde{\ell}$) and the number of clusters $k''$ affects both the selection quality and the runtime. This is essential for practical adoption.

4. **Add a pseudocode box for Algorithm 1** with explicit notation for which points are queried, which are sampled, and how weights are assigned. Clarify whether the $k$ cluster centers count toward the sample size in Theorem 5.

5. **For the regression experiments, either follow Algorithm 2 faithfully or explain why the simplification ($\zeta \to \infty$, ignoring losses) is justified.** The current description sounds like a different method from the one analyzed.

**Originality:** Good — novel combination of $(k,z)$-clustering + sensitivity sampling for data selection.
**Importance of question:** High — data selection is critical for large-scale training.
**Claims well-supported:** Partially — the core theoretical claim is plausible but unverifiable without the appendix; the experimental claims outstrip the evidence.
**Soundness of experiments:** Adequate but limited by narrow baseline scope and single regression dataset.
**Clarity:** Reasonable, but the theory-experiment disconnect and ambiguous algorithm description hurt coherence.
**Value to community:** Moderate — the approach has clear practical potential and the theoretical framing is clean, but the empirical validation needs strengthening.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>