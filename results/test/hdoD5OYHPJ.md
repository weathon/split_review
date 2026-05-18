Now I have a thorough understanding of the paper and can verify each claim. Let me produce the final consolidated review.

## Summary

This paper proposes AutoCLIP, a method that improves zero-shot VLM classifiers by reweighting prompt templates per image at inference time. Instead of uniformly averaging encoded class descriptors, AutoCLIP performs one step of gradient ascent on a logsumexp objective to assign higher weights to templates whose descriptors are more similar to the image embedding, with the step size automatically determined via bisection to control weight entropy. Extensive experiments across 8 datasets, 6 VLMs, 3 prompt strategies, and varying prompt counts (990 total settings) show consistent but modest improvements (0.45pp average, up to 3pp) over standard uniform weighting.

## Strengths

- **Consistent empirical improvements across a broad evaluation**: AutoCLIP outperforms the standard zero-shot baseline in 840 out of 990 tested combinations (≈85%) with an average improvement of 0.45 percentage points, across 6 VLMs, 8 datasets, and 3 prompt strategies (Figure 1, Table 1). Gains are positive on virtually every dataset except EuroSAT and hold across varying prompt counts (K=4 to K=500). This is a thorough and convincing evaluation.

- **Principled and hyperparameter-light design**: The entropy-controlled step size selection (β=0.85 globally, Section 3.4) replaces the dataset-dependent step size α with a single interpretable parameter. The ablation (Figure 3) shows that performance is relatively stable for β∈[0.7,0.9], meaning the method is not brittle to this choice. For a zero-shot setting where labeled tuning data is unavailable, this is a genuine practical strength.

- **Method operates entirely in embedding space, avoiding additional encoder passes**: Unlike test-time prompt tuning methods (TPT, RLCF) that require multiple image augmentations and backpropagation through the text encoder, AutoCLIP's adaptation is a pure embedding-space operation (Algorithm 2). The closed-form gradient computation (Section 3.3) further eliminates the need for automatic differentiation, which is relevant for edge deployment.

- **Extensive evaluation scope and clean experimental design**: The paper tests 6 VLMs (RN50, ViT-B/32, ViT-B/16, ViT-L/14, DataComp ViT-L/14, CoCa ViT-L/14), 8 datasets (including ImageNet variants for robustness), 3 prompt construction methods, and varying K with 7 runs each. The controlled synthetic experiment (Section 5) provides a mechanistic illustration of when and why AutoCLIP helps, using an interpretable entanglement parameter.

- **Qualitative analysis supports the guiding intuition**: Figure 5 shows that AutoCLIP assigns higher weights to semantically relevant templates (e.g., "photo of…" for food images) and lower weights to irrelevant ones (e.g., "tattoo of…"), with weights being consistent within a class.

## Weaknesses

### Fatal
None.

### Major

- **No quantitative runtime or efficiency analysis**: The paper repeatedly claims "minor additional computation overhead" (abstract, Section 1, Section 4, conclusion) but provides zero quantitative evidence — no wall-clock time, no bisection iteration counts, no FLOPs comparison, not even an order-of-magnitude estimate. The bisection procedure (Algorithm 2, Line 18) solves for α on [0, 10¹⁰] and requires multiple evaluations of softmaxentropy(α·g); without knowing how many iterations are typical (e.g., 10? 50?), the reader cannot evaluate the central claim that this is "cheap" compared to test-time prompt tuning. While the paper correctly argues that no *encoder* forward/backward passes are needed (unlike TPT), the actual overhead of the bisection + gradient step is never measured. This is a gap that should be addressed.

**Why this is major**: The paper explicitly frames computational efficiency relative to TPT as a key advantage (Section 1: "significantly lowers the test-time computation and memory overhead compared to prior TPT methods"). Leaving this entirely unquantified means the reader cannot assess whether the claimed advantage holds. However, note that the reviewer's suggestion that the bisection "could exceed a single forward pass" is not realistic — each bisection iteration evaluates softmaxentropy on a K-dimensional vector (K≤500), which is microsecond-scale computation, orders of magnitude cheaper than a VLM forward pass. The gap is the *absence of measurement*, not a real risk that the overhead is large.

- **Missing a simple softmax-weighting baseline in the main experiments**: The paper compares against mean, max, and entropy aggregation in the main experiments, but does not include a conceptually simpler baseline: weighting prompts by a softmax of their average similarity to the image across classes (which IS included in the controlled experiment, Figure 6). Without this baseline, the reader cannot tell whether the logsumexp gradient step is necessary or whether a direct reweighting of similarities would work as well. This could inform whether the gradient-based optimization or merely the reweighting is responsible for the gains.

