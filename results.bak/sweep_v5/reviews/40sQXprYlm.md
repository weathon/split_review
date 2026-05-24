Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper introduces Distributed Neural Architectures (DNAs), a framework where each token/patch follows its own learned path through a collection of modules and routers, with no fixed notion of depth or width. DNAs generalize conditional computation methods (MoE, MoD, early exit, weight sharing) by letting routing and module composition emerge end-to-end. The paper demonstrates feasibility in both vision (ImageNet, ViT-small scale) and language (FineWeb-edu, GPT-2 medium scale), showing that DNAs are competitive with dense baselines, can learn to skip computation, and exhibit interpretable routing patterns and power-law path distributions.

## Strengths

- **Conceptually novel and well-motivated framework**: The idea of letting each token compose its own computational path from a pool of modules — including ordering and module selection — is a natural and clean extension of MoE, MoD, and early-exit ideas. The framing of these existing methods as special cases of a single unified architecture is insightful and may influence future architecture design.

- **Demonstrated feasibility across two modalities with competitive dense-baseline performance**: The top-1 DNA vision model achieves 79.1% on ImageNet (vs. ViT-small at 79.8%), and the top-2 DNA language model achieves lower validation loss than GPT-2 medium (2.674 vs. 2.720) while outperforming it on 4 of 7 zero-shot benchmarks (Table 3). These results convincingly show DNAs are trainable at non-trivial scale.

- **Practical contribution: identity-module bias trick for learned compute efficiency (Eqs. 2–3)**: Adapting DeepSeek's load-balancing bias to encourage skip decisions is simple, effective, and reusable. The paper shows this leads to content-dependent compute allocation (Fig. 5) where simpler images use fewer modules — a clean demonstration of emergent efficiency.

- **Honest and informative analysis of emergent structure**: The power-law path distribution finding, including the admission that random networks also exhibit power-law behavior (exponent -1), provides a useful baseline. The analysis that emergent specialization in vision (Figs. 3, 4) is qualitatively meaningful, and the deep-dream-style reconstruction (Fig. 4) offers a genuinely interesting view into what routing stages encode.

## Weaknesses

### Major

- **Missing baselines against existing conditional computation methods**: The paper claims DNAs "generalize" MoE, MoD, and weight sharing, yet provides no comparisons against any of these at matched active-parameter counts or compute budgets. Without MoE transformers (same active params, fixed ordering) or MoD models (dynamic depth), it is impossible to assess whether DNA's flexible routing provides any benefit over simpler alternatives. This gap undermines the central claim that DNAs represent a meaningful advance rather than just a more complex instantiation of known ideas. *Verification: Tables 1–3 compare only against dense ViT and GPT-2 baselines; no MoE or MoD entries appear.*

- **Efficiency claims lack controlled compute/accuracy trade-off evidence**: The paper asserts that DNAs "learn to use less compute with minor effects on performance," but no FLOPs, latency, or throughput measurements are reported. The vision compute analysis (Fig. 5) uses "normalized compute" (module counts) — a proxy that ignores that different modules may have different FLOPs — and no Pareto curve of accuracy vs. compute is provided. The language model with 30% skip (2.784 loss) shows a clear degradation vs. GPT-2 (2.720) without any measurement of compute saved. The efficiency claims are descriptive, not evidential. *Verification: "FLOP" and "latency" do not appear anywhere in the paper; Section 3.3 uses module counts normalized to [0,1] as the sole compute metric.*

- **No variance reporting across runs**: All vision and language experiments report results from a single "best run" with no multiple seeds or error bars. Given the acknowledged sensitivity to hyperparameters (grid search over learning rate and weight decay for vision), the absence of variance estimates makes it impossible to assess the reliability of the reported comparisons. *Verification: The paper states "best run of each model" for both vision (Sec. 3.1) and language (Sec. 4.1) experiments.*

- **Confounded language baselines**: The top-2 DNA (433M active, 603M total params) is compared against GPT-2 medium (406M). The 7% active-parameter advantage and 48% total-parameter advantage mean the comparison does not isolate the routing mechanism as the source of improvement. The "30% shallower GPT-2" baseline does not match active parameter count either. Notably, the top-1 DNA (406M active, same as GPT-2) performs slightly *worse* than GPT-2, which tempers the claims but also highlights the need for properly controlled comparisons. *Verification: Table 2 shows active parameter counts; Table 3 shows top-1 DNA (406M) loss 2.754 vs. GPT-2's 2.720.*

### Minor

- **Interpretability analysis is qualitative and lacks quantitative validation**: The path specialization observations (Figs. 3, 8) and routing decision visualizations (Fig. 4) are based on hand-picked examples. No metrics (mutual information between paths and semantic classes, clustering purity, ablation studies) are used to verify that the patterns are systematic rather than cherry-picked. While interesting as exploratory findings, the paper's claim that DNAs are "interpretable" is not rigorously supported. *Verification: Section 3.2 describes path specialization via visual inspection of 60 patches per path; no numerical clustering metrics are reported.*

- **Language models are acknowledged as severely undertrained**, yet conclusions about routing patterns, module specialization, and path distributions are still drawn from them. The paper notes models are "way too small to truly absorb" the 21B tokens (Sec. 4), which limits confidence that the observed patterns would persist at properly trained scales. This is an inherent limitation of the experimental setup that the paper acknowledges but does not address.

### Trivial

- **Toy-scale nature**: The vision models are ViT-small scale (22M params) and language models are GPT-2 medium scale (406M). While appropriate for a proof-of-concept, this limits conclusions about scalability and practical utility. The paper acknowledges this, so it is not a flaw per se, but it constrains the scope.

## Nice-to-Haves

