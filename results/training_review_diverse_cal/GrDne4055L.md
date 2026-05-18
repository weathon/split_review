Now I have all the evidence I need. Let me write the consolidated review.

---

## Summary

This paper proposes AROS, a method for adversarially robust out-of-distribution (OOD) detection that combines (1) an adversarially trained encoder to produce robust embeddings, (2) generation of fake OOD embeddings by sampling from low-likelihood regions of class-conditional Gaussians fitted to ID data, (3) a Neural ODE (NODE) with a loss function inspired by Lyapunov stability theory, and (4) an orthogonal binary classification layer. The paper claims large robustness gains (e.g., 37.8% → 80.1% robust AUROC on CIFAR-10 vs. CIFAR-100) without requiring auxiliary OOD image datasets or pretrained models.

## Strengths

- **Large empirical robustness gains, well-supported by the paper's own tables.** The improvements reported (up to ~40 percentage points on challenging adversarial benchmarks, using strong attacks including PGD^1000, AutoAttack, and Adaptive AutoAttack) are substantial and internally consistent across the abstract, results section, and evaluation details. The method achieves these gains without auxiliary OOD datasets or pretrained models, which is a practically meaningful contribution.

- **Effective fake OOD generation strategy validated by ablation.** The ablation study (Config D vs. Config E) shows that low-likelihood sampling from class-conditional Gaussians substantially outperforms random noise as fake OOD data, confirming that conditioning on the ID boundary is critical. This is a clean way to avoid costly auxiliary dataset collection.

- **Comprehensive evaluation across diverse scenarios.** The method is tested on adversarial attacks, natural corruptions (CIFAR-10-C/100-C), open-set recognition (OSR) across six datasets, and large-scale settings (ImageNet-1k, ADNI medical data). The breadth strengthens the empirical case.

- **Orthogonal binary layer shows empirical benefit.** Ablation (Config C vs. Config E) demonstrates improved performance compared to a standard binary layer, even if the precise mechanism (discussed below) is not fully isolated.

## Weaknesses

### Major

1. **The Lyapunov stability regularizers are disabled (γ₂=γ₃=0), creating a fundamental gap between claimed contribution and actual implementation.** The paper's title, abstract, introduction, method section, and conclusion all center on using Lyapunov stability theory to obtain robust embeddings. The loss function in Eq. (3) is presented as the mechanism that enforces the stability conditions from Theorems 1–3. However, the paper explicitly states: *"We choose the hyperparameters as γ₁ = 1 and γ₂ = γ₃ = 0"* (line 126). The γ₂ term enforces the negative trace condition (Theorem 2: all eigenvalues with negative real parts), and the γ₃ term enforces the diagonal dominance condition (Theorem 3). With both set to zero, **the training objective does not enforce any Lyapunov stability condition.** The remaining γ₁ term (‖h_φ(X_train)‖₂) encourages the initial state z(0) to be an equilibrium point (by making dz/dt ≈ 0 at t=0), but this alone does **not** guarantee that the equilibrium is *stable* or *attracting* — the defining property of Lyapunov stability (Definition 1). This means the claimed theoretical grounding is not actually present in the trained model. The paper's improvements cannot be attributed to Lyapunov stabilization when no stabilization condition is enforced. At best, the theory is motivational but disconnected from practice; at worst, the paper misrepresents what the method does. This is the most serious weakness and significantly undermines the paper's central claim.

2. **Missing ablation on the stability regularizers.** The ablation study (Configs A–F) tests removing the entire L_SL loss (Config A), removing adversarial training (Config B), replacing the orthogonal layer (Config C), and replacing fake OOD sampling (Config D), but never tests varying γ₂ and γ₃ to non-zero values. This is the most important missing experiment: without it, we cannot know whether (a) the stability regularizers would hurt performance, (b) they would improve it further, or (c) the method's success is entirely due to the other components (adversarial training, fake OOD sampling, NODE dynamics, and the orthogonal layer). Given that the paper's framing hinges on Lyapunov stability, this omission is critical.

### Minor

1. **The orthogonal binary layer's claimed mechanism is not verified.** The paper asserts that orthogonality *"maximizes the distance between the equilibrium points of ID and OOD samples"* (line 7, line 118), but provides no direct evidence — e.g., measurements of ID/OOD equilibrium distances with and without the orthogonality constraint, or a comparison against a non-orthogonal layer matched for capacity. The ablation (Config C vs. Config E) shows an empirical improvement, but the paper's specific mechanistic claim about equilibrium distance remains unsubstantiated. The orthogonal layer's benefits could equally come from gradient norm preservation or Lipschitz control (which the paper also mentions).

