Now I have sufficient information to write the consolidated review. Let me produce the final output.

## Summary

This paper proposes a data-selection algorithm that combines $(k,z)$-clustering (e.g., $k$-means) with sensitivity sampling. Under the assumption that the model loss is $(z,\lambda)$-Hölder continuous with respect to a data embedding, the authors prove (Theorem 5) that selecting $k$ cluster centers, querying their losses, and then sensitivity-sampling $O(1/\varepsilon^2)$ additional points yields a weighted subset whose average loss approximates the total loss up to an additive error that scales with the $k$-means clustering cost $\Phi_{k,z}(\mathcal{D})$ — improving on the $k$-center-based bound of Sener & Savarese (2018) which scales with the dataset diameter and is outlier-sensitive. Experiments on a regression dataset and on neural-network benchmarks (CIFAR-10, among others) compare the method against uniform sampling and the $k$-center coreset baseline.

## Strengths

- **Improved theoretical bound via clustering cost**: Theorem 5 bounds the additive error by $\varepsilon(\sum\ell(e) + 2\lambda\Phi_{k,z}(\mathcal{D}))$, where $\Phi_{k,z}(\mathcal{D})$ is the $(k,z)$-clustering cost. This directly improves on the $k$-center bound of Sener & Savarese (2018) which involves $n\cdot\lambda\cdot\min_{|C|=k}\max_e\min_c\|e-c\|$ — the clustering cost is inherently less outlier-sensitive. (Section 1.1, lines 70–71; Theorem 5, lines 185–191)

- **Sublinear inference complexity**: The 1-round algorithm requires only $k$ queries to the loss function $\ell$ (on the cluster centers) to construct the sample $S$, after which the remaining points are selected via sensitivity sampling without further model inferences. This addresses the practical challenge that model inference is costly for large models. (Section 3.2.1, Theorem 5; Section 1, challenge (2))

- **Generality beyond classification**: The Hölder continuity assumption (Section 2.2) naturally covers both classification and regression losses. The paper provides a dedicated algorithm for linear regression (Section 4, Algorithm 2) and validates on both a regression dataset (gas sensor, Figure 1) and multiple neural-network classification tasks (Figure 2), answering the question of broader applicability raised against prior work. (Section 1, question (4))

- **Empirical improvement over $k$-center coreset**: On CIFAR-10, the proposed loss-based and gradient-based variants consistently outperform the $k$-center coreset method of Sener & Savarese (2018) and uniform sampling across multiple sample sizes, with results averaged over 100 runs and error bars reported. (Figure 2, Section 5.2)

- **Competitive runtime for regression**: On the gas sensor regression dataset, the clustering-based algorithm achieves $1-R^2$ error nearly as low as leverage score sampling while being substantially faster, since $k$-medoids runs in linear time whereas leverage scores require solving a full linear system per data point. (Section 5.1, Figure 1)

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Inconsistency between Theorem 5 and abstract on query count**: Theorem 5 states the algorithm "makes $k$ queries to $\ell$" (lines 185–186), while the abstract says it "only requires very few inferences from the model ($O(k + 1/\varepsilon^2)$)" (line 22). The intended interpretation is that $k$ queries are made to the cluster centers and the $O(1/\varepsilon^2)$ sampled points are outputs that do not require separate queries — but the two phrasings are inconsistent and could confuse readers about what the query budget actually is. This is a presentation flaw, not a structural one, but it should be corrected.