- A comparison against an MoE baseline with the same active parameter count and number of experts would immediately clarify whether the dynamic ordering in DNAs provides value beyond expert choice alone. Even a simple ablation where routers are shared (as in standard MoE) would be informative.
- Reporting inference FLOPs alongside the normalized compute metric would make the efficiency claims verifiable and publishable as a reference point.
- Multiple seeds (at least 3) with error bars on the key comparisons (ImageNet accuracy, language validation loss, zero-shot benchmarks) would substantially strengthen the reliability of the results.

## Removed Points

*These points were raised by reviewers but are removed from the main review for the following reasons:*

1. **"Backpropagation through discrete top-k not discussed"** — The paper uses softmax probabilities ρ_i weighted by expert outputs in Eq. (1). Gradients flow through ρ (differentiable), and the hard top-k only gates which modules participate. This is standard practice in MoE literature and does not require special treatment like straight-through estimators.

2. **"Fully causal claim is misleading because routing decisions are made in parallel"** — The paper's claim about causality refers to the forward pass of tokens (each token's representation depends only on its own path history, not on other tokens' futures), which is correct. Parallel routing decisions do not conflict with causality.

3. **"No discussion of how DNAs would scale or how routing overhead affects latency"** — The paper explicitly delegates deployment/scaling concerns to future work (Section 2.1: "infrastructure should shape/constrain the emergent structure... we leave this direction to future work"). Criticizing a proof-of-concept for not providing production-scale analysis is scope creep.

4. **Missing related work concerns** — The reviewer references specific papers that may not exist in the paper's reference list. Per protocol, all cited references are assumed valid and the reviewer does not have complete knowledge to verify whether a paper is missing.

5. **"Anecdotal interpretability" framed as fatal** — While the interpretability analysis is qualitative, the paper explicitly characterizes this as exploratory analysis (Section 3.2: "To further understand the DNA routing decision structure"), and the findings (e.g., boundary patches being compute-intensive) are consistent with established results (Riquelme et al., 2021). The criticism is valid as a minor weakness but not structural.

## Novel Insights

The harsh critic and strength finder largely agree on the paper's nature: it is a conceptually interesting proof-of-concept with genuine novelty in its unified routing framework, but its empirical evaluation is incomplete in ways that prevent strong conclusions. The most interesting observation from the combined reviews is that the paper's own honest reporting (e.g., that random networks also produce power-law path distributions, that top-1 DNA at equal active params underperforms the dense baseline) undermines some of its positive claims while simultaneously raising its credibility. The identity-module bias trick stands out as the most practical contribution, and the deep-dream reconstruction analysis (Fig. 4) is a genuinely creative approach to understanding routing structure that goes beyond typical attention-map visualizations. The paper's core tension is that its most interesting claims (emergent ordering, dynamic compute allocation, path specialization) require richer evaluation than a feasibility study typically provides — putting it in an uncomfortable middle ground between conceptual contribution and empirical demonstration.

## Suggestions

1. Add an MoE transformer baseline with matched active parameters (same number of experts as DNA modules, fixed ordering across layers). This single addition would most directly validate the "generalization" claim.
2. Report wall-clock inference FLOPs or relative latency for the skip-enabled models alongside the normalized compute metric.
3. Run all main experiments with 3 random seeds and report mean ± std for the key accuracy/loss numbers and the zero-shot benchmarks.
4. Add a quantitative interpretability metric: e.g., compute the mutual information between path assignments and ImageNet class hierarchy (or POS tags for language) and compare against a random-baseline routing.

## Score and Decision

**Calibration anchors** (all retrieved; those read in full marked with ✓):

| Paper | Avg Score | Comparison |
|-------|-----------|------------|
| From Sparse to Soft Mixtures of Experts ✓ | 7.50 | Well-executed MoE method with comprehensive FLOPs-accuracy evaluation across scales. Significantly stronger on evaluation rigor and practical impact. |
| Jointly-Learned Exit and Inference ✓ | 7.50 | Strong early-exit method with ablations, uncertainty analysis, and solid evaluation. More thorough empirical work. |
| Dynamic Mixture of Experts ✓ | 7.00 | Auto-tuning MoE with extensive experiments across vision/language/VL. Stronger on breadth and controlled comparisons. |
| Tight Clusters Make Specialized Experts ✓ | 7.00 | MoE routing improvement with theory + large-scale experiments. Stronger on theoretical grounding and evaluation. |
| MIND over Body ✓ | 7.00 | Adaptive computation with strong results surpassing much larger models. Stronger empirical validation. |
| More Experts Than Galaxies ✓ | 5.67 | Biologically-inspired fixed routing. Comparable: interesting framework, moderate evaluation, similar scope. |
| Automatic Organization of Neural Modules ✓ | 4.75 | Graph-based neural organization. Weaker: missing key method details, unclear advantages. |
| A-MoD: Attention for MoD Routing ✓ | 4.00 | Attention-based MoD routing. Weaker: narrow scope, missing SOTA comparisons, limited contribution. |

Positioning: This paper is stronger than A-MoD (4.00) and the Auto-Organization paper (4.75) — it has a clearer contribution, works in two domains, and has more interesting findings. It is roughly comparable to COMET (5.67) in being an interesting new framework with moderate evaluation rigor. It is clearly weaker than the 7.00+ anchors which have stronger empirical validation, controlled comparisons, and often theoretical backing.

The paper's strengths (conceptual novelty, demonstrated feasibility, interesting emergent structure findings) are real, but the evaluation gaps (no conditional computation baselines, no FLOPs measurements, no variance reporting, confounded language comparisons) prevent it from reaching the bar set by the 7.00+ papers. The paper is best read as a promising proof-of-concept that needs significant additional experiments before its core claims can be properly evaluated.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>