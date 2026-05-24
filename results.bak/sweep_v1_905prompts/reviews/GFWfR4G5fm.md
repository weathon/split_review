Now I have a solid calibration. Let me write the final consolidated review.

**Calibration summary:**

Round 1 bracket: 5.0–7.0

Round 2 narrowing anchors consulted in full:
- **Demystifying amortized causal discovery with transformers** (5.00, Reject): Bivariate-only SCL analysis, no new method, synthetic data only. Current paper is clearly stronger — it proposes a new method, tests on real data, and addresses multivariate settings.
- **Robust agents learn causal world models** (5.75, Accept): Pure theory paper with no experiments. Different style of contribution but comparable overall quality in its domain.
- **Zero-Shot Learning of Causal Models** (6.25, Reject): Strong assumptions (known causal graphs, ANM), limited real evaluation. Current paper is comparable — similar level of assumption reliance but more practical applicability.
- **Test-Time Ensemble** (6.50, Accept): Solid empirical TTA paper. Current paper is slightly weaker due to missing std devs and under-specified AD metric.
- **Active Test-Time Adaptation** (6.75, Accept): Has theory + comprehensive experiments. Current paper is weaker on both theoretical and experimental completeness.

The current paper sits below Active TTA (6.75) and Test-Time Ensemble (6.50) due to clear reporting gaps, but above Demystifying amortized CD (5.00) due to proposing a genuinely new framework with real-data results. Score: **6.0**.

---

## Summary

This paper identifies three fundamental out-of-distribution challenges in static Supervised Causal Learning (SCL): fragility to distribution shifts, compositional generalization failure, and poor transfer from synthetic to real data. To address these, it proposes **TTT-SCL**, a framework that dynamically generates a training set aligned with each test instance, and instantiates it as **TACTIC**, which uses a likelihood-based Alignment of Distribution (AD) metric with an L₀ sparsity penalty to guide stochastic graph search, then trains an SCL model on the resulting synthetic data. Experiments on synthetic, pseudo-real (SynTReN), and real-world (Sachs) data show TACTIC significantly outperforms baselines, including a +11.8 AUROC gain over PC on Sachs.

## Strengths

1. **Clear diagnosis of three genuine limitations in static SCL.** Section 3 provides controlled experiments (Figure 2, Table 1) demonstrating that existing SCL models degrade under distribution shifts across graphs, mechanisms, and noise; fail at compositional generalization even when all components are seen in isolation; and collapse from ~98 AUROC on synthetic benchmarks to ~62 on real Sachs data. This empirical evidence convincingly motivates the need for a paradigm shift.

2. **Novel TTT-SCL framework with principled formulation.** The idea of generating training data at test time that is causally aligned with each test instance is a genuine contribution. The AD metric (Equation 3) and the L₀ sparsity penalty (Equation 4) formalize alignment in a tractable way. The ablation (Table 3) validates that removing the sparsity term hurts performance, and the stage-wise analysis (Table 4) shows both search-driven and learning-driven improvements, cleanly separating the contribution of each component.

3. **Strong empirical results on real data.** TACTIC (Notears) achieves 78.9 AUROC on Sachs (vs. next-best PC at 67.1) and 80.1 on SynTReN (vs. next-best AVICI at 65.4), while remaining competitive on synthetic benchmarks. These are the most practically relevant evaluations in the paper. Results using additional metrics (AUPRC, F1, ACC) in Appendix D and on bnlearn benchmarks in Appendix G strengthen the evidence.

4. **Clear contrast with existing SCL work.** The paper distinguishes itself from Montagna et al. (2024) by identifying compositional generalization as a distinct failure mode that diversity-based scaling cannot solve, and from classical score-based methods by showing that training an SCL model on the generated data (Stage 2→3 in Table 4) yields substantially better graphs than stopping at the highest-scoring graph.

## Weaknesses

### Major

