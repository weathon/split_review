Now I have all the information needed. Let me produce the consolidated review.

---

## Summary

This paper proposes TopInG, a framework for intrinsically interpretable GNNs that uses persistent homology to identify rationale subgraphs. The core idea is to learn a filtration function such that the topological features of the rationale subgraph and its complement are maximally separated, measured by a proposed "topological discrepancy" loss. The paper provides theoretical bounds connecting topological discrepancy to Wasserstein distances, a uniqueness guarantee under certain conditions, and experiments on multiple benchmark datasets.

## Strengths

- **Novel application of topological data analysis to interpretable GNNs**: Using persistent homology to learn a filtration that separates rationale subgraphs from noise is a creative and well-motivated direction. The paper clearly identifies an important limitation of prior work (variiform rationales) and builds a method that is structurally suited to address it.

- **Theoretical bounds connecting topological discrepancy to distributional separation (Theorem 3.2)**: The paper proves both upper and lower bounds for the topological discrepancy, relating it to the Wasserstein distance between graph distributions via Gromov-Hausdorff stability and Kantorovich duality. This provides a principled foundation for the loss function and yields a tractable lower-bound approximation via learnable Lipschitz vectorizations of persistence diagrams.

- **Ablation studies validate design choices**: Table 3 confirms that removing either the topological regularizer or the prior Gaussian regularizer degrades performance, showing both components play complementary roles. Figure 4 demonstrates robustness across a range of hyperparameter values for the two regularizers on BA-HouseAndGrid.

- **Theoretical uniqueness guarantee (Theorem 3.4)**: Under the conditions that the ground-truth rationale is minimal (no proper subgraph carries the same label information) and that |E_X| < |E_ε|, the topological discrepancy term is uniquely optimized by the ground-truth indicator function. Remark 3.5 correctly notes this guarantee does not rely on invariance assumptions across instances, making it compatible with the variiform setting in principle.

## Weaknesses

### Fatal

None.

### Major

- **Unfair experimental comparison due to different backbones**: The main results (Tables 1 and 2) use GIN as the backbone for all baselines but CINPP as the backbone for TOPING (Section 4.1). The paper states this is "to test the wide applicability of TOPING," but this asymmetry fundamentally confounds the comparison: improvements claimed at up to 20%+ could arise from the stronger backbone rather than the topological method. The ablation study (Table 3) only ablates loss components within the TOPING+CINPP framework and does not include a version of TOPING with GIN. Without a controlled experiment using identical backbones, the claimed empirical advantage over prior methods is not reliably attributable to the proposed approach. This is the single most decisive flaw in the experimental evaluation and must be addressed for the paper's empirical claims to be credible.

### Minor

- **Theorem 3.4 covers only the topological discrepancy term, not the full loss**: The theorem proves that $d_{topo}$ is uniquely optimized by the ground truth, but the actual training objective $\mathcal{L}(\phi)$ also includes a classification risk $\mathcal{R}$ and a prior regularization term. The paper's abstract says "our loss is uniquely optimized by the ground truth," which overstates what is actually proven. While one expects the full loss to inherit the property under reasonable conditions (since $\mathcal{R}$ is also minimized at the ground truth), the gap between the theorem and the claim should be explicitly discussed.

- **Vague description of how the threshold $t$ is used in practice**: The theory assumes a global threshold $t$ such that $G_X = G_{<t}$ and $G_\epsilon = G_{>t}$. In practice, the paper sets $t=0.5$ for the extraction function $\sigma$ but for the topological discrepancy computation states only that they "compute the persistent homology along ascending ordering and descending ordering separately, to mimic a hard cut for some threshold $t$" (line 170). This description is too vague to be reproducible. The relationship between the theoretical $t$, the practical $t=0.5$, and the "ascending/descending ordering" procedure needs to be clearly articulated.

