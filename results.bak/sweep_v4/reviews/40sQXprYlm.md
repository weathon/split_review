Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper introduces Distributed Neural Architectures (DNAs), a framework where tokens follow learned, content-dependent paths through a set of modules and routers. DNAs generalize feed-forward networks, MoE, MoD, weight sharing, and early exit as special cases. The authors train DNA models in both vision (ImageNet, ViT-small scale) and language (FineWeb-Edu, GPT-2 medium scale), showing that they are trainable, broadly competitive with dense baselines, and can learn input-dependent compute allocation with interpretable routing patterns.

## Strengths

1. **Conceptual novelty and unified framing.** The idea that tokens can take arbitrary learned paths through a collection of modules — subsuming MoE, MoD, parameter sharing, and early-exit as special cases — is conceptually appealing and genuinely novel. The paper provides a clear formalization (equations 1–3, Fig. 1a–b) of how this can be instantiated.

2. **Feasibility demonstrated in two domains at non-trivial scale.** The paper trains DNAs on ImageNet (300 epochs, 2048 batch size, up to 34M params) and on FineWeb-Edu (21B tokens, up to 603M params). The top-2 DNA vision model (25% skip) reaches 78.8% accuracy with *fewer* total parameters (18M) than ViT-small (22M). The top-2 DNA language model (433M active params) achieves lower validation loss (2.674 vs 2.720) and outperforms GPT-2 medium on six of seven zero-shot benchmarks (Table 3). This establishes that the architecture class is trainable at moderate scales.

3. **Interpretable routing and specialization.** The paper shows several pieces of evidence that routing decisions are semantically meaningful: (i) low-rank vision paths aggregate patches sharing high-level features (edges, flat color), while high-rank paths capture specific concepts (brass instruments, puzzle pieces) (Fig. 3); (ii) reconstruction via routing-maximization (deep-dream style, Fig. 4) reveals a hierarchy from texture/edges to larger-scale structure; (iii) in language, early routers group semantically similar tokens — punctuation to one module, verb variants to another, plural nouns to a third (Fig. 8). These analyses are qualitative but well-illustrated.

4. **Honest reporting of limitations.** The paper explicitly acknowledges that: (a) random initialization already produces power-law path distributions (Fig. 1c–d caption); (b) a randomly initialized DNA can also cluster images, though by superficial features (Sec. 3.2); (c) in language, parameter sharing "is most likely random" (Sec. 4.3). This candor strengthens the credibility of the positive findings.

## Weaknesses

### Fatal
None.

### Major

1. **No experimental comparison to existing conditional computing methods (MoE, MoD, Layer-Skip).** The paper repeatedly states that DNAs "are a natural generalization of the sparse methods such as Mixture-of-Experts, Mixture-of-Depths, parameter sharing" and that "a mixture-of-*all*-of-these-methods emerges from end-to-end training." Yet the experiments contain zero comparison to any MoE, MoD, or Layer-Skip baseline. Without showing that DNAs match or outperform these simpler, well-studied techniques — on accuracy, compute efficiency, or interpretability — the central framing of the paper as a generalization of existing methods is unsupported. The authors explicitly scope the paper as a feasibility study ("our work is *not* focused on beating SOTA models"), but this does not excuse the absence of comparison to the very methods the paper claims to generalize. A feasibility study of a new architecture class should at minimum include the most natural baselines from that class.

2. **No ablation studies.** The DNA design involves multiple hyperparameters and design choices: backbone depth (`N_b = 0, 1, 2`), number of modules (`N_m`), number of routers (`N_r`), identity modules, the bias trick (Eq. 2–3), top-k value (1 vs 2), the residual combination (Eq. 1), and the backbone itself. Not a single ablation is performed. This makes it impossible to determine which choices are critical. For example, the backbone (1–2 non-routed layers) could dominate performance, making the "distributed" behavior a marginal add-on. Without ablations, the paper is a demonstration of *one specific configuration* rather than a scientific study of the method's principles.