1. **Missing variability measures for real and pseudo-real results.** Tables 1, 2, and 3 all report AUROC point estimates for Sachs and SynTReN without standard deviations, while standard deviations are consistently reported for synthetic columns. This matters because the paper's headline result (TACTIC 78.9 vs. PC 67.1 on Sachs) cannot be assessed for reliability without error bars. For a single dataset like Sachs, at minimum the stochastic search should be run with multiple random seeds or bootstrap resampling should be applied. This is a straightforward fix but a genuine evidential gap as submitted.

2. **AD metric implementation is under-specified.** Equation (3) defines AD as an average log-likelihood, and the text states that mechanisms are "regress[ed] ... from the observed D_test" via SIM. However, the paper never specifies: (a) what regression method is used (e.g., linear regression, Gaussian process, neural network with fixed architecture), (b) what likelihood model (e.g., Gaussian with estimated variance) is assumed for the log-probability computation, nor (c) how the sparsity penalty weight λ is chosen or what value is used. The noise is set to standard Gaussian for forward-sampling (Section 4.2), but the AD metric's own likelihood computation could differ. The paper mentions "many ways to implement AD as discussed in Appendix A" but the main text must be self-contained on this core component. Without these details, the method is not reproducible and the reader cannot assess whether AD relies on parametric assumptions that the test data may violate.

### Minor

3. **Seed sensitivity on real data is under-analyzed.** TACTIC (random) scores 58.6 on Sachs, which is *worse* than the simple baseline PC (67.1). While TACTIC (Notears) recovers to 78.9, the paper does not characterize how performance degrades as seed quality deteriorates. The claim that "strong performance of both variants confirms the robustness of our core approach" is contradicted by the Sachs result. An experiment with deliberately degraded seeds (e.g., random perturbation of NOTEARS output, or using PC as seed) would clarify the method's practical robustness boundaries.

4. **Stochastic search details are sparse.** The paper describes edge additions, deletions, and reversals with Metropolis-style acceptance but does not specify the number of search iterations, the proposal distribution, how acyclicity is maintained during proposals, or how the K=200 training graphs are selected from the search trajectory. Complexity analysis is deferred to the (stripped) Appendix F; including key scaling numbers (wall time for d=10,20,50) in the main text would help readers gauge practicality.

### Trivial

- None beyond the issues already noted.

## Nice-to-Haves

- An oracle upper-bound SCL model (trained on data from the *same* distribution as the test set) would clarify how much room for improvement remains beyond TACTIC.
- Explicitly testing TACTIC on a Component-mixed test instance vs. a static SCL model trained on the same Component-mixed set would directly validate the paradigm shift from diversity to concentration.
- A brief discussion of whether the final SCL model's improvement over the best-scoring graph (Table 4, Stage 2→3) can be attributed to ensembling over multiple high-scoring graphs vs. learning to correct biases in the likelihood score would strengthen the conceptual framing.

## Removed Points

These reviewer points are factually incorrect, based on speculating about missing appendix content, or are formatting/style nitpicks. They are listed for completeness but should not be weighed in the assessment:

