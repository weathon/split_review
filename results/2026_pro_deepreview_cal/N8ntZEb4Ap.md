Now I have all the information I need. Let me compile the final review.

---

## Summary

AutoNFS proposes a differentiable neural feature selection method that combines a Gumbel-Sigmoid masking network with a task predictor, trained end-to-end with a sparsity penalty (\(\mathcal{L}_{\text{select}} = \frac{1}{D}\sum m_j\)) that encourages the model to use fewer features. The method is evaluated on the Cherepanova et al. benchmark (11 datasets, 3 corruption scenarios) and 24 metagenomic datasets, where it achieves the best average rank among 11 methods while selecting substantially fewer features than competitors.

## Strengths

- **Strong empirical performance on a well-established benchmark:** AutoNFS achieves the best average rank across all three corruption scenarios in the Cherepanova et al. benchmark (Figure 2: average rank 2.1 for corrupted, 3.9 for random, 3.6 for second-order features), with zero misselection errors in two of three scenarios (Figure 3a). This is a concrete, well-measured result on a recognized evaluation framework.

- **Effective feature reduction while maintaining accuracy:** Across the 11 benchmark datasets, AutoNFS selects a small fraction of the total features (Table 1 RHS, e.g., 65/128 for ALOI, 5/8 for California) without compromising downstream performance. In the metagenomic analysis (Table 2), it reduces features to 7.7% of the original on average while improving MLP accuracy by 0.7 pp and RF accuracy by 1.2 pp.

- **Clean end-to-end differentiable design:** The method is straightforward and well-described: a masking network with Gumbel-Sigmoid relaxation, temperature annealing, and a simple mask-sum penalty — all trained jointly with the downstream task. This makes the method easy to understand, implement, and adapt.

- **Broad evaluation across domains:** The paper evaluates on 11 standard tabular benchmarks (classification and regression), 24 real-world metagenomic datasets, and includes analysis of feature importance (Figure 3b), misselection rates, and downstream classifier transferability (MLP and RF).

## Weaknesses

### Fatal

None.

### Major

- **Missing comparisons with directly comparable differentiable feature selection methods.** The paper cites Stochastic Gates (STG; Yamada et al. 2020), Concrete Autoencoders (Balin et al. 2019), and \(L_0\) regularization with Hard-Concrete gates (Louizos et al. 2017) in Related Work (Section 2), and correctly positions AutoNFS within this differentiable FS literature. Yet none of these methods appear as baselines in the experiments. STG and Concrete Autoencoders also use continuous relaxations of discrete masks trained end-to-end with sparsity penalties — making them the most natural comparators for AutoNFS. The baselines actually used (Lasso, LassoNet, Deep Lasso, tree-based methods) are relevant but do not represent the differentiable-relaxation paradigm that AutoNFS belongs to. This gap weakens the central empirical claim that AutoNFS advances the state of the art in differentiable FS specifically, rather than just performing well against traditional methods.

- **Overstated claim of "minimal" feature selection.** The paper repeatedly claims that AutoNFS "automatically determines the minimal set of features" (abstract, Section 1, contributions, conclusion). In reality, the method uses a standard sparsity-inducing penalty \(\mathcal{L}_{\text{select}} = \frac{1}{D}\sum_j m_j\) with \(\lambda = 1\). This encourages sparsity but provides no guarantee of minimality — the resulting feature count depends on the interplay between data, task loss, and \(\lambda\). The fact that \(\lambda=1\) "gives satisfactory results across datasets" is a practical convenience, not evidence of minimality. Figure 3b does show that removing any selected feature degrades performance (average drop of 0.313), which suggests the selected sets are *tight*, but this is a post-hoc check, not an automatic determination. The paper also concedes in Section 3.5 that features "can be ranked by their logit values when a specific top-\(k\) selection is desired," implicitly acknowledging that a user-defined budget may be needed. The framing of the method as automatically discovering the minimal set inflates the contribution beyond what the method's mechanism and experiments actually support.

- **Insufficiently supported computational complexity claims.** Section 4.3 reports a near-constant empirical scaling exponent \(\alpha \approx 0.08\) and claims this represents "a significant algorithmic advancement." However, the masking network outputs a \(D\)-dimensional vector, and any non-trivial architecture has at least \(\mathcal{O}(D)\) operations in its output layer. An exponent of 0.08 is therefore implausible as an algorithmic property and likely reflects fixed overheads dominating the measurement at the tested dimensionalities. The paper provides no description of the experimental setup for this analysis — what dataset was used, how features were generated, what hardware, what range of \(D\) was tested, how the masking network was configured across different \(D\) values. Without these details, the complexity claim is not credible as presented and could mislead readers about the method's scalability.

### Minor

- **Ambiguity about the downstream evaluation protocol.** The paper states "All methods use MLP as a downstream classifier" (Section 4.1). However, AutoNFS's task network \(g\) is trained jointly with the mask, while traditional FS baselines have their features selected first and then train a separate classifier. If the reported AutoNFS performance uses the jointly-trained \(g\) while baselines use separately-trained MLPs, the comparison is not strictly like-for-like. The paper notes it follows the Cherepanova et al. benchmark protocol, but clarifying whether the jointly-trained \(g\) or a freshly-trained MLP was used for AutoNFS evaluation would strengthen confidence in the comparison.