3. **Parameter count mismatch in key comparisons.** The top-1 DNA vision model (34M total) has 55% more total parameters than ViT-small (22M). The top-1 DNA language model (583M total, 406M active) — the variant with matched *active* parameters — underperforms GPT-2 medium (406M) on six of seven benchmarks (Table 3: loss 2.754 vs 2.720, ARC-E 56.9 vs 58.9, HellaS 38.6 vs 40.5, etc.). The top-2 DNA language model (603M total, 433M active) does beat GPT-2, but has 48% more total parameters. While "active parameters" is the standard comparison in conditional computing, the paper should also control for total parameters (or provide a variant that does so) to establish that the routing overhead is justified. Note: the top-2 vision model with 25% skip (18M total) actually has *fewer* total parameters than ViT-small, so this criticism does not apply uniformly — but the paper's strongest claims rely on the cases where the mismatch is largest.

### Minor

4. **Power-law path distribution is confounded with random initialization.** The paper reports that randomly initialized DNAs already produce power-law path distributions with exponent ≈ −1 (Fig. 1c–d caption). The trained vision model also shows exponent ≈ −1 (no change), and the trained language model shifts from −1 to −1.2. The paper treats the power-law as evidence of emergent structure, but the random baseline makes it unclear how much of this structure is inherited from combinatorial path-count statistics rather than learned routing. The paper acknowledges this observation but does not disentangle it — the subsequent interpretability analysis (path specialization) does not control for the random baseline pattern. The specialization analysis in Fig. 3 and Fig. 8 *is* separate evidence of meaningful structure, so this weakness does not invalidate those findings, but the power-law claim itself is weaker than presented.

5. **Language results are mixed and partially undermine the narrative.** The paper honestly reports that parameter sharing in language DNAs "is most likely random" (Sec. 4.3), with no cross-model correlation. The top-1 DNA language model underperforms GPT-2 on most metrics. The top-2 DNA with 30% skip drops sharply in performance (Table 3: loss 2.784 vs 2.720, Wiki perplexity 52.6 vs 33.7). The compute distribution for text (Sec. 4.3) shows most examples requiring similar compute, with low-compute examples corresponding to out-of-distribution text (HTML, non-English characters) — suggesting the model is not learning nuanced compute allocation for typical text. These results suggest that DNAs work better for vision than language at this scale, which limits the generality of the claims.

6. **Interpretability analysis is entirely qualitative.** The path specialization claims (Fig. 3, Fig. 8), routing reconstruction (Fig. 4), and compute allocation analysis (Fig. 5) rely on curated examples and visual inspection. There are no quantitative metrics: no label-based validation that patches following the same path share semantic categories, no statistical significance tests for routing patterns, no quantitative measure of how well routing decisions predict human-annotated image properties. The qualitative analysis is interesting and suggestive, but the lack of quantification weakens the "interpretability" contribution.

### Trivial
None.

## Nice-to-Haves

- Compare to MoE/MoD/Layer-Skip baselines with matched active *and* total parameters. This is the single most important addition for validating the paper's framing.
- Ablate the backbone (try `N_b = 0`), the bias trick (try fixed skipping), and the top-k value.
- Provide quantitative validation of path specialization (e.g., do patches on the same path have the same semantic label?).
- Measure actual FLOPs savings rather than just "effective compute nodes."
- For language, consider adding a load-balancing loss to discourage unused modules and see if performance improves.

## Removed Points

- **"Power-law path distribution undermines the specialization claim entirely"** — REMOVED. The specialization analysis (Figs. 3, 8) is based on content of paths, not the power-law shape. The paper's claim that paths specialize is supported by evidence independent of whether the power-law is learned or inherited.
- **"Bias trick might produce random skipping, no evidence of intelligent skipping"** — REMOVED. The paper provides evidence in Fig. 5 that compute allocation correlates with visual content (boundary patches, object complexity). This contradicts the speculation of uniform random skipping.
- **"Equation (1) lacks justification"** — REMOVED. The paper cites Roberts et al. (2022) and Doshi et al. (2023) for signal propagation properties.
- **"Language results actively undermine narrative"** — DEMOTED to Minor (point 5). The paper is honest about these results; honesty should not be penalized. The finding that parameter sharing is random in language is an interesting negative result, but it limits the generality of the paper's claims.
- **"Missing ablations of various components"** — MERGED into Major point 2.
- **"50% more total parameters for top-2 DNA"** — REMOVED for the vision case; the top-2 DNA (25% skip) has *fewer* total params than ViT-small (18M vs 22M). For language, retained with correction (48% more total, 6.7% more active).
- Various formatting/style nitpicks — REMOVED per rules.
- Missing appendix content — REMOVED per rules (parser strips sections).

