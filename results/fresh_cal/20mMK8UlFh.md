Now I have all the information needed to verify every claim. Here is my consolidated review.

## Summary

This paper proposes OSA (One-step Anti-Noise), a method that uses a pre-trained multimodal model (CLIP/ALIGN) as a fixed estimator to compute cosine similarities between input pairs, then applies a scoring function to convert those similarities into training weights that down-weight likely-noisy samples. The method requires only one extra forward pass per sample (no backward pass), making it substantially cheaper than prior noise-mitigation approaches (~21 min added vs. ~226 min for NPC). Empirical results on MS-COCO, Flickr30K, CC120K, WebFG-496, and CARS98N show consistent improvements over baselines and competitive or superior performance compared to SOTA noise-mitigation methods, with particularly large gains at high noise ratios (e.g., +20.9 i2t R@1 on Flickr30K at 60% noise).

## Strengths

1. **Practical efficiency with strong empirical results.** OSA adds only ~21 minutes over a 97-minute CLIP training run (vs. 226 extra minutes for NPC). Despite this low overhead, it consistently outperforms baselines and SOTA methods across multiple tasks, noise levels, models, and architectures — including on a real-world noisy dataset (CC120K) and on noise-vulnerable backbones (ResNet-152, VGG-19 where baselines collapse at 50% noise but OSA maintains 30–55 R@1).

2. **Model-agnostic design with broad transferability.** The estimator is decoupled from the target model, allowing OSA to be applied to any architecture (ViT, ResNet, VGG) and any task (image-text retrieval, classification, image retrieval) without modification. It even further improves the SOTA method NPC when stacked on top (Table 6), demonstrating genuine complementarity.

3. **Near-perfect noise detection and re-weighting.** Noise detection recall reaches 97–99% (Table 8), and the Mean Noise Rank is within 0.3–1% of the theoretical optimum (Table 7), showing that the scoring function reliably places noisy samples near the bottom of the weight ordering.

4. **Empirical grounding of the boundary hypothesis.** Figure 1 provides clear visual evidence that clean and noisy cosine-similarity distributions from CLIP and ALIGN have a consistent intersection point with minimal overlap across two datasets, motivating the core idea. The paper further shows (Table 1) that the mean cosine similarity of random pairs coincides with this intersection, supporting the shifted-orthogonal-boundary interpretation.

## Weaknesses

### Major

1. **Theoretical framework has a significant proof-to-practice gap.** Theorem 1 proves that relative cosine-similarity ordering is preserved when vectors pass through a *randomly initialized* neural network (Gaussian weights/biases with specific variance scaling). The paper then applies this conclusion to *trained* CLIP/ALIGN encoders. Training fundamentally changes the embedding geometry — it is the entire point of contrastive learning to pull positives together and push negatives apart. There is no argument or experiment showing that the random-network preservation property transfers to trained models. The paper's qualitative analysis in Sec. 2.3 partially acknowledges the difficulty but does not bridge the gap. This weakens the claimed theoretical grounding substantially; however, the empirical results stand independently.

2. **Scoring function design is conceptually inconsistent with stated requirements.** The paper states that for samples with positive cosine similarity, "the function gradient should increase rapidly as the cosine similarity moves further from zero" (line 135). Yet the actual function w(t) = t²(1-t) (where t = s-β) peaks at t = 2/3 and then *decreases* back toward zero at t = 1 (line 184). For very clean pairs with near-perfect similarity, the assigned weight paradoxically drops. In practice, the decrease is small (peak ≈ 0.148 at t=2/3 vs. ≈ 0.143 at t=0.735) and t rarely exceeds 0.8, so the practical impact is likely negligible — but the mismatch between the stated design principle and the actual formula is a genuine conceptual flaw that should be either fixed (use a monotonic function) or justified (explain why the non-monotonicity is intentional and beneficial).

### Minor

3. **Improvements on 0%-noise (clean) data are unexplained.** Across multiple tables (e.g., COCO 1K at 0%: CLIP 80.1 → CLIP+OSA 82.2; ALIGN 84.9 → 85.3; Flickr30K at 0%: CLIP 86.2 → 88.6), OSA improves performance even when no artificial noise is added. If the method is designed to suppress noisy samples, applying it to clean data should at best preserve performance and likely degrade it (since some clean samples receive weights < 1). The paper does not discuss this phenomenon. Possible explanations (the "clean" split contains inherent noise, the estimator provides a beneficial curriculum/regularization effect, etc.) should be explored rather than left as a puzzle.

