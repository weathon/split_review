- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 6, 3
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper investigates the adversarial robustness of Graph Lottery Tickets (GLTs) — jointly sparse GNNs and graph adjacency matrices. It first demonstrates that GLTs identified by the standard UGS method collapse under poisoning attacks. To address this, it proposes ARGS (Adversarially Robust Graph Sparsification), an iterative pruning framework with a loss function that combines: (a) cross-entropy on train nodes, (b) feature-smoothness regularization (homophily-aware: attribute-smoothness for homophilic graphs, positional-smoothness for heterophilic graphs), (c) pseudo-label-guided cross-entropy on test nodes, and (d) ℓ₁ sparsity regularization. The paper claims ARGS produces ARGLTs that maintain competitive accuracy at high sparsity levels under PGD, MetaAttack, and PR-BCD poisoning attacks.

## Strengths

1. **Clear problem identification with concrete evidence.** Figure 2 shows that UGS-based GLTs suffer substantial accuracy degradation under PGD and MetaAttack (e.g., ~25% drop at 20% perturbation + 30% graph sparsity on Cora). This convincingly motivates the need for robust sparsification methods — a direction the paper is the first to explore.

2. **Insightful analysis of adversarial edge properties.** Figure 3 demonstrates that for homophilic graphs (Citeseer), PGD-attack-introduced edges tend to connect nodes with dissimilar attribute features, while for heterophilic graphs (Chameleon), they connect nodes with dissimilar positional (DeepWalk) features. This analysis is data-driven and provides a principled justification for the two variants of the feature-smoothness loss (Eq. 4 and Eq. 5).

3. **Novel loss design that jointly targets adversarial edge removal and sparsity.** The ARGS loss (Eq. 7) combines train-node CE, feature-smoothness regularization (using either attribute or positional features depending on graph type), test-node CE via MLP pseudo-labels, and ℓ₁ sparsity on both graph and weight masks. The use of pseudo-labels for test nodes, motivated by the observation that attacks modify mainly train-node neighborhoods (Li et al., 2023), is a reasonable adaptation.

4. **Demonstration of adversarial edge removal over iterations.** Figure 4 quantifies that after 20 ARGS iterations (5% per iteration), train-train adversarial edges drop by 68.13%, train-test by 47.3%, and test-test by 14.3% on Cora under PGD. This provides direct evidence that the loss function is achieving its intended effect.

## Weaknesses

### Fatal
None.

### Major

1. **The dedicated experimental section (Section 4) is absent from the provided manuscript.** The paper jumps from Section 3 (Methodology) to Section 5 (Conclusion) with no Section 4 containing experimental setup, full result tables, baseline comparisons, or ablation studies. While some results are scattered in Section 3 (Figures 2–4, text claims about sparsity and accuracy), the paper lacks the systematic evaluation needed to verify the comprehensive claims made in the abstract — e.g., evaluations "on various benchmarks" with "PGD, MetaAttack, PR-BCD attack, and adaptive attacks" across six datasets. Without the organized experimental section, readers cannot assess whether the method delivers what is promised. This is the single largest barrier to acceptance.

2. **No ablation studies of the loss components.** The ARGS loss (Eq. 7) has three main terms (train-node CE, feature-smoothness, test-node pseudo-label CE) plus two ℓ₁ regularizers. The individual contribution of each term is not isolated. It is unclear, for instance, whether the pseudo-label term or the smoothness term drives the improvement over UGS, or whether they interact positively. Given the complexity of the loss, ablations are essential to understand which components matter and to guide future work.

3. **Attack-property analysis limited to PGD.** Figure 3 analyzes edge properties only under the PGD attack. The text mentions "MetaAttack, PGD, and PR-BCD" (line 75) but Figure 3 is explicitly for PGD. Without corresponding analysis for MetaAttack and PR-BCD, the generality of the observation (and thus the justification for the loss design) is unverified for those attacks. If MetaAttack or PR-BCD produce different structural signatures, the loss may be less effective.

4. **Hyperparameter values for β, λ₁, λ₂ are not specified.** The paper states "where β, λ₁, and λ₂ are the hyperparameters and the value of α and γ is set to 1" (line 115), but never provides the actual values used. Similarly, the pseudo-label confidence threshold (referred to as "high prediction confidence" on line 100) is not quantified, and the DeepWalk dimension P for positional features (Eq. 5) is not given. These gaps hinder reproducibility.

### Minor

