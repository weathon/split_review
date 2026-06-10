## Summary

This paper proposes KAE, an autoencoder that replaces standard linear layers with learnable polynomial activation functions (up to degree p) in the spirit of KAN networks. The key architectural change is computing h(x) = c₀·1 + c₁·x + c₂·x² + ... + c_p·x^p and then passing it through σ(·+b). Experiments on five image datasets (MNIST, Fashion-MNIST, SVHN, CIFAR-10, CIFAR-100) compare against AE, KAN, FourierKAN, and WavKAN on reconstruction, similarity search, classification, and denoising tasks.

## Strengths

- **Multi-task, multi-dataset evaluation with statistical repetition**: Experiments span five datasets across four tasks (reconstruction, retrieval, classification, denoising), each repeated with 10 random seeds (lines 154). This breadth provides reasonable evidence that the polynomial-based KAE consistently outperforms the compared baselines in the tested regime.

- **Model-capacity analysis (Figure 4)**: The paper controls for parameter count, showing KAE with p=2,3 uses only 75–101K parameters while exceeding the accuracy of KAN (250K params) and FourierKAN (251K params). This demonstrates that the improvement is not simply an artifact of higher capacity (line 219).

- **Convergence-speed advantage documented**: Figure 3 and line 210 show KAE converges within 10–20 epochs while WavKAN and AE "struggle to converge even after 50 epochs." This faster convergence is a practically relevant finding, even if it does not substitute for converged-comparison experiments.

## Weaknesses

### Fatal
None.

### Major

1. **Mathematically incorrect claim about polynomial invertibility.** Line 131 states: "For polynomial orders up to four, an inverse function exists, ensuring the required inversion between the encoder and decoder." This is false. A quadratic polynomial (degree 2) is not globally invertible on ℝ; a quartic (degree 4) can have up to four distinct preimages for a given output. Even cubics are not guaranteed monotonic without additional constraints on coefficients. The entire justification for preferring polynomials over B-splines, Fourier, or wavelet functions in the KAN layer rests in part on this invertibility claim. While the empirical results may still be valid for other reasons (e.g., polynomial functions provide a good inductive bias), the stated theoretical foundation is incorrect and needs to be either corrected with a precise condition (e.g., monotonicity constraints, domain restriction) or removed.

2. **Unfairly undertrained baselines undermine the comparison.** All models are trained for only 10 epochs (line 154), yet line 210 states that "other models, particularly WavKAN and AE, struggle to converge even after 50 epochs." The comparison therefore reflects which architecture converges fastest in the first 10 epochs, not which achieves the best final representation quality. The paper's headline claims of "superiority" (abstract, line 296) are not supported by evidence from converged models. Running all models to convergence (100+ epochs or using early stopping) is necessary to determine whether KAE's advantage persists at full training.

### Minor

1. **Trivial interpretability analysis.** The interpretability section (lines 282–290) shows that C_E·C_D^⊤ is approximately diagonal and C_E·C_E^⊤ is approximately diagonal. The first property simply confirms the encoder and decoder are approximate inverses (expected of any well-trained autoencoder); the second confirms features are decorrelated. Neither provides insight into what individual latent dimensions *mean*, which is the actual goal of interpretability. Calling this "interpretability" overstates what the analysis demonstrates.

2. **Minimal hyperparameter search.** The hyperparameter sweep covers only 4 configurations (2 learning rates × 2 weight decays, line 154). When comparing architectures with very different training dynamics, this narrow search raises concerns about whether the best configuration was found for each baseline, and whether the reported results are robust or cherry-picked.

3. **No discussion of variance in the text.** Although the paper states that results are averaged over 10 seeds with standard deviations (line 154), the experimental sections (4.2, 4.3.2, 4.3.3) discuss only point estimates in the prose. Without explicit statistical significance or effect-size commentary, the reader cannot assess whether the reported improvements are reliable.

### Trivial
- The similarity search discussion (preceding Section 4.3.2) lacks an explicit subsection header for 4.3.1.

## Nice-to-Haves
- Compare against KANs using other basis functions (e.g., Chebyshev, Legendre polynomials) to isolate whether the improvement comes from polynomial functions specifically or just from having learnable univariate functions with smooth basis expansions.
- Provide training time / FLOP analysis for the polynomial layers, especially for high-dimensional inputs (e.g., 784-d MNIST), since polynomial layers of degree p may have significantly different computational cost than linear layers.

## Removed Points

These points were raised in the original reviews but are removed with justification:

1. **"KAE is not a KAN layer"** — REMOVED (factually wrong). The KAE layer (Eq. 3) computes h(x) = c₀·1 + c₁·x + c₂·x² + ... + c_p·x^p. This can be rewritten as output_k = Σ_j φ_{k,j}(x_j) where φ_{k,j}(t) = Σ_m (c_m)_{kj}·t^m. Each φ_{k,j} is a learnable univariate polynomial function, which satisfies the definition of a KAN layer (a matrix of learnable 1D functions). The paper's framing as a KAN variant using polynomial basis functions is appropriate.

2. **"Tables are embedded as images and cannot be read"** — REMOVED (parser artifact). Tables are rendered as images by the PDF extraction pipeline; this does not reflect the original submission.

3. **"No related works comparison with VAEs/DAEs"** — REMOVED (scope creep). VAEs and DAEs are different model families with different training objectives (variational inference vs. reconstruction, denoising-specific corruption). The paper compares architectures within the same family (standard autoencoder, KAN variants of the same architecture). Demanding VAE/DAE baselines would change the paper's scope.

4. **"No computational cost analysis"** — REMOVED (partially addressed). Figure 4 provides training time in seconds (line 217: "KAE models complete training in 30-36 seconds"), so computational cost is not entirely absent.

5. **"The optimization of W is traditionally performed through black-box AI systems" is meaningless** — REMOVED (trivial phrasing issue). This is a minor imprecision in wording, not a substantive weakness.

6. **"Interpretability analysis shows trivial properties"** — This is kept as a Minor weakness (see above), not removed. The harsh critic's specific disdain for it was accurate; the strength finder's enthusiasm for it was overblown.

## Novel Insights

None beyond the paper's own contributions. The reviews surfaced a clear mathematical error that the paper's own framing would not have flagged, and the training-epoch problem is a standard but important experimental-design concern. No deeper synthesis emerged.

## Suggestions

1. Fix the invertibility claim: either provide a correct mathematical justification (e.g., restricting to monotonic polynomials via coefficient constraints, or noting that in practice the learned polynomials happen to be approximately monotonic on the data support), or remove the invertibility argument entirely and justify polynomial choice on empirical grounds alone.

2. Re-run all experiments to convergence (100+ epochs or early stopping) and report final results. This is the most impactful single change the authors could make.

3. Add explicit statistical significance commentary (e.g., confidence intervals, paired test results) to the experimental sections.

4. Expand the hyperparameter search (more learning rates, more seeds for the search itself) to reduce the risk of cherry-picked results.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>