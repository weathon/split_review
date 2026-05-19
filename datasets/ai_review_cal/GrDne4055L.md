- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 5, 6
Now I have all the information I need. Let me compose the final consolidated review.

## Summary

The paper proposes AROS, a method for adversarially robust out-of-distribution detection that uses a Neural ODE with a loss regularizer that encourages equilibrium points, an orthogonal binary layer to separate ID/OOD representations, and a fake OOD sampling strategy that generates OOD embeddings from low-density regions of the ID feature distribution. The method achieves impressive robust AUROC improvements (e.g., 37.8% → 80.1% on CIFAR-10 vs. CIFAR-100 under strong attacks) without requiring auxiliary OOD image datasets, and is evaluated across multiple benchmarks including large-scale datasets and medical imaging.

## Strengths

- **Large, verified improvement under strong adversarial attacks.** The paper demonstrates a dramatic improvement in robust AUROC from 37.8% to 80.1% on CIFAR-10 vs. CIFAR-100 and from 29.0% to 67.0% on CIFAR-100 vs. CIFAR-10 (abstract, Table 1). These are striking empirical results that address a well-known weakness of prior methods.

- **Rigorous adversarial evaluation.** The evaluation uses PGD¹⁰⁰⁰ with 10 random restarts, AutoAttack, and Adaptive AutoAttack (Section 5). The paper explicitly notes that prior methods (e.g., ALOE, ATD, RODEO) were evaluated under weaker attacks or different benchmarks, making the comparison credible.

- **Method does not require auxiliary OOD image datasets.** By generating fake OOD embeddings in feature space via class-conditional Gaussians, AROS avoids the costly and labor-intensive curation of disjoint auxiliary OOD datasets that prior robust detectors (e.g., ALOE, ATD, RODEO) require. This is a clear practical advantage.

- **Systematic ablation study.** The ablation (Section 6, Table 5) replaces individual components with alternatives and demonstrates each component's necessity: removing the Lyapunov loss (Config A), removing adversarial pretraining of the encoder (Config B), replacing the orthogonal binary layer with a standard linear layer (Config C), and replacing fake OOD sampling with random noise (Config D) all degrade performance. This provides direct evidence that the specific design choices drive the reported gains.

- **Generalization beyond adversarial settings.** The method improves AUROC on corrupted benchmarks (CIFAR-10-C vs. CIFAR-100-C: 72.5% → 81.8%) and is evaluated across diverse benchmarks including ImageNet-1k, open-set recognition, and medical imaging (ADNI), supporting generalizability.

## Weaknesses

### Fatal

None.

### Major

- **Disconnect between theoretical framing and actual implementation: the Lyapunov stability regularizers are set to zero (γ₂ = γ₃ = 0).** The loss function in Equation (3) introduces three regularization terms: γ₁∥h_φ∥₂ encourages training embeddings to be near equilibrium points; γ₂ and γ₃ enforce the strict diagonal dominance condition from Theorem 3, which is required to guarantee that the Jacobian eigenvalues have negative real parts (i.e., Lyapunov stability). However, at line 126 the paper states: "We choose the hyperparameters as γ₁ = 1 and γ₂ = γ₃ = 0." With γ₂ = γ₃ = 0, the loss reduces to binary cross-entropy plus an L₂ norm regularizer on the NODE output. The eigenvalue condition from Theorems 1–3 is never enforced during training. This means the paper's central claim—that it "applies Lyapunov stability theory to ensure that both ID and OOD data converge to stable equilibrium points"—does not reflect what is actually being optimized. The method may still work well (the γ₁ term does encourage equilibrium, and the orthogonal binary layer may help), but the theoretical justification as presented is misleading. **The authors must either (a) use non-zero γ₂, γ₃ and demonstrate that these regularizers improve results, or (b) honestly reframe the contribution without claiming Lyapunov stability.** Until this is resolved, the paper's advertised contribution is not verifiable from the text as written.

### Minor

- **Missing architectural parity with baselines.** The paper uses a WideResNet-70-16 as the encoder — a very large backbone for CIFAR-10/100. The architectures used for baseline methods (ATOM, ALOE, ATD, RODEO, DHM) are not specified. If baselines use smaller backbones (e.g., ResNet-34), the reported gains could partially reflect model capacity rather than the proposed method. Controlled experiments using the same backbone would strengthen the comparison.

