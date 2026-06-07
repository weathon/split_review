## Summary

This paper studies the effect of the L0 sparsity hyperparameter in sparse autoencoders (SAEs) for LLM interpretability. Using toy models with known ground-truth features, it demonstrates that setting L0 too low causes SAEs to mix correlated features to improve reconstruction at the cost of monosemanticity — producing latents that score *better* on MSE than a correct ground-truth SAE at the same low L0. The paper proposes a diagnostic metric (c_dec, pairwise absolute cosine similarity of decoder vectors) that is minimized at the true L0 in toy models, and shows that the "elbow" of the c_dec curve in real LLM SAEs (Gemma-2-2b, Llama-3.2-1b) coincides with peak performance on k=16 sparse probing tasks. The core claim is that L0 is not a free parameter: if set incorrectly, the SAE cannot learn correct features.

## Strengths

- **Clean toy model demonstration that low-L0 SAEs mix correlated features (Sections 3.1–3.2, Figures 2–3):** The paper constructs toy models satisfying the linear representation hypothesis (orthogonal features, correlated Bernoulli firing) and shows, via decoder cosine similarity heatmaps, exactly how an SAE with L0 below the true L0 blends positively-correlated features and negatively-correlated features. The experiment initializing the low-L0 SAE to the ground-truth solution and observing gradient pressure move it away (Section 3.1) is particularly convincing — it proves the mixing is an MSE-driven effect rather than a local-minimum artifact.

- **Direct counterexample to the assumption that better reconstruction implies better features (Section 3.3–3.4, Figure 4):** At L0=5 (below the true L0=11), the ground-truth SAE achieves MSE 4.88 while a trained SAE with polysemantic latents achieves MSE 2.73. Figure 4 sweeps all L0 values and shows the trained SAE consistently beats the ground-truth SAE on variance explained below the true L0. This is a clean, quantifiable refutation of the field's default assumption that better sparsity-reconstruction tradeoff = better SAE.

- **Real LLM validation connecting c_dec to sparse probing performance (Section 4, Figures 8–9):** The paper trains 32k-latent BatchTopK SAEs on Gemma-2-2b and Llama-3.2-1b across a range of L0 values and shows the "elbow" in the c_dec curve (the sharp increase at low L0) aligns with peak F1 on the k=16 sparse probing benchmark. This links the toy-model mechanism to actual downstream task performance on two model families, a non-trivial empirical validation.

- **JumpReLU SAEs replicate the core finding and reveal a "sticking" property (Section 3.6, Figure 7):** The c_dec minimum at the true L0 also holds for JumpReLU SAEs, and the paper observes that JumpReLU L0 "sticks" near the correct value across a wide range of λ_s — an architectural insight that helps explain why JumpReLU SAEs degrade less at high L0 than BatchTopK SAEs.

## Weaknesses

### Fatal
None.

### Major

1. **The c_dec metric has an unaddressed geometric confound in overcomplete dictionaries.** The metric averages pairwise absolute cosine similarity between all decoder vectors. In the real SAEs, h=32768 and the residual stream dimension is d=2048. Since at most 2048 vectors in ℝ²⁰⁴⁸ can be mutually orthogonal, the remaining ~30,000 decoder vectors are *necessarily* non-orthogonal by geometry alone — regardless of L0, training, or feature mixing. The observed c_dec values (~0.02 in the real SAEs) could be dominated by this geometric baseline. The toy model avoids this issue entirely (h=g=50, d=100, so all 50 vectors *can* be orthogonal), making the toy → real transfer of the metric qualitatively different from what the paper assumes. The paper does not subtract an expected baseline (e.g., the expected c_dec of 32768 random unit vectors in ℝ²⁰⁴⁸) or otherwise attempt to isolate the L0-driven signal from the geometric baseline. This is a significant evidential gap for the metric's main claimed use case.