- **EuroSAT degradation is discussed but not analyzed**: On EuroSAT, AutoCLIP degrades performance by -0.24pp on average (Table 1). The paper briefly hypothesizes this is due to poor embeddings but does not investigate whether the bisection is selecting degenerate α values, the gradient direction is wrong, or something else. For a paper claiming broad applicability, understanding the failure mode would strengthen the contribution.

### Minor

- **β default inconsistent with the paper's own ablation**: The ablation (Figure 3, discussed in Section 4, paragraph "Ablations") shows that β=0.7 performs better on average and improves results notably on Oxford Pets and EuroSAT, yet the paper uses β=0.85 as the default throughout all main experiments and only "recommends" β=0.7 for future work. This is a minor inconsistency — the default should match the evidence, or the paper should explain why β=0.85 is preferred (e.g., conservatism across settings not tested). The paper does neither.

- **Bisection edge cases not discussed**: The bisection on α∈[0,10¹⁰] assumes that softmaxentropy(α·g) is strictly decreasing in α and reaches ≈0 at α=10¹⁰. While this holds empirically, the paper does not discuss potential edge cases: (a) a gradient of exactly zero (theoretically possible, though unlikely in practice), (b) numerical stability of softmax(α·g) for very large α values, or (c) what happens if the target entropy is not achievable. The upper bound 10¹⁰ is also heuristic — a clear justification would be helpful. These are unlikely to cause problems in practice (the method works across 990 settings), but documentation would improve robustness.

- **"Makes no assumptions on the underlying VLM" is slightly overstated**: The method assumes a joint embedding space where cosine similarity between image and text is meaningful and that class descriptors and images can be embedded in this space. These are standard assumptions shared by all VLM zero-shot classifiers, so the statement is not misleading, but it is a minor overclaim — the method does not apply to non-embedding-based models or models without a shared vision-language space.

### Trivial
None.

## Nice-to-Haves
- Measure the average/max number of bisection iterations per sample across datasets, as well as a wall-clock time comparison to the VLM forward pass.
- Include a softmax-weighting baseline in the main (real-data) experiments to isolate the benefit of gradient-based optimization from reweighting.
- Analyze a few failed EuroSAT samples to understand whether the degradation is due to the gradient direction or the bisection step size selection.
- Measure a proxy of prompt-class "entanglement" in real VLM embeddings (e.g., RN50 vs. ViT-L-14) to ground the synthetic experiment's mechanistic explanation.
- Consider changing the default β to 0.7 or providing a stronger justification for keeping 0.85.

## Removed Points

- The critic's claim that "the overhead could exceed a single forward pass" (Critical Issue 1): This is not credible. Each bisection iteration evaluates softmaxentropy on a K-dimensional vector (K≤500), which is microsecond-scale computation, orders of magnitude cheaper than a VLM forward pass. The real weakness is the absence of measurement, not the risk of large overhead.
- The critic's framing of the controlled experiment as "the conclusions drawn are too strong": The paper uses hedged language ("possible explanation," "strongly simplified setting") throughout Section 5. The reviewer overstates the paper's claims.
- The critic's concern about "make no assumptions on the underlying VLM" being too strong: This is a very minor overstatement for a shared assumption in the field. Moved to Minor.

## Novel Insights

The reviewers collectively surface an interesting tension: the paper positions computational efficiency as a primary advantage, yet provides no quantitative evidence for it. This is a self-inflicted vulnerability — the bisection over a K-dimensional softmax is provably cheap, so measuring it would only strengthen the paper. The other substantive issues (missing softmax baseline in main experiments, β default inconsistency, EuroSAT analysis) are all addressable in a revision and do not threaten the core contribution. The synthetic experiment's entanglement-based explanation for why AutoCLIP helps smaller models more is genuinely interesting but would benefit from grounding in actual VLM embedding statistics.

## Suggestions

1. **Add runtime measurements** to Section 4: report mean/max bisection iterations, wall-clock overhead per image vs. the VLM forward pass.
2. **Include a softmax-weighting baseline** in the main experiments (Section 4) alongside the existing mean/max/entropy comparisons.
3. **Add a brief discussion of bisection edge cases** (zero gradient, numerical stability) to Section 3.4 and note the empirical observation that no failures occurred across 990 settings.
4. **Either change the default β to 0.7 or justify β=0.85** with a rationale more specific than "it was set first."
5. **Analyze a few EuroSAT failure cases** to confirm whether the bisection or the gradient direction is at fault.

## Score and Decision

This is a solid paper. The core idea is simple, well-motivated, and empirically validated across an unusually broad set of configurations (6 VLMs × 8 datasets × 3 prompt strategies × varying K = 990 settings). The method is sound and the improvements, while modest, are consistent and come at negligible computational cost. The weaknesses are real but addressable — missing runtime quantification, a missing baseline, a minor β inconsistency — none of which undermine the core contribution. The paper would be strengthened by addressing these points but is already a useful contribution to the VLM zero-shot classification literature.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>