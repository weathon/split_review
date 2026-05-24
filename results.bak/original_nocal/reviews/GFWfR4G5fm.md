Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper identifies three fundamental out-of-distribution generalization failures of static supervised causal learning (SCL) — fragility under distribution shifts, failure in compositional generalization, and a gap between synthetic and real-world performance. To address these, it proposes TTT-SCL, a framework that dynamically generates a training set aligned with each test instance. The first instantiation, TACTIC, uses a likelihood-based Alignment of Distribution (AD) score with an L₀ sparsity penalty to search for candidate graphs via stochastic refinement, then trains an SCL model on synthetic data generated from those graphs. TACTIC (seeded with NOTEARS) achieves state-of-the-art AUROC on Sachs (78.9), Syntren (80.1), and several synthetic benchmarks, substantially outperforming both traditional causal discovery methods and the static SCL baseline AVICI.

## Strengths

1. **Systematic diagnosis of static SCL limitations.** Section 3.2 (Figure 2, Table 1) provides clear controlled experiments demonstrating that SCL models (AVICI, SiCL) are fragile under distribution shifts across graph structure, mechanism, and noise; fail on novel combinations of seen components (compositional failure); and show a dramatic synthetic-to-real-world gap (AVICI drops from 97.8 AUROC on RFF_G to 62.3 on Sachs). This diagnosis is concrete and well-motivated.

2. **TACTIC (Notears) achieves state-of-the-art on real-world and pseudo-real data.** Table 2 shows TACTIC (Notears) outperforming all baselines on Sachs (78.9 AUROC vs. 67.1 PC, 62.3 AVICI) and Syntren (80.1 vs. 65.4 AVICI), directly addressing the key failure of static pre-training to transfer to realistic domains. On Linear_U and Chebyshev_G it also achieves best performance, demonstrating robustness under distribution shifts where static SCL degrades.

3. **Stage-wise analysis validates the two-stage framework.** Table 4 provides a clear decomposition: seed graph → highest-scoring graph from search → final SCL output. The final SCL output consistently outperforms the highest-scoring graph (e.g., Sachs: 66.6→78.9; Chebyshev_G: 75.8→83.0), demonstrating that training on TACTIC-generated data adds value beyond the score-based search. The sparsity ablation (Table 3) confirms the L₀ penalty is essential.

4. **Conceptually clean TTT-SCL framework.** The high-level idea of dynamically generating test-aligned training data is a principled response to the static pre-training bottleneck. The framework is agnostic to the choice of identifiability assumption (LiNGAM, nonlinear ANM, Post-NonLinear), broadening its potential applicability.

## Weaknesses

### Fatal
None.

### Major

1. **The paper's claim about "search improvement" is contradicted by its own data on Linear_U.** Line 249 states: *"The higher AUROC of the highest-score graph compared to the seed graph shows that TACTIC's stochastic refinement effectively improves graph quality through distributional alignment."* However, Table 4 shows that on Linear_U, the highest-scoring graph (80.1 AUROC) is **worse** than the seed graph (82.0) — a clear decrease, not an improvement. While the search improves on 3 of 4 settings, the unconditional claim in the text is factually incorrect for Linear_U. This anomaly is never explained, raising questions about the reliability of the AD+sparsity score as a proxy for graph quality. Since the paper's entire framework hinges on this score to guide the search, understanding when and why it misleads is critical.

2. **TACTIC (random) is often uncompetitive, undermining claims of general applicability.** From Table 2: TACTIC (random) achieves 58.6 on Sachs (vs. 67.1 for PC), 88.4 on RFF_G (vs. 97.8 for AVICI), and 79.6 on Chebyshev_G (vs. 81.7 for AVICI). On 3 of 5 test settings, the random-seed variant is beaten by strong baselines. The method only becomes consistently state-of-the-art when seeded with NOTEARS. While good initialization is helpful for any method, this dependence constrains the generality of the TTT-SCL framework — the paper should characterize when TACTIC (random) works and when it does not, rather than presenting it as a robust alternative.

### Minor

1. **The AD metric is a standard penalized likelihood score, not a novel "alignment" measure.** The paper frames AD (Eq. 3) as a "proposed" metric, but it is explicitly based on log-likelihood — a standard model fit criterion. The real contribution is the TTT-SCL framework itself (using the score to generate training data for an SCL model), not the metric. The presentation should be clearer about this. The claim that AD captures "similarity via distributional alignment" is largely a restatement of how well the graph explains the data under the assumed noise model.

2. **Missing hyperparameter sensitivity analysis.** The paper does not report how λ (sparsity penalty strength) is chosen or how sensitive results are to its value. λ directly controls the trade-off between fit and sparsity and is central to avoiding degenerate dense graphs. Similarly, K=200 training graphs is presented without any analysis of how performance varies with K (e.g., whether K=20 or K=50 would suffice). The practical cost of TACTIC depends on these choices.