- **Fake OOD sampling parameter β is not precisely specified.** The paper states β is "very small (e.g., 0)" (line 78). A threshold of exactly 0 is impossible for a continuous density (density > 0 everywhere). The actual β value used and its sensitivity are not reported, making this step difficult to reproduce precisely.

- **No error bars or variance reporting for main results.** Key results in Tables 1, 2a, and 2b are reported as single numbers. Adversarial training and OOD detection involve stochasticity; standard deviations across multiple runs would help assess whether improvements are stable.

- **The contribution of the NODE+regularizer stage relative to the encoder is not isolated.** The ablation study (Config B) confirms that removing adversarial pretraining of the encoder substantially degrades performance, but there is no ablation that removes the NODE and Lyapunov regularizer entirely and uses the encoder embeddings directly with the Gaussian model for OOD detection. This would clarify how much the NODE stage adds beyond the already-robust encoder embeddings.

### Trivial

- **Incomplete sentence in the β description.** Line 78 reads "where we choose β to be very small (e.g., 0." — appears to be missing a closing parenthesis or period (parser artifact), but the original likely has this formatting issue.

## Nice-to-Haves

- A sensitivity analysis on β (number of fake OOD samples and the density threshold) would strengthen the characterization of the fake OOD sampling strategy.
- Analysis of when the method might fail (e.g., near-distribution OOD where the Gaussian approximation is poor) would improve the paper's scientific completeness.
- Discussion of the computational cost of end-to-end PGD through the NODE solver would be informative for practitioners.

## Removed Points

- **"Config F undercuts the no-extra-data emphasis"** (from Harsh Critic): The ablation shows that adding real OOD data *further* improves performance. This is an honest and informative result; it does not contradict the paper's claim that AROS works *without* extra data. A method not requiring extra data is still valuable even if extra data can help further.
- **"The paper does not discuss gradient computation through NODE"**: Computing gradients through ODE solvers is standard practice (adjoint method / direct backprop), well-established in the NODE literature cited by the paper. This is not a missing contribution.
- **Various speculative criticisms** about whether the orthogonal layer's mechanism is unclear or about missing analysis of the time-invariance assumption: these are general research questions rather than specific weaknesses, as the ablation does demonstrate the orthogonal layer's importance (Config C).
- **Several generic strength-finder claims** that praised the problem being "important" without specific evidence or that duplicated content already captured in the concise strengths listed above.

## Novel Insights

The harsh critic identifies a genuine and significant disconnect: the Lyapunov stability regularizers that constitute the paper's theoretical centerpiece are set to zero, meaning the method as implemented does not enforce the conditions derived from Theorems 1–3. This observation goes beyond a typical hyperparameter nitpick — it exposes a gap between the paper's advertised contribution ("Lyapunov-stabilized embeddings") and what is actually optimized. The strength finder correctly identifies the empirical results as impressive and the ablation as systematic, but does not catch this framing issue. The tension between the two inputs yields a useful synthesis: the paper's empirical contribution may be real and valuable, but it needs to be honestly described without claiming a theoretical guarantee that the implementation does not provide.

## Suggestions

1. **Resolve the γ₂ = γ₃ = 0 issue decisively.** Either run experiments with non-zero γ₂, γ₃ and report the results, or — if the γ₁ term alone is sufficient — remove the claim that the method "applies Lyapunov stability theory" and clearly state that the method encourages equilibrium points via an L₂ regularizer, without the eigenvalue conditions from Theorems 1–3. The title should also be revised if the latter path is taken.
2. **Control for architecture.** Re-run baseline methods using the same encoder backbone (or AROS using smaller backbones) to ensure fair comparison.
3. **Add an ablation that removes the NODE entirely** and uses the encoder's output embeddings directly with the Gaussian model for OOD detection, to isolate the NODE stage's contribution.
4. **Report error bars.** Provide standard deviations across at least 3–5 seeds for the main results (Table 1, Table 2a).
5. **Specify the actual β value** used for fake OOD sampling, and ideally include a sensitivity analysis.
