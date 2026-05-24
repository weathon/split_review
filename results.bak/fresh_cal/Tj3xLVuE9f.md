Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper introduces the concept of "availability" (distinct from predictivity) to explain shortcut learning, proposes a generative framework for independently manipulating predictivity and availability in synthetic datasets, and presents empirical results showing that nonlinear models systematically prefer more-available features even when they are less predictive. A theoretical NTK analysis (2-layer infinite-width, with approximations) proves linear networks are unbiased while ReLU networks exhibit availability bias. Experiments on naturalistic images (Waterbirds, CelebA) demonstrate related phenomena in practice-relevant settings.

## Strengths

1. **Clean generative framework disentangling predictivity and availability.** Section 3 defines independent parameters for predictivity (ρ_i via μ_i) and availability (amplification α_i and nesting η_i), enabling controlled experiments that prior work (e.g., Pezeshki et al., 2021, which confounded these under a single "strength" notion) could not perform. The heatmap in Figure 2 systematically varies both axes and directly tests the paper's central claim that availability can override predictivity.

2. **Clear demonstration that nonlinearity is necessary for shortcut bias.** Figure 3B compares linear, ReLU, and Tanh activations in matched architectures on the same data: linear activations yield near-zero bias, while both nonlinear activations produce substantial bias. Figure 3C further shows that a single hidden ReLU layer suffices, whereas linear hidden layers do not produce bias. This cleanly ties the phenomenon to nonlinearity in a controlled way.

3. **Theoretical NTK proof that availability bias is absent in linear networks but present in ReLU networks.** Theorems 5–7 provide a formal mathematical result showing the sensitivity difference |ζ₁|−|ζ₂| is identically zero for all m≥1 in linear networks, while for ReLU networks the first non-zero term appears at m=9 with an explicit form linking predictivity (μ_i) and availability (a_i). Though limited by the 2-layer infinite-width setting and quadratic kernel approximation, this gives a principled explanation for why linear vs. nonlinear networks differ qualitatively.

4. **Extension to naturalistic datasets.** Section 7 shows that ResNet-18 trained on Waterbirds and CelebA relies on non-core features beyond what a Bayes-optimal classifier would predict, and that explicit availability manipulations (spatial extent, color) shift feature reliance. This connects the controlled findings to real-world shortcut learning phenomena.

## Weaknesses

### Major

1. **Theory–empirics gap and overclaimed scope.** The NTK analysis (Section 6) is conducted for a *two-layer infinite-width* network with additional approximations (small covariance, quadratic ReLU-kernel approximation). Yet the abstract and contributions say the theory "indicates that shortcut bias is an inevitable consequence of nonlinear architectures," a generalization far beyond what the theory's setting supports. The conclusion appropriately scopes this to "a single-hidden-layer nonlinear (ReLU) MLP," but the stronger language in the abstract and contributions is misleading. Moreover, the theory uses a sensitivity measure (high-order derivatives of alignment) that is never directly validated against the empirical bias measure in the same 2-layer setting the theory covers. The paper provides qualitative consistency rather than quantitative verification of the theoretical prediction.

2. **Missing statistical reporting.** The central experiments (Figures 2, 3A, 3B, 3C) report only mean bias values. There is no mention of the number of random seeds, no error bars, confidence intervals, or variance information. Given that the generative procedure involves random embedding vectors (w_i) and random weight initializations, the variance across seeds could be substantial. The paper makes parametric claims ("model depth increases shortcut bias," "model nonlinearity increases shortcut bias") without statistical support, making it impossible to assess the reliability of individual cells in the heatmap or whether observed differences are significant.

3. **Nesting experiments mentioned but not presented.** Section 4 states: "We also conducted experiments manipulating a second factor we expected would affect availability... the relative nesting of representations, i.e., η_c − η_s ≥ 1." Despite nesting (η) being introduced as a core component of availability in Section 3, no results from these experiments are shown anywhere in the paper. This is a significant gap given the paper's claim to study two availability factors.

### Minor

1. **Additive embedding assumption not discussed as a limitation.** The generative procedure combines feature embeddings by summation (x = e'_s + e'_c), assuming the two features' representations are additive in pixel space. In natural images, features often interact non-additively (e.g., texture and shape). The paper does not discuss this assumption as a limitation.

