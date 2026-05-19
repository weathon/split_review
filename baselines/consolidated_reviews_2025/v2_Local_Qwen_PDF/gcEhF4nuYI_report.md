## Summary
# Final Review Report

## Summary
This paper proposes FTP (Fine-grained Token-wise Pruner), a dynamic token routing framework for large language models that adaptively skips less important tokens across transformer blocks during inference without requiring model retraining. The method introduces a genetic algorithm-based sparsity scheduler to allocate block-wise pruning ratios and a lightweight dynamic router that utilizes four low-dimensional factors (token position, attention scores, rank, and sparsity requirements) instead of high-dimensional hidden states. Extensive experiments on LLaMA and Qwen series models demonstrate that FTP achieves state-of-the-art accuracy retention among token-wise pruning methods, significantly outperforming block-wise baselines like BlockPruner and ShortGPT at comparable sparsity levels. While the empirical results are promising, the manuscript requires improvements in novelty bounding, statistical rigor (variance reporting), methodological clarity (loss design, normalization), and practical deployment analysis (KV cache overheads).

## Strengths
1. **Novel Methodological Design:** The proposal of a lightweight dynamic router using four low-dimensional factors (position, attention scores, rank, sparsity requirement) instead of high-dimensional hidden states is a practical and efficient design choice. This reduces training overhead and improves generalization compared to prior token-routing methods like MoD.
2. **Decoupled Optimization Strategy:** The three-step pipeline (initial sparsity search with static router, dynamic router training, sparsity scheduler fine-tuning) effectively simplifies the joint optimization of sparsity allocation and token routing, leading to stable training and strong empirical performance.
3. **Strong Empirical Results:** FTP demonstrates impressive accuracy retention across multiple LLMs (LLaMA2-7B/13B, LLaMA3-8B, Qwen1.5-7B) and benchmarks, significantly outperforming block-wise pruning baselines at comparable sparsity levels without requiring model retraining.
4. **Comprehensive Ablation Studies:** The paper includes detailed ablation studies on sparsity allocation strategies, router inputs, and router architectures, providing clear evidence for the effectiveness of each proposed component.

## Weaknesses
1. **Overgeneralized Claims and Novelty Bounding:** The abstract and introduction contain overgeneralized statements (e.g., "always introduce additional training costs") and lack precise novelty bounding against recent token-routing methods like MoD. The contribution statements are informal and descriptive rather than highlighting specific methodological innovations.
2. **Weak Statistical and Empirical Rigor:** The token redundancy analysis relies on a small sample (50 sequences) and a single similarity metric without sensitivity validation. Main results lack variance reporting (mean ± std over multiple seeds), undermining statistical reliability. The comparison between token-wise and block-wise pruning lacks explicit metric clarification and computational cost (FLOPs/time) alignment.
3. **Methodological Ambiguities:** The sparsity constraint loss is asymmetric, allowing over-pruning without penalty. The distillation loss is applied only at the final block, ignoring intermediate representation alignment. The guide loss decay schedule and input normalization for heterogeneous router factors are not explicitly defined, hindering reproducibility.
4. **Practical Deployment Limitations:** The inference speedup analysis focuses on prefilling, with modest gains (1.28× at 30% sparsity) suggesting kernel/memory overhead dominance. The KV cache compatibility modification relies on an ad-hoc threshold for the last token, complicating routing logic and potentially negating parallel processing benefits.

## Key Issues
1. **Claim-Evidence Mismatch in Redundancy Analysis:** The motivation for block-wise adaptive sparsity relies on token similarity analysis over only 50 sequences. High similarity does not strictly guarantee prunability without sensitivity validation. *Impact:* Weakens the foundational motivation for the GA-based scheduler.
2. **Asymmetric Sparsity Constraint Loss:** The loss $L_s$ only penalizes under-pruning, allowing the router to skip more tokens than targeted without penalty. *Impact:* Can lead to unpredictable accuracy drops and unstable training dynamics.
3. **Missing Variance Reporting:** Main results and ablations lack standard deviation over multiple seeds. *Impact:* Prevents assessment of statistical reliability, especially given the single-seed evaluation protocol.
4. **Ad-hoc KV Cache Modification:** The threshold-based mechanism for last-token sparsity is heuristic and not learned. *Impact:* Complicates routing logic, potentially negating parallel processing benefits and reducing practical deployment appeal.
5. **Unbounded SOTA Claims:** The paper claims SOTA performance without explicitly bounding the comparison to the specific setting of "token-wise dynamic pruning without retraining." *Impact:* Risks rejection if reviewers identify comparable prior work in broader pruning or conditional computing landscapes.