## Novel Insights

The harsh critic and strength finder largely converge on the same core assessment, differing mainly in tone. The most interesting insight that emerges from reading both against the paper is that the DNA framework's primary strength — its generality as a unified conditional computing framework — is also its primary weakness in this paper: the paper does not include the experiments needed to validate that generality. The finding that power-law structure appears even in random models raises a broader methodological question for the field: how many "emergent" phenomena in trained neural networks are partly inherited from combinatorial/statistical properties of the architecture rather than learned from data?

## Suggestions

1. Add experiments comparing DNAs to MoE and MoD baselines with matched active *and* total parameters. This is essential to support the framing claim.
2. Add at least two ablations: (a) backbone vs. no backbone, (b) learned skipping (bias trick) vs. fixed random skipping schedule.
3. Provide a controlled comparison where total parameters are matched (e.g., a DNA with total params equal to the dense baseline, accepting more active params).
4. Add a quantitative measure for path specialization (e.g., compute the agreement between path-assignment and human-annotated semantic categories for patches).
5. Strengthen the language experiments by training at larger scale or with load-balancing losses, and discuss why the vision case shows more structure.

## Score and Decision

### Calibration anchors

**High-scoring:**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jxpsAj7ltE.md` (avg 7.50) — *From Sparse to Soft Mixtures of Experts*: Comprehensive experiments, strong baselines, clear outperformance on vision tasks. The DNA paper has much weaker experimental validation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/MY0qlcFcUg.md` (avg 7.33) — *Denoising Task Routing for Diffusion Models*: Clean experiments, clear improvements, well-executed. The DNA paper is far weaker in experimental methodology.

**Medium-scoring:**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/z1mLNhWFyY.md` (avg 5.25) — *Gradient Routing*: Novel training method with diverse experiments; some methodological concerns. Comparable in novelty and scale, though the DNA paper is weaker on baselines.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uWvKBCYh4S.md` (avg 5.00) — *Mixture of LoRA Experts*: Has extensive ablations and cross-domain experiments. The DNA paper is weaker on experimental rigor.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ar9tcnD4e9.md` (avg 4.75) — *Automatic Organization of Neural Modules*: Similar in spirit (neural modules with emergent connectivity), with weak experiments on simple datasets. The DNA paper has stronger experiments (ImageNet, language) but similar absence of key baselines.

**Low-scoring:**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/XVHXVdoV11.md` (avg 3.40) — *Collective Model Intelligence*: Ill-defined concepts, weak experiments. The DNA paper is significantly stronger in both execution and result quality.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/gInIbukM0R.md` (avg 2.50) — *Quantifying Emergence in Neural Networks*: Poorly motivated, weak evidence. The DNA paper is substantially more coherent.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/11oqo92x2Z.md` (avg 2.50) — *Solar Farm Detection*: Narrow applied contribution. Not comparable.

### Assessment

The paper's core weakness is the gap between its framing (DNAs as a generalization of MoE/MoD/weight-sharing/early-exit) and its evaluation (only dense baselines). For a feasibility study, this might be acceptable, but the paper pushes beyond feasibility claims into "mixture-of-*all*-of-these-methods emerges" and "competitive performance" without validating against those specific methods. Combined with the absence of ablations and the mixed language results, the contribution is not yet at the bar for acceptance at a top venue. The conceptual idea is genuinely novel and the qualitative analysis is interesting, but the experimental validation needs substantial strengthening.

**Score: 4.5**

**Decision: Reject**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>