4. **Overstatement about domain adaptation being "unnecessary."** The paper asserts domain adaptation is unnecessary (line 167), but Table 4 shows that at 50% noise, CLIP (w/ DA) outperforms CLIP (w/o DA) on most metrics (e.g., 80.4 vs. 79.6 on COCO 1K i2t R@1). The difference is small and the zero-shot estimator is indeed competitive, but calling DA "unnecessary" while presenting evidence that it sometimes helps is an overstatement. A more precise claim would be that zero-shot CLIP performs comparably, with optional DA providing marginal gains at high noise.

5. **No statistical significance or variance reporting.** All results are reported as single-run point estimates. Given that improvements are sometimes small (especially at 0% noise) and the experimental setup involves randomness from multiple sources, providing at least a few runs with standard deviations or significance tests would strengthen the evidence. This is not uncommon in the field for large-scale benchmarks, but it is worth noting.

6. **Limited details on baseline setup for classification/retrieval tasks.** In Table 4 (image classification and retrieval), the "Baseline" method is described only as "contrastive learning" with no architecture, optimizer, hyperparameters, or training details specified. Combined with the lack of comparison to existing noise-mitigation methods on these tasks, it is difficult to assess how strong the baseline is.

### Trivial

- None.

## Nice-to-Haves

- A quantitative noise-detection evaluation (accuracy/recall) on the SDM unfamiliar-domain dataset would strengthen the claim that the boundary is robust across domains. Currently only distribution plots are shown.
- An ablation of the scoring function form (e.g., compare the proposed cubic to a simple threshold, linear ramp, or sigmoid) would validate the design beyond the estimator-type ablation already provided.
- An ablation with β set to zero (no spatial debiasing) would directly test whether the cone-effect correction matters.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Optimal rank numerical error (Harsh Critic).** The critic claimed the optimal Mean Noise Ranks (1815.5 and 1524.0) were miscalculated. Verification: for 2000 samples with 370 noisy samples ranked last, mean rank = (1631 + 2000)/2 = 1815.5 ✓; for 953 noisy samples, mean rank = (1048 + 2000)/2 = 1524.0 ✓. The paper's values are correct; the critic's alternative formula was wrong. **Removed as factually incorrect.**

- **Ambiguity about β computation (Harsh Critic).** The critic questioned whether "random sample pairs" (used to compute β) come from the training set and might include noisy pairs, "confounding the debiasing." The paper's method is clear: random pairs are constructed from randomly sampled images and texts — they approximate random vectors regardless of whether individual samples are mislabeled, because the pairing is random, not semantic. The mean of such pairs converges to the cone center. This is not a confound. **Removed based on misreading of the method.**

- **Missing appendix/references/formatting nitpicks.** Any criticism about missing appendix content, references, typos, or formatting artifacts is a parser issue, not a paper problem. **Removed as parser artifacts per review policy.**

- **Generalized speculation not anchored to the paper.** Several reviewer observations (e.g., "could the metric be measuring a proxy?", "if the normalization were X, the reported values would be impossible") are speculative and not tied to specific, verifiable flaws in the paper as written. **Removed per filtering discipline.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Either fix the theoretical framing or remove the invalid claim.** Theorem 1 as stated does not extend to trained models. Either (a) replace the theorem with an empirical characterization showing that the boundary is stable across many pre-trained models, datasets, and noise types — which would be more honest and still useful — or (b) add a bridging argument or experiment showing that the random-network preservation property continues to hold after contrastive training (e.g., by measuring the rank correlation of cosine similarities before and after random projections of the actual CLIP embeddings).

2. **Fix the scoring function or justify the non-monotonicity.** The simplest fix: use a monotonic function such as w = max(0, t)² (a rectified quadratic) or w = 1/(1 + e^{-k(t - τ)}) (a sigmoid) that aligns with the stated "gradient increases as similarity moves from zero" requirement. If the cubic form is intentionally non-monotonic, explain why — e.g., very high similarity may indicate memorization rather than clean semantics.

3. **Discuss the 0% noise improvements.** Run the control experiment: compare OSA-weighted training vs. training with all weights = 1 (identical to baseline) under the same pipeline. If OSA still helps, discuss the mechanism (regularization, pre-trained estimator knowledge transfer). If not, report that and adjust the claims accordingly.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>