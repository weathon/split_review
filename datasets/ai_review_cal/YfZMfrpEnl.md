- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5
Now I have all the information needed. Let me synthesize the final review.

---

## Summary

This paper proposes a stochastic vision transformer for self-supervised learning that encodes image patches as elliptical Gaussian distributions (mean + covariance), replaces standard dot-product attention with negative 2-Wasserstein distance attention, and adds Wasserstein-based contrastive regularization terms to both pre-training and fine-tuning objectives. The goal is to improve predictive accuracy and uncertainty calibration across in-distribution, out-of-distribution, corruption, and semi-supervised settings. The method is built on top of the data2vec SSL framework with a ViT backbone and is evaluated on CIFAR-10, CIFAR-100, and SVHN.

## Strengths

1. **Well-motivated and principled approach** – Injecting stochasticity into ViT embeddings for SSL uncertainty quantification is a legitimate and underexplored problem. The use of elliptical Gaussian embeddings with a closed-form 2-Wasserstein distance is a natural technical choice, grounded in prior work on distributional embeddings (Vilnis & McCallum 2015, fan2022stosa) and Wasserstein-based optimization (Gao & Kleywegt, Kuhn et al.). The three components (stochastic embeddings, Wasserstein attention, distance-aware regularization) form a coherent methodological package.

2. **Evaluation across multiple robustness axes** – The paper tests its method on in-distribution generalization, OOD detection, corrupted/perturbed datasets, and semi-supervised learning. This goes beyond standard accuracy-only reporting and follows the Plex evaluation protocol, which is appropriate for a reliability-focused paper. The experimental design covers four distinct scenarios that are relevant to deployment.

3. **Computational efficiency analysis** – The ablation includes a comparison of parameters, memory, and training time against Deep Ensembles, showing that the proposed method achieves stochasticity without the multiplicative cost of ensemble training (Table \ref{tab:cost}). This is a concrete practical advantage worth highlighting.

4. **Hyperparameter and augmentation ablation provides calibration guidance** – The visible ablation tables (regularization coefficients $\lambda_1,\lambda_2$, RandAugment magnitude/amount) systematically explore sensitivity to key hyperparameters, offering practical guidance for tuning the method.

## Weaknesses

### Fatal
None.

### Major

1. **Missing component-level ablations that isolate the three core contributions** – The paper never ablates the individual contributions against suitable controls:
   - What is the effect of using Gaussian embeddings with *standard dot-product attention* (no Wasserstein)?
   - What is the effect of using deterministic embeddings with *Wasserstein attention*?
   - What is the effect of adding Wasserstein regularization to a *deterministic baseline*?
   
   Without these ablations, it is impossible to attribute any observed gains to specific components. The claimed improvements could come from any single component (or from interactions among them), and the central narrative that the full method is necessary remains unsubstantiated. This is the most significant evidential gap in the paper.

2. **ViT architecture details for 32×32 images are unspecified** – The paper uses ViT-B (designed for 224×224 inputs with 16×16 patches) on CIFAR-10/100 (32×32). There is no mention of input resizing, patch size, or architectural modifications. With standard 16×16 patches on a 32×32 image, only 2×2=4 patches are produced, which is trivially small for self-attention. If a smaller patch size was used (e.g., 4×4 → 8×8=64 patches, or 2×2 → 16×16=256 patches), this is a critical architectural detail that must be reported for reproducibility. The paper is currently unreproducible on this point.

### Minor

3. **No error bars or variance reporting** – The paper states "results shown were averaged over 5 runs" for compared methods, but the only visible results (ablation tables) report single accuracy values (e.g., 69.420, 71.370) without any variance. Without confidence intervals or standard deviations, readers cannot assess whether the reported advantages are statistically reliable or within the noise range of a single seed. This is particularly important given the small-scale datasets used.

4. **Possible formula typo in 2-Wasserstein distance** – Both Eq. 66 and Eq. 101 contain:
   `Tr( Σ_1 + Σ_2 - 2( Σ_1^{1/2}Σ_1Σ_2^{1/2})^{1/2})`
   where the standard closed-form is:
   `Tr( Σ_1 + Σ_2 - 2( Σ_1^{1/2} Σ_2 Σ_1^{1/2})^{1/2})`
   
   The paper uses $\Sigma_1^{1/2}\Sigma_1\Sigma_2^{1/2}$ instead of $\Sigma_1^{1/2}\Sigma_2\Sigma_1^{1/2}$. If this reflects the actual implementation, the attention scores are mathematically incorrect. If it is a typesetting error, it should be corrected, as it creates ambiguity about implementation correctness.

