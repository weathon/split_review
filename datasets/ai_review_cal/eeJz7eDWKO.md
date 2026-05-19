- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a thorough understanding of the paper and both reviews. Let me produce the final consolidated review.

## Summary

This paper proposes the Bayesian Causal Neural Process (BCNP), a meta-learning model that learns to approximate the Bayesian posterior over causal DAGs directly from data. The key architectural innovations are (1) an encoder that enforces permutation invariance w.r.t. samples and permutation equivariance w.r.t. nodes, and (2) a decoder that samples acyclic DAGs by combining a Gumbel-Sinkhorn distribution over topological orderings with a lower-triangular Bernoulli distribution over edges. The model is trained by minimizing KL-divergence to the true posterior via a Monte Carlo objective. Experiments on synthetic and semi-synthetic data show BCNP outperforms or matches existing Bayesian meta-learning methods (AVICI, CSIvA) and explicit Bayesian methods (DiBS, BayesDAG), particularly on dense graphs, while also correctly handling the unidentifiable 2-variable case where prior methods fail.

## Strengths

1. **Decoder that directly samples acyclic DAGs from the learned posterior** (Section 3.2, Figure 2): The combination of Gumbel-Sinkhorn permutations with lower-triangular Bernoulli matrices guarantees that every sampled graph is acyclic by construction. This directly addresses a known failure of prior meta-learning methods — Table 3 shows AVICI produces 19% cyclic samples in the 2-variable case. This architectural contribution is concrete, well-explained, and correctly motivated.

2. **Empirical verification of correct posterior sampling in a controlled setting** (Table 3, Section 4.1): In the unidentifiable 2-variable case where the true posterior is known to be a 50/50 split between \(X\rightarrow Y\) and \(Y\rightarrow X\), BCNP outputs exactly this distribution. AVICI fails (32% no-edge, 19% cyclic). This directly validates BCNP's ability to capture edge dependencies and sample from the correct posterior, at least in this minimal setting.

3. **Competitive or superior performance on 20-variable dense graphs** (Table 4, Section 4.2): On ER60 graphs (the densest setting) across three functional families (Linear, NeuralNet, GPCDE), BCNP (especially ER20-60) achieves higher AUC and expected edge F1 than explicit Bayesian methods (DiBS, BayesDAG) and other meta-learning models (AVICI, CSIvA). The single model trained on a mixture of densities (BCNP ER20-60) maintains performance across all densities, demonstrating practical utility.

4. **Principled encoder design** (Section 3.1): Alternating attention over samples and nodes, followed by cross-attention for the summary representation, correctly enforces permutation invariance w.r.t. samples and permutation equivariance w.r.t. nodes. This is a well-motivated design that encodes known symmetries of the posterior.

5. **Generalization to semi-synthetic data** (Table 2, Section 4.3): On Syntren data (realistic gene expression), BCNP is competitive despite not being trained on the exact generating distribution. The use of a wide mixture of training distributions proves effective.

6. **Theoretical insight into distribution mismatch** (Section 5, Equation 14): The paper provides a clear equation showing that if the KL from the training distribution to the model is zero, performance on a target distribution depends on the KL between the training and target distributions. This is explicitly supported by the "ER20-60" mixture-training results.

## Weaknesses

### Fatal
None.

### Major

1. **The key claimed advantage — capturing edge dependencies for >2 variables — is not directly evaluated.** The paper prominently claims that BCNP "encodes dependencies between edges" (abstract, introduction, Table 1) as a central advantage over AVICI. However, the main 20-variable experiments (Section 4.2) report only marginal/aggregate metrics (AUC, log Bernoulli probability, expected SHD, expected edge F1). The paper itself acknowledges (line 178) that AUC and log probability "only consider marginal edge probabilities" and that AVICI and BCNP show "comparable performance in these metrics." The 2-variable experiment (Section 4.1) directly validates edge-dependency capture but only for a single binary pair. For the regime where the paper's claims matter most (graphs with many variables where complex posterior dependencies arise), there is no evaluation that actually measures whether the joint distribution over DAGs is correct — no calibration of credible sets, no comparison of predicted vs. true joint edge probabilities, no measurement of edge-correlation recovery. Without such evidence, the claimed improvement over AVICI on this specific dimension remains architecturally plausible but empirically unsubstantiated for larger graphs.