2. **The central framing of a single "correct L₀" is in tension with the paper's own findings in Section 4.2.** The paper's title, abstract, and core argument are built around the existence of a single true L₀ — the average number of "true features" firing per token. This is well-defined in the toy model, where features are orthogonal and firing probabilities are fixed. However, Section 4.2 observes that at L₀=750 on real SAEs, "some latents become more monosemantic while other latents mix underlying features becoming less monosemantic" and concludes "there is likely a range of L₀s where some latents are firing more than they ideally should while other latents are firing less." This is a significant concession: it suggests the "correct L₀" is not a single number but a distribution across latents, and that the toy model phenomenon (where a single L₀ suffices because all features have the same firing probability) may not map cleanly onto real LLMs. The paper does not adequately reconcile this tension.

3. **The claim that "most commonly used SAEs have an L₀ that is too low" (abstract, introduction) is asserted without systematic support.** This headline claim is supported only by a reference to a "cursory search of open source SAEs on Neuronpedia" in Appendix A.13. Even if the appendix provides some evidence, the strength of the claim in the abstract is disproportionate to its support. This is a presentational overreach that a reader may reasonably object to.

### Minor

1. **No comparison of c_dec against existing SAE quality heuristics.** The paper proposes c_dec as a guide for L₀ selection but does not compare it against any existing metric (e.g., reconstruction MSE at fixed L₀, explained variance, number of dead latents, or feature interpretability scores from automated interpretability). A simple comparison — even on the toy model where ground truth is known — would clarify whether c_dec provides complementary information or merely correlates with existing measures.

2. **The toy model uses exactly orthogonal features, while the LRH posits *nearly* orthogonal features.** The paper acknowledges this framing (line 13, 59: "(nearly) orthogonal") but does not analyze how small deviations from orthogonality in the true features would affect c_dec's baseline. If true features have small non-zero cosine similarity, c_dec would show a positive baseline even for a correct SAE. This is a gap between the idealized toy model and the real setting.

3. **The sparsity-reconstruction critique relies on an artificial ground-truth SAE construction.** The ground-truth SAE with fixed encoder/decoder forced to L₀=5 is a theoretical construct, not a realistic alternative architecture. While the argument is conceptually valid, framing it as a practical critique of how "most SAE papers" evaluate architectures (line 117) overstates its relevance to standard practice, where comparisons are between *trained* architectures, not against a hand-constructed ground-truth SAE.

### Trivial

1. Line 153: "We calculate pairwise calculate similarity c_dec for each of the BatchTopK SAEs we trained on toy models from Section 3.5" — should reference Section 3.2 (where the SAEs are trained), not Section 3.5 (which introduces c_dec). This is a self-reference/typographical error.

## Nice-to-Haves

- Normalize c_dec by subtracting the expected pairwise cosine similarity of h random unit vectors in ℝᵈ, so the metric isolates L₀-driven signal from the geometric baseline of overcomplete dictionaries.
- Provide qualitative feature examples (e.g., top-activating text snippets for a latent at L₀=50 vs L₀=200 vs L₀=1000) to ground the "feature mixing" claim in human-readable evidence, complementing the quantitative proxy metrics.
- Tone down the "single correct L₀" framing in the title/abstract, or add a dedicated discussion of how the concept maps to real LLMs where features are non-orthogonal and have heterogeneous firing probabilities.

## Removed Points

These points were flagged by reviewers but are removed as invalid, speculative, or misreadings:

- **Harsh critic's claim that the sparsity-reconstruction critique is overstated**: The critic argued these plots compare architectures at the same L₀ (not determine correct L₀). But the paper's Figure 4 *does* compare two SAEs at the same L₀ and shows the incorrect one wins — this is a valid critique that the critic misread. **Removed.**
- **Harsh critic's suggestion that JumpReLU "sticking near correct L₀" is only shown in toy models**: This is true by definition — the "correct" L₀ can only be verified where ground truth exists. The paper does not claim otherwise. **Removed.**
- **Strength Finder's generic/superficial claims about the importance of the problem**: These are generic statements that do not constitute concrete evidence-based strengths. **Removed.**
- **Harsh critic's criticism about statistical significance (3 seeds for LLM experiments)**: Standard practice in this field for large-scale SAE training runs. **Removed as scope creep.**
- **Criticism about missing qualitative evidence being a "notable gap"**: The paper's claims are about feature quality as measured by c_dec and sparse probing; qualitative evidence would strengthen but is not required for the paper's core contributions. Demoted to Nice-to-Have.

