## Summary

This paper demonstrates that aggregate auto-interpretability metrics (fuzzing/detection AUROC) for sparse autoencoders (SAEs) do not reliably distinguish between SAEs trained on real vs. randomly initialized transformers. Across five Pythia model sizes (70M–6.9B) and four randomization strategies, the authors find that randomized models often achieve AUROC scores comparable to trained models, while a Gaussian-noise control remains at chance. The key insight is that randomized models produce simpler, single-token features that are easy to explain, and the paper uses token-distribution entropy to reveal this difference in feature abstractness that aggregate scores miss.

## Strengths

- **Comprehensive empirical sweep across model scales and randomization schemes**: The paper evaluates SAEs on five Pythia model sizes (70M–6.9B) with four distinct randomization strategies (re-randomized incl./excl. embeddings, step-0, and a Gaussian-noise control). The consistency of results across scales and the clear separation from the control baseline provide robust evidence for the central claim (Figures 1, 2; Appendices B, C).

- **Token-distribution entropy analysis provides genuine insight**: The entropy metric cleanly separates trained and randomized models: trained models show increasing entropy (more abstract features) with layer depth, while randomized models remain at low entropy (token-specific features). This directly demonstrates *what* aggregate AUROC misses, going beyond mere phenomenology (Figure 2, last row; Appendix H, Figure 20).

- **Well-constructed Gaussian-noise control validates metric sensitivity**: Replacing token embeddings with i.i.d. Gaussian noise at inference time yields near-chance AUROC (~0.5), proving the auto-interpretability pipeline can detect the absence of structure. This rules out the concern that the metrics are simply insensitive to everything (Figures 1, 2).

- **Robustness to training scale and SAE hyperparameters**: Results hold when SAEs are trained on 1B tokens instead of 100M (Appendix C) and across varying expansion factors (16–128) and sparsity levels (16, 32) (Appendices F, G), ruling out under-training or hyperparameter artifacts.

- **Calibrated, honest claims**: The paper carefully avoids overstatement. It explicitly notes that results "do not imply that SAEs trained on real models fail to learn meaningful computational features" (Section 6) and acknowledges limitations transparently (Section 5). The recommended practice of routine randomized baselines is actionable and sensible.

## Weaknesses

### Fatal
None.

### Major
- **The core finding, while correct and well-documented, is partially self-explanatory given the paper's own analysis**: The paper shows that randomized features have lower token-distribution entropy (are simpler) and that simpler features are easier to explain (Appendix H). It is therefore not surprising that aggregate AUROC fails to separate trained from random — the metric is measuring something close to "explainability of activation patterns," and random models' simpler patterns are indeed explainable. The paper's contribution is effectively demonstrating *that* the metric fails and *why*, which is useful but not deeply surprising. The framing as a "sanity check" is appropriate but the result is more of a cautionary confirmation than a revelation.

### Minor

- **Uncertainty quantification limited to the smallest model**: Only Pythia-70m has multi-seed error bars (Appendix E, 5 seeds). For larger models (Pythia-1b, 6.9b) we have single-point estimates with 100 latents sampled per SAE. While the consistency across model sizes and randomization schemes suggests the trends are robust, reporting uncertainty for at least one larger model would strengthen confidence.

- **Toy model section (Section 4) is loosely connected to the main empirical findings**: The paper acknowledges this explicitly — "we leave the question of which predominates in the case of randomized transformers … to future work" (Section 4). The toy models demonstrate plausibility of two mechanisms (preservation and amplification of superposition) but do not directly test which mechanism explains the transformer results. This section reads as a sensible but incomplete hypothesis exploration. The main empirical contribution does not depend on it.

- **No concrete alternative metric proposed**: The paper identifies what aggregate AUROC misses and recommends "targeted measures of feature abstractness," but stops short of proposing or validating a specific alternative. The entropy metric is presented as a proof-of-concept diagnostic but not developed into a calibrated evaluation tool. This limits the paper's constructive contribution relative to its critical one.

### Trivial

- The per-latent entropy–AUROC scatter plots (Appendix H, Figure 20) contain some of the paper's most informative analysis showing how trained models uniquely produce high-entropy, high-AUROC latents. Elevating this visualization or its key insight to the main text would strengthen the narrative.

## Nice-to-Haves

- Testing whether the findings hold with an alternative explanation-generation LLM (beyond Llama-3.1-70B) would probe the robustness of the explanation pipeline itself, though the paper acknowledges this limitation.
- Extending the entropy analysis into a formal metric (e.g., entropy-weighted AUROC) would move the paper from critique to constructive proposal, though this is beyond the stated scope.

## Removed Points

**These points are flagged to be removed, treat them with caution.**

1. **"The paper's central framing misconstrues what auto-interpretability metrics are designed to do" (Harsh Critic, Point 1)**: This criticism is factually wrong. The paper explicitly frames its contribution as a sanity check (following Adebayo et al., 2020) — applying a test that the metric was not originally designed for, to see if it nonetheless passes. This is standard and valid methodology. The paper does not claim the metric was designed for this purpose; it claims the metric is *used* as evidence of meaningful feature discovery, and the sanity check reveals this evidence is insufficient. The section explicitly states the paper's scope: "High aggregate auto-interpretability scores do not, by themselves, guarantee that learned, computationally relevant features have been recovered" — which is precisely what the experiments support.

