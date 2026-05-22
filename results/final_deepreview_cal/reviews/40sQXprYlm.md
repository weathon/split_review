Now I have a thorough understanding of the paper and the reviewer inputs. Let me write the final consolidated review.

## Summary

The paper introduces Distributed Neural Architectures (DNAs), where each token follows an individually learned path through a collection of modules (MLP, attention, transformer blocks). Routers determine the path, and identity modules enable variable compute per token. DNA vision models are trained on ImageNet (competitive with ViT-Small: 79.1% vs 79.8%) and language models on FineWeb-Edu (top-2 DNA achieves lower validation loss than GPT-2 Medium: 2.674 vs 2.720). The paper analyzes emergent path distributions (power-law), routing specialization, and interpretable compute allocation.

## Strengths

- **Cross-domain feasibility demonstrated**: DNA models are successfully trained in both vision (ImageNet, within 0.7% of ViT-Small) and language (competitive with GPT-2 Medium, outperforming on 5/7 zero-shot benchmarks). This non-trivial result — that fully flexible token-level routing can be trained end-to-end — is the paper's core empirical contribution.

- **Emergent interpretable specialization**: The paper provides compelling visual evidence (Figs. 3, 8) that routing decisions are semantically meaningful. In vision, low-rank paths group edges/color regions while high-rank paths capture specific concepts (brass instruments, puzzle pieces). In language, the first router consistently sends punctuation to one module, verb forms to another, prepositions to distinct modules — across different documents. This goes beyond anecdotal by analyzing both trained and randomly initialized models to establish a baseline.

- **Honest analysis of limitations**: The paper explicitly acknowledges when findings are weak or negative. For language models, it notes that parameter sharing "is most likely random" and does not correlate with text features, and that models are "way too small to truly absorb" the 21B tokens. The random initialization baseline for path distributions is also provided. This intellectual honesty strengthens the paper's credibility.

- **Power-law path distribution finding**: The observation that path frequencies follow a power-law distribution (exponent ≈ −1.2 for trained vs −1 for random), and the analysis of what this means for specialization, is a genuinely interesting finding about the emergent structure of DNAs.

## Weaknesses

### Fatal
None.

### Major

1. **No comparison to the conditional computing methods the paper claims to generalize**: The paper explicitly positions DNAs as "a natural generalization of the sparse methods such as Mixture-of-Experts, Mixture-of-Depths, parameter sharing" and says the construction "includes feed-forward, MoE, MoD, weight sharing, early exit as particular cases." Yet no comparison to any of these methods is provided. A standard top-2 MoE transformer or Mixture-of-Depths model of comparable width/depth would be the natural baseline to determine whether the extra flexibility of DNAs is beneficial or merely adds complexity. Without this, the paper cannot substantiate its strongest claim — that the generalization is useful.

2. **Compute efficiency evaluation is thin**: Only one skip rate is tested per domain (25% in vision, 30% in language) with no ablation across different compute budgets. Compute is measured only as "effective compute nodes" — no FLOP counts, wall-clock time, or throughput are reported. The 1% accuracy drop for the 25%-skip vision model is presented without comparison to a smaller dense model of matched FLOPs, making it unclear whether the trade-off is favorable relative to simply training a smaller model. The overhead introduced by the routers themselves (parameters and compute) is also not analyzed.

3. **No hyperparameter ablation on core architectural choices**: The paper introduces several critical design parameters — number of modules ($N_m$), number of routers ($N_r$), backbone depth ($N_b$), maximum steps ($s_{\max}$) — but provides no ablation on any of them. It is unclear how sensitive the results are to these choices, which limits the guidance for future work.

### Minor

1. **Path specialization analysis is primarily qualitative**: While the visualizations are compelling (Figs. 3, 8), the paper does not provide quantitative metrics for specialization (e.g., mutual information between path and class, clustering purity, or a statistical test comparing trained vs. random model specialization). The paper acknowledges that random models also cluster images, but does not quantify *how much* additional structure the trained model provides.

2. **Language models are undertrained (acknowledged)**: The 21B token training for models at GPT-2 Medium scale is far below compute-optimal (Chinchilla) ratios. The paper acknowledges this, but it limits the strength of conclusions about language capabilities. The language results (Table 3) show mixed outcomes — the top-1 DNA is slightly worse than GPT-2 Medium on most metrics — which casts some doubt on whether the routing flexibility helps or hurts in language at this scale.

3. **Causality mechanism for attention in language is underspecified**: The paper states the forward pass is "fully causal" and that attention is computed "only between these tokens," but does not explicitly describe the masking strategy when attention modules receive a non-contiguous subset of tokens from the original sequence. The intended mechanism (standard causal masking based on original positions, applied only to the subset of tokens that arrive at each module) is recoverable from context, but a clearer specification would improve reproducibility.

### Trivial

- Table 3 has "GPT-2 (30% shallover)" — likely a format-breaking artifact of "shallower" (confirmed by the caption which reads "shallower GPT-2"). Minor typo, not a paper error.

## Nice-to-Haves

