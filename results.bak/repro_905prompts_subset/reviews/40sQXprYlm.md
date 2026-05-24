Now I have a solid calibration. Let me finalize the score at **5.0** and write the review.

**Score bracket from round 1:** The paper is clearly stronger than the 3.0–4.0 band (ViMoE, A-MoD) and weaker than the 6.0–6.33 band (Initialisation/Specialisation paper). This places it squarely in the 4.5–5.5 range.

**Narrowing (round 2):** The Neural Modules paper (4.75) and Hyper-UT paper (5.0) are the closest anchors. The DNA paper has a more novel conceptual framework and broader scope (two domains, extensive qualitative analysis) than Neural Modules, but shares similar weaknesses in evaluation rigor. It is somewhat stronger than the A-MoD paper (4.0), which was rejected for limited applicability and unfair comparisons, because DNA's contribution is more fundamental. It is weaker than the Specialisation paper (6.0), which has formal theoretical grounding. The paper sits at **5.0**: genuine novelty and interesting findings, held back by incomplete evaluation.

---

## Summary

The paper introduces Distributed Neural Architectures (DNAs), a framework where each token follows a learned, token-specific path through a collection of modules (transformer, MLP, attention blocks) guided by learned routers. The framework generalizes MoE, MoD, weight sharing, and early exit as special cases that can emerge during training. Vision DNAs (at ViT-small scale) and language DNAs (at GPT-2 medium scale) are trained from scratch and shown to be competitive with their dense baselines, while learning to skip compute (25–30% of tokens) and to share parameters in a data-dependent manner. The paper's main contribution is a rich qualitative analysis of the emergent structure: path distributions follow power laws, routers specialize (e.g., punctuation to one module, verbs to another), and compute allocation correlates with visual complexity.

## Strengths

- **Novel and conceptually interesting framework.** The idea of allowing every token to follow an arbitrary learned path through a collection of modules, with no fixed notion of depth or width, is genuinely novel. The paper correctly identifies that MoE, MoD, weight sharing, and early exit are all special cases that can emerge from the same framework, and the vision experiments confirm that a mixture of all these strategies does indeed co-emerge during training. This is a conceptual advance over prior work that typically focuses on one technique in isolation.

