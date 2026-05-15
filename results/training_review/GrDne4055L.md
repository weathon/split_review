Now I have all the evidence I need. Let me synthesize the final consolidated review.

## Summary

This paper proposes AROS, a method for adversarially robust OOD detection that uses Neural ODEs with a loss function motivated by Lyapunov stability theory. It generates "fake" OOD embeddings by sampling from low-likelihood regions of class-conditional Gaussians in the feature space, and employs an orthogonal binary layer to separate ID/OOD equilibrium points. The method reports large robustness gains (e.g., 37.8% → 80.1% AUROC on CIFAR-10 vs. CIFAR-100 under attack).

## Strengths

- **Large and consistent robustness gains under strong attacks**: AROS improves robust AUROC from 37.8% to 80.1% on CIFAR-10 vs. CIFAR-100 and from 29.0% to 67.0% on CIFAR-100 vs. CIFAR-10 (abstract). Gains hold across PGD^1000, AutoAttack, and Adaptive AutoAttack benchmarks — magnitudes that, if reproducible, represent a substantial advance.

- **Eliminates need for auxiliary real OOD datasets**: Instead of collecting additional OOD images (a costly, bias-prone process), AROS generates fake OOD embeddings by sampling low-likelihood tails of class-conditional Gaussian distributions fitted to ID embeddings (Section 4.1). This is a practical contribution that reduces data collection cost and avoids biasing the detector toward specific OOD examples.

- **Comprehensive evaluation across diverse benchmarks**: AROS is tested on standard CIFAR splits, large-scale ImageNet, open-set recognition (MNIST, FMNIST, Imagenette), corrupted data (CIFAR-10-C, CIFAR-100-C), and medical imaging (ADNI) — demonstrating broad applicability.

- **Ablation study confirms contribution of key components**: Table 5 shows that removing the designed loss (Config A), standard (vs. adversarial) pre-training of the encoder (Config B), the orthogonal binary layer (Config C), and the fake OOD strategy (Config D) all degrade performance, confirming that each component contributes to the final result.

## Weaknesses

### Fatal

None. While the paper has significant issues (see below), the empirical results and the fake-OOD-generation + orthogonal-layer components are genuine contributions that survive independently of the Lyapunov framing. The problems, though serious, are not at the level of methodological fraud or complete invalidation.

### Major

- **The Lyapunov stability regularizers are disabled (γ₂=γ₃=0), undermining the paper's central theoretical claim.** The loss function in Eq. (3) contains three regularization terms. The first (γ₁∥h_ϕ(X_train)∥₂) encourages the initial state to be an equilibrium point (h(z)≈0). The second and third terms implement the eigenvalue conditions from Theorems 2 and 3 (negative real parts via diagonal dominance). The paper explicitly states (line 126): "We choose the hyperparameters as γ₁ = 1 and γ₂ = γ₃ = 0." This means the two terms that enforce *stability* of the equilibrium (as opposed to just equilibrium proximity) are turned off. The title, abstract, introduction, and conclusion repeatedly claim that the method "applies Lyapunov stability theory" and "ensures that both ID and OOD data converge to *stable* equilibrium points," but the actual training objective only ensures z(0) is near an equilibrium — it does not enforce that this equilibrium is stable in the Lyapunov sense.

  *Why this is major, not fatal*: The L2 penalty ∥h_ϕ(z)∥₂, while not sufficient for Lyapunov stability, does encourage the dynamics to be near equilibrium. The paper's other contributions (fake OOD generation, orthogonal binary layer, strong empirical results) do not depend on γ₂,γ₃ being nonzero. However, the paper as written presents Lyapunov stability as the core mechanism, and this claim is directly contradicted by the hyperparameter choice. The authors must either (a) provide experiments with γ₂,γ₃ > 0 to validate that the theoretical framework was used, or (b) honestly reframe the contribution without invoking Lyapunov stability as an active constraint.

- **No ablation evaluates the effect of the Lyapunov regularizers (γ₂,γ₃).** The ablation study (Section 6, Table 5) replaces the loss function entirely (Config A), changes pretraining (Config B), replaces the orthogonal layer (Config C), and replaces fake OOD with random noise (Config D) — but never tests γ₂,γ₃ > 0. Since the default configuration already sets both to zero, there is zero experimental evidence that the Lyapunov-inspired terms (Theorems 2 and 3) contribute to performance. Without this ablation, the paper cannot attribute any robustness gain to the Lyapunov stability framework, and the reader cannot assess whether enabling these terms would help, hurt, or cause training instability (which might explain why they were disabled).

### Minor

- **The β threshold for fake OOD sampling is underspecified.** Equation (1) defines fake OOD samples via p(r|y=j) < β, and the text says β is "very small (e.g., 0." The parser truncation aside, β=0 would require sampling from regions with strictly negative density — impossible for any continuous distribution. The intended procedure (sampling from distributional tails) is conceptually clear, but the exact threshold needs specification (e.g., a quantile of the Mahalanobis distance) to be reproducible. This is fixable but relevant because the entire training dataset construction depends on this step.

- **The claim that an orthogonal weight layer "maximizes the distance between equilibrium points" is unsubstantiated.** Section 4.3 asserts that an orthogonal binary layer "maximizes the separation between the equilibrium points of ID and OOD data" without proof. Orthogonality preserves norms and can prevent vanishing/exploding gradients, but the paper provides no theoretical or empirical argument that orthogonality specifically maximizes inter-class equilibrium separation over a non-orthogonal linear layer. The ablation (Config C vs. E) empirically shows the orthogonal layer helps, but the "maximizes" characterization is overstated.

