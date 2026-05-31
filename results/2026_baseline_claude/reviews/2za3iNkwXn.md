## Summary

This paper investigates how compression techniques—quantization, distillation, and pruning—affect the reasoning capabilities of Large Reasoning Models (LRMs), specifically DeepSeek-R1 and its distilled variants. The study proceeds along two complementary axes: (1) comprehensive performance benchmarking across four reasoning tasks of varying difficulty (AIME 2024, FOLIO, Temporal Sequences, MuSiQue) and (2) mechanistic interpretation via adapted difference-of-means steering vectors and attribution patching to pinpoint which weight matrices are causally responsible for reasoning behaviors. Three empirically validated findings emerge: weight count matters more for knowledge memorization than reasoning; the MLP `up_proj` in the final layer of distilled LRMs is the single most important component; and current quantization methods excessively compress final-layer modules and MLP gate projections—protecting just 2% of weights raises average accuracy by 6.57% over the 3-bit baseline.

---

## Strengths

- **Comprehensive benchmarking across compression paradigms.** Table 1 systematically compares dynamic quantization (2.51/1.73/1.58-bit), multiple 4- and 3-bit post-training quantization schemes (AWQ, GPTQ, GPTAQ, ANY4/3), SparseGPT/AlphaPruning pruning, and distillation—with three-pass averaging for most models—on reasoning tasks spanning mathematical, logical, temporal, and multihop reasoning. This breadth fills a real gap noted by the authors and provides an unusually rich reference table for practitioners.

- **Actionable mechanistic finding with direct empirical validation.** The identification of `32_up` (the final-layer `up_proj`) as the most important component is not just a visualization claim: Table 3 shows that quantizing *only* this single matrix (0.7% of parameters) to 3-bit drops average accuracy by 16.3%, and the component rank from the importance scores broadly correlates with the measured accuracy drop. This tight loop between interpretation and ablation strengthens the causal claim considerably.

- **Novel application of mechanistic interpretability to compression analysis.** Adapting difference-of-means and attribution patching jointly—at the granularity of every linear module across every layer—to track *importance shift* induced by compression is methodologically novel. Prior work (Venhoff et al., 2025) studied layer-wise contributions without this compression lens; quantization and pruning papers rarely go beyond perplexity-level analysis.

- **Protection experiment with significant practical impact.** Table 4 demonstrates that retaining 16-bit precision for final-layer MLP modules while applying 3-bit AWQ everywhere else yields a 6.57% average improvement and outperforms every 3-bit baseline in Table 1 for the 8B Llama model. The mechanism is concise, interpretable, and directly motivated by the analysis.

- **Collapse-point analysis correlating with benchmark difficulty.** Table 2 provides a fine-grained sparsity sweep (0–80%) and finds that collapse point consistently tracks benchmark difficulty—AIME 2024 collapses first, Temporal last—which is a clean empirical regularity not reported in prior pruning literature.

---

## Weaknesses

### Fatal
None.

### Major

1. **The importance-shift visualization discards all increases, which is a biasing design choice.** The authors set all *increases* in relative importance to zero, arguing only decreases are informative. However, this asymmetry risks systematically highlighting losses at certain layers (e.g., the final layer) while masking compensatory gains elsewhere. If quantization re-routes importance rather than destroying it, the visualization will overstate how much the final layer is uniquely harmed. The justification is deferred to Appendix H (unavailable), so the reader cannot assess this choice. A symmetric or net-change visualization, even as a supplementary figure, is needed to rule out confirmation bias.

2. **Reliance on GPT-4o annotation for reasoning-behavior labeling is a significant uncontrolled source of noise.** The entire mechanistic interpretation pipeline depends on GPT-4o correctly tagging token sequences in reasoning chains as instances of backtracking, uncertainty estimation, example testing, or adding knowledge. Annotation robustness is stated to be "demonstrated in Appendix G" (unavailable), but the main text gives no quantitative inter-annotator agreement, error rate, or sensitivity analysis. If the annotation is noisy—especially on models that may express these behaviors differently after compression—the resulting steering vectors and importance scores could be systematically skewed.

