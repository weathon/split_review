Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper proposes COGT, a generative training/inference strategy for vision-language compositional understanding. The core idea is to use a dependency parser to build a DAG from a caption, then train a decoder to predict each word conditioned only on its ancestors in that DAG (plus visual features and syntactic type), producing a semi-parallel autoregressive generation process. Experiments on five compositional benchmarks (ARO, SugarCrepe, VL-CheckList, ColorSwap, FG-OVD) show large improvements over prior methods, including generative models trained on orders of magnitude more data. Ablations confirm the contribution of the parser quality, syntax-specific masked tokens, and multi-layer visual features.

## Strengths

1. **Novel and well-motivated generative strategy.** The semi-parallel AR factorization guided by dependency parsing is a genuinely new approach to compositional understanding. Table 1 directly shows COGT outperforming standard Sequential-AR (+20 points), Fully-Parallel (+17.77 points), and Mixed strategies across all five benchmarks, demonstrating that the CGM-guided factorization captures useful inductive biases that standard AR and parallel factorizations miss. The motivation (predicting "brown" after knowing it modifies "bird" rather than before) is clearly illustrated.

2. **State-of-the-art results across multiple benchmarks with less data.** COGT-CLIP trained only on COCO (~100K images) outperforms all CLIP-based methods including DAC-LLM trained on CC3M (~3.3M images) by 12.27 points average (Table 3). COGT-XVLM⁺ surpasses Cap and CapPa (pre-trained on 1B images) despite using only ~3.4M images (Table 5). These results are consistent across three different VLM backbones (CLIP, XVLM, InstructBLIP), providing convergent evidence.

3. **Systematic ablation isolating each design choice.** Table 2 cleanly separates the contribution of the parser (Deep Biaffine + RoBERTa best), mask-specific syntactic tokens (+2.69 over generic mask), and two-layer visual features (+4.75 over single layer). This provides fine-grained evidence for the method's components.

4. **No degradation on non-compositional tasks.** Table 6 shows that COGT's frozen visual encoder (with the learned mapping network) preserves or slightly improves linear probing accuracy on CIFAR-10, CIFAR-100, and ImageNet, addressing a known concern (Doveh et al., 2023b) that compositional fine-tuning can harm standard downstream performance.

## Weaknesses

### Fatal
None.

### Major

1. **The AR baseline comparison (Table 1) requires stronger calibration evidence.** COGT outperforms Sequential-AR by ~20 points on average — an order of magnitude larger than typical gaps in this area. The paper uses a same-size decoder (3 blocks, ~39M params) for both, but the AR decoder has a harder task (causal attention over sequential order) and may require different capacity, learning rate, or decoding strategy. The paper describes Sequential-AR as a "re-implementation of Cap" (Section 4.1) but provides no evidence that hyperparameters (learning rate, scheduler, beam search vs. teacher forcing at inference) were carefully tuned. Since the central claim that "CGM structure is decisive" rests heavily on this ablation, the authors should demonstrate that the AR baseline is not artificially weak — e.g., by reporting the best result achievable with a well-tuned AR decoder of matched or slightly larger capacity, or by showing where AR fails qualitatively that COGT succeeds.

### Minor

2. **No variance or significance reporting.** The paper reports a single run per configuration with no standard deviations, confidence intervals, or multiple seeds. Given the extraordinary margins (e.g., +41 points on ColorSwap), readers cannot assess whether results are stable. While single-seed evaluation is not uncommon in this area, the magnitude of the reported gains makes this a notable absence.

3. **ColorSwap improvement lacks analysis.** The 77.61 vs. 36.33 gap over CLIP-like methods (Table 3) is extreme and the paper offers no explanation. Because COGT uses generative likelihood scoring while baselines use contrastive similarity, it is worth analyzing whether the advantage is genuinely from compositional understanding or from a scoring mechanism that systematically assigns lower likelihood to negatives in small candidate sets. A breakdown by attribute type (color, material, texture) or qualitative examples would clarify.

4. **No discussion of dependency parser limitations.** The method depends on an external parser whose errors could propagate into both training (incorrect dependency structure) and inference (incorrect likelihood estimates for negative captions). The paper compares three parsers in Table 2 but does not measure how often parsing errors occur or degrade accuracy on any benchmark. Acknowledging and quantifying this would strengthen the paper.

5. **No computational cost comparison.** Since COGT computes likelihood for each candidate caption at inference (requiring a forward pass through the decoder per candidate), the practical cost relative to a single forward pass of CLIP is relevant but unreported. This is important for practitioners considering the method.

6. **The "causal" framing is somewhat overstated.** The dependency parser produces syntactic relations, not causal relations in the Pearlian sense (no interventions, no tests of invariance). The paper acknowledges this to some degree (Section 3, "we interpret the dependency relations extracted by a dependency parser as causal relations because they directly model the (linguistic) influence"), but the title "Causal Graphical Models" and repeated causal language imply a stronger guarantee. This does not invalidate the method — which is simply a structured generative model based on syntactic dependencies — but is a coherence issue between the framing and the delivered contribution.

### Trivial
None.

## Nice-to-Haves

- Provide pseudocode or a more detailed description of the level-order traversal inference procedure (currently mentioned only briefly in Section 3.1).
- Analyze which compositional subtasks (relation swaps vs. attribute swaps) benefit most from COGT, using existing per-task breakdowns in the benchmarks.
- A dedicated limitations section would improve transparency.

## Removed Points

- **Harsh Critic:** "The extremely large margins over all baselines are suspicious in the absence of variance or detailed analysis" — kept as Minor weakness #2 and #3 above, but the "suspicious" framing implying intentional or accidental inflation is removed. The paper's results could genuinely be large; the concern is about missing variance and analysis, not about integrity.
- **Harsh Critic:** "Missing appendix details/incomplete decoder architecture description" — removed per instructions: the appendix was stripped by the PDF parser and exists in the original submission.
- **Harsh Critic:** "The ablation against Sequential-AR raises serious calibration concerns" — kept as Major weakness #1 above with softened, non-accusatory framing.
- **Strength Finder:** Generic claim that "this paper addresses an important problem" — removed as generic and not specific to the paper's contribution.
- **Strength Finder:** "Causal ordering significantly outperforms both standard AR and parallel prediction" — merged into Strength #1.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Calibrate the AR baseline.** Run a hyperparameter sweep over decoder capacity (2–6 blocks), learning rate, and inference strategy for Sequential-AR under the same COCO training setup. Report the best result obtainable. If the gap remains large, provide qualitative analysis (e.g., which swap types AR fails on that COGT handles correctly). This is the single most important piece of evidence for the paper's core claim.

2. **Report results with at least 3 random seeds** for the main COGT and Sequential-AR configurations, including mean and standard deviation.

3. **Add a brief analysis of the ColorSwap results** — e.g., breakdown by color/attribute type, or a discussion of why generative likelihood might be particularly advantageous there.

4. **Add a limitations paragraph** discussing dependency parser error rates, potential error propagation, and failure cases.

5. **Include inference time comparisons** (e.g., seconds per image for COGT vs. a single CLIP forward pass) to help practitioners assess the trade-off.

## Score and Decision

This paper presents a genuinely novel and well-motivated approach to compositional understanding, with consistent and large improvements across multiple backbones and benchmarks. The main concern is the calibration of the internal AR ablation, which is essential to the central claim but addressable. The external comparisons with published methods (Tables 3–5) provide strong convergent evidence that the method works. I recommend acceptance contingent on the AR baseline concern being convincingly addressed.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>