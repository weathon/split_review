Now I have verified all claims. Let me synthesize the final review.

## Summary

The paper proposes AROS, a framework for adversarially robust out-of-distribution (OOD) detection that: (1) generates fake OOD embeddings by sampling low-likelihood regions of class-conditional Gaussians in feature space, (2) uses a Neural ODE with a time-invariant assumption for stable representations, (3) applies an orthogonal binary layer for ID/OOD classification, and (4) employs a loss function with terms motivated by Lyapunov stability theory. The empirical evaluation shows strong gains in robust AUROC across multiple benchmarks (CIFAR, ImageNet, OSR, corrupted data) under strong attacks (PGD¹⁰⁰⁰, AutoAttack, Adaptive AutoAttack).

## Strengths

- **Large and consistent empirical gains in adversarial robustness**: AROS improves robust AUROC from 37.8% to **80.1%** on CIFAR-10 vs. CIFAR-100 under PGD¹⁰⁰⁰ (abstract, line 7), and from 45.9% to **74.0%** on the main robust OOD benchmark (Section 5, line 157). These gains are large and consistent across multiple metrics and datasets.

- **No reliance on auxiliary OOD datasets or pretrained models**: Fake OOD embeddings are generated purely from ID data using class-conditional Gaussian estimation (Section 4.1, Eq. 1–2). Despite this restriction, AROS outperforms prior methods (ATOM, ALOE, ATD, RODEO) that use extra OOD images — a practically meaningful advantage.

- **Comprehensive and rigorous evaluation**: The method is tested on multiple benchmarks (CIFAR-10/100, ImageNet-1k, OSR setups, corrupted data) under strong attacks (PGD¹⁰⁰⁰ with 10 random restarts, AutoAttack, Adaptive AutoAttack). The ablation study (Section 6) systematically validates the contribution of each component.

## Weaknesses

### Fatal
None.

### Major

- **The Lyapunov regularization terms are disabled, creating a disconnect between claimed mechanism and implementation.** The loss function in Equation (3) includes two exponential terms (controlled by γ₂, γ₃) designed to enforce strict diagonal dominance of the Jacobian — the mechanism that would implement Lyapunov stability (Theorems 2–3). However, the paper states: "We choose the hyperparameters as γ₁ = 1 and γ₂ = γ₃ = 0" (line 126). With γ₂ = γ₃ = 0, these terms are entirely removed from the objective. What remains is binary cross-entropy loss plus an L₂ penalty on the NODE output. The paper's central framing — "Lyapunov-Stabilized Embeddings" (title, abstract, contributions) — strongly implies these stability constraints are active, but they are not. The L₂ term alone encourages outputs near zero but does not enforce the diagonal-dominance conditions that provide the theoretical stability guarantees the paper invokes. This does not invalidate the empirical results, but it makes the paper's claimed contribution misleading: a NODE with L₂ regularization and an orthogonal binary layer is not the same as a Lyapunov-constrained system. The paper must either (a) activate γ₂, γ₃ > 0 and demonstrate that the Lyapunov terms contribute to robustness, or (b) honestly reframe the contribution without invoking the Lyapunov mechanism as an implemented component.

### Minor

- **Fake-OOD sampling condition is imprecisely specified.** Equation (1) requires sampling embeddings satisfying \(p(r \mid y=j) < \beta\) where β is described as "very small (e.g., 0)" (line 78). If β = 0, no valid sample can satisfy this inequality since probability densities are non-negative. The paper does not clarify the actual value of β used, nor the concrete sampling procedure (rejection sampling? optimization? a percentile cutoff?). This underspecification directly affects reproducibility of the fake-OOD generation — one of the paper's key components.

- **Inconsistency between reported performance numbers across the paper.** The abstract (line 7) reports an improvement "from 37.8% to 80.1% on CIFAR-10 vs. CIFAR-100," while the Results Analysis section (line 157) states "improves adversarial robust OOD detection performance from 45.9% to 74.0%" without specifying the dataset. These are clearly different numbers for different settings/metrics, but the text does not reconcile them or explain which baseline/benchmark each refers to. This ambiguity undermines the reader's ability to assess the method's absolute merit without the tables.

- **Overstated claim about the orthogonal layer.** The paper states the orthogonal binary layer "maximizes the distance between the equilibrium points of ID and OOD data" (line 118). An orthogonal transformation (\(w^T w = I\)) is norm-preserving — it does not, by itself, increase separation between two points in the feature space. The genuine benefits of orthogonality (gradient norm preservation, Lipschitz control) are valid and well-documented in the cited literature, but the claim about *maximizing* separation is not justified by the orthogonal constraint alone and should be softened or clarified.

- **Missing ODE solver details.** The implementation (line 166) specifies integration time \(T=5\) but does not report the ODE solver type, tolerance, or number of integration steps. These details are important for reproducibility, especially given the sensitivity of NODE stability to solver configuration.

### Trivial
None.

## Nice-to-Haves

- Reporting statistical significance (means and standard deviations across multiple seeds) would strengthen the empirical claims, especially given the stochasticity in fake-OOD sampling and model initialization.
- A brief limitations paragraph discussing failure cases (e.g., when ID and OOD distributions are very close, or when the Gaussian approximation is poor) would improve the paper.
- Clarifying whether a full or diagonal covariance matrix is used for the class-conditional Gaussians, and how inversion is handled when feature dimension exceeds per-class sample count, would aid reproducibility.

## Removed Points

These points are flagged to be removed, treat them with caution:
- *"The paper should explicitly state which hyperparameters (attack budget, steps, restarts) are identical across all methods."* — The paper does state these details (Section 5, Evaluation Details). Removed as factually incorrect.
- *"Lyapunov regularisation terms are 'silently zeroed'" with implication of deception* — The paper explicitly states γ₂=γ₃=0 (line 126). The issue is not concealment but a disconnect between narrative and implementation. Reframed above as a structural claim/implementation gap.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same tension the paper creates: strong empirical results paired with a claimed mechanism (Lyapunov stability) that is not actually executed. This is a paper whose experimental methodology and results are ahead of its theoretical narrative.

## Suggestions

- **Enable the Lyapunov regularization terms (γ₂, γ₃ > 0) in at least one experimental condition.** Run an ablation where these terms are active and compare against the current setting (γ₂=γ₃=0). If the Lyapunov terms hurt or don't help, honestly report this and reframe the contribution around the components that do work (time-invariant NODE + L₂ regularization + orthogonal layer + fake OOD). If they help, this directly validates the paper's central thesis.
- **Fix the fake-OOD sampling specification.** State the exact value of β used, describe the sampling procedure (rejection sampling, optimization, or percentile-based thresholding), and provide a distributional analysis of the generated embeddings (e.g., distance to ID centroids, visualization).
- **Reconcile the numerical discrepancies** between the abstract (37.8% → 80.1%) and the Results Analysis (45.9% → 74.0%) by specifying which baselines and settings each number corresponds to.
- **Soften the claim about the orthogonal layer** "maximizing" separation — replace with a more precise description of the benefits (gradient norm preservation, Lipschitz control, improved conditioning of the decision boundary).

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>