## Actionable Suggestions
1. **Tighten Novelty and Claims:** Replace absolute statements about prior training costs with nuanced comparisons. Bound SOTA claims to "token-wise dynamic pruning without retraining." Rewrite contribution bullets to be formal, specific, and evidence-aligned (see PDF annotations).
2. **Strengthen Redundancy Analysis:** Expand the token similarity analysis to 500+ diverse sequences. Add a sensitivity ablation: randomly skip high-similarity tokens and measure performance drop to empirically validate the "prunable" hypothesis.
3. **Fix Loss Design and Reproducibility:** Modify $L_s$ to a symmetric penalty (e.g., MSE) to strictly enforce target sparsity. Explicitly define the guide loss decay function (e.g., linear decay) and report final effective loss weights. Clarify normalization strategy for the four heterogeneous router inputs.
4. **Improve Statistical Rigor:** Report main results and ablations as mean ± std over at least three random seeds. Add a computational cost comparison (FLOPs or inference time) to provide a fairer efficiency benchmark against block-wise baselines.
5. **Refine Deployment Analysis:** Report speedup separately for prefilling and autoregressive generation. Discuss memory bandwidth and kernel overheads. Replace the ad-hoc KV cache threshold with a learned mechanism or explicitly acknowledge it as a practical heuristic with limitations.

## Storyline Options + Writing Outlines
### Abstract Outline (S1-S5)
- **S1 (Problem):** LLM scaling increases inference overhead, hindering industrial deployment.
- **S2 (Gap):** Static pruning often requires retraining or hardware support; dynamic methods can incur heavy predictor costs.
- **S3 (Method):** We propose FTP, a fine-grained token-wise pruning framework that adaptively skips tokens via a lightweight dynamic router and GA-based sparsity scheduler, without retraining.
- **S4 (Mechanism):** The router utilizes four low-dimensional factors (position, attention scores, rank, sparsity) and is optimized via decoupled training with guide, sparsity constraint, and distillation losses.
- **S5 (Result):** FTP achieves SOTA accuracy retention among token-wise pruning methods, outperforming BlockPruner/ShortGPT by ~10 points on LLaMA2-7B/Qwen1.5-7B at comparable sparsity.

### Introduction Outline (P1-P4)
- **P1 (Motivation & Gap):** LLMs are powerful but expensive. Compression techniques (quantization, distillation, static pruning) face trade-offs in retraining costs, hardware dependency, or accuracy drops. Dynamic conditional computing offers flexibility but often relies on heavy predictors or full-model fine-tuning. *Gap:* Need for lightweight, adaptive token-wise pruning without retraining.
- **P2 (Insight & Method):** We uncover depth-dependent token redundancy (middle blocks exhibit higher similarity). This motivates FTP, which decouples sparsity scheduling from router training. FTP introduces a static router for initial GA-based sparsity search, followed by dynamic router training using low-dimensional factors, and final scheduler fine-tuning.
- **P3 (Evidence Preview):** Extensive experiments on LLaMA and Qwen series models demonstrate FTP's superiority over block-wise baselines in accuracy retention and prefilling speedup, with robust ablation studies validating each component.
- **P4 (Contributions):** (1) Analysis of depth-dependent token redundancy motivating adaptive sparsity. (2) FTP framework with low-dimensional router and decoupled optimization. (3) SOTA results in no-retraining token-wise pruning setting.

