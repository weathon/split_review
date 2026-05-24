Now I have a clear picture. Let me write the consolidated review.

## Summary

This paper introduces Distributed Neural Architectures (DNA), a new architecture family where tokens (or patches) are dynamically routed through a pool of heterogeneous modules (transformers, attention, MLPs, and identity operations). Unlike fixed feed-forward or MoE designs, DNAs allow any token to traverse any sequence of modules, with connectivity and compute allocation emerging entirely from end-to-end training. The authors train DNA models for image classification (ImageNet) and language modeling (FineWeb-Edu), demonstrating that they are competitive with dense baselines, exhibit interpretable emergent routing patterns (power-law path distributions, module specialization), and can learn to allocate compute dynamically.

## Strengths

- **Novel architectural contribution with broad scope.** The paper proposes a genuinely new point in the architecture design space — going beyond MoE or MoD by allowing fully distributed, learned routing across a heterogeneous module pool. This subsumes many existing sparse and conditional-computation methods as special cases and opens an interesting research direction.

- **Competitive performance across two domains.** The top-1 DNA reaches 79.1% ImageNet accuracy against ViT-Small's 79.8% (Figure 2), and the top-2 DNA language model achieves lower validation loss and higher zero-shot scores than GPT-2 medium on most benchmarks (Table 3: e.g., 2.674 vs 2.720 loss, 59.2 vs 58.9 ARC-E, 67.9 vs 66.9 PIQA). This substantiates the core claim that distributed architectures are trainable and not obviously broken.

- **Compelling emergent structure.** The power-law distribution of token paths (Figure 1c,d, exponent ≈ −1.2 after training), the interpretable grouping of patches by path frequency (Figure 3: low-rank paths capture edges/flat regions, high-rank paths capture object-specific concepts), and the deep-dream routing reconstruction (Figure 4) all provide genuine insights into how the trained models organize computation. These are non-trivial observations that go beyond standard benchmark reporting.

- **Honest scoping and self-critique.** The paper explicitly states it is a proof-of-concept, not a SOTA-chasing exercise ("we emphasize that our work is *not* focused on beating SOTA models"), and acknowledges limitations including the random nature of parameter reuse in language models (Section 4.3). This intellectual honesty strengthens the contribution.

## Weaknesses

### Fatal

None.

### Major

- **Efficiency-performance tradeoff is weakly substantiated.** The paper's abstract claims that "DNA models can learn to use less compute with minor effects on performance," but the supporting evidence is incomplete. For the vision top-2 DNA (25% skip), the accuracy is shown in Figure 2 (78.8%) but it is ambiguous whether this figure refers to the skip variant or a different top-2 model — the table and figure use inconsistent naming. More critically, for language, the top-2 DNA (30% skip) achieves a validation loss of 2.784, which is worse than both the dense GPT-2 (2.720) and the shallower GPT-2 baseline (2.772), and its downstream scores degrade substantially (e.g., LAMBADA drops from 34.0 to 23.8). The shallower GPT-2 baseline, which was designed to match the skip model's effective depth, actually *outperforms* the skip DNA. This undermines the claim that the learned routing provides an advantage over simply using a shallower fixed network. The paper should either soften this claim or provide a controlled comparison demonstrating that skipping via learned routing beats skipping via uniform depth reduction.

- **Interpretability claims remain qualitative and lack quantitative support.** The visualizations in Figures 3, 4, and 8 are evocative, and the observations about path specialization are suggestive, but no quantitative metrics are provided. Without measuring routing consistency (e.g., do the same tokens always follow the same paths across different contexts?), predictive information between paths and token properties (e.g., mutual information between path rank and POS tags), or controlled baselines (e.g., comparing path clustering quality against a fixed-order network), the claim that routing is "interpretable" and paths "specialize" remains anecdotal. The paper itself acknowledges that random networks already produce power-law path distributions (exponent −1), so the trained model's exponent of −1.2 is a modest shift; the difference between trained and random specialization is not rigorously characterized.

### Minor

- **Parameter-matching in comparisons is imperfect.** The vision top-1 DNA uses 34M total parameters against ViT-Small's 22M while achieving 0.7% lower accuracy. The language top-2 DNA uses 433M active parameters against GPT-2 medium's 406M. While the paper does not claim parameter-matched superiority, these mismatches complicate the interpretation of the competitive results — the performance could reflect parameter scaling rather than architectural benefit.

- **Limited architectural ablation.** The number of modules ($N_m$), routers ($N_r$), backbone layers ($N_b$), and top-$k$ are set without sensitivity analysis. Reporting how performance varies with these choices would help the community understand whether DNAs are robust to these hyperparameters or require careful tuning.

- **Single training runs without variability estimates.** While single-run evaluation is standard for ImageNet-scale experiments, reporting at least the variance across the grid search (3 learning rates × 4 weight decays for vision) would give readers a sense of training stability.

### Trivial

