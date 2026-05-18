Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper provides a theoretical and experimental comparison of Kolmogorov-Arnold Networks (KANs) and multi-layer perceptrons (MLPs), focusing on two axes: (1) expressiveness via representation theorems and approximation rates, and (2) spectral bias in training dynamics. The paper proves that MLPs can be exactly represented by KANs of comparable size (and vice versa with a width penalty proportional to grid size), derives optimal approximation rates for KANs on Sobolev spaces, and analyzes the spectral bias of single-layer KANs by showing their Hessian is well-conditioned (condition number bounded by a constant times input dimension, independent of grid size). Experiments on 1D frequency fitting, Gaussian random fields, and a Poisson PDE demonstrate that KANs learn high-frequency components substantially faster than MLPs, even when MLPs are given more parameters and more training iterations.

## Strengths

1. **Novel representation theorems (Theorem 1 and Theorem 2).** The paper proves that any ReLU$^k$ MLP can be exactly represented by a KAN of depth at most $2L$ and grid size 2 (Theorem 1), establishing that KANs are at least as expressive as MLPs. Conversely, Theorem 2 shows that KANs (without SiLU) can be represented by MLPs with a width penalty of $O(G)$, suggesting KANs with large grids may be more parameter-efficient for certain functions. These are clean, rigorous results that directly support the paper's expressiveness claims.

2. **First theoretical analysis of spectral bias in KANs (Theorem 3).** The paper proves that the Hessian of a single-layer KAN's least-squares loss has eigenvalue ratio bounded by $Cd$ (independent of grid size $G$), in contrast to the $n^4$ scaling for two-layer ReLU MLPs. This is the first formal result explaining why KANs may not exhibit the strong low-frequency bias of MLPs, and it provides a rigorous starting point for understanding KAN training dynamics.

3. **Compelling experimental demonstration of reduced spectral bias.** The 1D frequency fitting experiment (Figures 1–2) is particularly striking: KANs with sufficient depth and grid size learn all frequencies nearly simultaneously, while MLPs with 10× more parameters and 10× more training iterations still fail on high-frequency components. The GRF and PDE experiments extend this finding to higher dimensions and more realistic tasks, with the GRF experiments showing that KANs outperform MLPs on rough (high-frequency) functions while MLPs remain competitive on smooth functions.

4. **Approximation rates for KANs on Sobolev spaces (Corollary 1).** By combining the MLP-to-KAN representation theorem with existing results for ReLU networks, the paper derives optimal approximation rates $O(L^{-2s/d})$ for very deep KANs on Sobolev spaces. This extends the theoretical foundation for KANs beyond the compositionally smooth functions covered by the original KAT theorem.

5. **Systematic investigation of hyperparameter effects and the overfitting trade-off.** The experiments vary depth, width, and grid size, providing practical guidance (larger grids for rough functions, shallower nets for smooth functions). Section 4.3 explicitly demonstrates that KANs' reduced spectral bias leads to overfitting on noisy data, and that increasing training samples alleviates this—a nuanced finding that acknowledges the trade-off rather than overselling KANs.

## Weaknesses

### Major

1. **Gap between the spectral bias theory and the experiments.** The theoretical analysis (Section 4.1) is limited to a single-layer KAN, which is a linear model. The experiments, however, use deeper KANs (depth 2–4) with grid extension. The paper explicitly acknowledges this limitation (lines 20, 155, 431), stating the analysis is "necessarily highly simplified and heuristic" and that "future work includes developing theory which can describe the training of deeper KANs." Nonetheless, the framing in the abstract ("we demonstrate that KANs are less biased toward low frequencies than MLPs") and the conclusion overstate what the theory actually proves. The theory shows that a *single-layer* KAN's Hessian is well-conditioned—it does not formally establish that *deep* KANs inherit this property, nor does it connect the B-spline Gram matrix eigenvectors to Fourier frequency modes. The empirical results are convincing on their own, but the theoretical claim about deep KANs remains a conjecture supported by heuristic intuition and experimental evidence, not by the mathematical analysis presented. The authors should recalibrate the theoretical claim to explicitly state what is proven (shallow case) and what is conjectured (deep case).

### Minor

2. **Disconnect between the two halves of the paper.** The representation/approximation theorems (Section 3) and the spectral bias analysis (Section 4) are presented as separate contributions that do not reinforce each other. The representation theorems show KANs and MLPs can represent each other, which would suggest *similar* training dynamics if architecture alone determined spectral bias. But the spectral bias experiments show *different* training dynamics. The paper never reconciles this tension—e.g., by arguing that the B-spline parameterization (rather than the function class) drives the difference. This makes the paper read as two independent studies rather than a unified argument. While having two contributions is not a flaw per se, the lack of integration weakens the narrative.