3. **The protection experiment (Table 4) is demonstrated for only one model.** The abstract claims the finding "applies to current pruning methods" and generalizes broadly, but the quantitative validation of 6.57% improvement via selective protection is shown exclusively for R1-Distill-Llama-8B under 3-bit AWQ. Given that the importance patterns on Qwen and Llama differ (gate-proj importance shifts occur in different layer ranges; Figures 6 vs. 3), whether the same targeted protection would yield comparable gains on other models is entirely speculative without corroborating experiments.

### Minor

1. **The comparison between Llama-70B and Qwen-32B to support the "weight count affects knowledge more than reasoning" claim confounds parameter count with architectural differences and training differences between the two model families.** A cleaner test would compare models of the same family at different sizes.

2. **R1 is evaluated with only a single pass** (marked †), while compressed variants use three passes. The 2.51-bit R1 scores slightly *higher* than original R1 on AIME 2024 (76.7 vs. 73.3). Without variance estimates for R1, the claim that "2.51-bit R1 achieves close-to-R1 performance" cannot be statistically substantiated—it could simply reflect single-pass sampling noise.

3. **The "23.17% over state-of-the-art" claim** refers to the improvement over 3-bit ANY3 on the 8B model (52.57% vs. 29.4%), which is a comparison to the weakest relevant baseline in a single model configuration. Presented alongside the more restrained 6.57% average improvement claim, the 23.17% figure could mislead readers about the typical magnitude of gains.

### Trivial

- The annotation dataset of 120 instances (30 per benchmark) is small for deriving layer-wise importance scores across 32 layers × 7 modules. While the aggregation may mitigate variance, a brief discussion of sample-size sensitivity would strengthen confidence.

---

## Nice-to-Haves

- Run the selective protection experiment on at least the Qwen-7B model to test generalizability of Table 4.
- Provide symmetric importance-shift heatmaps (or residual maps) alongside the decrease-only visualizations so readers can assess whether importance is destroyed or rerouted.
- Report variance across three passes for R1 (full-precision) to allow proper statistical comparison with compressed variants.
- Include a brief ablation on annotation quality (e.g., swap GPT-4o labels for random labels and observe that importance maps collapse) to establish that the annotation pipeline is load-bearing.

---

## Novel Insights

The most genuinely novel insight in this paper is the mechanistic-interpretability-guided identification of the final-layer `up_proj` as a compression bottleneck, combined with the evidence that this bottleneck is *distillation-induced*: the importance-shift analysis from distilled Llama-8B back to vanilla Llama-3.1-8B shows that the up_proj outlier in the last layer emerges specifically from distillation rather than being a pre-existing property of the backbone. This reframes the compression problem: it is not merely that the final layer is generally fragile, but that distillation concentrates reasoning capability into specific weight matrices that current quantization calibration routines are not designed to protect. The secondary insight that both AWQ and GPTQ exhibit the same pattern of excessive compression in the final layer and mid-layer gate projections despite their different calibration objectives suggests a structural blind spot in the design of activation-aware and Hessian-based quantization methods that deserves targeted attention.

---

## Suggestions

- Extend the selective-protection experiment to Qwen-7B and Llama-70B to give the "2% weights, 6.57% gain" result broader credibility.
- Report a symmetric or net-change importance-shift heatmap to complement the decrease-only views; this would let readers distinguish importance destruction from importance rerouting under compression.
- Provide three-pass variance for the base R1 model to enable statistically valid comparisons against compressed variants.
- Briefly quantify GPT-4o annotation reliability in the main text (e.g., precision/recall against a small human-labeled gold set) to preempt concerns about the behavior-tagging pipeline.
- Explore whether selective protection of gate projections in middle layers—identified in Figures 3 and 6 as another bottleneck—yields complementary improvements on top of final-layer protection.

---

## Score and Decision

The paper addresses a timely and important problem with a comprehensive evaluation and a novel mechanistic angle. The core finding about the final-layer `up_proj` is well-supported by targeted ablations, and the protection experiment demonstrates clear practical value. The primary weaknesses—the biasing one-sided importance-shift visualization, reliance on an unvalidated GPT-4o annotation pipeline, and limited scope of the protection experiment—are real but not fatal; they reduce confidence in the mechanistic claims without undermining the empirical findings that form the bulk of the contribution. The paper is above the acceptance threshold for a venue like ICLR, though the mechanistic claims need stronger methodological grounding.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>