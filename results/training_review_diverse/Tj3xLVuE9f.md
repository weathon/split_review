Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper introduces a conceptual framework that separates *predictivity* (how reliably a feature predicts the label) from *availability* (how easily a feature can be extracted from inputs) to study shortcut learning. It presents a generative procedure for constructing synthetic datasets where both factors can be independently manipulated, and shows empirically that nonlinear models exhibit shortcut bias toward more-available features even when those features are less predictive — an effect that is absent in linear models. A Neural Tangent Kernel analysis provides a theoretical account for the ReLU vs. linear difference, and experiments on Waterbirds and CelebA extend the findings to naturalistic images.

## Strengths

- **Formal dissociation of predictivity and availability**: The paper's generative framework (Section 3) enables independent manipulation of feature predictivity ρ and availability (via amplification α and nesting η), going beyond prior work (e.g., Pezeshki et al. 2021) that confounds these under a single "strength" notion. The synthetic experiments (Figure 2) cleanly demonstrate that availability can override predictivity in nonlinear models, establishing the core conceptual contribution on solid empirical footing.

- **Systematic identification of architecture as a causal driver**: The controlled experiments varying depth, width, and activation function (Figure 3) show that bias increases with depth and emerges specifically with nonlinear activations (ReLU, Tanh), while linear networks remain unbiased. This goes beyond observational studies by varying architecture under controlled data, isolating the causal role of nonlinearity.

- **NTK analysis providing a mechanistic hypothesis**: The theoretical section (Section 6) proves that, for a quadratic approximation of the ReLU kernel, the sensitivity of model predictions to feature availability is asymmetric — a sign that depends on both availability α and predictivity ρ — while the linear kernel yields no asymmetry. This provides a mathematically grounded, non-trivial candidate explanation for why nonlinear architectures are more susceptible to shortcut bias, and it correctly predicts the qualitative pattern (bias toward more-available features, with predictivity modulating the boundary).

- **Availability manipulations on naturalistic data**: The Waterbirds and CelebA experiments (Section 7, Figure 4/5) go beyond synthetic data by showing that explicit manipulations of background properties (spatial extent, color, patch removal) shift model feature reliance, bridging the gap between controlled studies and real-world image classification.

## Weaknesses

### Fatal
None.

### Major

- **Theory and experiments address different quantities with no formal bridge established**. The empirical bias measure (Section 3) is `reliance_model − reliance_optimal`, computed from classification decisions on a probe grid in latent space. The theoretical analysis (Section 6) studies ζ_i — the m-th order derivative of alignment γ between predictions under perturbed availability scaling B. The paper asserts that ζ_i "indicates how much the model relies on feature i" (line 292), but the connection between this sensitivity-of-alignment metric and the empirical reliance/bias measure is asserted, not derived. The theorems show that |ζ₁|−|ζ₂| is zero for linear networks and non-zero at order m=9 for ReLU networks, but this result concerns how *alignment between two prediction functions* changes when you perturb availability — not how much the model prefers one feature over another in the sense of the empirical bias. The paper presents the theory as "an alternative approach" (line 168) and describes the findings as "consistent" (abstract), but there is no formal argument or simulation demonstrating that the conditions producing non-zero |ζ₁|−|ζ₂| also produce non-zero empirical shortcut bias. This gap means the theoretical account does not explain the specific empirical quantity the paper measures. Bridging this — e.g., by computing the empirical bias from the NTK predictor for the synthetic setting, even numerically with the quadratic kernel — would be needed to claim the theory actually accounts for the experimental results.

- **The nesting factor is proposed in the framework but never empirically demonstrated**. The framework (Section 3) posits two availability factors: amplification α and nesting η. The latter — the complexity of inverting a nonlinear transformation to recover a latent feature — is the more conceptually novel factor, as amplification amounts to a relatively intuitive signal-strength manipulation. The paper states "We also conducted experiments manipulating a second factor ... the relative nesting of representations" (lines 136–138), but no results are presented in the main text, and the appendix (stripped) cannot be verified. The main contribution on availability thus rests entirely on amplification, a single manipulation. Either nesting results should be shown (even a null result) or the framework should be scoped to amplification only.