1. **The comparison to UGS is informative but insufficient to contextualize robustness.** The paper compares ARGLTs only to UGS-based GLTs and clean-graph accuracy. It does not include a reference point such as a full (unpruned) robust GNN (e.g., GNNGuard, ProGNN, or adversarially trained GCN) under the same attacks. This makes it difficult to assess the robustness cost of sparsification: if a full robust GNN achieves 85% accuracy under attack and ARGLT achieves 82%, the trade-off may be favorable; if the full robust GNN achieves 90%, the gap is more concerning. This would be a straightforward addition to strengthen the evaluation.

2. **The analysis of UGS GLT collapse (Section 3.1) only covers two datasets (Cora, Citeseer) and two attacks (PGD, MetaAttack).** While this is sufficient to motivate the problem, the paper would benefit from extending this motivating analysis to heterophilic datasets and PR-BCD to better establish the scope of the vulnerability.

3. **No discussion of limitations or failure modes.** The paper does not discuss scenarios where ARGS might struggle — e.g., high perturbation rates where pseudo-labels become unreliable, graphs with very few training nodes, or settings where the attack does not conform to the homophily/positional-signature assumption.

4. **Figure 1 lacks the "full model under attack" accuracy line.** Figure 1 shows accuracy vs. graph sparsity for ARGS and UGS, but the baseline "full model" accuracy is only shown for the clean graph, not under attack. This would help calibrate how much accuracy loss is due to the attack vs. due to sparsification.

### Trivial
- The DeepWalk dimension P and pseudo-label confidence threshold are mentioned but not quantified.
- Some variable names use inconsistent notation (e.g., ∇m_θ on line 51 vs. m_θ elsewhere).

## Nice-to-Haves
- Ablation study isolating the contribution of each loss term (ℒ_fs, ℒ_1, pseudo-labels, ℓ₁ regularization).
- Complete hyperparameter documentation (β, λ₁, λ₂ values, confidence threshold, DeepWalk dimension P, pruning schedule per dataset).
- Comparison of ARGLT accuracy to a full (unpruned) robust defense (e.g., GNNGuard or ProGNN) under the same attack budget, to contextualize the robustness-sparsity trade-off.
- Extension of the adversarial edge analysis (Figure 3) to MetaAttack and PR-BCD to verify generality of the homophily/positional-signature assumptions.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Missing comparison to other graph sparsification methods (e.g., GDC, NeuralSparse) under attack"** (Harsh Critic): The paper scopes itself to GLTs and compares against the standard GLT baseline (UGS). GDC and NeuralSparse are different paradigms (graph diffusion, edge prediction) that are not designed for the GLT setting. This is scope creep.
- **"No statistical significance or variance reporting"** (Harsh Critic): While stated in the critique, the paper's figures and text do not explicitly show error bars. However, single-run evaluation without variance bars is common practice in this sub-area (most graph defense papers report point estimates for accuracy). This is field-standard practice, not a unique flaw.
- **"No discussion of limitations"** framed as a missing section (Harsh Critic): This is a reasonable suggestion but more of a presentation improvement than a weakness that threatens the paper's validity.
- **Strength Finder point 6 ("Evaluation across multiple datasets and attack types, including large-scale graphs")**: This strength relies on claims that would be verified in the missing Section 4. The abstract and introduction claim evaluations on OGBN-ArXiv, Chameleon, Squirrel, etc., but the actual results are not present in the provided manuscript. This is an unverifiable claim in the current form.

## Novel Insights

None beyond the paper's own contributions. The two reviewer perspectives largely converge on the paper's strengths (well-motivated problem, interesting property analysis, novel loss design) and weaknesses (incomplete evaluation, missing ablations, under-specified hyperparameters). Neither review surfaces an insight that meaningfully reinterprets the paper's contribution beyond what the authors state.

## Suggestions

1. **Complete and include the experimental section** with full result tables for all six datasets (Cora, Citeseer, PubMed, OGBN-ArXiv, Chameleon, Squirrel) under all three attacks (PGD, MetaAttack, PR-BCD), including standard deviations across multiple runs.
2. **Add ablation studies** that remove each component of the loss function (ℒ_fs, ℒ₁, pseudo-labels) and report the resulting accuracy-sparsity trade-off.
3. **Specify all hyperparameters** (β, λ₁, λ₂, pseudo-label confidence threshold, DeepWalk dimension P, pruning percentage per iteration for each dataset) in a reproducibility table.
4. **Extend the adversarial edge analysis** (Figure 3) to at least MetaAttack to verify the generality of the homophily/positional-signature observation.
5. **Include a comparison point** showing the accuracy of a full (unpruned) robust GNN (e.g., GNNGuard or an adversarially trained GCN) under the same attack, to contextualize the robustness achieved at high sparsity.