## Novel Insights

The most interesting observation not fully explored by the paper is the connection between Section 4.2's finding (different latents may need different L₀s) and the JumpReLU "sticking" property. The paper notes JumpReLU SAEs degrade less at high L₀ because per-latent thresholds can adapt, but it does not connect this to Section 4.2's finding that BatchTopK SAEs at intermediate L₀ (750) simultaneously have some latents that are too active and others too inactive. This suggests that the "correct L₀" question may be better framed as a per-latent threshold optimization problem rather than a global hyperparameter search — a direction the paper gestures at but does not develop. The c_dec metric's "elbow" (the point before the low-L₀ jump) may be capturing the threshold below which the *most frequent* features begin to hedge, not a single correct value for all features.

## Suggestions

1. **Address the geometric confound directly.** Compute the expected c_dec for 32768 random unit vectors in ℝ²⁰⁴⁸ and subtract it from your real-SAE c_dec values. If the L₀-driven signal survives this correction, the metric is on much firmer ground.
2. **Reframe the contribution.** Instead of "find the single correct L₀," present the contribution as: "L₀ being too low is harmful because it incentivizes feature mixing; practitioners should err higher or use adaptive per-latent methods (JumpReLU). The c_dec elbow provides a heuristic lower bound."
3. **Add a comparison table** of c_dec vs. MSE, explained variance, and dead latent fraction across the L₀ sweep for both toy and real SAEs, to clarify whether c_dec captures information these existing metrics miss.
4. **Soften the "most SAEs have too-low L₀" claim** or support it with a systematic audit, not a cursory search.

## Score and Decision

### Calibration Anchors

| Path | Avg Human Score | Round | Comparison to this paper |
|------|----------------|-------|------------------------|
| Sparse Autoencoders Do Not Find Canonical Units of Analysis (ICLR 2025) | 7.00 | R1 | **Stronger** — more novel methodology, cleaner experiments, far more minor weaknesses |
| Towards Principled Evaluations of Sparse Autoencoders | 7.00 | R2 | **Stronger** — principled framework, rigorous evaluation, fewer evidential gaps |
| Beyond Interpretability: Gains of Feature Monosemanticity | 5.80 | R2 | **Slightly weaker** — less direct SAE relevance, but accepted |
| Incidental Polysemanticity | 5.67 | R2 | **Comparable** — similar toy-model → implications structure, similar weakness profile; rejected |
| Applying Sparse Autoencoders to Unlearn Knowledge | 5.25 | R2 | **Comparable** — both have real SAE experiments with similar limitations |
| SAEs Find Highly Interpretable Features in LMs (ICLR 2024) | 4.80 | R1 | **Comparable** — pioneering work with outlier low score; this paper has cleaner experiments |
| Compute Optimal Inference in SAEs | 4.67 | R1 | **Weaker** — limited real experiments, theoretical concerns; rejected |

### Round 1 Bracket
Between 3.5 (weak band) and 7.5 (strong band), specifically between 4.5 and 6.5 after examining the middle-band anchors.

### Round 2 Narrowing
The paper is weaker than the 7.00 anchors (geometric confound, framing tension) but stronger than the 4.67–4.80 anchors (has real LLM validation the weaker papers lack). Compared to Incidental Polysemanticity (5.67, Reject) — a structurally similar paper — this paper has better real-world validation but a more significant methodological weakness (geometric confound). This places it around 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>