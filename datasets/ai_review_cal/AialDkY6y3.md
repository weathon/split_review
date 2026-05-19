- Decision: Reject
- Avg Score: 4.40
- Scores: 3, 5, 3, 5, 6
Now I have all the information needed. Here is the consolidated review.

---

## Summary

This paper introduces the Dirac-Bianconi Graph Neural Network (DBGNN), a GNN architecture derived from Bianconi's topological Dirac equation on graphs. Unlike Laplacian-based GNNs that tend to smooth node features through repeated propagation, the Dirac operator treats nodes and edges symmetrically and, by design, has no kernel — meaning the dynamics cannot converge to a homogeneous steady state. DBGNN instantiates this as a repeated weight-shared Euler discretization of the Dirac equation with learnable feature-space matrices, followed by nonlinearities. Experiments are conducted on three tasks: power grid stability prediction (where DBGNN achieves strong in-distribution and out-of-distribution results), protein–ligand binding affinity prediction, and peptide property prediction on the Peptides-struct benchmark.

---

## Strengths

1. **Principled physics-inspired architecture with theoretical grounding for avoiding over-smoothing.** Section 2 provides a spectral analysis showing that the Hermitian Dirac operator ∂_DB + diag(β, –β) has no kernel (its eigenvalues are bounded away from zero by |β|²), so dynamics driven by it cannot converge to a feature-uniform equilibrium. This gives the approach a theoretical foundation distinct from heuristic anti-smoothing modifications in prior GNNs. The Dirichlet energy experiments (Figures 5, 7) empirically validate that DBGNN maintains high feature heterogeneity even after hundreds of steps — both untrained (vs. GCN, Figure 5) and after training (Figure 7, with five seeds).

2. **Strong out-of-distribution generalization on power grid stability prediction.** On the tr20ev100 task (training on 20-node grids, testing on 100-node grids), DBGNN substantially outperforms all baselines reported in Nauck et al. (2023). This result is the paper's most compelling empirical contribution: it demonstrates that the architecture can learn structural relations that transfer across graph sizes, which is valuable for real-world grid analysis.

3. **Direct evidence of long-range wave-like propagation in controlled synthetic settings.** Figure 6 systematically compares the linear and nonlinear DB equation against MPNN variants on a 5×20 grid with a localized initial condition. The DB equation produces a propagating leading edge that spreads rapidly into the graph, while MPNN variants exhibit only diffusion. The analysis isolates the role of the Dirac dynamics from that of edge nonlinearities.

4. **Competitive performance on Peptides-struct with substantially fewer parameters.** DBGNN achieves an MAE of 0.580 on Peptides-struct with 63,911 parameters, outperforming GCN baselines that use ~500k parameters. While the comparison is not perfectly controlled (different parameter budgets), this suggests the Dirac dynamics efficiently capture long-range molecular structure.

---

## Weaknesses

### Fatal
None.

### Major

1. **No error bars, variance reporting, or number of runs for main experimental results (Tables 1–3).** The paper reports only point estimates for all three tasks. The binding affinity improvement (MSE 0.294 vs. 0.309) is small enough that without standard deviations or multiple seeds, it could easily be within noise. Even for the power-grid OOD result — where the gap is large — the absence of any variance information is a significant omission that prevents assessing reliability. This is the single most important weakness: it undermines the central empirical contribution. (Only the Dirichlet energy analyses in Figures 5 and 7 report five seeds.)

2. **No ablation study attributing performance to specific architectural components on real tasks.** The paper makes strong mechanistic claims: that wave-like dynamics (not edge nonlinearities) drive long-range propagation, that the equal node/edge treatment is beneficial, and that the absence of over-smoothing explains performance. None of these are tested through ablations on the actual tasks. For the power grid dataset (no input edge features), one could ablate: removing edge state updates entirely, using symmetric coupling to destroy wave structure, varying T to test whether deeper propagation matters, or removing edge nonlinearities. Without such ablations, the source of the empirical improvement is unexplained — it could be due to skip connections, residual structure, or other generic factors rather than the Dirac-specific properties.

3. **Binding affinity baseline is not re-implemented in the same pipeline.** For the Davis dataset, the paper replaces 3 GCN layers with 1 DBGNN layer within the framework of Gorantla et al. (2023), but the baseline GCN result (MSE 0.309) is taken from that separate paper, not re-run in the authors' own pipeline. Differences in random seeds, data splits, hyperparameters, or minor implementation variations between two codebases can easily account for a gap of 0.015 MSE. An apples-to-apples comparison (re-running the GCN baseline in the same code) is needed to determine whether the improvement is genuine.

### Minor

