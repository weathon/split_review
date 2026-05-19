- Decision: Reject
- Avg Score: 3.40
- Scores: 3, 5, 3, 3, 3
Now I have thoroughly read the paper. Let me synthesize the final review.

## Summary

This paper proposes MAGC, a modularity-aided graph coarsening framework for attributed graph clustering. It augments the Feature Graph Coarsening (FGC) objective with a modularity maximization term and several regularizers (Dirichlet energy, reconstruction error, logdet of the coarsened Laplacian, ℓ₁,₂ regularization), producing an optimization problem solved via block majorization-minimization. The loss is composable with multiple deep architectures (GCN, VGAE, GMM-VGAE), yielding variants Q-GCN, Q-VGAE, and Q-GMM-VGAE. Experiments on attributed (Cora, CiteSeer, PubMed) and non-attributed (Airports) benchmarks demonstrate competitive NMI, ARI, and ACC, alongside significant speedups (e.g., 75% reduction on PubMed vs. GMM-VGAE).

## Strengths

1. **Modularity term rescues FGC for clustering.** The paper explicitly identifies that FGC alone fails at coarsening ratios below 0.001 (needed for clustering), and the added modularity term bridges this gap. Section 4.1 and the reported comparison "Q-FGC > FGC" (e.g., from 8.2% to 37.6% NMI on Brazil airports) provide direct evidence that the modularity extension is essential.

2. **State-of-the-art NMI on three standard attributed benchmarks.** The text claims that Q-GMM-VGAE achieves the highest NMI on Cora, CiteSeer, and PubMed among all listed methods, outperforming strong baselines including DMoN, ARGA, DAEGC, SDCN, DCRN, and base GMM-VGAE. The modularity-vs-NMI tradeoff analysis (Table 4a) — showing a 40% NMI gain with only an 8% modularity drop on CiteSeer — directly supports the multi-term loss design.

3. **Large computational speedup.** Section 5.5 reports that Q-GMM-VGAE runs in under 15 minutes on PubMed versus ~60 minutes for GMM-VGAE and R-GMM-VGAE, a 75% reduction, while maintaining or improving NMI. The simpler Q-FGC variant runs in 6 minutes and achieves 90% of the performance.

4. **Versatility across attributed and non-attributed graphs.** The framework achieves competitive NMI on non-attributed Airports datasets using only degree one-hot features (Table 2a), and is composable with GCN, VGAE, and GMM-VGAE backbones — each integrated variant outperforms its base architecture.

5. **Honest discussion of modularity's limitations.** The paper explicitly shows (Table 4a) that DMoN achieves higher modularity but lower NMI, and states "maximum modularity labelling of a graph does not always correspond to the ground truth labelling." The conclusion honestly notes the method's limitation when ground-truth labels have low modularity, and demonstrates it still performs well on Airports.

## Weaknesses

### Fatal

None.

### Major

1. **The claimed convexity of the C-subproblem (Lemma 2) is unsupported and likely incorrect as stated.** The paper asserts that "all the terms in the objective function... with respect to C while keeping X̃ are convex functions" and defers the proof to supplementary material. The term −γ logdet(C^T Θ C + J) is not obviously convex in C: while −logdet(·) is convex over the PSD cone, its composition with the quadratic map C ↦ C^T Θ C does not generally preserve convexity. The paper provides no justification that this composition remains convex, and the proof in the main text is a bare assertion ("More details are in supplementary material"). Since the paper advertises "extensive theoretical analysis" and "provably convergent" algorithms, this is a significant overclaim. **However**, the MM update (Equation 8) is still a valid algorithmic step even if the subproblem is nonconvex — the majorant quadratic term (L/2)‖C−C^t‖² can dominate nonconvex structure for sufficiently large L. The fix is to either provide a correct proof or drop the convexity claim and instead justify convergence via the standard MM framework.

2. **No variance or statistical significance is reported for any experimental result.** The paper reports single numerical values for NMI, ARI, and ACC across all tables. Graph clustering is sensitive to initialization and hyperparameter choices, especially for methods using GNN backbones and the nonconvex objective of Equation 6. Without standard deviations over multiple runs (or an explicit statement that results are from a single fixed-seed run), the reader cannot assess whether reported improvements over baselines are robust or within noise. This weakens the headline claim of state-of-the-art performance.

