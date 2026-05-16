Now I have a thorough understanding of both the paper and the reviews. Let me synthesize the consolidated review, carefully verifying each claim against the paper.

---

## Summary

This paper introduces Sparling, a method for learning extremely sparse intermediate representations (≥99% sparsity) from end-to-end supervision only. It uses a hard-thresholded ReLU (ReLU(z − t)) with quantile-based adaptive thresholding and an annealing schedule that reduces target density as validation accuracy improves. The method is evaluated on three domains (DigitCircle, LaTeX OCR, AudioMNIST) and shown to recover ground-truth latent motifs (e.g., digit positions) without any intermediate supervision. The core empirical contribution — that a hard threshold layer combined with accuracy-gated annealing enables stable training at extreme sparsity levels while recovering interpretable structure — is well-supported.

## Strengths

1. **Achieves extreme sparsity with low motif error across diverse domains.** On DigitCircle, Sparling reaches 0.005% density (99.995% sparsity, within 0.0005% of the theoretical maximum) while maintaining 98.84% motif accuracy. This is demonstrated across three domains with confidence intervals over 9 seeds (Figures 5, 7, Table 1). The contrast with baselines is clear: at comparable density levels, L₁ yields E2EE of 70%+ (error) and motif errors of 45–95%, while Sparling keeps all motif errors below ~10%.

2. **Recovers ground-truth motifs from end-to-end supervision alone.** Across three domains, Sparling's motif predictions align with true motifs: false positive error, false negative error, and confusion error are all below 10% except for fraction bars in LaTeX OCR (Figures 3, 4). Confusion matrices show that each ground-truth motif maps to a dedicated channel after permutation alignment, confirming structure discovery without intermediate labels.

3. **Ablations empirically validate both key design choices.** Removing batch normalization before the sparsity layer causes E2EE to rise to 71% (the model cannot learn the task). Starting at the target density (no annealing) yields E2EE of 68–71% (Section 5.3). These ablations demonstrate that both components are essential, not incremental.

4. **Rigorous evaluation metrics for motif identifiability.** The paper defines false positive error (FPE), false negative error (FNE), and confusion error (CE) with explicit handling of channel permutations and footprint alignment. This careful design allows precise, fair comparison and could serve as a template for future work on latent structure discovery.

5. **Demonstrates out-of-distribution generalization.** On AudioMNIST, the model is trained on speakers 1–51 and tested on speakers 52–60, still achieving low motif error (Figure 3). This confirms the learned motifs capture generalizable features rather than memorizing training-set artifacts.

6. **Reveals and leverages a sparsity–accuracy tradeoff.** Figure 5 shows that as sparsity increases during annealing, CE drops sharply while E2EE rises modestly. The adaptive algorithm exploits this by allowing post-hoc selection of a desired sparsity level based on validation accuracy.

## Weaknesses

### Fatal
None.

### Major

1. **The necessity assumption is used as a post-hoc explanation for high FNE on LaTeX OCR, but is never independently verified.** The paper attributes the high false-negative error on LaTeX (~25%) to fraction bars, parentheses, and plus signs being "unnecessary" for predicting the LaTeX code (Section 5.2, Figure 3 caption). This is a plausible explanation, but the paper provides no evidence — e.g., by removing those motifs from ground-truth annotations and confirming that end-to-end accuracy does not drop, or by modifying the task to make them necessary and showing Sparling then recovers them. As it stands, the reader cannot distinguish between a genuine limitation of the method and a genuine property of the task. Since Motif Identifiability is a central claim, this evidential gap weakens the paper's argument. The authors should either test the necessity assumption directly (e.g., construct a variant of the LaTeX task where parentheses are required) or explicitly document the non-necessary motifs as a known limitation and report motif accuracy only on the necessary subset.

2. **The information bound derivation (Section 2.4) is incomplete and does not connect to the method.** The derivation introduces η without definition (line 132: "$H(\mathcal M[i,c]) \leq H(B(\delta_{i,c})) + \eta \delta_{i,c}$"), presents a dangling fragment ("Then, let $\delta_{i,c}$" on line 129), and jumps to a final expression $SC(H(B(\delta)) + \eta\delta)$ without explaining how the per-channel terms aggregate or what governs η's value. Critically, this bound is never used to reason about why Sparling works, to set hyperparameters (e.g., choosing target density), or to inform experimental design. The section is presented as theoretical motivation but is too sloppy to serve that purpose and does not connect to the algorithm. It should be either fixed with a clear, self-contained derivation and linked to the method, or removed to avoid detracting from the empirical contribution.

### Minor

1. **Hyperparameter sensitivity is unexplored.** The three key hyperparameters (evaluation frequency $M=2\times10^5$, target accuracy decay rate $d_T=10^{-7}$, density reduction factor $\delta_{\text{update}}=0.75$) are reported without any sensitivity analysis. The algorithm's behavior may depend significantly on these values — e.g., reducing density too quickly could cause collapse, too slowly wastes compute. A small grid over even one parameter (e.g., varying $\delta_{\text{update}}$ from 0.5 to 0.95) would substantially strengthen claims of robustness.