- **The "Bayes-optimal classifier" in naturalistic experiments is not defined, undermining the central claim of that section**. For synthetic data, the optimal classifier is well-specified as LDA in latent space (line 84). For Waterbirds and CelebA (Section 7), the paper states that "a Bayes optimal classifier is far less sensitive to the predictivity of the non-core feature" (line 344) and labels it in Figure 4A/B, but never states how this optimal classifier is constructed. If it is a classifier that uses the same latent variables (bird label, background label) that the authors assume, then the comparison stacks the deck: the optimal classifier receives the latent variables directly, while the model must extract them from pixels, and features that are harder to extract will naturally show larger divergence from this latent-level optimum. The paper needs to either (a) define the optimal classifier explicitly and justify its appropriateness, or (b) re-frame the claim to compare against a more meaningful baseline (e.g., a linear probe on the model's own representations, or a model trained on the same pixels but with the core feature being the only available one).

### Minor

- **Claims of "inevitability" exceed the scope of the evidence**. The abstract says shortcut bias is "a fundamental characteristic of deep nonlinear architectures" and the introduction says it is "an inevitable consequence of nonlinear architectures" (line 42). The theory is limited to: two-layer networks, a quadratic approximation of the ReLU kernel, a small-covariance asymptotic, and a sensitivity metric (not the empirical bias). No other activations (Tanh, GELU) are analyzed theoretically, and depth effects — which the experiments show amplify bias — are outside the theory's scope. The conclusion (line 353) does qualify "for a single-hidden-layer nonlinear (ReLU) MLP," but the abstract and intro do not. This invites justified skepticism and weakens the paper on a dimension that matters for its central rhetorical arc.

- **No error bars or variance estimates on any figure**. All figures report only means. Given the relatively small training set (3200 samples) and the complexity of the bias measure, variance across random seeds could be substantial. Without error bars, the reader cannot assess whether the observed patterns, especially at boundary conditions where bias changes sign, are reliable.

- **No sensitivity analysis for fixed experimental parameters**. The synthetic experiments fix d=100, n_train=3200, σ_sc=0.6, and probe-grid bounds ±3μ. The paper does not test whether the main findings (bias increases with availability ratio, nonlinear models show more bias than linear ones) hold across variations in these choices, so it is unclear whether the results are artifacts of specific parameter settings.

- **No discussion of alternative explanations**. The paper attributes shortcut bias to availability, but other mechanisms could produce similar patterns — for example, simplicity bias (models learning simpler functions first during training), spectral bias (preference for low-frequency functions), or differences in learning speed between features. The NTK analysis provides one candidate mechanism, but the paper does not consider or rule out alternatives. A limitations paragraph acknowledging this would strengthen the paper.

### Trivial

- The reliance measure is defined over a uniform probe grid in latent space (±3μ), but the paper does not discuss sensitivity to grid resolution, range, or the fact that the uniform grid differs substantially from the training distribution (Gaussian mixture).

## Nice-to-Haves

- It would be informative to compute the empirical bias measure directly from the NTK predictor for the synthetic Gaussian mixture setting (even numerically with the quadratic kernel) to bridge the theory-experiment gap.
- For the naturalistic experiments, the paper could compare models against a classifier trained on the same pixels but with the core feature being the only available feature (e.g., a ResNet with the background masked out) to provide a meaningful availability baseline.
- Sensitivity analyses varying d, n_train, and σ_sc in the synthetic experiments would increase confidence that the effects are not parameter artifacts.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper does not discuss how pretraining affects availability bias"** (from harsh critic's Section-by-Section notes). The paper does address this at line 346, noting that ImageNet-pretrained models also exhibit the phenomenon. This criticism is factually incorrect about the paper's content.

- **Criticisms about missing appendix content / proofs in appendix** (multiple locations). The parser strips appendix sections from all papers; they exist in the original submission. These are parser artifacts, not author omissions.

- **"The paper would need to either (a) derive the empirical bias in the NTK framework... or (b) explicitly acknowledge that the theory addresses a different quantity"** — this demand for theory-experiment bridging is valid as a weakness but the phrasing that it's a "structural" issue is too strong. The theory does address a related quantity (sensitivity to availability) and independently arrives at the same qualitative conclusion (ReLU biased, linear unbiased). The gap is real but the paper does not claim formal equivalence; it calls the theory "an alternative approach" and describes findings as "consistent." Retained as Major but reframed.

- **"No discussion of alternative explanations"** is kept as a Minor weakness. This is a genuine gap.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a key structural tension: the paper's theoretical contribution (NTK sensitivity analysis) and its empirical contribution (bias = reliance_model − reliance_optimal) are only loosely coupled. Both point in the same direction, but neither the paper nor the reviews identify a way to formally connect them. This suggests an open problem for the field: developing measures of "feature reliance" that are simultaneously amenable to theoretical analysis from the kernel perspective and to practical measurement in trained networks. The paper's framework for independently manipulating predictivity and availability is a useful step toward making this problem tractable.

## Suggestions

1. Either bridge the theory and experiments (e.g., compute the empirical bias metric from the NTK predictor for the Gaussian mixture setting) or explicitly reframe the theory as a separate, independent argument about sensitivity of predictions to availability scaling — not an account of the specific bias measure.

2. Either present the nesting experiments or remove the nesting factor from the paper's claimed contributions. If results exist in the appendix, summarize them in the main text.

3. Define the "Bayes-optimal classifier" for Waterbirds and CelebA explicitly, or replace it with a defensible baseline.

4. Temper the "inevitability" and "fundamental characteristic" claims to match the theoretical scope (two-layer ReLU networks with a quadratic kernel approximation).

5. Add error bars (or intervals) to all figures and include a sensitivity analysis for at least the most critical fixed parameters (d, σ_sc, grid range).

## Score and Decision

This paper addresses an important problem — why models privilege certain features beyond what predictivity would dictate — and makes a genuine contribution by providing a clean experimental framework for separating predictivity from availability. The synthetic experiments are well-designed and the core finding (nonlinear models exhibit availability bias, linear models do not) is convincingly demonstrated. The NTK analysis is an ambitious attempt at a mechanistic explanation, and the naturalistic experiments suggest the framework transfers beyond synthetic data.

However, the paper has three significant gaps that prevent it from being a complete contribution in its current form: (1) the theory and experiments measure different things without a formal or even clearly argued connection; (2) the nesting factor — half of the proposed framework — is introduced but never empirically validated; (3) the central claim about naturalistic data ("heightened sensitivity beyond a statistical account") rests on an undefined optimal baseline. These are not fatal — they do not invalidate the core synthetic experiments — but they mean the paper's strongest claims (theoretical inevitability, naturalistic evidence of availability trumping predictivity) are not fully supported. With substantial revisions to address these gaps, the paper could make a solid contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>