- **Variiform rationale experiments lack sufficient detail**: The synthetic dataset BA-HouseOrGrid-nRnd is central to demonstrating the method's ability to handle variiform rationales (Figure 3), but the paper does not describe its exact generation process. It is also unclear whether baselines (GSAT, DIR) were given any systematic hyperparameter adaptation for this specific setting — their default configurations may be suboptimal for the variiform scenario, weakening the conclusion that only TOPING handles it.

- **Hyperparameter sensitivity shown for only one dataset**: Figure 4 only analyzes coefficient sensitivity on BA-HouseAndGrid. For the SpuriousMotif datasets where the largest improvements are claimed, no similar analysis is provided, leaving open the question of whether gains are robust or arise from a lucky hyperparameter choice.

### Trivial

- The paper uses an unusual significance reporting method ("mean - 1×std > baseline mean" for shadowed entries) rather than reporting standard deviations directly alongside means in tables. Conventional reporting (e.g., mean ± std) would be more informative and allow readers to assess variability directly.

## Nice-to-Haves

- An ablation comparing node-based vs. edge-based filtrations would be useful, since the paper uses node filtrations for efficiency but acknowledges they carry less information. Showing the empirical cost/benefit tradeoff would strengthen the implementation choices.
- The upper bound in Theorem 3.2 ($d_{topo} \leq 2 d_{wass}$) establishes that topological discrepancy is a reasonable surrogate for distributional separation but is not experimentally exploited. Discussing or visualizing when this bound is tight could deepen the theoretical analysis.

## Removed Points

These points were flagged by reviewers but are removed after verification:

- *"The minimality assumption contradicts the variiform setting"* — The minimality assumption (no proper subgraph carries the same label information) applies within each individual graph; the variiform challenge is about variation across graphs. These are orthogonal and do not conflict. Removed as factually incorrect.
- *"Typos (varriform, Guassion, descrepency)"* — These are parser artifacts and minor formatting issues. Removed per formatting-nitpick rule.
- *"The notation $\mathcal{T}\circ\mathcal{F}$ is never fully defined"* — The paper defines $\mathcal{T}$ as the persistence diagram functor (line 103) and $\mathcal{F}$ as the filtration. This is standard notation in TDA and is adequately defined. Removed.
- *"Missing related works"* — Removed per rule (no external sources to confirm).
- Generic/redundant strengths from the Strength Finder that add no information beyond what is already captured above.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface genuinely novel observations about the paper that the authors themselves did not already articulate.

## Suggestions

1. **Run a controlled backbone experiment**: Either (a) implement TOPING with GIN as the backbone and compare against GSAT/DIR also with GIN, or (b) adapt the baselines to CINPP. Only then can the method-specific contribution be separated from backbone effects. This is the single most important fix.
2. **Clarify the practical loss function**: Clearly state how the threshold $t$ is determined (fixed, learned, or integrated via the bimodal prior) and provide precise pseudocode for how the topological discrepancy is computed in practice, including the "ascending and descending ordering" procedure.
3. **Describe the BA-HouseOrGrid-nRnd generation process**: Provide full details and confirm that baselines received reasonable hyperparameter tuning for this setting.
4. **Report standard deviations alongside means** in all result tables, and consider adding hyperparameter sensitivity analysis for the SpuriousMotif datasets.
5. **Correct the overclaim in the abstract**: Theorem 3.4 proves uniqueness for the topological discrepancy term; the abstract should accurately reflect this scope.

## Score and Decision

The paper tackles a well-motivated problem and introduces a genuinely novel application of topological data analysis to interpretable GNNs. The theoretical bounds and uniqueness guarantee provide a principled foundation. However, the experimental evaluation suffers from a decisive flaw: baselines use GIN while the proposed method uses a different, likely stronger backbone (CINPP), making the claimed 20%+ improvements uninterpretable. Until this confound is resolved through controlled experiments, the central empirical claims are not supported. The paper requires major revision before its contributions can be assessed fairly.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>