2. **KL-divergence baseline results are only reported qualitatively.** The paper states the KL baseline was "unable to achieve a density below 0.1%" even with $\lambda=10^5$ and $3\times10^6$ steps, but provides no table of actual densities or errors. A complete table analogous to the L₁ results would be more informative and allow readers to assess whether KL might still be useful at intermediate sparsity levels.

3. **The L₁ baseline uses only fixed loss weights; annealing of the L₁ weight is not explored.** Since Sparling's key innovation is the annealing procedure for the sparsity constraint, a natural baseline would be L₁ with an annealing schedule on its weight. The paper does not test this, making the comparison less informative about whether the *hard threshold* or the *annealing* drives the performance gap.

4. **L₁ baseline results lack confidence intervals.** Table 1 reports only point estimates for L₁ runs (presumably single seed), while Sparling results include 95% bootstrap confidence intervals over 9 seeds. For fairness, baselines should be run with multiple seeds and reported with comparable intervals.

### Trivial
- The variable η in Section 2.4 is undefined (this is a specific instance of the Major weakness #2 above, listed separately only for precision).

## Nice-to-Haves
- A controlled test of the necessity assumption on the LaTeX domain (e.g., modify the output generation to force parentheses to be necessary, then verify Sparling recovers them).
- An ablation where the initial density is set to a moderate value (e.g., 1% or 0.1%) and held constant throughout training, as a cleaner test of whether annealing is necessary versus simply starting with a reasonable density.
- Sensitivity analysis for the three key hyperparameters ($M$, $d_T$, $\delta_{\text{update}}$).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Mischaracterization of the L₁ baseline — the paper claims extreme sparsity is unachievable by other methods, but L₁ λ=2 achieves 99.977% sparsity with 70% accuracy."** REMOVED because the critic misread E2EE (edit distance error) as accuracy. The paper defines E2EE as error (line 93–95); at λ=2, L₁ has 70.31% error → ~29.7% accuracy, which IS below 50%. The paper's claim that alternatives "either do not produce extreme sparsity or have accuracy below 50%" (line 33–34) is factually supported by its own data. The specific framing that Sparling achieves "levels of activation sparsity unachievable using other techniques" (abstract) refers to its exact density (0.005%), which L₁'s best (0.023%) does not match — though the phrasing could be clearer.

2. **"End-to-End Error (Figure 12): Retrained does not close the gap and has higher error than Sparling itself."** REMOVED because the paper's text (Section 5.4) states Retrained "tends to perform similarly to or only slightly worse than the Non-Sparse setting," meaning Retrained ≈ Non-Sparse (lowest error) < Sparling (higher error). This description is internally consistent and supports the claim that Retrained "makes up most of the gap." Without the figure data, the critic's contrary claim is unverifiable and appears to be a misreading.

3. **"The paper should also cover Y / domain Z / additional tasks."** REMOVED as scope creep — the paper demonstrates its method on three diverse domains, which is sufficient for a methods paper.

4. **Missing appendix, missing proofs, formatting/style nitpicks.** REMOVED per instructions (parser artifacts or out-of-scope demands).

5. **Generic strengths from Strength Finder** (e.g., "addresses an important problem," "targets an interesting question") were dropped as they lack specific citation or concrete content.

## Novel Insights

The most interesting insight emerging from these reviews is about the specificity of Sparling's contribution: the paper's true value lies not in achieving extreme sparsity *per se* (L₁ can also reach >99.9% sparsity, as the data show), but in demonstrating that a *hard threshold combined with accuracy-gated annealing* yields a representation that is simultaneously sparse *and* interpretable (low motif error), whereas soft penalties like L₁ achieve comparable sparsity only at the cost of motif collapse (FPE >90%, CE >45%). The key differentiator appears to be that the hard threshold forces the model to make discrete "commitments" about which channels fire, and annealing prevents the optimization from getting stuck in poor local minima. This suggests a more general principle: for discovering latent discrete structure, hard architectural constraints + annealing may be systematically preferable to soft regularization, even when both achieve similar sparsity levels.

## Suggestions

1. Test the necessity assumption on LaTeX OCR: create a variant of the task where parentheses or plus signs are required for correct output generation, then verify whether Sparling recovers them. Alternatively, report motif accuracy separately on the "necessary" subset of motifs and explicitly document non-necessary motifs as a limitation.

2. Either repair the information bound derivation with a clear, self-contained chain of inequalities and a concrete connection to method design, or remove it. As written, it adds no value.

3. Add a sensitivity study for the three key hyperparameters ($M$, $d_T$, $\delta_{\text{update}}$), even a small grid over one parameter.

4. Report KL baseline results in a complete table, and run L₁ baselines with multiple seeds and confidence intervals.

## Score and Decision

This paper makes a real empirical contribution — a practical algorithm for learning extremely sparse, interpretable intermediate representations from end-to-end supervision — and supports it with careful experiments across diverse domains, rigorous evaluation metrics, and ablations that validate design choices. The main weaknesses (unverified necessity assumption, sloppy theory section, missing sensitivity analysis) are genuine but fixable and do not undermine the core empirical findings. The paper is a solid methods contribution with clearly demonstrated value.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>