5. **No justification for squaring the attention matrix in the covariance update** – Equation \ref{eq:att_cov} uses $A^2_{\boldsymbol{z}} V_\sigma$ while the mean update uses $A_{\boldsymbol{z}} V_\mu$ (Eq. \ref{eq:att_mean}). Squaring the attention matrix is not standard and is not explained or justified. This is a nontrivial design choice that could affect whether the covariance update preserves meaningful geometric properties.

6. **No large-scale experiments** – All experiments are on CIFAR-10/100 and SVHN (32×32 images). For a ViT-based SSL method, the absence of at least one ImageNet-scale experiment (e.g., linear probing on ImageNet-1K) limits the significance of the contribution. A method that only works at small scales addresses a narrower scope than the paper's general framing suggests.

### Trivial

None.

## Nice-to-Haves

- **Qualitative uncertainty analysis** – Calibration curves, entropy distributions for OOD vs. ID samples, or reliability diagrams would strengthen the calibration claims beyond scalar metrics like ECE.
- **Comparison with stochastic variants of the backbone** – e.g., adding MC-Dropout or a Bayesian prediction layer to data2vec, to directly compare stochastic embeddings vs. stochastic parameters.
- **Analysis of the positive/negative sampling strategy** – The paper uses random sampling from other classes as negatives during fine-tuning. An ablation comparing this to harder negative mining or distance-based sampling would be informative.
- **Clarification on the interaction between l₁ and l₂** – The two regularization terms both involve Wasserstein distances but have different functional forms (log-sigmoid vs. hinge). An analysis of their relative importance would be helpful.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Results tables are missing / unreviewable"** – The main results tables (IND, OOD, corrupted, semi-supervised) are referenced via `\input{}` directives that the parser stripped. Per instructions, these exist in the original submission. The paper's reported claims about these results cannot be independently verified from the extracted text, but this is a parsing artifact, not an author omission.

2. **"Missing comparison to Bayesian SSL / probabilistic backpropagation methods"** – The paper compares against data2vec, Deep Ensembles, MC-Dropout, Sinkformer, and SNGP, which are the standard and appropriate baselines for this line of work. The call for additional SSL-specific uncertainty methods exceeds the paper's stated scope and reflects reviewer domain expectations rather than a gap in the presented comparison.

3. **"Positive/negative example definition is glossed over"** – The paper does define these: unmasked patches as positives during pre-training, unaugmented patches as positives during fine-tuning, and random samples from other classes as negatives. While the details could be expanded, the definitions are present and clear enough.

4. **"The definition and relationship between l₁ and l₂ is unclear"** – The paper explains that l₁ regularizes distances between input embeddings and examples, while l₂ enforces a margin between positive and negative examples. This is sufficiently clear for a methods paper.

5. **"No mention of whether the method uses data2vec v1 or v2 and other framework details"** – This level of implementation detail is standard to defer to the code release, which the paper states is included in the supplementary material.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder do not surface observations that meaningfully extend the paper's own analysis.

## Suggestions

1. **Add the missing component-level ablations** – Test at least four configurations: (a) deterministic baseline (data2vec), (b) deterministic + Wasserstein regularization, (c) Gaussian embeddings + dot-product attention, (d) Gaussian embeddings + Wasserstein attention. This directly isolates each claimed contribution.

2. **Specify the ViT-B patch size and input resolution used for 32×32 images** – State whether images are resized, what patch size is used, and any architectural modifications. Without this, the experiments are not reproducible.

3. **Report error bars** – Provide standard deviations over at least 3 seeds for all reported metrics and baselines.

4. **Correct the Wasserstein formula** – Verify that the implementation uses the standard `Tr( Σ_1 + Σ_2 - 2( Σ_1^{1/2} Σ_2 Σ_1^{1/2})^{1/2})` and correct the typeset equations accordingly.

5. **Justify or remove the squaring of the attention matrix** in the covariance update (Eq. \ref{eq:att_cov}), or add an ablation comparing A_z vs. A²_z.

6. **Include at least one larger-scale experiment** (e.g., ImageNet-100 linear probing or transfer to a non-CIFAR dataset) to demonstrate the method's generality beyond tiny-image benchmarks.