- **Experimental setup for baselines not fully specified**: The neural-network experiments (Section 5.2) describe a warm-start procedure (initial model trained on $k' = 0.2k$ random points) for the proposed method, but do not specify whether the $k$-center baseline of [SS18] receives the same warm-start model and initial random pool. Since the original [SS18] method also uses a warm-start, the omission makes the comparison hard to evaluate. The uniform baseline naturally doesn't require a warm-start (it selects $k$ points at random regardless), so this concern applies specifically to the [SS18] comparison. The paper should clarify this setup.

- **"State-of-the-art" claim overstates baseline coverage**: The abstract claims the method "outperforms state-of-the-art methods" (line 24). The neural-network experiments compare against only two approaches: uniform sampling (a basic baseline) and the $k$-center coreset method of [SS18] (a single SOTA method). While [SS18] is a legitimate SOTA baseline, the plural "methods" and the absence of other active-learning approaches (e.g., margin sampling, BADGE, Monte Carlo dropout) make the claim sound broader than the evidence supports. The claim should be narrowed to the specific methods compared, or additional baselines should be added.

- **Limited description of experimental parameters**: The paper does not state how $\lambda$ (the Hölder constant used in the extrapolation formula $\widetilde{\ell}(e) = \ell(\text{center}) + \lambda\|e-\text{center}\|^2$, line 261) is chosen in practice. Similarly, the description of which datasets appear in Figure 2(b) beyond CIFAR-10 is absent from the text (line 269). These details are needed for reproducibility.

### Trivial

- Figure reference to "Figure 2 and 3" (line 262) mentions "Figure 3" which is not described in the text.
- The notation $\Phi_k(\mathcal{D})$ in Theorem 5 uses $k$ but the $(k,z)$-clustering cost depends on $z$; this is clarified elsewhere but could be made explicit in the theorem statement.

## Nice-to-Haves

- A sensitivity analysis varying $k''$ (number of clusters), $\lambda$, and the $k'/k$ ratio would demonstrate robustness of the method.
- A limitations section discussing when the Hölder assumption might fail or when the clustering cost $\Phi_{k,z}(\mathcal{D})$ is large enough to make the bound vacuous would strengthen the paper.
- Statistical significance tests (e.g., paired $t$-tests or confidence intervals) for the accuracy differences in Figure 2 would clarify whether the improvements are reliable given the overlapping standard deviation bands.

## Removed Points

**Critic point: "Theorem 5's query guarantee is internally inconsistent / structural flaw"** — This is removed because it reflects a misunderstanding. Theorem 5 states the algorithm makes $k$ queries to $\ell$ (to the cluster centers) and *outputs* a sample $S$ of size $O(1/\varepsilon^2)$. The bound $\Delta(S) = |\sum \ell(e) - \sum w(s)\ell(s)|$ is a theoretical guarantee about the quality of $S$ as a coreset — it does not require the algorithm to query $\ell$ on the sampled points. The output $S$ is the set of points to train on; their loss values $\ell(s)$ appear in the bound as a mathematical statement, not an additional computational step. The $k$ queries are sufficient to construct $S$. (The separate issue of the abstract vs. theorem wording on query count is kept as a Minor weakness above.)

**Critic point: "The warm-start issue invalidates the performance claims"** — Downgraded from a decisive flaw to a Minor omission. The uniform baseline does not benefit from a warm-start model (it selects points at random regardless), and the [SS18] baseline was originally designed with a warm-start. The omission of explicit details is a weakness but does not invalidate the results.

**Critic point: "No theoretical guarantee for the regression case"** — The paper explicitly states "We do not achieve such a general statement" (line 221), so there is no claim of a full guarantee for the regression case. The paper is transparent about this limitation.

**Critic point: "Section-by-section notes" about the problem formulation being "arguable"** — The paper provides a clear argument for why its formulation is "more challenging" (lines 111–112: "proving a bound on $\Delta(S)$ implies the result of Sener & Savarese (2018)"). This is a reasonable claim, not a weakness.

**Critic point: "No limitations section"** — Moved to Nice-to-Haves.

**Strength Finder strengths that are generic** (e.g., "This paper addressed an important problem") — Removed; only specific, evidence-grounded strengths retained.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the work that the authors themselves have not already articulated or implicitly addressed.

## Suggestions

1. **Harmonize the query-count language**: In Theorem 5, either state "makes $k$ queries to $\ell$ to construct $S$" or change the abstract to "$O(k)$ inferences" rather than "$O(k + 1/\varepsilon^2)$" — whichever accurately reflects the algorithm.
2. **Specify the [SS18] experimental setup explicitly**: State whether the $k$-center baseline receives the same $k'$ warm-start points and initial model.
3. **Add at least one more active-learning baseline** (e.g., margin sampling or BADGE) or soften the "outperforms state-of-the-art methods" claim to "outperforms prior coreset-based and uniform baselines."
4. **Report how $\lambda$ is set** in the neural-network experiments and name all datasets appearing in Figure 2(b) in the text.

## Score and Decision

The paper presents a genuine theoretical contribution — combining $(k,z)$-clustering with sensitivity sampling for data selection and proving a bound that improves on the prior $k$-center-based guarantee — along with reasonable empirical support. The weaknesses are all at the Minor level (presentation inconsistencies, insufficient experimental detail, limited baseline scope) and are addressable in revision without undermining the core contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>