- **Multidomain feasibility demonstration.** Training DNAs in both vision (ImageNet, ViT-small scale) and language (FineWeb-Edu, GPT-2 medium scale) shows the framework is not a one-off trick. The top-2 vision DNA reaches 78.8% (vs. ViT-small's 79.8%), and the top-2 language DNA surpasses GPT-2 medium on 6 of 8 benchmarks (HellaSwag: 41.8 vs. 40.5, PIQA: 67.9 vs. 66.9). Given the explicit disclaimer that the paper is not focused on beating SOTA, these results convincingly establish that DNAs are trainable and competitive.

- **Rich qualitative analysis of emergent structure.** The paper goes beyond reporting aggregate metrics and extensively visualizes what the model learns: path distributions are power-law distributed (Fig. 1c–d), patches following the same path share semantically meaningful features (edges, objects, backgrounds — Fig. 3), early language routers group tokens by syntactic role (punctuation → M₂₇, word pieces → M₂₉ — Fig. 8), and deep-dream reconstructions show progressive feature extraction (texture → lighting → large-scale features — Fig. 4). This level of analysis is rare and genuinely insightful for understanding what conditional computation models discover.

- **Honest reporting and appropriate scope.** The paper explicitly states it is not focused on SOTA (§1), acknowledges negative findings (language parameter sharing "is most likely random", §4.3), and provides an honest discussion of limitations. This intellectual honesty strengthens the credibility of the positive findings.

## Weaknesses

### Fatal
None.

### Major

- **No comparison to existing conditional computation methods.** The paper positions DNA as a generalization of MoE and MoD, yet never directly compares against a standard MoE or MoD baseline at the same scale. Without this comparison, the reader cannot assess whether the extra complexity of DNAs (routers at every step, variable-length groups for sparse attention) yields any benefit over simpler conditional computation methods, or whether a standard MoE/MoD model would match or exceed DNA performance with fewer moving parts. This is the most significant gap in the evaluation. The paper convincingly shows DNAs *are feasible* but does not show they are *distinctive* relative to existing approaches.

### Minor

- **Compute efficiency claims lack absolute quantification.** The paper reports "25% skip" and "30% skip" and shows normalized compute distributions (Fig. 5), but never reports FLOPs, latency, or throughput relative to the dense baseline. The accuracy–efficiency claims (e.g., "can learn to use less compute with minor effects on performance") would be substantially strengthened by reporting average FLOPs per image/token for the DNA models vs. the dense baseline. As written, the magnitude of the compute savings is unclear: 25% skip rate does not translate to 25% FLOP reduction because the top-2 routing uses two modules per step for non-skipped tokens, and the sparse attention patterns have variable cost.

- **Language model comparison is not parameter/compute controlled.** The top-2 DNA (433M active params) has more active parameters than GPT-2 medium (406M), and the top-2 routing processes two modules per step, likely increasing FLOPs per token relative to the dense baseline. While the paper reports these numbers transparently (Table 2), the claim that top-2 DNA "matches or exceeds" GPT-2 is weakened by this asymmetry. A comparison with a top-1 DNA at matched active parameters (or a FLOPs-controlled comparison) would cleanly separate architecture quality from capacity.

- **Interpretability analysis is entirely qualitative.** The claims about path specialization, routing interpretability, and emergent grouping are supported only by visual inspection of example patches and deep-dream images. While striking, these visualizations do not constitute a quantitative evaluation (e.g., measuring mutual information between path identity and semantic categories, or a human evaluation of whether routing decisions correspond to label-relevant features). The paper's own comparison to a random baseline (§3.2) notes that the random model also clusters images, but does not formalize the difference.

- **Gradient propagation through discrete routing is underspecified.** The paper uses softmax probabilities ρ_i^{(s)} to weight module outputs in Eq. (1), which is the standard approach in MoE routing (gradients flow through the differentiable ρ weights). However, the paper's phrasing "the routing decision is made by sampling with hard top-k" is imprecise — the top-k selection is deterministic given ρ, and how gradients reach the router parameters of non-selected modules is not discussed. A brief clarification (e.g., "gradients flow through the softmax probabilities ρ_i^{(s)} that weight the module outputs; selected modules' contributions are ρ-weighted, making the router differentiable") would resolve the ambiguity. This is not a fatal gap — the mechanism is standard — but the current presentation is insufficiently clear for reproducibility.

### Trivial
- The footnote about Eq. (1) ("Somewhat awkward form...") could be integrated into the main explanation for clarity.
- The "flow of patches" diagrams (Fig. 2 bottom) are difficult to parse because circle sizes encode activation frequency but the clustering in columns makes sparse structure hard to see.

## Nice-to-Haves
- A FLOPs-controlled comparison with a standard MoE and MoD model at the same scale would substantially strengthen the paper's claim that DNAs are a useful generalization of conditional computation.
- A quantitative metric for path interpretability (e.g., mutual information between path rank and WordNet hypernyms for vision, or POS tags for language) would move the analysis from suggestive to demonstrative.
- The paper could discuss how the sparse attention patterns (tokens only attend within their routed group) are implemented in practice (padding? dynamic batching?), as this is a non-trivial engineering detail.

## Removed Points
These points from the input reviews were removed; treat them with caution:
- **"Critical structural gap" about gradient estimation.** The harsh critic claimed the paper has no mechanism for gradient propagation through discrete routing. This is incorrect: Eq. (1) uses differentiable softmax probabilities ρ_i^{(s)} to weight module outputs, which is the standard approach used throughout the MoE literature. The paper could be clearer, but there is no missing component. Downgraded from Fatal to Minor.
- **Complaints about missing appendix/hyperparameter details.** These are parser artifacts; the appendix exists in the original submission. Removed per protocol.
- **Complaints about "not yet released" or "cannot be independently verified" for cited models/references.** Removed per protocol (all cited entities are assumed to exist).
- **Strength Finder claims about "competitive performance" that overstated results.** The Strength Finder's claim that top-2 DNA "surpasses GPT-2 medium on 6 of 8 benchmarks" is factually correct and grounded in Table 3 (though the active-params asymmetry is noted).
- **Strength Finder's claim about "emergent parameter sharing without explicit regularization" being a strength.** This is a reasonable observation but the paper's own analysis in the language domain concludes module reuse is "most likely random" — the strength and weakness conflict, so the strength is downgraded (the finding is that sharing is not semantically meaningful in language). Moved here.

## Novel Insights
The most interesting finding is the contrast between vision and language in how path structure emerges: vision paths specialize by semantic content (object boundaries, backgrounds, textures) in a way that is consistent across random seeds, while language parameter sharing turns out to be "most likely random" (§4.3). This asymmetry suggests that the nature of the training data (and possibly the objective — discriminative vs. generative) fundamentally shapes what kind of modularity conditional computation discovers. This is a useful caution for the field: not all emergent structure in routed models is semantically meaningful; some may be an artifact of the optimization process. The power-law path distribution (exponent ~−1.2 for language vs. ~−1 for random) also provides a quantitative signature that distinguishes learned from random routing, which could serve as a diagnostic tool for future work.

## Suggestions
1. Add a FLOPs comparison (or at least relative compute cost) for the skip models vs. the dense baseline and vs. a standard MoE/MoD model at the same scale.
2. Include a top-1 DNA in the language experiments with active parameters matched to GPT-2 medium (adjust d_embed or N_m accordingly) to enable a cleaner comparison.
3. Provide at least one quantitative metric for interpretability: e.g., for vision, measure whether patches routed to the same path have lower variance in pixel-level features than random baselines, or compute the adjusted Rand index between path assignments and semantic categories derived from ImageNet synsets.
4. Clarify the gradient flow through routers in Section 2.2 with one sentence stating that gradients propagate through the softmax probabilities ρ_i^{(s)} in Eq. (1).

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|-------------------------|
| XVHXVdoV11 | 3.40 | R1: weak bracket | Weaker — less rigorous, narrower contribution |
| KaYXsoCxV7 | 3.00 | R1: weak bracket | Weaker — limited scope, less novelty |
| sTI75sFQkn | 3.25 | R1: weak bracket | Weaker — narrower domain |
| OovfCS4FYT | 3.25 | R1: weak bracket | Weaker — narrower contribution |
| tI3eqOV6Yt | 5.00 | R1: middle bracket | Similar — both introduce novel routing methods with evaluation gaps |
| 0pLCDJVVRD | 7.00 | R1: middle bracket | Stronger — more rigorous analysis, formal grounding |
| aN4Jf6Cx69 | 4.50 | R1: middle bracket | Weaker — narrower scope, simpler model |
| rUC7tHecSQ | 6.33 | R1: middle bracket | Stronger — more mechanistic analysis |
| 5Ca9sSzuDp | 8.00 | R1: strong bracket | Much stronger — rigorous interpretability methodology |
| jIAKjjEmWi | 4.00 | R2: low-mid bracket | Similar but weaker — narrower (vision only), less novelty |
| pNgY6ODeMp | 4.25 | R2: low-mid bracket | Weaker — different subfield |
| McqeEcMSzy | 3.67 | R2: low-mid bracket | Weaker — narrower analysis |
| ZSvOIT5Ai2 | 4.33 | R2: low-mid bracket | Similar quality, different subfield |
| RQz7szbVDs | 6.00 | R2: mid bracket | Stronger — formal theoretical analysis |
| nt8gBX58Kh | 6.33 | R2: mid bracket | Stronger — quantitative analysis method |
| S04xvGXjEs | 6.00 | R2: mid bracket | Stronger — more rigorous methodology |
| ar9tcnD4e9 | 4.75 | R2: mid bracket | Similar — both propose flexible graphs with incomplete evaluation |

**Round-1 bracket:** Between ~3.5 and ~7.5, plausibly 4.5–5.5.

**Round-2 narrowing:** The anchor papers at 4.75 (Neural Modules) and 5.0 (Adaptivity/Modularity) are the closest comparators. The DNA paper has a more novel and ambitious framework than either, and provides broader evidence (two domains, extensive qualitative analysis). However, it falls short of the 6.0 anchors (which have formal theoretical grounding or rigorous quantitative methodology). The missing MoE/MoD comparison, lack of FLOPs quantification, and purely qualitative interpretability analysis prevent it from reaching the 6.0 tier. Score set at **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>