2. **Pixel-footprint experiment connects to α only by hypothesis.** Section 5 treats object size as a direct proxy for the amplification parameter α, but no formal relationship is established between pixel footprint and the α parameter from the generative model. The experiment shows that object size affects bias, which is interesting, but asserting it instantiates the same "availability" mechanism requires an additional leap.

3. **Confounding in naturalistic availability manipulations.** The manipulations in Figure 6C (bird size, background patch removal, color drop) are intended to reduce non-core (background) availability, but they may also affect core (bird) feature availability (e.g., making the bird larger increases its pixel footprint, which the paper argues increases *its* own availability). The direction of this potential confound is not discussed.

4. **No discussion of limitations.** The paper ends without discussing limitations of the generative framework (additive embedding, Gaussian latent assumption) or the theoretical analysis (approximations, narrow setting), which would help readers calibrate the scope of the contributions.

### Trivial

None.

## Nice-to-Haves

- Validate the theoretical prediction (sign of |ζ₁|−|ζ₂| vs. empirical bias) directly in the 2-layer, large-width setting the theory covers, to bridge the theory–empirics gap.
- Report nesting (η) experiment results that are mentioned as completed but not shown.
- Include error bars or confidence intervals for all main figures.
- Show the effect of varying training set size to further address finite-sample concerns.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Finite-sample conflation with availability bias (Harsh Critic Critical Issue 2):** The critic argues that the bias measure (reliance_model − reliance_optimal) could capture finite-sample estimation error rather than availability bias. However, the paper's own experiments already address this: linear models trained on the *same* 3200 samples show near-zero bias, while nonlinear models on the same data show substantial bias. If the effect were driven by finite-sample noise, both would be affected. The paper's design (optimal classifier from the known generative distribution, not estimated from data) also avoids conflating estimation error with bias. This criticism is not well-supported by the evidence in the paper.

- **CelebA Bayes-optimal classifier computation (from Harsh Critic Section 7):** The critic questions how the Bayes-optimal boundary is computed for CelebA, but the paper references Supplementary Materials for details. Per meta-reviewer guidelines, missing appendix content (stripped by the parser) should not be penalized.

- **Concerns about 9th-order derivative tenuousness (Harsh Critic Critical Issue 3):** While the specific 9th-order derivative result is not directly validated, the theory's core qualitative prediction (linear networks → no bias, ReLU networks → bias) is directly and cleanly validated by experiments in Figure 3B/3C. The critic's framing that the theory is "tenuously linked" understates the clear qualitative consistency that the paper demonstrates and acknowledges.

- **Generic criticisms about "availability" being operational rather than abstract (Section-by-Section note on Section 1):** The paper explicitly defines availability *operationally* via α and η, which is standard and appropriate for an empirical paper. The critic's call for a more abstract definition is a philosophical preference, not a flaw.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper that is not already present in or directly derivable from the paper's own framing.

## Suggestions

1. **Scope the theory claim precisely.** Replace "inevitable consequence of nonlinear architectures" (abstract, contributions) with language that explicitly reflects the 2-layer infinite-width setting and approximations used. In the conclusion, where this is already done well, the abstract and contributions should match.

2. **Add error bars and seed counts** to all main figures. Report the number of random seeds used and show standard deviations or confidence intervals, especially for the heatmap in Figure 2 where individual cell values are currently uncalibrated.

3. **Either show the nesting experiment results** (Section 4) or remove the claim that they were conducted. If the experiments were done, present them with the same rigor as the amplification experiments; if not, remove the sentence.

## Score and Decision

The paper makes a meaningful contribution by formalizing the role of feature availability in shortcut learning and providing a controlled framework for studying it. The empirical finding that nonlinearity is necessary for shortcut bias is cleanly demonstrated. The theoretical analysis provides suggestive formal support. However, the paper overclaims the scope of its theory, lacks basic statistical reporting for its central results, and mentions key experiments (nesting) that it does not present. These weaknesses are fixable but currently undermine the reliability and precision of the paper's strongest claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>