- **The 37.8% baseline achieving the "before" performance is not named in the abstract.** The abstract states "improves robust detection performance from 37.8% to 80.1%" without identifying which method produces 37.8%. While tables presumably contain this information, the omission in the abstract makes the headline comparison less informative than it should be.

### Trivial

None beyond what has been mentioned.

## Nice-to-Haves

- An experiment varying γ₂,γ₃ (enable the stability regularizers) would directly test whether the theoretical framework adds value. If training becomes unstable or performance drops, the paper should explain why and consider reframing.
- A clearer specification of β (e.g., sampling from the 5th-percentile Mahalanobis distance tail) would improve reproducibility.
- An explanation of *why* γ₂=γ₃=0 was chosen: was it an empirical finding of no benefit, a training instability concern, or an oversight? The paper is silent on this.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Attack not fully adaptive due to non-differentiable fake sampling step"** (Harsh Critic): Factually wrong. The fake sampling is a training-time data generation procedure. During inference, the pipeline (encoder → NODE → binary layer → OOD score) is fully differentiable end-to-end. The attack computes ∇_x S_F(x) through this inference pipeline, which does not involve the sampling step at all. Removed.

- **"Gaussian assumption on embeddings is unvalidated"**: This is a standard assumption widely used in the OOD detection literature (VOS, MD, etc.) and is not an error specific to this paper. Removed.

- **"Time-invariance assumption should be relaxed and tested"**: The paper explicitly adopts this from SODEF and provides empirical motivation (Table 4.a). Demanding the paper also explore the non-autonomous case is scope creep; the assumption is a documented design choice, not an oversight. Removed.

- **"Config D (random noise) is a straw-man baseline"**: The ablation config D tests whether replacing fake OOD samples with random noise degrades performance. This is a standard sanity check — it tests whether the fake OOD distribution being conditioned on ID data matters. The result showing degradation validates the design choice. Not a straw-man. Removed.

- **"Results only in tables without seeing them in main text"**: Parser artifact — table contents exist in the original submission. Removed.

- **"Different attack budgets for baselines"**: The paper explicitly acknowledges this (line 153) and explains the discrepancy. This is transparency, not a flaw. Removed.

## Novel Insights

The most interesting observation across the reviews is the fundamental tension between what the paper claims as its core mechanism ("Lyapunov stability") and what it actually implements (L2 penalty on the hidden state). The reviewer landscape splits sharply: the harsh critic correctly identifies this as a significant overclaim, while the strength finder uncritically accepts the paper's framing. The truth is nuanced — the paper has genuine empirical contributions (fake OOD generation in embedding space, orthogonal binary layer, strong results) that are independent of whether γ₂,γ₃ are enabled, but the Lyapunov framing is misleading. A novel insight that emerges is that the L2 penalty ∥h_ϕ(z)∥₂ alone (forcing z(0) to be near an equilibrium by making the derivative small) may be sufficient for practical robustness even without the stricter eigenvalue constraints — but the paper never makes this argument explicitly, suggesting either an oversight or a missed opportunity to reframe the contribution more honestly.

## Suggestions

1. **Address the γ₂,γ₃=0 issue head-on.** Either (a) run experiments with γ₂,γ₃>0 and report results (even if they are worse — that is valuable scientific information), or (b) if the terms were disabled for a principled reason (e.g., training instability, negligible impact), explain why and reframe the paper's contribution without claiming to "apply Lyapunov stability theory" as an active constraint. The current framing is misleading.

2. **Specify β clearly.** Provide the exact threshold used (e.g., "β = 1e-6" or "we sample from the tail beyond the 99.9th percentile Mahalanobis distance"). This is essential for reproducibility.

3. **Quality the orthogonal layer claim.** Replace "maximizes the distance between equilibrium points" with a more measured claim (e.g., "increases separation" or "maintains separation") unless a theoretical justification is provided.

4. **Add an ablation varying γ₂ and γ₃** to the study. This is the most directly missing experiment.

5. **Name the baseline** for the headline 37.8% number in the abstract.

## Score and Decision

**Originality:** Strong on the architectural combination (NODE + fake OOD embeddings + orthogonal binary layer), though individual components (VOS for fake features, SODEF for NODE stability) are borrowed.  
**Importance of research question:** High — robust OOD detection under adversarial attacks is practically critical and underexplored.  
**Claims well supported:** No — the main theoretical claim (Lyapunov stabilization) is contradicted by γ₂=γ₃=0. Empirical results appear strong but lack the critical ablation.  
**Soundness of experiments:** Mixed. Evaluation is broad and uses strong attacks, but missing the one ablation that validates the claimed mechanism.  
**Clarity of writing:** Clear organization, though the disconnect between theory and implementation is papered over.  
**Value to the research community:** Potentially high if the issues are addressed — the fake OOD generation in embedding space and the performance numbers are valuable.

The paper presents interesting empirical results and a reasonable overall pipeline, but the central claim about Lyapunov stability is not supported by the actual implementation (γ₂=γ₃=0 disables the stability-enforcing regularizers), and the missing ablation prevents attributing gains to the claimed mechanism. The problems are addressable, but the paper in its current form overstates its contribution.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>