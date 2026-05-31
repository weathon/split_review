## Summary

This paper identifies three fundamental limitations of static Supervised Causal Learning (SCL): fragility to distribution shifts, failure in compositional generalization, and a synthetic-to-real performance gap. To address these, the authors propose Test-Time Training for Supervised Causal Learning (TTT-SCL), a framework that dynamically generates causally-aligned training data at test time. Their concrete method, TACTIC, uses an Alignment of Distribution (AD) metric combined with a sparsity penalty to guide MCMC-style search in DAG space, producing customized training data for each test instance. Experiments show TACTIC substantially outperforms static SCL and traditional causal discovery methods, especially on real-world data.

---

## Strengths

- **Well-motivated and rigorously demonstrated limitations**: The three issues (distribution shift, compositional generalization failure, synthetic-real gap) are not mere assertions—they are backed by systematic experiments with controlled factorial combinations of mechanism/graph/noise, making the motivation for the new paradigm compelling and concrete.

- **Genuinely novel TTT-SCL framework**: Applying test-time training to supervised causal learning is a creative reframing. The insight that training-test similarity can be operationalized via distributional alignment (AD), and that generating aligned training data is more tractable than finding the exact test graph, is both principled and practically grounded.

- **Informative stage-wise ablation (Table 4)**: The three-stage breakdown (seed → highest-scoring TACTIC graph → final SCL output) is the paper's strongest empirical contribution. The consistent and substantial 2→3 improvement (e.g., 66.6→78.9 on Sachs, 75.8→83.0 on Chebyshev) demonstrates that the SCL model trained on TACTIC-generated data genuinely adds value beyond what the score-based search alone recovers—this is non-trivial and validates the core claim.

- **Ablation on sparsity (Table 3)**: The removal of the sparsity penalty causes consistent performance drops across all domains, providing clean evidence that causal minimality enforcement is necessary and that AD alone leads to degenerate dense solutions.

- **Breadth of evaluation**: Results span synthetic, pseudo-real (SynTREn), and real-world (Sachs) benchmarks, with multiple metrics (AUROC, AUPRC, F1, ACC) reported in supplementary material, offering comprehensive coverage.

---

## Weaknesses

### Fatal
None.

### Major

1. **Test-time computational cost is substantial and undercharacterized in the main text**: For each test instance, TACTIC must (i) run a traditional CD method as a seed, (ii) execute a MCMC chain for K=200 steps with per-step mechanism regression on D_test, (iii) forward-sample K datasets, and (iv) train a full SCL neural network from scratch. This is orders of magnitude more expensive than a single forward pass of AVICI. The paper defers complexity analysis entirely to Appendix F. Without a clear wall-clock comparison in the main body, readers cannot assess the cost-benefit tradeoff, which is central to evaluating real-world applicability—the very concern the paper raises about prior work.

2. **Conceptual proximity to score-based causal discovery is underdiscussed**: The AD metric (Eq. 3) is a likelihood-based graph scoring function, and the stochastic refinement with transition probability α = min[1, score(G_{k+1})/score(G_k)] is exactly Metropolis-Hastings over the DAG space. This is structurally very similar to score-based causal discovery methods (e.g., MCMC-based variants). The key distinction—using found graphs as training data for an SCL model rather than outputting them directly—is important and is empirically validated in Table 4. However, the paper does not adequately discuss why the SCL model trained on these K graphs outperforms simply averaging/ensembling the K graphs directly, nor does it explain the theoretical basis for the 2→3 improvement. Without this, the contribution of the SCL training stage over score-based MCMC search remains empirically demonstrated but mechanistically opaque.

3. **Sensitivity to K and λ is not analyzed in the main text**: TACTIC has two key hyperparameters: K (number of generated training graphs, set to 200) and λ (sparsity trade-off, Eq. 5). The paper does not present any sensitivity analysis for these in the main text, making it unclear how robust the method is to these choices in practice.

### Minor

1. **Default Gaussian noise assumption in forward sampling**: TACTIC's training data generation fixes noise to N(0,1) regardless of the test domain (Section 4.2, Step 3). This strong assumption may limit applicability to real-world data with non-Gaussian noise, and the paper does not empirically examine its impact.

2. **Single Sachs test instance**: Results on Sachs are single-point estimates without standard deviation. As a benchmark with one consensus graph, this is expected, but the paper should explicitly note this limitation for the reader.

3. **TACTIC vs. AVICI gap on in-distribution data**: TACTIC (Notears) achieves 91.8 on RFF_G while AVICI (scm-v0) achieves 97.8—a ~6-point gap when AVICI was explicitly trained on RFF_G. While the paper acknowledges this, it does not discuss whether a static SCL model trained on TACTIC-generated data (without test-time adaptation) could close this gap, which would help separate the contribution of the framework from the data quality.

### Trivial

- The transition probability α formula in the TACTIC description corresponds to a simple ratio acceptance rule; calling it a "stochastic refinement" understates the established connection to Markov chain Monte Carlo and may obscure relevant theoretical properties (mixing time, convergence).

---

## Nice-to-Haves

- A wall-clock runtime comparison in the main body (even approximate), breaking down the MCMC search vs. SCL training phases, would make the cost-benefit tradeoff more transparent.
- An analysis of why the SCL training phase (2→3) improves over direct use of the highest-scoring graph—possible explanations include variance reduction via ensemble training data, regularization from the full K-graph distribution, or the SCL model's implicit Bayesian averaging.
- An experiment varying K (e.g., K ∈ {50, 100, 200, 500}) to show the performance-cost curve.
- Discussion of whether TACTIC's Gaussian noise assumption can be relaxed, e.g., by estimating the noise distribution from D_test before forward sampling.

---

## Novel Insights

The most genuinely novel observation is that training an SCL model on a set of K graphs that are distributionally similar to the test instance yields substantially better predictions than simply outputting the highest-scoring graph found during the search (Table 4). This suggests that the SCL model is not merely memorizing the search result, but is learning a more robust causal representation from the ensemble of aligned training instances—an implicit form of Bayesian model averaging in the space of causal structures. The finding that compositional generalization fails even when all individual components are seen during training (Issue 2) is an independently important empirical observation about SCL models that motivates the test-time concentration strategy and has broader implications for the design of synthetic pre-training curricula.

---

## Suggestions

- Add a timing table to the main text comparing per-instance wall-clock time for TACTIC vs. traditional baselines vs. AVICI.
- Provide a sensitivity analysis for K and λ in the main text (even a single figure showing AUROC vs. K on one or two datasets would suffice).
- Empirically assess the impact of the Gaussian noise assumption by running TACTIC on a dataset with known non-Gaussian noise and comparing against a variant that estimates noise distribution from the test data.
- Clarify the Metropolis-Hastings connection explicitly and discuss (even briefly) implications for convergence and the practical number of steps needed.

---

## Score and Decision

TACTIC presents a creative and well-executed solution to a genuine problem in supervised causal learning. The three-issue diagnosis is rigorous, the TTT-SCL framework is novel, and the 2→3 improvement is compelling evidence that the approach does more than replicate score-based causal discovery. The primary concerns—computational cost at test time and insufficient mechanistic explanation of the SCL learning stage—are significant but not fatal. The paper earns acceptance, though revisions clarifying cost and the source of the 2→3 gain would strengthen it considerably.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>