### Minor

1. **Model selection protocol is underspecified.** The paper states "the best models were selected based on the NMI scores" (Section 5.3) but does not clarify whether selection occurs on a held-out validation set or the test set. If NMI on the test set is used for both tuning and final reporting, results risk overfitting. The split, tuning ranges, and selection criterion should be explicitly described.

2. **Hyperparameter values (α, β, γ, λ) are not listed per dataset.** The architecture is described (3 GCN layers, hidden sizes 128/64), but the four key hyperparameters controlling the loss terms are absent from the main paper. Only a qualitative sensitivity analysis is given (Section 5.5: α most sensitive, then γ, β, λ). A table of values per dataset would substantially improve reproducibility.

3. **The Lipschitz constant L in the majorization (Equation 8) is not discussed.** The MM update uses L in the quadratic majorant, but there is no description of how L is computed or bounded. This affects the convergence behavior of the C-subproblem update.

4. **Running time comparison lacks methodology details.** Section 5.5 reports "75% reduction" and "6 minutes for Q-FGC on PubMed" but does not specify the hardware, whether timing includes GNN training and optimization, or whether early stopping was used.

### Trivial

None.

## Nice-to-Haves

- A full ablation table (in the main paper) removing each term of Equation 6 one at a time, with NMI/ARI/ACC values, would quantify each term's contribution beyond the qualitative discussion.
- Convergence plots (loss vs. iterations) for the Q-FGC optimization would empirically demonstrate convergence given the theoretical concerns.
- A discussion of any dataset where a simple baseline (e.g., k-means on features) outperforms the proposed method would sharpen the boundaries of the contribution.
- Reporting the SBM ablation (currently in supplementary) in the main paper would strengthen the evidence that the method recovers planted community structure.

## Removed Points

1. **"Core experimental results are image placeholders"** — This is a parser artifact (images stripped from PDF). The actual submission contains proper tables. Removed per instructions about parser artifacts.

2. **"Missing appendix/supplementary content"** — The parser strips supplementary sections from all papers; they exist in the original submission. Removed per instructions.

3. **"No discussion of failure cases"** — The Conclusion (Section 6) already discusses the limitation about low-modularity ground truth and states the method still works on Airports. Partially addressed, and the reviewer's stronger claim is not fully accurate.

4. **Strength Finder's item 4 (theoretical convergence guarantees)** is partially in tension with the verified convexity weakness. The strength that "the paper provides Lemma 1 and Lemma 2 proving convexity" is weakened by the fact that Lemma 2's claim is unsupported. However, the MM framework itself is valid, so I retain a weakened version of this strength in spirit.

## Novel Insights

Beyond the paper's own contributions, the key insight from the review synthesis is that the paper's core empirical contribution — adding modularity to FGC with carefully chosen regularizations — is sound and well-motivated, but the theoretical scaffolding around it (convexity claims, "provably convergent") overreaches. The paper would be stronger by explicitly acknowledging the C-subproblem is nonconvex and justifying convergence through the standard MM argument (the majorized surrogate is convex for sufficiently large L). This is a straightforward fix that would align the theoretical narrative with the actual mathematics while preserving the algorithmic contribution.

## Suggestions

1. **Fix Lemma 2.** Either (a) remove the convexity claim and instead note that the MM surrogate is convex (which it is, due to the quadratic term), or (b) provide a rigorous proof of the claimed convexity with necessary conditions. The rest of the paper does not depend on the C-subproblem being convex for the algorithm to work.

2. **Add variance reporting.** Run each method 5–10 times with different seeds and report mean ± std for NMI, ARI, and ACC. If standard deviations are very small, state this explicitly.

3. **Clarify validation protocol.** Specify what fraction of data is used for validation, how hyperparameters are selected (grid search ranges), and whether reported numbers come from the validation or test set.

4. **Provide a hyperparameter table.** List α, β, γ, λ per dataset to enable reproducibility.