3. **No formal connection between Hessian conditioning and Fourier-frequency learning.** Theorem 3 bounds the condition number of the Hessian in parameter space, showing gradient descent converges at roughly equal rates in all parameter-space directions. The experiments then measure frequency-domain learning (Fourier coefficients of the learned function). The paper implicitly equates "all parameter-space directions converge equally" with "all frequency components are learned equally," but does not establish this bridge formally. This is a conceptual gap, though the experimental results (particularly the 1D Fourier plots) provide strong empirical evidence that the connection holds in practice.

### Trivial

4. **Limited scope of the PDE experiment.** The Poisson equation experiment is 1D with a single high-frequency parameter sweep. While clean and reproducible, this is a simple setting; the paper would benefit from at least one higher-dimensional PDE or more complex problem to strengthen the practical relevance claim.

## Nice-to-Haves

- A parameter-matched and training-budget-matched comparison in the 1D setting (width/grid-size sweep where KAN and MLP have comparable total parameters) would further isolate the architectural advantage. Currently the asymmetry favors the MLP (more parameters, more iterations), which makes the KAN's advantage *stronger* evidence, but a matched comparison would silence concerns cleanly.
- The grid extension technique is highlighted as practically important but receives no theoretical treatment. A brief intuitive explanation of why multi-grid training helps high-frequency learning (beyond what the static-grid analysis already shows) would strengthen the practical narrative.
- A direct measurement of the empirical NTK or Hessian eigenvalues for deeper KANs (depth 2–3) compared to MLPs would bridge the theory-experiment gap, though this is a substantial additional experiment.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"The experimental comparisons are not controlled... asymmetry in capacity, training budget, and optimizer (L-BFGS vs. ADAM in some cases)"* — **Removed per hard rule**: the asymmetry favors the baseline MLP (more parameters, more iterations), making the KAN's advantage a stronger result. In the GRF and PDE experiments, both models use the same optimizer (LBFGS) with comparable iteration counts (500 vs. 500 for GRF; 200 vs. 200 for PDE). The claim about optimizer asymmetry is factually incorrect.
- *"But MLPs with one hidden layer are also linear models in a lifted feature space... The paper does not address why the KAN case is fundamentally different beyond the condition number bound"* — **Removed**: the paper explicitly addresses this by contrasting the KAN's Hessian condition number ($Cd$, independent of grid size) with the two-layer ReLU MLP's condition number ($n^4$) in line 151. The condition number bound IS the difference.
- *"A discussion of the computational cost of evaluating B-spline activation functions versus ReLU activations"* — **Removed per hard rule**: this is a nice-to-have, not a weakness.
- *"The GRF plots and PDE plots are difficult to read... subfigure captions are partially garbled"* — **Removed per hard rule**: parser-induced formatting artifacts.
- *"Missing related works"* — **Removed per hard rule**: cannot confirm without external sources.
- *"Missing appendix, missing proofs in appendix"* — **Removed per hard rule**: parser strips appendices; they exist in the original submission.

## Novel Insights

The most interesting observation emerging from the reviews is the inherent tension between the two halves of the paper. The representation theorems (Section 3) show that KANs and MLPs can represent each other with bounded overhead—suggesting their *function classes* are similar. Yet the spectral bias experiments (Section 4) show dramatic differences in *training dynamics*. This tension implies that the advantage of KANs lies primarily in optimization/inductive bias rather than representation capacity. The paper would benefit from explicitly framing the narrative around this distinction: KANs do not necessarily represent more functions, but they learn different functions first. The well-conditioned Hessian of the shallow KAN is a first step toward formalizing this, but a deeper theoretical account of why the B-spline basis yields better conditioning than the ReLU basis in the NTK regime remains an open problem that the paper surfaces but does not resolve.

## Suggestions

1. **Recalibrate the theoretical claims.** Rewrite the abstract, introduction, and conclusion to clearly distinguish what is proved (shallow KANs have a well-conditioned Hessian, suggesting reduced spectral bias) from what is observed experimentally (deep KANs exhibit reduced spectral bias across several tasks). The phrase "we demonstrate that KANs are less biased toward low frequencies than MLPs" is acceptable for the empirical finding but should not be presented as a proven theoretical result for deep KANs.

2. **Add at least one controlled comparison with matched parameter counts.** While the current asymmetry (MLP advantaged) makes the results stronger, a cleaner comparison where both models have similar total parameters and training budgets would eliminate a persistent source of reader skepticism. The 1D setting is simple enough to do this cleanly.

3. **Acknowledge the spectral bias theory explicitly as a shallow-KAN result in the title or section header.** The current section title is "Spectral bias theory for shallow KANs," which is appropriate, but the abstract and introduction should more prominently signal that the theory covers the shallow case while the experiments extend to the deep case.

## Score and Decision

The paper makes genuine contributions: first rigorous spectral bias analysis for KANs, novel representation theorems, new approximation rates, and compelling empirical evidence. The main weakness—the gap between shallow theory and deep experiments—is acknowledged by the authors and does not invalidate the empirical findings, which stand on their own. The paper is publishable with revisions to recalibrate the strength of the theoretical claims.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>