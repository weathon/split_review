Now I have a thorough understanding of the paper and both reviews. Let me produce the consolidated review.

## Summary

FoRDE proposes a particle-based variational inference (ParVI) method for neural network ensembles that performs repulsion in the space of first-order input gradients rather than in weight or function space. The method uses an RBF kernel on unit-normalized input gradients with a PCA-derived lengthscale matrix that sets stronger repulsion along high-variance data directions. Experiments on CIFAR-10/100-C, TinyImageNet-C, and transfer learning show that FoRDE-PCA achieves substantial gains in corrupted accuracy (+1.3% on CIFAR-100-C, +2.4% on CIFAR-10-C over the next-best method) while maintaining competitive clean-data performance.

## Strengths

1. **Consistent and substantial gains under covariate shift.** FoRDE-PCA achieves the best corrupted accuracy, NLL, and ECE on both CIFAR-100-C (Table 1) and CIFAR-10-C (Table 2), with clear margins over DE, weight/function/feature-RDE, LIT, SWAG, and node-BNNs. These results directly support the core claim that input-gradient repulsion with PCA-derived lengthscales improves robustness to perturbations.

2. **Principled, data-dependent kernel design.** The PCA-based kernel (Section 3.3, Eq. 5) sets inverse lengthscales to the eigenvalues of the training-data covariance, connecting FoRDE to the EmpCov prior while embedding data-manifold structure into the repulsion term. Table 3 shows that FoRDE-PCA outperforms all methods even when baselines use the EmpCov prior, isolating the additive benefit of gradient-space repulsion beyond the prior alone.

3. **Evidence that FoRDE avoids the underfitting problem of function-space repulsion.** The 1D regression and 2D classification illustrations (Section 5.1, Figures 1–2 descriptions) show that FoRDE yields higher predictive uncertainty in out-of-distribution regions than DE, weight-RDE, and function-RDE, directly addressing the known limitation of function-space methods that underfit when functions are compared only on training inputs.

4. **Superior transfer learning results.** The transfer learning experiment (Figure 3) using Vision Transformer features shows FoRDE outperforming DE, weight-RDE, and function-RDE on both in-distribution and shifted test sets across CIFAR-10, CIFAR-100, CINIC-10, and CIFAR-10/100-C, demonstrating the method's applicability beyond the main benchmark.

5. **Honest complexity analysis.** Section 3.4 provides concrete runtime numbers (101 vs. 31 sec/epoch for ResNet18/CIFAR-100), allowing a clear cost–benefit assessment of the ~3× training overhead.

## Weaknesses

### Fatal
None.

### Major

- **Acknowledged but unanalyzed bias in the stochastic repulsion gradient.** The paper explicitly states (line 208) that the mini-batch approximation of the kernel inside the logarithm leads to biased stochastic gradients of the repulsion term. This means the update no longer corresponds to a proper Wasserstein gradient flow of KL divergence with respect to the target posterior, weakening the claimed ParVI foundation. The paper merely notes "we found no convergence issues" without any theoretical analysis (e.g., bounding the bias) or empirical verification (e.g., comparing full-batch vs. mini-batch repulsion on a small-scale problem). While the empirical results stand on their own, the method's grounding in the ParVI framework is compromised, and readers cannot assess whether the bias meaningfully affects the dynamics or the final ensemble quality. This is a significant gap for a paper that presents itself as a methodological contribution.

### Minor

- **No diagnostics on gradient-normalization stability.** The base kernel normalizes input gradients to unit vectors (line 158). The authors motivate this correctly—gradient norms approach zero as the softmax saturates at convergence. However, normalizing near-zero gradients can amplify numerical noise, potentially making the repulsion signal erratic in later training stages. The paper provides no analysis of when or how often this occurs, nor any comparison of normalized vs. unnormalized gradients (e.g., tracking gradient norms and repulsion magnitudes during training). A simple diagnostic plot would clarify whether this is a practical concern.

- **Transfer learning figure appears to lack error bars.** Figure 3 (described in Section 5.3) reports transfer learning results averaged over 5 seeds, but the figure caption comments out the mention of error bars ("%Each result is averaged over 5 seeds"). If the bar plots do not include standard deviations or confidence intervals, the significance of the claimed improvements cannot be assessed.

- **Interaction between PCA lengthscales and the median heuristic is not empirically examined.** The median heuristic (line 214) introduces a global bandwidth that adapts to pairwise distances in the PCA-transformed space. If eigenvalues vary widely, distances along high-variance dimensions may dominate, causing the median heuristic to set a large global bandwidth that dilutes repulsion in important directions. The paper argues this is "avoided in practice" (line 187) but provides no empirical check (e.g., comparing effective lengthscales with and without the median heuristic). A brief ablation would strengthen confidence in the kernel design.

### Trivial
None.

## Nice-to-Haves

- **Full-batch vs. mini-batch comparison on a small problem.** Running a small-scale experiment (e.g., 2D classification or a UCI regression task) that compares the full-batch and mini-batch repulsion updates would either confirm the bias is negligible or reveal its impact. This would clarify the method's relationship to ParVI.

- **Ablation of gradient normalization.** Comparing FoRDE with and without normalization (using unnormalized gradients in the RBF kernel) would isolate whether the method's success depends on direction-only repulsion or also on gradient magnitudes.

- **Impact of ensemble size.** All main experiments use 10 ensemble members. Showing that FoRDE's advantage holds for smaller ensembles (e.g., 5 members) would increase the practical applicability.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **FoRDE-Tuned tuning protocol and potential data leakage (Harsh Critic's issue #3):** The paper states "Details on lengthscale tuning are presented in \cref{sec:tuning_lengthscales}" — this appendix section was stripped by the PDF parser. Per policy, weaknesses about content in the missing appendix are removed; the details exist in the original submission.

2. **"Up to translation" phrasing imprecision:** The claim that input gradients "uniquely characterize a function up to translation" is a standard mathematical fact for smooth functions on a connected domain (neural networks with smooth activations). This does not require additional qualification for the paper's purposes.

3. **Equation (5) "double approximation":** This criticism is effectively the same as the mini-batch bias concern (merged into the Major weakness above). No separate point needed.

4. **Baseline hyperparameter selection:** The paper references \cref{sec:image_exp_details} for experimental details — content removed by the parser. Per policy, this criticism is removed.

## Novel Insights

None beyond the paper's own contributions. The two reviews converge on the same core tension: the paper presents a well-motivated, empirically effective method whose theoretical framing (ParVI) is weakened by an acknowledged but unexamined gradient bias. Neither reviewer identifies a flaw that invalidates the empirical results, and both recognize the contribution as significant if the gaps are addressed.

## Suggestions

1. **Address the mini-batch bias head-on.** The paper should either (a) provide a theoretical bound on the bias magnitude, (b) present an empirical comparison of full-batch vs. mini-batch repulsion on a small problem, or (c) reframe the method as a heuristic inspired by ParVI rather than an instance of it, then evaluate it on that basis.

2. **Add diagnostic plots.** Include a figure showing the distribution of gradient norms across training epochs and a comparison of repulsion magnitudes with normalized vs. unnormalized gradients. This would directly address the normalization instability concern.

3. **Add error bars to the transfer learning figure.** Include standard deviations or confidence intervals for the bar plots in Figure 3, since results are averaged over 5 seeds.

4. **Add an empirical check on the PCA+median heuristic interaction.** Show that the effective lengthscales after the median heuristic retain the desired PCA-induced anisotropy (e.g., by visualizing pairwise distances before and after the median heuristic scaling).

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>