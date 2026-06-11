## Summary

This paper proves a first-order equivalence between activation steering (adding vectors to intermediate activations during inference) and influence functions (tracing the effect of re-weighting training data on model outputs). It introduces Influence-Aligned Steering (IAS), a constructive algorithm that maps between steering vectors and training-data influence weightings, along with: (i) a principal-angle diagnostic γ that quantifies when steering can faithfully substitute for weight-space editing, (ii) a spectral optimality result for choosing steering directions under an ℓ₂ budget, and (iii) generalization bounds for low-rank steering interventions. Experiments on GPT-2 Medium validate the first-order linearity (cosine 0.978 between predicted and actual logit shifts) and show that γ increases monotonically with layer depth.

## Strengths

1. **Closed-form duality between steering and influence (Theorem 4.2).** The paper proves that any steering vector can be represented as a signed influence measure over training data, and vice versa, with an explicit construction whose ℓ₁ norm equals the steering magnitude |α|. This is the first closed-form mapping between two previously separate interpretability techniques.

2. **Alignment diagnostic γ with tight no-free-lunch bounds (Theorems 5.1, 6.2).** The principal-angle cosine γ quantifies when activation steering can faithfully reproduce the effect of a parameter perturbation, and the bound √(1−γ²) on the relative logit error is tight (proved by Theorem 6.2). This gives practitioners a concrete, computable criterion for deciding when steering is feasible, using only two small SVDs.

3. **Empirical validation of first-order equivalence (Section 7.2, Figure 1).** Over 5000 prompt-token pairs on GPT-2 Medium, predicted and actual logit shifts from IAS achieve cosine 0.978. This directly confirms the core duality on a realistic model and dataset, not a toy setting.

4. **Explicit computational cost model.** The paper clarifies that all quantities reduce to two Jacobian-vector products per input, a rank-d pseudoinverse (bounded by layer width, not model size), and a small SVD — making the practical viability transparent.

5. **Layer-depth alignment analysis (Section 7.3, Figure 2).** The paper empirically demonstrates that γ increases monotonically with layer depth (from 0.64 at layer 0 to 0.94 at layer 11), validating the theory's prediction that later layers offer better subspace overlap and providing a concrete heuristic for practitioners.

## Weaknesses

### Major