## Priority Revision Plan
| Priority | Task | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Report mean ± std over ≥3 seeds for all main results and ablations. | Establishes statistical reliability; critical for acceptance. | Low |
| **P0** | Fix asymmetric sparsity loss $L_s$ to symmetric penalty; clarify guide loss decay and input normalization. | Resolves methodological ambiguity; improves reproducibility. | Low |
| **P0** | Bound SOTA claims to "token-wise dynamic pruning without retraining"; rewrite contribution bullets formally. | Prevents novelty rejection; strengthens positioning. | Low |
| **P1** | Expand token redundancy analysis to 500+ sequences; add sensitivity ablation for high-similarity tokens. | Validates foundational motivation for adaptive sparsity. | Medium |
| **P1** | Report speedup separately for prefilling and autoregressive generation; discuss kernel/memory overheads. | Improves practical deployment analysis. | Medium |
| **P2** | Replace ad-hoc KV cache threshold with learned mechanism or acknowledge as heuristic limitation. | Enhances routing elegance and generalization. | High |
| **P2** | Add computational cost (FLOPs/time) comparison against block-wise baselines. | Provides fairer efficiency benchmark. | Medium |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Limitation |
|---|---|---|---|---|---|---|
| E1 | Token redundancy analysis | 50 seqs, 64 tokens, LLaMA2/Qwen1.5 | Cosine similarity | Middle blocks show >99% similarity >0.8 | Motivates adaptive sparsity | Small sample; no sensitivity validation |
| E2 | Main results vs SOTA | LLaMA2/3, Qwen1.5; 5 benchmarks | Accuracy retention | FTP outperforms BlockPruner/ShortGPT by ~10 pts | SOTA in token-wise pruning | No variance; sparsity metric mismatch |
| E3 | Sparsity scheduler ablation | Uniform vs BI-score vs GA | Accuracy | GA scheduler drops 24% less than uniform | Validates GA allocation | Single-seed |
| E4 | Router input ablation | Hidden states vs 4 factors | Accuracy | 4 factors outperform hidden states | Validates low-dim design | Missing normalization details |
| E5 | Inference speedup | Alpaca prompts, LLaMA2-7B | Speedup ratio | 1.28x-1.61x at 30-40% sparsity | Validates efficiency | Prefilling only; overheads unanalyzed |

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Cost | Gain |
|---|---|---|---|---|---|---|---|
| Statistical reliability | Gains are consistent across seeds | Run E2/E3/E4 over 3 seeds | Same setup | Mean ± std | Std < 0.5% | Low | High |
| Redundancy prunability | High similarity tokens can be safely skipped | Randomly skip high-sim tokens in validation | Dense baseline | Accuracy drop | Drop < 1% | Low | High |
| Autoregressive speedup | FTP maintains speedup during generation | Measure tokens/sec on text generation | Dense + KV cache | Tokens/sec | >1.1x speedup | Medium | High |
| Loss symmetry impact | Symmetric $L_s$ stabilizes training | Replace asymmetric $L_s$ with MSE | Current $L_s$ | Accuracy/Sparsity | Stable target sparsity | Low | Medium |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10
**Post-Revision Target:** [7.5, 8.5]/10

**Justification:** The paper presents a promising and practically motivated method (FTP) for token-wise dynamic pruning without retraining, with strong empirical results and a well-designed decoupled optimization pipeline. However, the score is moderated by overgeneralized claims, lack of variance reporting, methodological ambiguities in loss design, and weak statistical validation of the redundancy motivation. Addressing the P0/P1 revision items (variance reporting, loss symmetry, claim bounding, redundancy sensitivity) would significantly strengthen the paper's scientific rigor and novelty positioning, justifying a higher post-revision score.

```text
ASCII Diagram — Paper Structure & Evidence Map
[Problem: LLM inference overhead]
    -> [Gap: Static pruning needs retraining/hardware; dynamic methods are heavy]
    -> [Insight: Depth-dependent token redundancy (similarity >0.8)]
    -> [Method: FTP (GA scheduler + 4-factor dynamic router)]
    -> [Evidence: SOTA accuracy retention vs BlockPruner/ShortGPT]
    -> [Gap: Missing variance, asymmetric loss, ad-hoc KV threshold]
    -> [Fix: Multi-seed eval, symmetric loss, learned threshold]
```

```text
ASCII Diagram — Revision Strategy Roadmap
| Priority | Low Effort | High Effort |
|---|---|---|
| High Impact | Bound SOTA claims + fix asymmetric loss | Add multi-seed variance + redundancy sensitivity |
| Medium Impact | Clarify loss decay/normalization | Report autoregressive speedup + overhead analysis |
```

```text
ASCII Diagram — Related-Work Taxonomy Tree (Layered)
LLM Compression (Root)
├── Branch 1: Static Pruning
│   ├── Leaf 1.1: Weight-level (SparseGPT, Wanda)
│   ├── Leaf 1.2: Width/Depth (LLM-Pruner, ShortGPT, BlockPruner)
├── Branch 2: Dynamic/Conditional Computing
│   ├── Leaf 2.1: Weight/Head Activation (DejaVu, ShadowLLM)
│   └── Leaf 2.2: Token Routing (MoD [hidden states], FTP [low-dim factors])
└── Branch 3: Prompt/Context Compression
    ├── Leaf 3.1: Perplexity-based (LLMLingua)
    └── Leaf 3.2: RL-based (PCRL)
Manuscript Position: Leaf 2.2 (Differentiated by no-retraining + low-dim inputs)
```