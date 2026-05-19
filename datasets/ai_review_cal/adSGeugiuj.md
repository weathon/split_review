- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 6, 3, 6
Now I have a clear picture of the paper's content and can verify the reviewer claims against the actual text. Let me produce the final consolidated review.

---

## Summary

This paper derives a recursion that expresses higher-order posterior *central* moments in Gaussian denoising solely in terms of derivatives of the MSE-optimal denoiser (Theorems 1–2), and extends this result to one-dimensional projections of the signal (Theorem 3). The authors leverage these theoretical results for practical uncertainty quantification: they show how to compute posterior principal components via finite-difference subspace iteration using only forward passes through a pre-trained denoiser (avoiding the cost of storing the full covariance or performing backprop), and how to estimate marginal posterior distributions along those directions via maximum entropy moment matching. The method is demonstrated qualitatively on face denoising, MNIST, natural images (SwinIR), and microscopy data (Noise2Void).

## Strengths

1. **Clean recursion for posterior *central* moments (Theorems 1–2, Section 3)**. Prior work (Meng et al., 2021) gave a recursion for *non‑central* moments that does not simplify cleanly for central moments. The authors prove a direct, simple recursion for central moments ($\mu_{k+1}=\sigma^2\mu_k' + k\mu_{k-1}\mu_2$ for $k\geq3$), which connects directly to variance, skewness, and kurtosis. This is a genuine theoretical advance over the state of the art, and the paper correctly identifies why the non-central recursion of Meng et al. does not trivially translate.

2. **Training‑free posterior PC computation (Section 4.1, Eq. 13)**. The paper shows that posterior covariance eigenvectors can be obtained via subspace iteration using finite-difference Jacobian-vector products (forward passes only), never storing the full $d\times d$ covariance. The reported **6× memory reduction** for an 80×92 patch with SwinIR concretely demonstrates the practical advantage over automatic differentiation approaches. The ability to compute PCs for arbitrary user-chosen image regions at test time (without retraining) is a genuine capability not available in prior covariance-prediction methods.

3. **Theorem 3 (directional posterior moments, Section 3.2)**. Extending the recursion to one-dimensional projections enables marginal posterior estimation along any direction. This is a non-trivial extension that the authors correctly motivate as necessary for uncertainty visualization, since higher-order moment tensors are impractical to store or visualize directly.

4. **Demonstration on real-world microscopy data (Section 5, Fig. 5)**. The method is applied to FMD microscopy data using Noise2Void, where the noise is neither white nor Gaussian and $\sigma$ is unknown. The fact that the posterior PCs capture semantically meaningful variation (e.g., cell size, septum existence) despite the theoretical assumptions being violated demonstrates practical robustness.

## Weaknesses

### Fatal
None.

### Major

1. **Main-text experimental validation is predominantly qualitative, with limited quantitative evidence.** The paper's central practical claims — that the method is *accurate*, *fast*, and *memory-efficient* — are supported almost entirely by visual results (Figs. 1–5) and a single memory-measurement data point (6× reduction for one patch size with SwinIR, line 192). The paper states that quantitative comparisons (eigenvalue accuracy, comparisons against a posterior-sampling baseline) are in the appendix (line 194), but the main text itself provides no runtime measurements, no wall-clock time comparisons across image sizes, no comparison of eigenvector accuracy against ground-truth covariances on a tractable problem, and no systematic comparison against alternative UQ approaches (e.g., the covariance prediction method of Meng et al. 2021, or Langevin-based posterior sampling). A reader relying solely on the main text cannot assess whether the method's approximations are quantitatively accurate or whether the claimed efficiency advantages hold beyond a single patch size. This gap undermines the paper's applied contribution, even though the theoretical contribution stands independently.

2. **No sensitivity analysis for the step size $c$ in the finite-difference approximation.** The method's practical performance depends critically on choosing $c$ to be "sufficiently small" (line 191) without numerical instability. The paper acknowledges that high-order numerical differentiation "can be unstable with low-precision computation" (lines 250–252), but provides no systematic study of how the computed eigenvalues/eigenvectors vary with $c$, nor any practical guidelines for choosing $c$ given a denoiser's scale and operating range. A practitioner has no way to determine whether their chosen $c$ yields reliable results.

### Minor

1. **No experimental comparison against alternative UQ methods.** While the paper is primarily introducing a new computational tool rather than benchmarking, the practical contribution would be substantially strengthened by even a single comparison — e.g., comparing posterior marginal estimates against samples from a Langevin-based posterior sampler on small images, or comparing the cost and accuracy of the computed PCs against the covariance prediction method of Meng et al. (2021). The paper's silence on these comparisons limits the reader's ability to contextualize the method's utility.

2. **Sensitivity to $\sigma$ misspecification is mentioned but not quantitatively studied.** The paper acknowledges using an estimated $\sigma$ for blind denoising (lines 218, 236–237) and references the appendix for discussion, but the main text provides no experiment showing how the computed PCs or marginals degrade as $\sigma$ deviates from the true value. For a practitioner applying the method to real data where $\sigma$ is uncertain, this is relevant information.

3. **The maximum entropy moment-matching step is described only by reference.** The paper cites Botev (2011) but provides no description of how the maximum entropy distribution is computed in practice, whether there are numerical issues (non-convexity, sensitivity to moment errors), or how the order-four truncation was chosen. A brief note would improve reproducibility.

### Trivial
None.

## Nice-to-Haves

- A systematic study of how the accuracy of the computed PCs varies with the number of subspace iteration steps would be useful.
- An analysis comparing the PCA-based uncertainty visualization with alternative approaches (e.g., per-pixel variance maps, semantic groupings) would help clarify what the PCs reveal versus conceal.
- A brief empirical note on how double precision affects the numerical stability of the derivatives (the paper mentions using it but provides no comparison to single precision).

## Removed Points

These points are flagged to be removed; treat them with caution. They were excluded because they are factually incorrect, misunderstand the paper, or violate the filtering rules.

- **"The paper portrays its contribution as determining the entire posterior but gives only four moments."** The paper explicitly states at line 200 "in practice, we compute derivatives up to third order, which allows us to obtain all moments up to order four." The paper's theoretical claim (line 27) about "determining the entire posterior" is about the recursive relation (which in principle yields all moments), and is immediately caveated by the practical scope in Section 4.2. This is not a weakness; it is standard ground-truth-vs-approximation exposition.

- **"The paper does not discuss conditions for moment determinacy (e.g., Carleman's condition)."** The paper discusses this at lines 97–98: "if the moments do not grow too fast, then they uniquely determine the underlying distribution... This is the case e.g. for distributions with a compact support and is thus relevant to images, whose pixel values typically lie in [0,1]." This criticism is factually wrong.

- **"The paper does not discuss the assumption of white Gaussian noise."** The paper discusses this repeatedly: at lines 218 ("Our theoretical analysis applies to non-blind denoising, in which σ is known"), lines 236–237 ("The FMD dataset was collected using real microscopy imaging, and as such its noise is most probably not precisely white nor Gaussian"), and lines 269 ("While the theoretical basis of our method applies only to additive white Gaussian noise, we show empirically that our method provides qualitatively satisfactory results also in blind denoising on real-world microscopy data"). This criticism is factually wrong.

- **"The quantitative validation is relegated to the appendix, which we cannot see."** The rule specifies that appendix content exists in the original submission and was stripped by the parser; penalizing the paper for content in the appendix is not permitted. The valid remaining criticism (limited quantitative evidence in the main text) is retained above as Weakness 1 in Major.

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface an independent perspective that the paper itself does not already articulate.

## Suggestions

1. **Add a small-scale quantitative validation to the main text.** Use a tractable setup (e.g., 32×32 images with a small denoiser where the full Jacobian can be computed) to report cosine similarity between the finite-difference PCs and the exact eigenvectors, relative eigenvalue errors, and wall-clock time vs. autodiff. Even one table would substantially strengthen the practical claims.

2. **Include a brief sensitivity study for the step size $c$.** A simple plot showing how the top eigenvalue estimate varies with $c$ (for a representative image and denoiser) would give practitioners a practical guideline.

3. **Add a runtime/memory scaling table.** Report wall-clock time and peak GPU memory for computing $K$ PCs at increasing image resolutions (e.g., 64×64, 128×128, 256×256, 512×512), comparing the proposed forward-pass method against the autodiff alternative.

4. **Provide a brief description of the maximum entropy computation** (one paragraph) to improve reproducibility.