- An ablation over different skip ratios (e.g., 10%, 25%, 50%) to show the compute-accuracy Pareto frontier.
- FLOP counts or wall-clock measurements to ground the compute efficiency analysis.
- A comparison to a smaller dense model with matched active parameters/FLOPs for the compute-efficient variants.
- Comparison to a standard MoE or MoD baseline of comparable scale and compute budget.

## Removed Points

These points from the harsh critic are flagged for removal; treat them with caution:

- **"Gradient propagation through discrete routing is unresolved"** — REMOVED. The paper uses softmax probabilities (ρ) as differentiable weights in Eq. (1) with hard top-k selection, which is standard practice in MoE routing (gradients flow through the softmax weights of selected modules; non-selected modules receive zero gradient). This is sufficiently specified and not novel to this paper.
- **"Causality is a structural flaw that invalidates language experiments"** — DEMOTED to Minor. The paper explicitly states the forward pass is "fully causal" and attention is computed "only between these tokens." The intended mechanism (causal masking on original positions, applied to each module's subset) is standard and adequately implied. The description could be more explicit, but it does not threaten the validity of the experiments.
- **"Parameter sharing claim is misleading"** — REMOVED. The paper uses "emergent, input-dependent weight sharing" and "parameter sharing can be learnt from data" interchangeably, both of which accurately describe the observed phenomenon (modules receiving input from many tokens, creating de facto weight sharing across those tokens).
- **"GPT-2 (30% shallover) needs clarification"** — REMOVED. The caption clarifies this as "shallower GPT-2"; it is a parser artifact.
- **"The bias update justification is thin"** — DEMOTED to Minor/nice-to-have. The paper adapts the DeepSeek bias trick for a different purpose (skip encouragement rather than load balancing). A brief analysis of convergence would be nice but is not required for a feasibility paper.
- **Strength Finder's generic claims about "important problem"** — REMOVED or merged into substantive strengths above.

## Novel Insights

The most interesting insight not fully articulated by the paper itself is the contrast between the vision and language domains in terms of routing dynamics. In vision, routing specialization is clear: path choices correlate strongly with visual features (edges, backgrounds, object boundaries), compute allocation aligns with image complexity, and parameter sharing patterns are consistent across random seeds. In language, however, the same analysis reveals weaker structure: parameter sharing "is most likely random," path specialization is less crisp (common words appearing in rare/high-rank paths), and the compute distribution is nearly uniform despite the dataset's diversity. This asymmetry suggests that the optimal routing structure depends strongly on the modality and task — visual classification may inherently favor spatially-localized specialization, while language modeling's sequential prediction objective may not reward path separation as strongly. This observation, which the paper honestly reports but does not foreground, is a valuable guide for future DNA designs: the routing topology may need to be modality-aware rather than one-size-fits-all.

## Suggestions

1. Add at least one conditional computing baseline (MoE, MoD, or layer-skip) at comparable parameter and compute budgets. This is the single most impactful addition — it would allow the paper to substantiate its main claim that DNAs are a *useful* generalization.
2. Include FLOP counts or throughput measurements for the compute-efficiency experiments, along with a Pareto analysis over multiple skip ratios.
3. Ablate at least one key architectural hyperparameter ($N_m$ or $N_b$) to show sensitivity.
4. Provide a quantitative measure of path specialization (e.g., clustering purity or adjusted mutual information compared to the random initialization baseline).
5. Explicitly describe the causal masking strategy for attention modules in language DNAs.

## Score and Decision

**Round 1 — Bracketing**: Three queries anchored weak (score < 3.5), middle (3.5–7.5), and strong (> 7.5) papers. Weak anchors included papers on decentralized training (2.00) and structural adaptation (2.33–3.40). Strong anchors included papers on interpretability (7.60–8.00) and vision-language understanding (8.00). The DNA paper is clearly above the weak band and well below the strong band, placing it in the middle band (3.5, 7.5).

**Round 2 — Narrowing**: Within the middle band, I queried 4.5–6.0 and 6.0–7.5. The paper is stronger than Gradient Routing (5.25, Reject) which had thinner experimental validation and narrower scope, and comparable to COMET (5.67, Accept) which similarly proposes a modular/sparse routing architecture without exhaustive baselines. The DNA paper's cross-domain validation and honesty about limitations are strengths, but it is clearly weaker than SparseFormer (6.25), Denoising Task Routing (7.33), and LLaVA-Mini (6.50) which have more rigorous experimental methodology. Among lower-middle anchors: Adaptivity and Modularity (5.00, Reject), Gradient Routing (5.25, Reject), COMET (5.67, Accept), Words in Motion (4.80, Accept). The DNA paper sits above the rejected papers due to its cross-domain validation and genuinely interesting emergent phenomena, but below the stronger papers due to missing baselines and thin efficiency evaluation.

**Final score**: 5.5. The paper presents a novel and interesting architectural framework with honest analysis. The main gap — absence of comparison to the conditional computing methods it claims to generalize — prevents it from reaching a stronger score. The idea has real potential and the cross-domain feasibility demonstration is valuable.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>