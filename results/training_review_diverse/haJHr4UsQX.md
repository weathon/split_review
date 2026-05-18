Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper proposes COGT (Causally-Ordered Generative Training), a method for vision-language compositional understanding. COGT uses an off-the-shelf dependency parser to build a Causal Graphical Model (CGM) defining dependency relations among words, then trains a decoder to predict tokens following a semi-parallel, partially-ordered strategy guided by this CGM — each word is conditioned only on its ancestors in the dependency tree. Extensive experiments on five compositional benchmarks across multiple VLM backbones (CLIP, XVLM, InstructBLIP) show large and consistent improvements over prior methods.

## Strengths

- **Large and consistent outperformance over prior state-of-the-art methods.** COGT-CLIP trained only on COCO (~100K images) beats the second-best method DAC-LLM (trained on CC3M, 3.3M images) by 12.27 points on average across all five benchmarks (Table 3). COGT-CLIP+ widens the gap to ~22 points. This directly supports the claim of "large margin" improvement and is the paper's strongest empirical evidence.

- **Superiority over generative methods trained on orders-of-magnitude larger data.** COGT-XVLM+ achieves 96.66% on ARO, surpassing CapPa (93.99%) and Cap (93.06%), both pre-trained on a private 1B image-text dataset (Table 5). This shows that the CGM-guided strategy is more data-efficient than standard generative pre-training.

- **Ablation evidence that CGM-based semi-parallel prediction outperforms alternatives.** In Table 1, COGT obtains 93.37% average accuracy, outperforming Sequential-AR (88.52%), Fully-Parallel (75.60%), and the Mixed strategy (86.02%) under a controlled setting (frozen CLIP encoder, same decoder size, COCO training). This supports the core methodological claim that the CGM-guided factorization is beneficial.

- **Component analysis validates individual design choices.** Table 2 shows that using the best parser (Deep Biaffine + RoBERTa), mask-specific tokens, and two-layer visual features each contributes measurably to performance. Dropping mask-specific tokens costs −2.69 points; using only the last CLIP layer costs −4.75 points.

- **Preserves or improves general VLM capabilities on standard tasks.** Linear probing results (Table 6) show COGT-CLIP+ achieves the highest top-1 accuracy on CIFAR-10, CIFAR-100, and ImageNet among CLIP-based methods, outperforming even the original frozen CLIP encoder. This counters the degradation commonly reported by prior compositional fine-tuning methods.

- **Architecture-agnostic and applicable to diverse VLM backbones.** COGT is successfully applied to CLIP (encoder-only), XVLM (cross-modal encoder), and InstructBLIP (generative decoder-based model) in Tables 3–5, each time setting new state-of-the-art results for that backbone.

## Weaknesses

### Fatal

None.

### Major

- **The ablation in Table 1 confounds prediction order with architectural differences.** The central claim is that the CGM-based partial ordering is the driver of improvement. However, the three compared strategies use different attention mechanisms: Sequential-AR uses standard causal self-attention, Fully-Parallel uses only cross-attention (no inter-token attention), and COGT uses Dependency Guided Attention (masked tokens attend to visible ancestor tokens). Because both the prediction order AND the attention mechanism differ, the observed gains cannot be cleanly attributed to the partial ordering alone. A controlled comparison that keeps the attention mechanism fixed and varies only which tokens are conditioned on (all previous tokens vs. ancestors only vs. none) would directly test whether the partial order confers a benefit beyond the architectural change. Without this, the specific claim that "the CGM partial order" is the source of improvement is weakened, though the overall empirical superiority of COGT as a method remains well-supported by the large margins across multiple benchmarks.

### Minor

- **The exact CLIP model variant is not specified.** The paper does not state which CLIP model (e.g., ViT-B/32, ViT-L/14) is used in any experiment. Architecture affects the number and resolution of visual tokens, total parameter count, and baseline performance — without this information, it is difficult for readers to assess whether gains partially reflect using a stronger CLIP backbone than the baselines. Similarly, the paper uses two-layer visual features (last + penultimate layer), but it is unclear whether all compared methods had access to this richer representation or only a single layer.

- **Results are reported without confidence intervals or error bars.** All results are single numbers without standard deviations or ranges. While the margins in Tables 3–5 are very wide (mitigating concern), the ablation experiments (Tables 1, 2) show smaller differences where variance information would help assess stability. Standard errors over a few seeds should be reported at least for the main comparisons.

- **The "causal" framing is stronger than the evidence supports.** The paper repeatedly invokes causal language ("causal dependencies," "spurious associations," "causally sufficient") based on an off-the-shelf dependency parser that returns syntactic/semantic relations — not formally established causal mechanisms. The paper partially acknowledges this (Section 3: "While the causal dependency relations in C may not be exhaustively described by G..."), but the overall language overstates the rigor of the causal interpretation. The work is better described as using a parser-defined Bayesian network to factorize the joint distribution. This does not affect the empirical results but would benefit from more measured language.

### Trivial

None.

## Nice-to-Haves

- An analysis of what kinds of compositional errors COGT still makes — particularly cases where the dependency parser produces an incorrect tree — would deepen understanding of the method's boundaries.
- The reviewer's suggestion to run an ablation that fixes the Dependency Guided Attention mechanism and varies only the conditioning sets (ancestors only vs. all past tokens vs. no inter-token attention) would strengthen the attribution of gains to the CGM ordering specifically.

## Removed Points

- **FG-OVD "not described in the main text"** — Removed because this is factually incorrect. The paper describes FG-OVD in lines 108–109 of Section 4, including its origin, task construction (replacing attributes like color/material/texture in object-specific captions), and how it is used in an image-to-text retrieval setup.

## Novel Insights

Beyond the paper's own contributions, the most interesting cross-review insight is the tension between the paper's strong empirical results and the difficulty of cleanly attributing them to any single component. The ablation confound means we cannot fully disentangle whether the gains come from (a) the CGM-defined partial order, (b) the Dependency Guided Attention mechanism itself, or (c) the interaction of the two. The fact that the method works consistently across three different backbone architectures (CLIP, XVLM, InstructBLIP) suggests that the gain is robust, but the precise mechanism remains somewhat underspecified. This is a common pattern in systems papers that compare "holistic methods" — the whole is clearly better, but which part drives the improvement is harder to isolate.

## Suggestions

1. In the main text, specify the exact CLIP variant (model size, patch size) for every experiment.
2. Add standard deviations or bootstrapped confidence intervals to the main results, especially for ablation experiments.
3. Consider running an additional ablation that keeps the Dependency Guided Attention architecture fixed and varies only the conditioning sets (ancestors-only vs. all-previous-tokens vs. no-tokens) to isolate the effect of partial ordering.
4. Tone down the "causal" language and describe the approach more neutrally as a parser-guided factorization of the joint distribution.

## Score and Decision

This paper presents a novel, well-motivated method with extensive experiments and remarkably strong empirical results. The core idea — using a parser-derived factorization to guide generative training — is clever, and the gains are large, consistent, and demonstrated across multiple backbones and benchmarks. The main weaknesses (ablation confound, missing CLIP variant specification, no error bars, overclaimed causality) are real but addressable. The significance of the contribution, especially the data efficiency gains, outweighs the current shortcomings.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>