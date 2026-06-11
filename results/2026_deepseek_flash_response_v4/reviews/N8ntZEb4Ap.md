## Summary

AutoNFS proposes a differentiable neural feature selection method using Gumbel-Sigmoid masking trained end-to-end with a downstream task network and a cardinality penalty, enabling automatic determination of both which and how many features to select. The paper evaluates on 11 benchmark datasets (with three corruption scenarios) and 24 real-world metagenomic datasets.

## Strengths

- **Empirically measured near-constant time scaling**: Figure 4b reports a complexity exponent α ≈ 0.08 ± 0.03 over 5 runs, showing AutoNFS runtime grows sub-linearly with feature dimensionality while conventional FS methods scale linearly or worse (ANOVA/MI ≈ 1.0, RFE ≈ 1.41). This is a concrete, verifiable empirical finding.

- **Automatic feature count without per-dataset tuning**: The cardinality penalty with λ=1 works across all 11 benchmark datasets without per-dataset tuning (Section 3.3). The RHS of Table 1 shows selected counts vary meaningfully by dataset (e.g., 3–5 for CH, 65–69 for AL), confirming the method actually learns the count rather than relying on a fixed budget.

- **Zero misselection errors on two corruption scenarios**: Figure 3a shows AutoNFS achieves zero misselection errors for random and corrupted features, meaning it perfectly identifies which features are spurious in those settings — a result no other method matches.

- **Large-scale real-world validation**: Table 2 shows results on 24 metagenomic datasets (original dims 308–718), where AutoNFS reduces to a mean of 41 features (7.7% of original) while improving average accuracy for both MLP (+0.8 pp) and RF (+1.2 pp) downstream classifiers, demonstrating generalization across classifier families.

## Weaknesses

### Major

- **Benchmark comparison is structurally asymmetric**: The paper explicitly acknowledges (line 204) that "all baseline methods select the same number of features as were in the initial representation (before corruption), whereas our method automatically chooses a much smaller subset." Baselines are constrained to a fixed feature count (the original pre-corruption dimensionality) while AutoNFS is free to drop features aggressively. This conflates selection quality with the freedom to select fewer features, making the headline ranking results (Figure 2: AutoNFS ranks 2.1–3.9 vs. next best 3.8–4.7) ambiguous evidence of superior selection quality. A fairer comparison would allow baselines to use their own selection criteria (e.g., Lasso's regularization path, STG's gates) and compare at matched sparsity levels.

- **Novelty relative to differentiable FS methods is not established**: The paper mentions Hard-Concrete gates (Louizos et al., 2017), Stochastic Gates/STG (Yamada et al., 2020b), Concrete Autoencoders (Balin et al., 2019), and INVASE (Yoon et al., 2018) in Related Work (line 36) but never compares against them experimentally. These are the most directly relevant baselines. The core mechanism — continuous relaxation of a discrete mask via Gumbel-Sigmoid — is mathematically equivalent to a 2-class Gumbel-Softmax (σ(a) = softmax([a, 0])₁). The cardinality penalty L_select = (1/D) Σ m_j is standard L0 regularization. The paper claims prior methods require specifying the number of features (lines 18, 22, 38), but STG and Hard-Concrete also use sparsity-inducing regularization that automatically determines feature count. Without head-to-head comparison against these methods, the claimed novelty over existing differentiable FS is unsubstantiated.

- **The "nearly constant" complexity claim lacks supporting architectural and measurement details**: The masking network f: ℝ^De → ℝ^D has a final layer with D output units whose computation scales as O(De·D) — linear in D, not constant. The paper does not specify the architecture of f (number of layers, hidden sizes, activations), the value of D_e, or what exactly is being timed in Figure 4 (full training vs. single forward/backward pass). Without these details, the empirical claim of α ≈ 0.08 cannot be properly evaluated or reproduced. The resolution of this tension (how a network with O(De·D) compute can show α ≈ 0.08) is critical to the paper's central scalability claim.

### Minor

- **No comparison against differentiable FS baselines**: Despite citing Hard-Concrete, STG, Concrete Autoencoder, and INVASE as the most related work, only LassoNet appears in the benchmark (ranked 5.8–7.7). STG, Hard-Concrete, and Concrete Autoencoder are absent. A direct comparison against these methods — allowing them to use their own selection mechanisms — would be the most informative evaluation.

- **No ablation studies**: The paper lacks ablations of (a) Gumbel-Sigmoid vs. straight-through Gumbel-Softmax vs. Hard-Concrete, (b) learned embedding + masking network vs. direct per-feature logits, and (c) sensitivity to the λ hyperparameter beyond what is presumably in the stripped appendix.

- **No variance or statistical significance for ranking results**: The rankings in Figure 2 are reported without error bars or significance tests. Given 11 datasets, a non-parametric test (e.g., Wilcoxon signed-rank) against the best competitor would strengthen the claims.

- **Metagenomic experiments lack FS baselines**: Table 2 compares AutoNFS-reduced data only to full data, not to other FS methods. This shows that fewer features do not hurt performance, but does not establish that AutoNFS is particularly effective relative to alternatives on this data.

- **Name inconsistency**: The method is called "AutoNFS" throughout the text but labeled "GFS-NetWork" in Figure 2 and its associated table.

### Trivial