3. **Gaussian noise assumption for AD and forward sampling.** The paper states that noise is set to a standard Gaussian "by default" (line 178) for forward-sampling training data. Meanwhile, the Linear_U test data uses Uniform noise for identifiability. The AD likelihood computation (Eq. 3) implicitly assumes a Gaussian noise distribution for the conditional densities. When the true noise is non-Gaussian, this misspecification could bias the score. No sensitivity analysis is provided (e.g., using non-parametric density estimation for AD).

4. **Evaluation scope is narrow.** Synthetic experiments use d=10, Sachs has d=11, Syntren has d=20 — all small-scale graphs. Real-world causal discovery often involves 50-100+ variables. The paper claims broad applicability but provides no evidence on larger graphs. Scalability of the AD computation (which requires per-variable regression for each candidate graph) is not demonstrated. (The paper references Appendix F for complexity analysis, but the appendix is not available in this extract.)

5. **"Compositional generalization" framing is imprecise.** The Component-mixed condition tests whether models fail on novel *combinations* of seen components. This is a valid and interesting experiment, but the paper does not explain *why* an SCL model trained on dataset-to-graph mappings should be expected to generalize compositionally in the first place. The failure is better understood as another form of distribution shift (categorical shift in the joint distribution of (graph type, mechanism, noise)) rather than requiring a separate cognitive-type label like "compositional generalization." The claimed contrast with Montagna et al. (2024) is overstated — their work also examines generalization to unseen configurations.

### Trivial
None.

## Nice-to-Haves

- **Replace the SCL model with simpler aggregation.** A natural control is to replace the SCL training step with a simple ensemble (e.g., average adjacency predictions across the K candidate graphs, or logistic regression on edge features). If this yields similar gains, the SCL model is not essential. If it does not, the SCL model's role is better isolated. This would strengthen the paper's claims about the necessity of the full framework.
- **Compare against TACTIC with NOTEARS given additional computational budget.** To address whether the improvement over NOTEARS is simply due to more computation, run NOTEARS with additional refinement time (more iterations, restarts) and compare.
- **Sweep over λ and report K-sensitivity.** A simple plot showing AUROC as a function of λ and K would substantially strengthen the paper.
- **Visualize search trajectory.** Plot AD score, sparsity, and AUROC (where ground truth is known) over refinement iterations for a representative test case. This would reveal whether the score correlates with true graph quality.

## Removed Points

These points from the inputs were assessed and removed; treat them with caution:

- **"AD metric is a rebranding, the paper should just use the highest-scoring graph"** — The paper's contribution is the TTT-SCL *framework*, not the AD metric itself. Table 4 shows the SCL step consistently improves over the highest-scoring graph, demonstrating the value of the full pipeline. The harsh critic's claim that the score-based approach "is the natural approach" ignores this two-stage design.
- **"Closed loop prone to overfitting"** (SCL trained on data from D_test) — Speculative. The method performs well on real-world data (Sachs, Syntren), contradicting the concern that overfitting dominates.
- **"Unfair comparison with NOTEARS"** — TACTIC using NOTEARS as a seed and outperforming it is the intended behavior. The comparison demonstrates that the TTT refinement adds value. The paper does not disguise this dependency.
- **"Transition probability ratio is unclear"** — The acceptance probability α = min[1, score(G_k+1)/score(G_k)] is a standard Metropolis-style update. The score need not be a normalized probability for the ratio to be a valid acceptance criterion.
- **"Figure 2 bar chart is hard to read"** — Formatting nitpick from parser artifacts. The table below the chart provides the same data.
- **"Component-mixed experiment poorly described"** — The paper clearly defines it (line 98): training contains all individual components seen in isolation but excludes their test-set combinations. The criticism that SCL models shouldn't be expected to generalize compositionally is a matter of framing, not a factual error.
- **"Test-time adaptation from other domains should be discussed"** — Beyond the stated scope. The paper already notes TTA/ TTT literature (Liang et al., Sun et al., Wang et al., Liu et al., Sinha et al.) in Related Work.

## Novel Insights

The most interesting observation from the review process is the **Linear_U anomaly**: the AD+sparsity score selects a graph that is causally worse than the seed, yet the SCL model trained on data from that (worse) graph still recovers and produces the best overall result. This suggests that the training data generation step does not require perfectly accurate graphs — even moderately informative structural hypotheses can yield useful training data. This is a non-obvious property of the TTT-SCL approach that the paper only partially exploits. Conversely, it also hints that the score function may be measuring a proxy that correlates weakly with causal accuracy on some settings, which the paper should investigate rather than gloss over.

## Suggestions

1. Correct the unconditional claim on line 249 ("The higher AUROC...") to accurately reflect that the search improves performance on 3 of 4 settings but degrades it on Linear_U. Add analysis of why this happens.
2. Add sensitivity analysis for λ (sparsity penalty) and K (number of training graphs) — these are central design choices with no reported exploration.
3. Add a baseline where the SCL model is replaced by a simpler aggregation method (e.g., averaging top-K adjacency matrices) to isolate the benefit of the learned model.
4. Discuss the Gaussian noise assumption for AD when the test data has non-Gaussian noise, or show that results are robust to this choice.
5. Clarify in the presentation that AD is a likelihood-based score (not a novel metric), and reframe the contribution as the TTT-SCL framework.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>