2. **"The AUROC comparison is critically confounded by feature complexity" (Harsh Critic, Point 2)**: This criticism misunderstands the paper's argument. The paper's main point is *exactly* that aggregate AUROC fails to account for feature complexity/abstractness differences. The entropy analysis (Section 3, Appendix H) is not an overlooked confound — it is the paper's central explanatory mechanism. The paper explicitly states: "this suggests that standard SAE quality and auto-interpretability metrics are missing an important aspect of SAE features: their 'abstractness'" (Section 3). The claim that "without controlling for feature difficulty, the AUROC comparison is uninterpretable" inverts the paper's logic: the paper argues that the comparison *reveals* the need for such control.

3. **"The analogy to saliency map sanity checks is inappropriate" (Harsh Critic, Section-by-Section)**: The Adebayo et al. (2020) analogy is directly appropriate. Both cases involve: (a) an interpretability method that produces apparently meaningful outputs, (b) a sanity check comparing outputs on trained vs. randomized models, and (c) a finding that the outputs are similar, casting doubt on whether the method captures learned computation. The fact that "random projections preserve geometry" does not invalidate the analogy — it is part of *why* the result is interesting and worth documenting.

4. **"Figure 1/2 interpretation: randomized variants outperform trained — the paper does not discuss why this does not constitute distinguishing" (Harsh Critic)**: The paper does discuss this. Section 3 explains that randomized models produce simpler (lower-entropy) features, which are easier to explain. The fact that randomized models sometimes score higher is consistent with the paper's explanation and is not contradictory to the claim.

5. **"CE loss score is fine but does not add evidence" (Harsh Critic)**: Not a weakness — the paper itself notes CE loss only makes sense for trained models (line 332-335) and includes it for completeness.

6. **Strength Finder claim about "plausible mechanistic toy-model analysis" deepening the contribution "beyond pure phenomenology"**: While the toy models are interesting, the paper itself is cautious about their connection to the main results. This strength is overstated — the toy models demonstrate plausibility but do not provide mechanistic confirmation.

## Novel Insights

The paper's most novel insight is the use of token-distribution entropy to decompose what aggregate AUROC obscures: trained transformers produce a *mixture* of simple token-specific features and complex abstract features, while random transformers produce almost exclusively simple features. The entropy–AUROC scatter plots (Appendix H, Figure 20) reveal that trained models uniquely exhibit latents with *both* high entropy and high AUROC — features that are spread across many tokens yet whose activation patterns are consistently explained. This suggests that the "interesting" features we care about are precisely those in the upper-right quadrant of the entropy–AUROC space, providing a concrete target for future metric development.

## Suggestions

- Move the key insight from Appendix H Figure 20 into the main text: trained models uniquely produce high-entropy, high-AUROC latents, while randomized models' high AUROC is confined to low-entropy features. This single observation crystallizes the paper's message.
- Report multi-seed uncertainty for at least one larger model (e.g., Pythia-1b) to demonstrate that the trends are not an artifact of the 100-latent sample.
- Consider binned AUROC-by-entropy analysis as a bridge toward a difficulty-aware composite metric, even if only as a sketch for future work.

## Score and Decision

**Anchor comparison:**

| Path | Avg Score | How it compares |
|------|-----------|-----------------|
| `mqNKv0brqk` (CE-Bench) | 1.00 | Far weaker — fundamental execution quality issues, no proper baselines, withdrawn. Our paper is substantially stronger. |
| `119qowYLUX` (SAE Feature Sensitivity) | 3.50 | Similar domain (SAE evaluation critique). That paper had more limited scope and a mixed reception. Our paper has broader experimental coverage and a clearer explanatory mechanism (entropy). Our paper is stronger. |
| `Q4ooLNOFeR` (Interpretability vs Utility) | 4.50 | Most similar in spirit — demonstrates a limitation of interpretability metrics. That paper trained 90 SAEs and proposed a concrete solution (Δ Token Confidence). Our paper has comparable breadth (5 model sizes, 4 randomization schemes) and offers an explanatory mechanism (entropy) but does not propose a solution. Comparable — accepted as poster. |
| `EjInprGpk9` (SAEs Learn Different Features) | 5.50 | Similar empirical critique of SAE assumptions. That paper's finding (seed-dependent features) was more surprising and it proposed a novel matching methodology. Our paper's finding is somewhat more expected given the entropy analysis. Our paper is slightly weaker in novelty but comparable in execution quality. |
| `9lycwRxAOI` (Interpretive Equivalence) | 6.00 | Significantly stronger — formal theoretical framework with algorithms and proofs. Our paper is purely empirical. |
| `kHhMs642rR` (Evaluating SAE without explanations) | 3.50 | Related domain but different focus. Our paper has broader experimental coverage. |
| `XPm8t1J1g7` (Random Noise vs Saliency) | 4.00 | Different domain (CV attribution). Similar sanity-check spirit but different quality. Our paper is better executed. |

The paper sits between Q4ooLNOFeR (4.50) and EjInprGpk9 (5.50). It has comparable experimental breadth to both, a useful explanatory mechanism (entropy), honest scoping, and a clear message. The core finding, while well-documented, is partially self-explanatory (simpler features from random models are easier to explain). The paper would be stronger with a concrete proposed metric, but its contribution as a cautionary empirical study with actionable recommendations is solid and warrants acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>