- The embedding dimension D_e and masking network architecture details are not specified in the main text (presumably in the stripped appendix).
- The learning rates η₁ and η₂ in Algorithm 1 are listed without values.

## Nice-to-Haves

- A clearer explanation of how the masking network architecture achieves sub-linear scaling despite an O(De·D) final layer, distinguishing between per-iteration cost and total training cost.
- Reporting downstream task performance at matched sparsity levels would strengthen the selection quality claims.
- Comparisons on metagenomic data against other FS methods (even simple ones like Lasso or Mutual Information).

## Removed Points

These points are flagged to be removed, treat them with caution:
- **"The paper does not compare against LassoNet"** — REMOVED: LassoNet IS in Figure 2 (ranked 5.8–7.7).
- **"The predictive power interpretation is not justified"** — REMOVED: The interpretation that a large performance drop when removing a feature indicates individual importance is standard and reasonable.
- **"Missing related works"** — REMOVED per instructions (cannot verify without external sources).
- **"Reproducibility concerns about undisclosed hyperparameters"** — REMOVED per instructions (appendix stripped by parser).
- **"Writing/style nitpicks about the abstract overstating prior work limitations"** — REMOVED: common framing issue, not a scientific weakness.
- **"The number of selected features should have confidence intervals"** — REMOVED: not a standard expectation for this type of experiment.

## Novel Insights

The two reviews reveal a paper with genuine empirical findings (near-constant scaling, zero misselection, metagenomic validation) sitting on an unclear novelty foundation. The most critical gap is not in the method itself but in the evaluation design: the benchmark gives AutoNFS an asymmetric advantage by constraining baselines' feature count, and the paper omits the most directly comparable differentiable FS baselines (STG, Hard-Concrete). The complexity result (α ≈ 0.08) is the most novel empirical finding but requires architectural details to assess. The paper resembles RelChaNet (a neural FS paper scored 5.25 and rejected) in having interesting ideas but evaluation gaps that prevent the contribution from being clearly established.

## Suggestions

1. **Fix the benchmark**: Allow baselines to select their own number of features via their own mechanisms, or compare at matched sparsity levels.
2. **Add differentiable FS baselines**: Compare directly against STG, Hard-Concrete, and Concrete Autoencoder, allowing them to use their natural selection criteria.
3. **Add ablation studies**: Compare Gumbel-Sigmoid vs. Gumbel-Softmax vs. Hard-Concrete; learned embedding + masking network vs. direct per-feature logits; λ sensitivity.
4. **Clarify the complexity claim**: Provide the architecture of f, D_e values, and specify what Figure 4 measures. Explain how O(De·D) scaling yields α ≈ 0.08.
5. **Report significance**: Add confidence intervals or statistical tests for the ranking results.
6. **Unify naming**: Use "AutoNFS" consistently throughout all figures and tables.

## Score and Decision

**Calibration anchors used** (across all rounds):

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Feature selection neural estimation MI (lt6xKGGWov) | 2.33 | R1 (low) | Much weaker — fundamental flaws, far below AutoNFS |
| Gumbel-Softmax hardware control (m9BiWVTJDx) | 3.00 | R1 (low) | Much weaker — different domain, lower quality |
| MaskTab (Exkm5OReTY) | 3.25 | R1 (low) | Weaker — missing feature modeling, not comparable |
| RelChaNet (3M3jtMDjUb) | 5.25 | R1 (mid), R2 | Most comparable neural FS paper, same quality tier; AutoNFS has more data but weaker novelty differentiation |
| Neural Subset Selection (eepoE7iLpL) | 5.67 | R1 (mid) | Accepted but on different problem (set functions); more theory, less FS evaluation |
| Iterative Feature Space (xtTut5lisc) | 5.00 | R1 (mid), R2 | Comparable — similar evaluation gaps and clarity issues |
| difFOCI (KiN7g8mf9N) | 6.00 | R2 | Better — clearer novelty (making non-parametric method differentiable), cleaner evaluation; AutoNFS is below this |
| BiDST (qbw861vueP) | 4.33 | R2 | Worse — significant method clarity issues |
| Structured Matrices (pAVJKp3Dvn) | 5.67 | R2 | Accepted but different topic |
| Unsupervised FS dynamic (Ai4L058yoO) | 4.50 | R1 (mid), R2 | Worse — poor writing, missing baselines |

**Round 1 bracket**: 4.5–5.5 (between the 3.25 weak anchors and the 6.0 difFOCI anchor; most similar to RelChaNet at 5.25 and Iterative Feature Space at 5.00).

**Round 2 narrowing**: Closer to the 5.00–5.25 anchors than to the 6.0 difFOCI anchor. AutoNFS has broader experimentation than the 5.00/5.25 anchors but its novelty gap vs. existing differentiable FS methods is larger than RelChaNet's novelty gap vs. pruning methods. Net assessment: comparable to the 5.00–5.25 level.

**Final score**: 5.0 — The paper has genuine empirical findings and extensive evaluation, but the asymmetric benchmark comparison (which conflates selection quality with the freedom to drop features) and the lack of novelty differentiation from prior differentiable FS methods (STG, Hard-Concrete) are significant issues that prevent the core claims from being clearly supported. The paper would require substantial revisions — particularly fixing the benchmark comparison, adding direct differentiable FS baselines, and clarifying the complexity result — to be considered for acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>