2. **No runtime or scalability comparison.** The method involves adversarial training of a WideResNet-70-16 (200 epochs), fitting class-conditional Gaussians, training a NODE with adjoint solver (100 epochs), and an orthogonal layer. For a paper targeting practical deployment, the absence of runtime or compute cost comparisons against baselines is a limitation.

### Trivial

None.

## Nice-to-Haves

- An experiment that replaces the NODE+orthogonal layer with a standard two-layer MLP on the same fake OOD embeddings would help disentangle the source of robustness gains and test whether the NODE dynamics are driving the results.
- A sensitivity analysis of how varying β (the likelihood threshold for fake OOD sampling) affects the clean vs. robust performance trade-off would strengthen the empirical characterization.
- Reporting results with non-zero γ₂, γ₃ values (even if performance drops) would clarify whether the current hyperparameter choice is hiding a failure of the stability method, or whether the regularizers are genuinely unnecessary.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about β=0 being a mathematical error (Harsh Critic's Point 2).** The paper states *"β to be very small (e.g., 0"* — the text is clearly truncated by the PDF parser (the closing parenthesis is missing from the parsed output). In the original submission, this likely reads "(e.g., 0)" or "(e.g., 0.001)". The criticism that β=0 makes the sampling impossible is based on a parsing artifact, not the actual paper content. **Removed per hard rule on parser artifacts.**

- **Strength from Strength Finder: "Novel integration of Lyapunov stability theory for OOD detection."** This claimed strength conflicts with Verified Weakness #1 (the Lyapunov regularizers are disabled). A contribution that is advertised but not implemented cannot stand as a strength. **Removed per rule: when a strength and verified weakness disagree, the weakness wins.**

- **Criticism about missing appendix or proofs (implied by "Missing Parts and Places to Improve" section).** Per hard rules, these are parser-stripped sections that exist in the original submission. **Removed.**

## Novel Insights

None beyond the paper's own contributions. The core novelty tension — a method framed around provable stability theory that disables the stability-enforcing terms in its own loss function — is identified by the reviews but is a weakness, not an insight.

## Suggestions

1. **Either use the stability regularizers or reframe the contribution.** If γ₂, γ₃ are set to non-zero values and the Jacobian conditions are approximately satisfied, verify this empirically (e.g., report the distribution of Jacobian eigenvalues at trained equilibrium points). If the regularizers genuinely hurt performance, the method works despite Lyapunov theory, not because of it — in which case the title, abstract, and contribution claims should be revised to accurately reflect what the method actually does (adversarially robust OOD detection via fake OOD-embedding training with a NODE dynamics).

2. **Add the missing ablation on γ₂, γ₃.** Show results for at least a few positive settings (e.g., γ₂=γ₃=0.1, 1.0) to either validate or honestly report the failure of the stability regularization.

3. **Provide direct evidence for the orthogonal layer's claimed mechanism** — e.g., measure and report the distance between ID and OOD equilibrium points in the learned feature space with and without the orthogonality constraint.

4. **Clarify what the remaining L₂ term (γ₁=1) actually achieves theoretically.** If the paper believes that minimizing ‖h_φ(z(0))‖₂ alone provides meaningful stability guarantees, provide an argument or reference. Otherwise, acknowledge that the method enforces equilibrium points but not Lyapunov stability.

## Score and Decision

**Originality:** The general pipeline (adversarial training + fake OOD features + NODE binary classifier) has individually familiar components, with the claimed novelty being the Lyapunov stability framing. Since that framing is not actually implemented, the originality is lower than advertised.

**Importance of research question:** Robust OOD detection is an important and timely problem.

**Soundness of experiments:** The experimental setup is generally sound (strong attacks, multiple benchmarks, ablation study), but the most critical ablation (varying γ₂, γ₃) is missing, and the central claim is not supported by the implementation.

**Clarity of writing:** Clear description of components, but the disconnect between claimed theory and actual implementation is not acknowledged.

**Value to community:** The pipeline itself (adversarial encoder + fake OOD + NODE + orthogonal layer) yields strong empirical results and could be useful. However, the misleading theoretical framing and overselling of Lyapunov stability lower the paper's trustworthiness.

**Overall assessment:** The paper presents a plausible pipeline with impressive empirical results. However, the central methodological claim — that Lyapunov stability theory drives the reported robustness — is not supported: the regularizers designed to enforce stability conditions are set to zero, and the missing ablation prevents the reader from evaluating whether they would help. The gap between what the paper advertises and what it implements is too wide to ignore. A revision that either actually applies the stability regularizers and verifies their effect, or honestly reframes the contribution, could produce a sound paper.

**MY FINAL SCORE:** <pineapple>4.5</pineapple>
**MY FINAL DECISION:** <orange>Reject</orange>