1. **Missing specification of edge feature initialization for graphs without input edge features.** The power grid dataset has no input edge features (noted in Section 4). The DBGNN architecture maintains internal hidden edge features that are updated over time, but the paper does not specify how these are initialized when no input edge features exist (e.g., zero? learned embedding? random?). This is a reproducibility gap that should be straightforward to fix.

2. **Theoretical spectral guarantee does not directly extend to the unconstrained, discretized model.** The spectral analysis (Section 2) applies to the Hermitian operator with the imaginary unit and mass term. The actual DBGNN uses unconstrained real-valued weight matrices (no antisymmetry constraint) and an explicit Euler discretization. The paper notes this difference (line 98), and the Dirichlet energy experiments provide empirical validation. However, the theoretical motivation is presented as a guarantee ("has no kernel and no steady state") that strictly applies only to the Hermitian operator, not to the trained model. The gap should be discussed more explicitly.

3. **No GCN Dirichlet energy comparison on trained networks.** Figure 5 compares DBGNN and GCN Dirichlet energy on *untrained* networks. Figure 7 shows DBGNN Dirichlet energy on *trained* networks, but without a GCN comparison in the same trained setting. This weakens the claim that trained DBGNN avoids over-smoothing relative to alternatives.

4. **OOD generalization result lacks diagnostic analysis.** The paper reports a large OOD improvement but provides minimal analysis of *why* DBGNN generalizes so well (only a single sentence relating it to avoiding over-smoothing at depth). Diagnostic experiments — such as visualizing learned embeddings, checking whether wave-like propagation is present in learned weights, testing on intermediate grid sizes, or analyzing the learned filters — would turn this intriguing result into a grounded discovery. As presented, the explanation remains speculative.

5. **Slight inconsistency in the "no task adaptation" claim.** The conclusion states "the experiments as performed were conducted without adapting the model to the task at hand," but the binding affinity section mentions a hyperparameter study optimizing learning rates. This is a minor tension.

### Trivial
None.

---

## Nice-to-Haves

- For the Peptides-struct experiment, training a GCN or GINE baseline with a comparable parameter count (~63k) would provide a cleaner comparison and strengthen the parameter-efficiency argument.
- Including inference speed or parameter counts for all tasks would help contextualize the binding affinity comparison (1 DBGNN layer vs. 3 GCN layers).
- A brief discussion of limitations (e.g., that the synthetic wave analysis uses constrained weights not present in the trained model) would improve the paper's framing.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Criticism about missing Table 5 / hyperparameter details.** Per guidelines, sections that may have been stripped by the parser are assumed to exist in the original submission. Not penalized.
2. **Speculative concerns about data leakage or trivial transfer in the OOD result.** The harsh critic raised these ("accidental data leakage," "trivial transfer of some feature") as potential confounds, but no evidence or reasoning specific to the dataset supports them. These are generic suspicion, not a specific identified problem.
3. **Criticism that baselines for the power grid task rely on benchmark numbers from Nauck et al. (2023).** The power grid experiment uses a standardized, published benchmark — this is standard practice and not a weakness.
4. **"No analysis of whether the large OOD gap warrants further study."** The paper explicitly discusses the OOD result in Section 4 and mentions possible explanations (no over-smoothing at depth). The request for more analysis is valid (kept as Minor weakness #4 above), but the framing of "damages credibility" is overstated.
5. **Criticism about not controlling for parameter counts on Peptides-struct being "unfair."** The paper openly reports the parameter disparity (~63k vs. ~500k). Since the smaller model outperforms larger ones, this asymmetry favors the baseline, not the author's method. This is more naturally framed as a strength (parameter efficiency) than a weakness.
6. **Strengths from the Strength Finder that are generic or conflict with verified weaknesses.** No strengths needed removal — all five identified strengths are concrete, specific to the paper, and backed by evidence.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the paper's genuine strengths and gaps, with no additional observations that substantially reframe the contribution.

---

## Suggestions

1. **Add error bars to all main tables.** Re-run all experiments with at least 5 different random seeds and report mean ± std. This is the single highest-leverage improvement.
2. **Conduct ablation studies on the power grid task.** Test variants that: (a) remove edge state updates (fix hidden edge states), (b) use symmetric coupling matrices to break wave structure, (c) remove edge nonlinearities, and (d) vary T. Report which components drive the OOD generalization.
3. **Diagnose the OOD generalization.** Provide visualizations or quantitative analysis showing why DBGNN transfers across grid sizes — e.g., compare learned representations, test on intermediate sizes, check if weights learned on small grids produce wave-like propagation on large grids.
4. **Re-run the GCN baseline for binding affinity in the same pipeline** to ensure an apples-to-apples comparison.
5. **Specify edge feature initialization** for datasets without input edge features (e.g., power grid).

---