1. **IAS underperforms CAA on detoxification without discussion (Table 1).** IAS achieves toxicity 0.0164 versus CAA's 0.0150 and perplexity 13701 versus CAA's 13291 — worse on both metrics. The paper presents this comparison without any analysis or explanation. Since IAS is presented as a principled alternative that subsumes heuristic methods like CAA, this gap needs to be addressed (e.g., IAS optimizes a different objective; the first-order approximation breaks down at the tested magnitude; CAA's contrastive construction is better suited to this particular task).

2. **Systematic 50% scaling bias in Figure 1 is not addressed.** The linearity experiment shows a slope of 1.50, meaning actual logit shifts are on average 50% larger than first-order predictions. The paper describes this as "consistent with the expected linear regime," but a slope of 1.50 is a systematic quantitative error, not random fluctuation around the identity line. This matters because the core equivalence (Theorem 4.2) is first-order; the 50% gain factor could affect the claimed correspondence between steering magnitudes and influence weights at finite α. The paper should explain this discrepancy (e.g., as an effect of the damping regularizer λ or second-order curvature) or acknowledge it as a limitation.

### Minor

3. **Corollary 1 proof sketch is incomplete.** The "Idea of the proof" for ℓ₁-minimality argues that if another measure ν achieved the same shift with smaller norm, one could "scale ρ_s down and still match the shift, contradicting the definition of α as the steering magnitude." This reasoning does not hold as written — the existence of ν with smaller norm does not straightforwardly imply anything about scaling ρ_s. The claim is likely correct (it follows from basic-pursuit duality) but needs a proper argument. Since this corollary underlies the "trace provenance" practical claim, a correct proof matters.

4. **Theorem 5.3 (Spectral Optimality) objective is underspecified.** The theorem claims the top eigenvector of Σ maximizes "expected first-order logit change" without stating what "expected" means or over what distribution. The matrix Σ is defined over training-data quantities (J_{θ→h}, H_θ^{-1}, ∇_θ ℓ), while the logit change at a test point involves J_{h→y}(x). The connection between Σ and the logit-change objective needs clarification.

5. **Theorem 6.1 analyzes weight-space modification, not activation steering.** The bound models the intervention as a rank-k additive perturbation to the weight matrix (αUV^⊤). While implementing activation steering may be equivalent to such a perturbation, the paper treats activation steering as adding to activations during inference (frozen weights) and does not justify the equivalence. The generalization bound may apply to a different operation than the method actually used.

6. **Theorem 6.2 (No-Free-Lunch) statement is ambiguous.** The theorem refers to "the corresponding (best-possible) parameter perturbation Δθ" but does not specify the coupling between Δh and Δθ. Without a clear constraint relating them, the ratio can be made arbitrarily small by picking a small Δθ, trivially satisfying the bound.

7. **Equation 2 in Section 3 has an error.** From λ^* = -(J_{h→y} J_{h→y}^⊤)^† J_{θ→y} Δθ and Δh^* = J_{h→y}^⊤ λ^*, the resulting expression should be Δh^* = J_{h→y}^⊤ (J_{h→y} J_{h→y}^⊤)^† J_{θ→y} Δθ = J_{h→y}^† J_{θ→y} Δθ, not Δh^* = J_{h→y}^⊤ J_{θ→y} Δθ as written.

8. **Affine independence assumption in Corollary 1 is very strong.** With |𝒵| ≫ m (logit dimension typically much smaller than dataset size), the influence vectors are necessarily linearly dependent, making the assumption violated in most practical settings. This limits the corollary's applicability.

9. **The claimed "steer → trace provenance" workflow is never demonstrated.** The paper motivates the practical pipeline of tracing a steering vector back to its most causal training examples (lines 118, 130), but provides no experiment showing this. This is the paper's most distinctive practical claim and its absence weakens the empirical narrative.

### Trivial

- Lemma 5.4 expresses γ₁γ₂ as √(1−(1−γ₁²))√(1−(1−γ₂²)), which is just the same product written in terms of sines — this adds no simplification and appears to be a formatting artifact.

## Nice-to-Haves

- Confidence intervals or error bars on experimental results would be helpful given the small scale (50 prompts to construct vectors).
- Computing the Hessian inverse H_θ^{-1}v at scale for billion-parameter models is a practical challenge; the paper references Appendix D.1 (stripped from this version) but a brief note on the method used would improve the main text's self-containedness.

## Removed Points

These points from the harsh critic were removed or downgraded after verification:
- **"Corollary 1 proof is logically incoherent"** → Downgraded to Minor (incomplete sketch, not incoherent). The sketch is flawed but the claim is likely correct and provable with proper LP duality arguments.
- **"The Hessian size makes it intractable; paper never states how H_θ^{-1}v is computed"** → Partially removed. The paper bounds the pseudoinverse to layer width d (not model size P) and references Appendix D.1 for details — this is a standard scalable approach.
- **"No error bars"** → Moved to Nice-to-Have. While desirable, single-run evaluations are common in this setting and do not invalidate results.
- **"Computational budget underspecified"** → Partially removed. The paper explicitly lists two JVPs, a rank-d pseudoinverse, and a small SVD as the cost model.
- **"Lemma 5.4 'expanded form' adds nothing"** → Retained in Trivial as a minor presentation note.

## Novel Insights

None beyond the paper's own contributions. The meta-review surfaces that the paper has a systematic mismatch between its theoretical ambition and empirical demonstration: the central practical claim (steer → trace provenance) and the explanation of why IAS underperforms CAA are both absent, while the theoretical presentation has several gaps (Corollary 1 sketch, Theorem 5.3 specification, Theorem 6.2 ambiguity, Equation 2 error) that individually are minor but collectively undercut the paper's reliability. The paper would be stronger if it acknowledged these gaps and focused on what is solid (the duality, the γ diagnostic) rather than overclaiming a complete practical workflow.

## Suggestions

1. **Explain IAS vs CAA on detoxification.** Analyze whether the relative underperformance reflects a limitation of the first-order theory, a task misalignment (IAS optimizes for matching influence, not detoxification), or simply variance.
2. **Address the slope 1.50 in Figure 1.** Explain theoretically (e.g., as a consequence of the damping regularizer λ) or explicitly acknowledge it as a limitation of the first-order approximation at finite α.
3. **Fix the proof sketch for Corollary 1** with a correct argument using linear programming duality or basis pursuit.
4. **Clarify Theorem 5.3:** Specify what "expected first-order logit change" means and show the derivation connecting Σ to the logit-change objective.
5. **Demonstrate the provenance workflow at least once** (e.g., a toxicity steering vector traced back to the most influential training examples).
6. **Fix Equation 2** to include the proper pseudoinverse.
7. **Specify the coupling in Theorem 6.2** between Δh and Δθ.

## Calibration Report

**Round 1 bracket:** 3.5 – 6.0. The paper is clearly above papers like "Feature Selection with Neural Estimation" (2.33) and "KARA" (2.0), and clearly below strong accept papers like "NeurFlow" (6.5) or "Capturing Temporal Dependence of Training Data Influence" (8.0).

**Round 2 narrowing:** The two most topically similar anchors are "From Steering Vectors to Conceptors and Beyond" (avg 5.0, rejected) and "Steering Language Models with Activation Engineering" (avg 5.0, rejected). Both propose theoretical frameworks for activation steering. Our paper has comparable theoretical novelty but weaker empirical results — IAS underperforms CAA (the baseline) whereas the Conceptors paper outperforms its baselines. The systematic slope 1.50 bias also raises concerns. Hence our paper sits slightly below these anchors.

**Final anchors considered:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| lt6xKGGWov (Feature selection with neural estimation) | 2.33 | R1 | Clearly worse — much less substantial |
| OBrTQcX2Hm (KARA) | 2.00 | R1 | Clearly worse — thin contribution |
| z1yI8uoVU3 (Measuring Effects of Steered Representation) | 3.00 | R1 | Lower quality — evaluative, no theory |
| 9wjGUN65tY (Steering Vectors → Conceptors) | 5.00 | R1,R2 | Most comparable; similar theory but stronger experiments (outperforms baselines) |
| 2XBPdPIcFK (Activation Engineering) | 5.00 | R1,R2 | Comparable; less theory, stronger experiments |
| DKCtt2iqfw (Channel-wise Influence) | 5.50 | R1 | Related (influence functions) but different domain |
| GdbQyFOUlJ (NeurFlow) | 6.50 | R2 | Stronger — better experiments and clarity |

## Score and Decision

**Score:** 4.5  
**Decision:** Reject

The paper identifies a genuinely interesting connection between two active research areas and provides a clean geometric framework (the γ alignment diagnostic). The duality (Theorem 4.2) and alignment bound (Theorem 5.1) are real contributions. However, the paper is weakened by experimental gaps (IAS underperforms the baseline CAA without discussion, the slope 1.50 systematic bias is not explained, the core practical workflow is not demonstrated) and several theoretical presentation issues (Corollary 1 proof sketch, Theorem 5.3 specification, Theorem 6.2 ambiguity, Equation 2 error). These issues collectively prevent the paper from delivering on its claimed practical narrative. With the empirical and theoretical gaps addressed, this framework could form the basis of a compelling revision.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>