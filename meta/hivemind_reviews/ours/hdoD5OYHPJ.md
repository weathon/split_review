## Summary
AutoCLIP proposes a lightweight method for improving zero-shot classification with vision-language models. Instead of uniformly averaging encoded class descriptors across prompt templates, it computes per-image weights via a single gradient ascent step on a logsumexp objective, with the step size automatically determined by target-entropy bisection. The method operates entirely in the embedding space (no extra encoder passes or backprop), and experiments across 990 configurations (8 datasets, 6 VLMs, 3 prompt strategies) show consistent improvements: 0.45 pp average accuracy gain, with 85% of settings improved and gains up to 3 pp.

## Strengths
- **Extensive and systematic empirical validation.** The main results (Figure 3) cover 990 combinations spanning 8 datasets, 6 vision-language models, and 3 prompt-template strategies (CLIP, DCLIP, WaffleCLIP). AutoCLIP improves accuracy in 85% of settings with an average gain of 0.45 pp. The consistency across this large configuration space strongly supports the core claim.

- **Principled hyperparameter-free step-size selection.** Section 3.4's entropy-controlled bisection replaces a dataset-dependent step size α with a global entropy reduction factor β. The ablation (Figure 4) shows stable performance for β ∈ [0.7, 0.9], which is a desirable property in the zero-shot paradigm where per-dataset tuning is infeasible.

- **Closed-form gradient enables deployment without autodiff.** Section 3.3 derives an explicit formula for ∇_ρ logsumexp(s) in terms of softmax probabilities and descriptor-image similarities, which is valuable for edge-device inference where automatic differentiation is unavailable.

- **Honest treatment of limitations.** The paper openly discusses EuroSAT being the only dataset where AutoCLIP hurts performance on average (Δ = −0.24), and proposes a plausible hypothesis for why. This transparency strengthens credibility.

## Weaknesses
### Fatal
None.

### Major

- **No empirical comparison to the most closely related prior work (ZPE).** The paper correctly identifies Zero-shot Prompt Ensembling (Allingham et al. 2023) as the most similar method—both determine prompt weights in embedding space without backprop through the VLM. The paper argues that ZPE requires a batch of target samples and source-domain features, whereas AutoCLIP is per-image and source-free. However, for settings where ZPE's requirements *are* satisfied (e.g., ImageNet with whole-batch inference and pretraining data available), a direct accuracy comparison would be highly informative. Without it, the reader cannot judge whether AutoCLIP's design advantages come at an accuracy cost relative to ZPE. This is the single largest gap in the evaluation.

### Minor

- **β-value inconsistency between main experiments and ablation.** The main experiments (Figure 3, Table 1) use β = 0.85, yet the ablation (Figure 4) shows β = 0.7 yields higher average accuracy, and the authors "recommend this choice for future work" (Section 4, ablations paragraph). While the paper is transparent about this, presenting the main results with a suboptimal default weakens the narrative and could confuse readers.

- **No runtime measurements despite repeated claims of low overhead.** The abstract states "only a minor additional computation overhead," and the conclusion repeats "minimal inference-time overhead." However, no actual runtime numbers are reported (e.g., milliseconds per image for AutoCLIP vs. baseline, across different model sizes and K values). For a method whose central practical selling point is low computational cost, this omission is notable.

- **Controlled experiment's explanatory claims lack direct VLM evidence.** Section 5 uses synthetic Gaussian embeddings (C=5, d=128) with a manually injected entanglement parameter ρ to conclude that AutoCLIP benefits smaller VLMs more because their text embeddings are "more entangled." While the paper hedges with "possible explanation" (line 249), the causal link is asserted without any direct measurement of entanglement in real CLIP text encoders across model sizes. The controlled experiment is a useful intuition-builder, but the explanation remains untested.

### Trivial

- **Computational cost of bisection for large K not discussed.** With K up to 500, each bisection step evaluates softmax entropy over K weights. The paper does not mention how many bisection iterations are needed or the total cost.

- **Gradient formula given without derivation.** The closed-form gradient in §3.3 (line 139) is presented as a three-term product without step-by-step derivation. While the result is correct, a brief derivation would improve reproducibility.

## Suggestions
1. Add a direct comparison to ZPE (Allingham et al. 2023) on ImageNet with matched K values, even if only at a single configuration. This would let readers assess the accuracy trade-offs between the per-image/source-free AutoCLIP and the batch/source-dependent ZPE.
2. Report wall-clock runtime for AutoCLIP vs. baseline across a few representative settings (e.g., RN50/K=80, ViT-B/16/K=200, ViT-L/14/K=500) to substantiate the "minor overhead" claim.
3. Either commit to β=0.85 as the default (and explain why) or switch to β=0.7 in the main experiments, rather than presenting results with one value and recommending another.

## Score and Decision

**Originality:** The method is a novel combination of known components (logsumexp aggregation, gradient ascent on weights, entropy-controlled step size) applied to a well-motivated problem. It does not introduce a fundamentally new learning paradigm, but it offers a clean and practical solution.

**Importance of research question:** The question of how to best construct zero-shot classifiers from VLMs is practically significant, and the paper's emphasis on zero-shot compatibility (no labeled data needed) is well-motivated.

**Claims supported:** The core claim (AutoCLIP improves over uniform weighting) is strongly supported by the 990-configuration evaluation. The weaker claim about entanglement explaining model-size trends is only partially supported by synthetic data.

**Soundness of experiments:** The main experimental design is thorough, including multiple datasets, models, prompt strategies, and K values. The absence of a ZPE comparison is the main weakness in experimental completeness.

**Clarity of writing:** The paper is clearly written and well-structured. The method description, including algorithms, is precise. The ablation on β and objective function is helpful.

**Value to the research community:** AutoCLIP is simple, effective, and easy to implement. It could reasonably serve as a default zero-shot inference strategy, which gives it clear practical value.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
