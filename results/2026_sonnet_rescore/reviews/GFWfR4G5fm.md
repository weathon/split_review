## Summary
This paper identifies three concrete limitations of static Supervised Causal Learning (SCL) pre-training — fragility to distribution shifts, failure in compositional generalization, and a synthetic-to-real performance gap — and proposes TTT-SCL, a framework that addresses these by dynamically generating test-aligned training data at inference time. The first instantiation, TACTIC, combines an Alignment of Distribution (AD) metric with a sparsity constraint, uses Metropolis-Hastings–style stochastic refinement to search the DAG space, and trains an SCL model (AVICI) on the resulting K=200 synthetic instances tailored to the test case. Experiments across synthetic, pseudo-real, and real-world datasets demonstrate meaningful gains over static baselines, especially in OOD scenarios.

---

## Strengths

- **Systematic and concrete OOD diagnostic (Section 3, Figure 2, Table 1):** The paper constructs targeted distribution-shift experiments across three axes (graph, mechanism, noise) plus a compositional "Component-mixed" condition. The results are reproducible and show real, often large, performance degradation — e.g., Mechanism shift drops AVICI (RFF_G_97.8) from 100 to 42 AUROC — directly motivating the TTT-SCL paradigm.

- **Sparsity ablation is tightly controlled and confirms necessity (Table 3):** Removing λ (TACTIC Notears-s) consistently and substantially hurts AUROC — e.g., Chebyshev_G drops from 83.0 to 69.7, Sachs from 78.9 to 63.5. This validates that both AD and sparsity are necessary components of the optimization objective.

- **Two-stage improvement is empirically demonstrated (Table 4):** TACTIC's three-stage progression (seed → highest-score graph → final SCL output) shows monotonic improvement across all four domains. Most strikingly on Sachs: 61.8 (seed) → 66.6 (highest-score) → 78.9 (final). This confirms that the SCL training step adds value beyond simply selecting the best graph from the search.

- **Strong OOD performance on real-world and pseudo-real data:** TACTIC (Notears) achieves state-of-the-art AUROC on Linear_U (86.3), Chebyshev_G (83.0), Sachs (78.9), and Syntren (80.1) — the exact settings where static SCL fails — while remaining competitive on RFF_G. This directly addresses the synthetic-to-real gap identified in Table 1.

- **Better initialization demonstrably improves search (Table 2):** TACTIC (Notears) consistently outperforms TACTIC (random) — e.g., Sachs: 78.9 vs 58.6 — showing the framework can leverage existing causal discovery outputs without being overly sensitive to their quality.

---

## Weaknesses

### Fatal
None.

### Major

- **No acknowledgment of Bayesian structure learning via MCMC, and a critical missing baseline.** The acceptance rule in Figure 3 is α = min[1, score(G_{k+1})/score(G_k)], the standard Metropolis-Hastings ratio, targeting a distribution proportional to exp(AD(G, D_test) − λ‖A_G‖₀). This is structurally identical to Bayesian DAG-MCMC structure learning (e.g., Friedman & Koller 2003, Eaton & Murphy 2007), where the target is also a likelihood-based score with a sparsity prior. The paper's Related Work (Section 5) discusses constraint-based, function-based, and continuous optimization score-based methods, but does not mention or distinguish from MCMC-based Bayesian structure learning. This omission materially affects the positioning of the contribution. More critically, the paper's strongest claim — "the fundamental distinction between TACTIC and classical score-based causal discovery" (Section 4.4) — rests on Table 4's comparison of the highest-score graph vs. the final SCL output. But the natural competitor to the SCL training step is not the single best graph: it is Bayesian model averaging over all K sampled graphs (i.e., threshold-averaging the K adjacency matrices). Without this baseline, it cannot be determined whether the "Learning Improvement" in Table 4 reflects genuine SCL learning or is approximating ensemble smoothing. This is the most important missing experiment in the paper.

- **The SIM regression model is unspecified in the main text.** SIM (Structure-Induced Mechanism) is the operational backbone of both the AD computation and the forward-sampling step, but the specific regressor — whether linear, kernel, GP, or something else — is never stated in the main text. The paper says "detailed configurations can be found in Appendix B" but the main-text description of the AD metric and SIM procedure is incomplete without this. The choice of regressor determines what AD actually measures and whether it is correctly specified for Linear, RFF, or Chebyshev mechanisms. This is a clarity gap for a central methodological component.

### Minor

- **TACTIC (Notears) underperforms AVICI (scm-v0) on RFF_G by ~6 AUROC points (91.8 vs 97.8), with no explanation.** For a method that is specifically tailored to each test instance at inference time, this gap on the setting where AVICI was explicitly trained deserves more than the paper's "slightly lower" characterization. Even a brief analysis of why test-time adaptation fails to close the gap here (e.g., K=200 being insufficient to match AVICI's broad pre-training) would strengthen the paper's account of the method's scope and limitations.

- **K=200 is a fixed design choice with no justification or sensitivity analysis.** The number of dynamically generated training graphs is set to K=200 for all experiments, but no ablation varies K. A K-vs-AUROC curve would both justify this choice and characterize the convergence behavior of the stochastic refinement, directly supporting claims about the method's efficiency. The paper has an appendix with complexity analysis but no K-sensitivity result is mentioned.