2. **The factorization assumption within each permutation ordering is not discussed or justified.** Conditioned on a permutation (topological ordering), the decoder treats edges in the lower-triangular matrix as independent Bernoulli variables. This means any posterior dependencies that persist *within* a fixed ordering (e.g., two edges that tend to co-occur or mutually exclude each other under the same topological order) cannot be captured. While the mixture over orderings captures dependencies *across* orderings, the paper does not acknowledge this limitation or provide theoretical/empirical grounds for why it is acceptable. Given that the paper emphasizes "encoding dependencies between edges" as a key contribution, this unexamined structural assumption deserves explicit discussion.

### Minor

1. **The coupling mechanism between permutation and edge distributions is relatively weak.** The paper states that the permutation and edge distributions "share parameters" to "ensure dependence" (Section 3.2). However, the actual mechanism is that \(\mathbf{R}^{L_2}\) (used for the edge distribution) is computed from \(\mathbf{R}^{L_1}\) (used for the permutation distribution) by further transformer layers — there is no joint sampling procedure. The dependence is only through shared encoder representations, not through explicit coupling during sampling. The paper does not clarify or analyze whether this degree of coupling is sufficient for complex posteriors.

2. **Only the densest graph results (ER60) appear in the main paper.** Table 4 presents only ER60 results; results for ER20 and ER40 are deferred to supplementary tables (Tables 7–12). A compact summary (e.g., aggregated across densities) in the main paper would help readers gauge the general trend.

3. **The Syntren experiment is small-scale.** Only 10 datasets are used (Section 4.3), and the reported standard deviations are relatively high. The paper acknowledges this implicitly but could be more explicit about the resulting limitations on statistical significance.

4. **Theoretical analysis of distribution shift is insightful but brief.** Section 5 provides Equation (14) and some discussion, but the paper notes that "a more rigorous treatment of this question would be necessary to make stronger claims." The current analysis largely restates a well-known property of KL-divergence; concrete strategies (e.g., wider training distributions, domain adaptation) are not discussed.

### Trivial
None.

## Nice-to-Haves

- Direct evaluation of posterior joint distribution quality for >2 variables: calibration plots of marginal edge probabilities against ground-truth posterior, log-probability of the true graph, or edge-correlation recovery metrics. This would directly validate the paper's central claim.
- A simple baseline (e.g., uniform distribution over DAGs, or random edge probabilities) to contextualize absolute performance.
- Reporting the number of Monte Carlo samples \(S\) used in the loss (Equation 13), as this affects gradient variance.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism about missing hyperparameters (number of training datasets, batch size, learning rate, transformer dimensions, Sinkhorn iterations, temperature)** — The parser strips the appendix where these details reside. This is a parser artifact, not an author error.
- **Criticism about Table 1's row for "Sampling acyclic graphs" not being checked for CSIvA** — The paper explicitly states "CSIvA... does not guarantee acyclic samples" (Section 2.2). The table is accurate as presented.
- **Criticism about "no comparison to random baseline"** — This is a nice-to-have, not a weakness. The comparisons against existing methods (DiBS, BayesDAG, AVICI, CSIvA) are the appropriate baselines.
- **Criticism about AVICI "No relation" 32% output being an edge-dependency failure** — The paper already makes this point explicitly (Section 4.1, line 167).
- **Criticism about training-on-the-true-distribution setup being problematic** — The paper is transparent about this, and also evaluates on distribution-shifted Syntren data. The setup is standard for meta-learning evaluation.

## Novel Insights

None beyond the paper's own contributions. The reviews do not identify a perspective on the paper's approach or results that the authors themselves did not express.

## Suggestions

1. **Add a direct joint-distribution evaluation for 20-variable graphs.** The most impactful addition would be: (a) report the log-probability of the true graph under BCNP vs. AVICI (this is the loss being optimized, and directly measures how well the model scores the ground truth); (b) for smaller graphs (e.g., 5 nodes, where the true posterior can be enumerated), compare BCNP's predicted edge correlations against the ground-truth posterior. This would definitively validate or challenge the edge-dependency claim.

2. **Acknowledge and discuss the within-ordering independence assumption.** Add a paragraph in Section 3.2 or Section 5 noting that conditioned on a topological ordering, edges are modeled as independent, and discuss the types of posterior dependencies this can/cannot capture. This would strengthen the paper's intellectual honesty and guide future work.

3. **Include a compact summary of results across all graph densities** (ER20, ER40, ER60) in the main paper, even if just as a small table or aggregated metric, to let readers see the trend without consulting supplementary material.

4. **Clarify the coupling mechanism more precisely.** The paper claims the permutation and edge distributions are dependent through shared parameters — a schematic or brief analysis showing how changes in the encoder representation jointly affect both distributions would clarify the intended design.
