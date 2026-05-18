- Decision: Reject
- Scores: 3, 3, 3, 3, 5

## Merged Review

### Summary
The paper proposes EDMA, an instance-level explanation method for 3D molecular graphs, aiming to identify a small subgraph that best preserves the GNN prediction. It introduces an energy-based regularization to push soft mask scores towards 0 or 1, thereby reducing the gap between the soft and discrete masks. Experiments on two tasks from QM9 with DimeNet++ and SchNet backbones compare against GNNExplainer, PGExplainer, GraphMask, and SubgraphX.

### Strengths
- Tackles the important yet understudied problem of explaining 3D GNNs, where edge count is large due to cutoff-radius construction.
- Identifies the discrepancy between soft and discrete masks as a key challenge and proposes an energy-based regularization to enforce discreteness, going beyond typical relaxation approaches.
- Touches several often-overlooked aspects: mask discreteness, node-vs-edge masks, and regression explanation tasks.
- The paper is well-organized, clearly written, and uses clean notation; figures (Figs. 1-4) help clarify the method.
- Shows both quantitative (Fidelity- on QM9) and qualitative (Fig. 4 visualizations) results, plus an ablation study comparing EDMA with and without the discreteness loss (EDMA-soft).
- Reviewer 5 (score 5) is notably more positive, highlighting the relevance of 3D-specific explainability and the focus on regression, which is often neglected in XAI literature.

### Weaknesses
1. **Motivation for 3D-specific methods is not convincingly justified.**  
   - The claim that 2D explanation methods fail on 3D graphs is not backed by concrete examples or quantitative evidence (Reviewers 1, 4, 5).  
   - The two challenges in Section 3.1 (edge independence assumption, dense adjacency matrix) also apply to many 2D graphs (social networks, transaction graphs, etc.); reviewers 4 and 5 find this insufficient to justify ad-hoc 3D approaches.  
   - Interpreting edges defined by a cutoff radius (not chemical bonds) is of questionable chemical relevance; the paper does not explain why such extra edges need interpretation (Reviewer 1).

2. **Incremental novelty and insufficient comparison against standard discreteness techniques.**  
   - Using regularization to push masks toward 0/1 is ubiquitous (e.g., Gumbel-Softmax in PGExplainer and LRI); the paper neither compares against these alternatives nor demonstrates that the proposed energy-based approach is more effective than, e.g., applying L1 regularization to the mask or using a Gumbel activation (Reviewers 1, 2, 3, 5).  
   - The energy-based interpretation is considered superficial by Reviewer 2, as any softmax function can be viewed as an energy-based model.  
   - PGExplainer already produces discrete (edge-level) masks, reducing the novelty of addressing discreteness (Reviewer 3).

3. **Incomplete and outdated experimental evaluation.**  
   - Only the QM9 dataset is used; the results do not generalize to larger, more complex molecular datasets such as GEOM-Drugs or QMugs. Since QM9 contains only small molecules, the paper’s claim that the method scales to larger graphs is unsubstantiated (Reviewers 1, 2).  
   - Baselines are all from 2022 or earlier; recent graph explanation methods from 2024 (e.g., Huang et al. AAAI’24, Zhang et al. WWW’24, Chen et al. SIGMOD’24) are missing (Reviewers 1, 4).  
   - Evaluation uses only Fidelity– (deletion); Fidelity+ (insertion) and other standard metrics (e.g., from Yuan et al. TPAMI’22 or Longa et al. ACM Comput. Surv.’24) are omitted (Reviewer 5).  
   - No experiments on 2D graphs are provided; if the method is superior, it should at least match SOTA 2D explainers (Reviewer 2).

4. **Poor presentation of technical details, causing confusion.**  
   - Equation (7) is ambiguous: the variable \(\mathbf{r}\) is not defined, and the loss only sums over node \(i\) rather than all nodes; also the parameters to be optimized (presumably \(\zeta, \gamma\)) are not specified (Reviewers 1, 2, 3).  
   - Equation (5) is mislabeled: the left side is a graph, not a loss; should be an inequality of losses (Reviewer 3).  
   - The meaning of “pushing energy” and “budget” in Fig. 3 is unclear; the figure lacks explanation (Reviewer 3).  
   - Fig. 1 row b’s red dashed lines are not explained (Reviewer 4).  
   - Fig. 4 is cherry-picked; no failure cases or less clear examples are shown (Reviewer 2).  
   - The extraction of the optimal subgraph from the soft mask (threshold or argmax) is not specified (Reviewer 1).  
   - The hyperparameter controlling subgraph size (“budget \(K\)”) is not explained; it is unclear how the method avoids the trivial solution where the whole graph is retained (Reviewer 2).

5. **Missing ablation and parameter analysis.**  
   - The temperature \(T\) is the only difference between EDMA and EDMA-soft, yet its values are not reported; a study of \(T\)’s effect is missing (Reviewer 3).  
   - The impact of the energy regularization strength is not ablated.

6. **Suitability of the objective for explanation.**  
   - Using the learn-to-explain framework to minimize prediction error on the subgraph can yield high MAE (worse than original graph), questioning whether such subgraphs are truly the “most important” (Reviewer 1).  
   - The method may be more appropriate for property prediction on reduced graphs rather than explanation per se (Reviewer 1).

7. **Other requested comparisons and clarifications.**  
   - How do results change with different backbones (e.g., SchNet vs. DimeNet++)? Would the explanations differ? (Reviewer 1).  
   - Can the method be evaluated against ground-truth chemical explanations (like the expert knowledge in Fig. 4) quantitatively? (Reviewer 4).  
   - The performance of the explained model itself is not reported (Reviewer 4).  
   - Fig. 4(b,c) uses a multigraph and an adjacency matrix; it is unclear how an adjacency matrix can represent multiple edges between the same nodes (Reviewer 1).