- **Some compositional generalization drops in Issue 2 are modest.** The paper describes compositional generalization failure as a "fundamental limitation," but the Component-mixed vs. i.i.d. drops in Figure 2 are small for certain settings (e.g., RFF_G_62.3: 86 vs 90; Linear_U_62.3: 89 vs 92). The more compelling cases are Chebyshev_G_62.3 (83 vs 93) and Linear_U_97.8 (89 vs 100). The claim that this is "fundamental" would benefit from narrowing to the settings where the drop is large, rather than aggregating across all.

### Trivial
None.

---

## Nice-to-Haves

- A K-vs-AUROC curve to characterize MCMC chain convergence and justify K=200.
- A sensitivity analysis for λ (Equation 5), including a description of how it was selected — fixed universally vs. tuned per dataset.
- For the Sachs dataset (non-Gaussian protein expression), an analysis of whether the default N(0,1) noise assumption in forward sampling (Step 3) degrades training data quality relative to a noise distribution better matched to the test data.
- Testing whether a misspecified mechanism regression (e.g., using a linear regressor for Chebyshev test data) in SIM changes the performance profile — this would characterize robustness to mechanism misspecification.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic Claim: AD is not differentiated from standard local scores in score-based methods.** The paper never claims AD is a novel mathematical object in its own right; it explicitly says "while there are many ways to implement AD as discussed in Appendix A, in the main text we use the implementation based on likelihood" (Section 4.1). The novelty claim is for the TTT-SCL *framework* (using the MCMC sample chain as SCL training data), not for the AD formula in isolation. This criticism is a strawman.

- **Harsh Critic Claim: Training a DNN on K=200 instances is mechanistically underspecified and potentially ill-conditioned.** The paper states "more detailed configurations can be found in Appendix B." The appendix is stripped from the review copy. Per review rules, absent appendix content cannot be used as a basis for criticism.

- **Harsh Critic: "No standard deviations for single-instance real-world datasets."** Single-instance real datasets (one Sachs graph, one Syntren graph) cannot yield standard deviations — this is logically correct, not an oversight.

- **Strength Finder Strength: "Principled AD metric yields an effective search score."** Partially valid (the ablation confirms both components matter), but the claim that AD is "principled" in a novel sense is overstated given its relationship to existing likelihood-based decomposable scores. Downgraded; the sparsity ablation strength is kept directly.

---

## Novel Insights

The paper's most genuinely novel observation is the compositional generalization failure of SCL: models trained on all individual components (mechanism types, graph families, noise distributions) in isolation cannot handle their combinations, suggesting that static pre-training fundamentally cannot cover the combinatorial space of real-world distributions. This is a conceptually clean finding that goes beyond simple "the training set wasn't diverse enough" explanations and motivates why test-time adaptation — rather than scaling pre-training data — is the right architectural response. The use of a MCMC-sampled graph chain as a dynamically-constructed training set for a neural SCL model is a concrete and implementable operationalization of this insight.

---

## Suggestions

1. **Add model-averaging baseline to Table 4.** Threshold-average the K=200 adjacency matrices from the MCMC chain and compute AUROC. If the SCL step substantially beats this average, the paper has definitively proven genuine learning value. This is the most important single addition.

2. **Situate the MH-MCMC step relative to Bayesian structure learning in Related Work.** Acknowledge that the refinement procedure is structurally an MH sampler over DAG space, note key distinctions (e.g., the score is used to generate training data for an SCL model rather than to infer the graph directly), and cite the relevant DAG-MCMC literature.

3. **State the SIM regression model in the main text.** Even one sentence indicating whether it is a linear regressor, kernel regressor, or MLP would address the reproducibility gap without requiring appendix access.

4. **Add K-sensitivity experiment.** A brief K ∈ {50, 100, 200, 500} vs. AUROC curve on one dataset (e.g., Sachs) would justify the K=200 choice and serve as a convergence diagnostic for the MCMC chain.

---

## Evaluation on Core Axes

**Originality:** Good. The TTT-SCL framework is a novel framing; applying test-time training specifically to generate causally-aligned synthetic training data is not previously proposed. The MCMC step itself is not new, but its use as a training data generator for an SCL model is.

**Importance:** High. OOD generalization is the primary bottleneck for real-world SCL applicability; the paper directly attacks it with both diagnosis and a working remedy.

**Claims supported:** Mostly, but with a gap. The improvement over static baselines is well-supported. The claim that the SCL step is "fundamentally distinct from score-based methods" requires the model-averaging baseline to be fully supported.

**Soundness:** Adequate. The method is principled, but the Bayesian structure learning connection is unacknowledged and SIM is underspecified in the main text.

**Clarity:** Good overall; the staged exposition (problems → metrics → algorithm → ablation) is well-organized. Some implementation details that matter for understanding the mechanism are deferred to appendix.

**Community value:** High. The OOD diagnostic itself is a contribution to the community's understanding of static SCL limits; the TACTIC framework is immediately applicable.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>