- **The masking network uses a fixed random embedding \(e\) mapped through a network \(f_\phi\) to produce logits \(w\), but the paper does not discuss why this parameterization is preferable to directly learning a vector \(w \in \mathbb{R}^D\).** Since \(e\) is not data-dependent, the network could be replaced by a directly learned weight vector without losing expressiveness (the network may provide implicit regularization, but this is not discussed). This is not a flaw in the method but an underexplored design choice.

- **Temperature annealing is not ablated.** The decay schedule (\(\alpha = 0.997\)) is stated but its necessity relative to simpler alternatives (e.g., a fixed low temperature) is not explored. This limits understanding of which components of the method are essential.

### Trivial

- **Naming inconsistency:** The method is called "AutoNFS" in the text but labeled "GFS-NetWork" in Figures 2 and 4 (and "GFSNetwork" in Figure 4b). This should be unified.

## Nice-to-Haves

- A sensitivity analysis for \(\lambda\) — currently \(\lambda=1\) is presented as universal, but understanding the stability range would strengthen the "no tuning required" claim.
- Discussion of limitations of a global mask: correlated features with overlapping information are not explicitly handled, and instance-level feature importance is not captured.
- Comparison with other neural FS methods (LassoNet, STG) in the complexity analysis would make the scaling claims more meaningful.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Harsh critic's claim that the complexity analysis is "not credible" as a fatal flaw:** Demoted to Major. The analysis is insufficiently described but not provably false. The empirical observation could be explained by constant-factor dominance rather than being fabricated.
- **Harsh critic's suggestion that the masking network parameterization is redundant:** This is a design observation, not a weakness. Moved to Minor.
- **Harsh critic's criticism of "some datasets show large drops in accuracy (e.g., FengQ_2015, ThomasAM_2018a)" in metagenomic results:** REMOVED. Examining Table 2, FengQ_2015 shows MLP drops from 0.662 to 0.607 but RF improves from 0.833 to 0.889 — the pattern is mixed, not universally large drops. The paper acknowledges variation by reporting averages. Not a substantive weakness.
- **Strength Finder's claim of "near-constant computational scaling" as a core strength:** Demoted. The evidence for this claim is insufficiently supported (see Major weakness above).
- **Strength Finder's claim of "automatic determination of a minimal feature subset":** Qualified. The method does automatically determine the number of features, but "minimal" is overstated.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations largely confirm and clarify issues already present in the paper rather than generating genuinely new insights about the problem domain or methodology.

## Suggestions

- Add STG (Yamada et al. 2020) and/or Concrete Autoencoders (Balin et al. 2019) as baselines in the Cherepanova benchmark comparison. These are the most directly comparable methods and their inclusion would substantially strengthen the empirical contribution.
- Replace "automatically determines the minimal set" with precise language throughout: the model *learns a sparse subset under the chosen regularizer*, and the number of features is a *byproduct of optimization*, not a provably minimal set. Frame Figure 3b as evidence of *parsimony* or *tightness* rather than minimality.
- Either provide a detailed description of the complexity experiment setup (dataset, dimensionality range, hardware, masking network architecture at each \(D\)) and acknowledge the linear component, or remove the strong "near-constant time" claim and reframe the finding as "competitive empirical runtime."
- Clarify whether AutoNFS's reported performance in Section 4.1 uses the jointly-trained task network \(g\) or a separately-trained MLP, and ensure comparability with baselines.

## Score and Decision

**Calibration summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|-----------|
| MINERVA (lt6xKGGWov) | 2.33 | R1 | AutoNFS is far stronger — comprehensive experiments vs. synthetic-only |
| DDS unsupervised FS (Ai4L058yoO) | 4.50 | R1 | AutoNFS is stronger — clearer writing, more rigorous evaluation |
| RelChaNet (3M3jtMDjUb) | 5.25 | R2 | AutoNFS is somewhat stronger — better organized, more comprehensive benchmarks, but both have significant weaknesses |
| difFOCI (KiN7g8mf9N) | 6.00 | R2 | difFOCI is stronger — better theoretical grounding, cleaner motivation, though narrower experiments. AutoNFS has broader evaluation but more significant weaknesses (overclaiming, missing baselines) |
| TabR (rhgIgTSSxW) | 5.75 | R2 | TabR is somewhat stronger — breakthrough tabular DL results; AutoNFS has value but weaker evidence for core claims |
| GRANDE (XEFWBxi075) | 6.50 | R2 | GRANDE is stronger — more technically novel, accepted with higher scores |

**Round 1 bracket:** 4.0–7.0  
**Round 2 narrowed to:** 5.0–6.0

AutoNFS sits between RelChaNet (5.25) and difFOCI (6.00). The method is cleanly described and evaluated on comprehensive benchmarks with strong results, but the overclaiming of "minimal" feature selection, missing comparisons with directly comparable differentiable FS methods, and insufficiently supported complexity claims pull it below the acceptance threshold. These are addressable issues, but they materially weaken the paper's central narrative in its current form.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>