- Decision: Reject
- Scores: 3, 5, 5, 5

## Merged Review

### Summary
The paper compares unsupervised feature selection and unsupervised feature extraction for dimensionality reduction. It proposes a dynamic feature selection method (DDS) that uses a neural network to predict, for each sample, which features are useful via a reconstruction loss. The architecture separates weighting and indicator matrices and introduces training-stabilization tricks.

### Strengths
- The comparison of unsupervised feature selection versus extraction provides an interesting viewpoint that could be valuable for practitioners.
- The DDS network selects features per sample and is jointly optimized with a task model (e.g., autoencoder); the separation of weight and indicator matrices and the two training tricks are useful contributions.
- The problem of dynamic feature selection in an unsupervised context is novel and potentially impactful. Spatial information is preserved, allowing easy interpretation of selected features.
- The paper is well-written (Reviewer 3) with a logical structure; experiments cover data comparison and clustering, demonstrating model performance on MNIST and CIFAR-10.

### Weaknesses
**Writing and presentation**
- The paper is not well written; many phrasings are unclear and need improvement. Most of the paper is in future tense (e.g., “will be tested” instead of “was tested”). There are typos and missing punctuation after equations. (Reviewer 1; also noted by Reviewer 4: “writing unclear in places.”)

**Related work and comparisons missing or incomplete**
- Dynamic/local feature selection has been studied in supervised learning; the paper cites L2X and INVASE but misses LSPIN (Yang et al. 2022). Since differences are subtle, the method should be compared with LSPIN using an autoencoder architecture and regression loss (MSE).
- The claim “first attempt to provide DFS for unsupervised scenarios” is incorrect: [2] Nunes et al. 2016 and [3] Svirsky et al. 2023 provide unsupervised dynamic feature selection (for classification/clustering). These are missing.
- DDS architecture is essentially a hypernetwork; hypernetwork literature citations are missing.
- Section 2 lists L2X as a feature selection method, but L2X is primarily an explainability method. A clear distinction between explainability (post-training) and feature selection (preventing overfitting) should be made.
- The comprehensive study of DFS claimed in Section 1 is not shown; only three methods are briefly discussed.

**Method description and technical issues**
- Equation (4) is not a recursive function from a mathematical perspective; tilde{g} is not a set, and T(i)_{n+1} is defined in terms of itself. The function f just below is unused. (Reviewers 2, 4)
- How the top-M procedure in equation (4) is differentiable is unclear. Also, keeping top-M features and using both a Concrete layer and L0 regularization seems redundant; an ablation study is needed to justify each component.
- The Concrete gate is not properly described in Eqs. 3 and 5. In the Hard Concrete distribution, injected noise must be included (see Louizos et al. ICLR 2018). Equation (5) has a sum with no index. Equation (6) introduces noise, contradicting the earlier equations. (Reviewer 1)
- There is contradictory explanation about tau (rho). Reviewer 2 notes equation (1) and the explanation of how tau(x) should be used need clarification.
- The decaying factor (alpha) is not clearly motivated, and its effect is not demonstrated. All hyperparameters (e.g., regularization weight, decay rates) are not explained; it is questionable that the regularizer is the same for all datasets. (Reviewers 1, 4)
- Section 3.2.1 introduces an alternative distribution but its effect is never evaluated (Reviewer 4).
- Autoencoder in equation (1) aims to reconstruct the whole input from selected features; whether this recovery is reasonable when many features are noisy is questionable (Reviewer 2).

**Evaluation and experimental concerns**
- Feature selection is most relevant for high-dimensional tabular data (N < D). Images are less appropriate because individual pixels have no universal meaning, there is little practical value in sampling fewer pixels, and MNIST is notably sparse. The method is not evaluated on tabular data, and there is no controlled experiment demonstrating that informative features are identified while nuisance features are attenuated. (Reviewer 1; Reviewer 3 agrees MNIST sparsity may favor DDS.)
- Baseline clustering methods are self-supervised requiring image augmentations, not truly unsupervised, and are image-specific. The main benefit of unsupervised feature selection (improving clustering) is typically shown on high-dimensional low-sample tabular data.
- Table 1 shows TCL works better than IMC-SwAV, which contradicts the discussion in Section 4.2. (Reviewer 2)
- In Figures 2 and 3 the DDS is implemented with U-Net using residual links, while the baseline is a naïve U-Net without them; reported improvements may be due to residual links rather than the DDS selection module. (Reviewer 2)
- DDS with 10% selected features suffers significant performance degradation compared to DDS with full features and IMC-SwAV; comparing with models four years old is unfair, and the degraded clustering performance shows that DDS with few features hurts. (Reviewer 2)
- Figure 4(a) shows selected features that appear strange: the left-hand border of the image (all black pixels) is selected, suggesting selection of non-informative features. More samples (digits 3,4,5…) should be visualized. (Reviewers 3, 4)
- No experiments on simulated data where ground-truth relevant features are known, and no theoretical guarantees that correct features are recovered. L0 regularization does not guarantee correctness. (Reviewer 4)
- No ablation study or sensitivity analysis for the many tricks (e.g., Concrete vs. hard top-M, decay factors). (Reviewer 1; Reviewer 4 asks about stability of solutions with many hyperparameters.)
- The abstract does not properly represent the work (Reviewer 2).

**Additional missing content**
- The paper does not discuss limitations or cases where the method might not be suitable. (Reviewer 3)
- For reproducibility, parameter choices and statistical measures are not detailed. (Reviewer 3)
- Y-axis labels for Figures 1 and 3 are missing. (Reviewer 3)