- The identity-module bias update in Eq. (3) is accurately described as encouraging skip behavior, but calling it "not load-balancing" (Section 2.2) while it structurally resembles the DeepSeek load-balancing mechanism is imprecise phrasing.
- The relationship between Figure 2's "Top-2 DNA" label and Table 1's "top-2 DNA (25% skip)" label should be clarified — it is unclear whether they refer to the same model.

## Nice-to-Haves

- A controlled comparison isolating the effect of learned routing: e.g., a dense network with equivalent *total* parameters, and a dense network truncated to match the average FLOPs of the skip-DNA model. This would separate routing benefit from simple parameter/depth scaling.
- Quantitative routing specialization metrics: mutual information between path assignment and token POS tags (language) or patch object-mask membership (vision).
- Reporting FLOP counts or wall-clock latency rather than the "effective compute nodes" proxy.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "Missing performance metrics for efficient vision models undermines the efficiency story"** — The accuracy for the top-2 DNA (25% skip) vision model IS reported in Figure 2 as 78.8%. The confusion stems from inconsistent labeling between Table 1 and Figure 2, which is a presentation issue, not missing data. The language skip model IS evaluated (Table 3). The criticism that the accuracy is "never reported" is factually incorrect. However, the efficiency claim *is* weakened by the skip-DNA underperforming the shallower baseline in language, which is retained as a Major weakness above.

- **Harsh Critic: "The causal alignment of the language-model routing is under-specified and potentially problematic"** — The forward pass is inherently causal: each token's routing decision at step $s$ depends only on its own hidden state $h^{(s,t)}$, which is computed from previous steps. When multiple tokens are routed to the same attention module, standard causal masking within that module preserves autoregressivity. The paper states this in Section 2.1 ("the latter makes it clear that the forward pass is fully causal"). While a more detailed explanation would help, this is not a methodological gap.

- **Harsh Critic: "Comparison to baselines lacks the rigor needed to establish competitiveness"** — The paper performs grid search over learning rates and weight decay for both domains, which is standard practice. Single runs without error bars are typical for this scale of experiment (ImageNet ViT training). The parameter-matching concern is retained as a Minor weakness above, not as a rigor issue.

- **Strength Finder: "Power-law structure of path distributions" as a standalone strength** — While interesting, the paper itself notes that random networks also produce power-law distributions with exponent −1, so the trained exponent of −1.2 represents a modest shift. The strength of this finding is partially undercut by the paper's own baseline. The specialization finding (retained above) is the stronger contribution.

## Novel Insights

The most genuinely novel insight from the paper — and one that the reviews help crystallize — is that a fully distributed architecture with *no pre-specified depth or width* can be trained end-to-end without collapsing to a degenerate routing strategy, and that the resulting path distribution follows a power law even before training (suggesting the routing space itself has intrinsic structure that training sharpens rather than creates). This is a different category of finding from typical architecture papers that report only benchmark numbers, and it raises interesting questions about whether the routing landscape of randomly initialized modular networks has universal properties.

## Suggestions

- Restructure the efficiency section to present a clean head-to-head: skip-DNA vs. a shallower dense model matched for *average compute per token*. This single comparison would either validate or qualify the "minor effects on performance" claim.
- Add one quantitative table for interpretability: e.g., mutual information between path clusters and ground-truth token categories (POS tags for language, object-vs-background masks for vision). This transforms the interpretability claim from illustrative to testable without requiring a large new experimental effort.
- Clarify Figure 2 labeling to unambiguously map each plotted curve to the corresponding row in Table 1.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
| Anchor | Score | How it compares |
|--------|-------|-----------------|
| ViMoE (KaYXsoCxV7) | 3.00 | Weaker: limited to one domain, marginal novelty, narrow experiments |
| MoLE (uWvKBCYh4S) | 5.00 | Slightly weaker: straightforward MoE-LoRA fusion, less ambitious |
| SMEAR (QHzzAU7Qf9) | 6.00 | Comparable: novel routing method, good analysis, but rejected due to limited scale |
| Monet (1Ogw1SHY3p) | 7.00 | Stronger: tight integration of interpretability into architecture design with stronger evaluation |
| MoE++ (t7P5BUKcYv) | 8.00 | Stronger: clear efficiency contribution with strong experimental validation |

**Round 1 bracket: 4.0 – 6.5**

**Round 2 — Narrowing:**
| Anchor | Score | How it compares |
|--------|-------|-----------------|
| CORTEX (oW7jUu4gVg) | 4.25 | DNA is stronger: broader domain coverage, novel architecture, not just interpretability |
| INViTE (5iENGLEJKG) | 5.25 | DNA is comparable/slightly stronger: novel architecture vs. interpretation method for existing models |
| SMN (pEKJl5sflp) | 6.00 | DNA is slightly weaker: broader experiments but less theoretical grounding, weaker efficiency claims |

**Final score:** The paper lands between INViTE (5.25) and SMN (6.00). It has broader experimental coverage than either but its efficiency claims are weakly substantiated and the interpretability analysis is qualitative-only. These gaps place it closer to 5.5 than 6.0 — a solid proof-of-concept with genuine novelty and interesting findings, but with evaluation gaps that prevent stronger claims from being fully supported.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>