- *"The AD metric assumes additive Gaussian noise, which if violated biases the score."* — The paper does state it applies to LiNGAM, ANM, and PNL frameworks (Section 4), and the AD metric definition in Equation (3) is agnostic to the specific regression method used. The complaint about a specific parametric assumption is not verifiable from the paper as written because the regression method is not specified (which is separately captured as a weakness above). The critique about assumption-violation is speculative without knowing the implementation.
- *"Missing complexity analysis / algorithm details"* — Complexity and runtime are deferred to Appendix F, which is stripped by the parser. The main text provides the algorithmic skeleton.
- *"Missing hyperparameter λ discussion"* — This is partially valid (and kept as part of weakness #2 above), but the older formulation in the critic claiming it's a "critical issue" is overstated since the ablation at λ=0 demonstrates the term's importance.
- *Strength Finder: "Thorough ablation and stage-wise analysis"* — This is valid and kept.
- *Various formatting nitpicks, missing appendix references, and "strawman" claims about unfair baseline comparisons* — Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The key insight — that static pre-training in SCL suffers from compositional generalization failure (not just shift sensitivity) and that test-time alignment of training data is a principled solution — is the paper's own intellectual contribution, not something synthesized from the reviews.

## Suggestions

- **Report error bars for Sachs and SynTReN:** Run TACTIC with 5+ different random seeds for the stochastic search (keeping the test data fixed) and report mean/std for all methods on these datasets. For Sachs, also consider bootstrap resampling of the 853 observations.
- **Specify the AD implementation in detail in the main text:** What regression method is used for fitting mechanisms? What likelihood (Gaussian with estimated variance? Other?) is used for the log-probability in Equation 3? State the chosen λ value and how it was selected (e.g., cross-validation, BIC-style scaling).
- **Add a seed-degradation experiment:** Start from NOTEARS output, add random edge perturbations (e.g., swap 10%, 30%, 50% of edges) and measure TACTIC's AUROC degradation on Sachs to characterize robustness.
- **Report wall-clock time** for the full TACTIC pipeline on d=10, 20, 50 nodes to give readers a concrete sense of scalability.

## Score and Decision

**Calibration anchors consulted:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| AvXrppAS2o — Best of both worlds: Improved outcome prediction using causal structure learning | 3.00 | 1 | Much weaker; different task framing, no real data |
| JzFLBOFMZ2 — Causal Structure Learning Supervised by LLM | 3.20 | 1 | Weaker; limited empirical contribution |
| fSxiromxAq — Sparse Causal Model | 3.00 | 1 | Much weaker; niche sparse-data setting |
| TRHyAnInUC — D³PM: Diffusion Model for Causal Discovery | 3.25 | 1 | Weaker; diffusion-based CD with limited novelty |
| G2AMCTTpCc — Taming Continuous Spurious Shift in Domain Adaptation | 3.75 | 1 | Different domain (DA), weaker empirical grounding |
| PxL35zAxvT — Test Time Adaptation with Auxiliary Tasks | 4.67 | 1 | Rejected; conceptual flaw (reinventing DA as TTA) |
| pOoKI3ouv1 — Robust agents learn causal world models | 5.75 | 1 | Pure theory, no experiments; comparable overall quality |
| bMvqccRmKD — Towards Generalizable RL via Causality-Guided Self-Adaptive Representations | 7.00 | 1 | Stronger; broader evaluation, cleaner exposition |
| xByvdb3DCm — When Selection meets Intervention | 8.00 | 1 | Much stronger; deep theoretical contribution |
| Nx4PMtJ1ER — Signature Kernel CI Tests in Causal Discovery | 8.00 | 1 | Much stronger; rigorous theory + method |
| lQYi2zeDyh — Demystifying amortized causal discovery with transformers | 5.00 | 2 | Weaker; bivariate-only, no new method, synthetic only |
| iaP7yHRq1l — Robustness of Differentiable Causal Discovery in Misspecified Scenarios | 5.50 | 2 | Comparable; empirical benchmarking paper, accepted |
| HBf6HFnpmH — Challenging Growth: Evaluating Scalability of Causal Models | 5.50 | 2 | Comparable; empirical benchmarking, rejected |
| x3F8oPxKV2 — Zero-Shot Learning of Causal Models | 6.25 | 2 | Comparable; similar assumption-reliance, rejected due to limited real eval |
| YHUGlwTzFB — Active Test-Time Adaptation | 6.75 | 2 | Stronger; has theory + comprehensive experiments, accepted |
| 4wk2eOKGvh — Test-Time Ensemble via Linear Mode Connectivity | 6.50 | 2 | Stronger; clean empirical evaluation, accepted |

Round 1 bracket: 5.0–7.0. Round 2 narrowed the placement: the paper is clearly stronger than the 5.00 SCL analysis paper (bivariate-only, no new method) and the 4.67 TTA-paper (conceptual confusion), but weaker than the 6.75 Active TTA paper (which adds theory and more complete experiments) and the 6.50 Test-Time Ensemble paper (cleaner evaluation). It is comparable to Zero-Shot Learning of Causal Models (6.25), which had similar strengths (novel framework, strong motivation) and similar weaknesses (assumption reliance, reporting gaps). The current paper edges ahead due to testing on actual real-world data (Sachs) and performing compositional generalization experiments.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>