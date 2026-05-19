Now I have all the evidence I need. Let me compile the final review.

## Summary

This paper introduces "Gray-box" fine-tuning, a setting where a foundation model's weights and architecture remain hidden and only gradient information is exposed at entry points. The authors propose two variants: DGA (DarkGray-box Input/Output Adapters), which learns lightweight adapters at the model's input and output via backpropagation through the hidden backbone, and LGA (LightGray-box), which additionally permits learnable tokens at intermediate layers. Evaluated on text-image retrieval, text-video retrieval, image classification, and sketch-image retrieval using CLIP, BLIP, and DINOv2 backbones, DGA achieves results competitive with LoRA on several benchmarks (e.g., within 0.38 R@1 on COCO) and surprisingly outperforms white-box methods on some domain-specific tasks (Stanford-Cars), despite having no access to model weights.

## Strengths

- **Competitive performance under severe access restrictions**: On COCO Text-to-Image Retrieval, DGA achieves R@1 of 88.42 vs. LoRA's 88.80 (gap 0.38); on MSR-VTT Text-to-Video Retrieval, DGA scores 47.0 vs. LoRA's 47.5 (gap 0.5). These results convincingly demonstrate that meaningful adaptation is possible with only gradient access, which is the paper's central empirical claim.

- **Outperforms white-box methods on a domain-specific task**: On Stanford-Cars retrieval (Table 4), both DGA (P@1: 63.0) and LGA (P@1: 66.4) substantially surpass Full Fine-Tuning (35.9) and LoRA (39.9). The paper offers a plausible explanation (few samples, input-space flexibility advantage) and correctly notes this is not universal. This is an informative finding that goes beyond a "competitive" baseline comparison.

- **Simple and well-justified textual adapter**: The textual input adapter uses only two learned tokens (a shift token and an extra token), compared to 10–200 tokens with an additional MLP in Prefix-Tuning. This simplification preserves context length (relevant for CLIP's 77-token limit) and is a concrete design advantage attributable to the authors' approach.

- **Ablation cleanly isolates adapter contributions**: Table 8 systematically decomposes performance: input adapters alone yield +5.72 R@1, adding output adapters gives another +5.74, and the full configuration (both modalities, both I/O adapters) is best. This provides clear evidence that each design choice is individually beneficial.

- **Broad evaluation spanning multiple tasks and backbones**: The paper benchmarks on text-image retrieval (COCO, Flickr30K), text-video retrieval (MSR-VTT, VATEX), image classification (ImageNet-1k, ImageNet-Sketch), sketch-image retrieval (Sketchy), and domain-specific retrieval (Stanford-Cars), using CLIP, BLIP, and DINOv2 backbones. This breadth supports the generality of the findings.

## Weaknesses

### Fatal

None.

### Major

- **The privacy/IP motivation is weakened by unaddressed gradient leakage concerns**: The paper motivates gray-box fine-tuning partly through privacy, IP protection, and safety (Section 1), using hospital/medical-image examples. However, the method requires exposing gradients computed through the backbone model. While the paper cites model-theft literature (Milli et al. 2019 on gradient-based weight reconstruction, Horwitz et al. 2024 on LoRA weight recovery, Haim et al. 2022 on training data recovery from weights) and cautiously states that recovering architecture and weights from gradients is "not yet practical or feasible" for *arbitrary* models (Section 2), it does not engage with the well-established body of work on *training data leakage from gradients* (Zhu et al., 2019; Zhao et al., 2020; Geiping et al., 2020). For the motivating hospital scenario where patient data is involved, the possibility that gradients could leak training data is directly relevant and unaddressed. This does not invalidate the paper's core contribution (an empirical study of what is achievable under gradient-only access), but it means the privacy framing is significantly overstated as presented. The paper would benefit from either explicitly acknowledging this limitation or discussing mitigations (e.g., gradient perturbation, limited gradient steps).

### Minor

- **"Upper bound" framing contradicted by own results**: The paper states that LoRA and Full FT serve as "performance upper bounds" (Section 1, Section 4) because they can modify model parameters. Yet on Stanford-Cars (Table 4), DGA (P@1: 63.0) and LGA (P@1: 66.4) substantially outperform both LoRA (39.9) and Full FT (35.9). The paper discusses this anomaly in the text but continues to use the "upper bound" framing elsewhere. This should be corrected to "strong white-box baselines" to avoid the contradiction.

- **Missing error bars and statistical significance**: None of the reported results include confidence intervals, standard deviations, or statistical significance tests. Given that several comparisons show small gaps (e.g., <1 point R@1), it is impossible to assess whether these differences are meaningful. This is a basic methodological expectation for empirical papers.

- **No experimental details reported**: Learning rates, batch sizes, number of epochs, optimizer choice, regularization, training time, and hardware are absent. This undermines reproducibility. While not every detail needs to appear in the main paper, the complete absence of any training configuration information is a significant omission.

- **Third motivator (edge device optimization) is listed but never revisited**: The Introduction lists "optimization for edge devices" as one of three challenges the paper addresses, but the method and evaluation never discuss or evaluate this aspect. The paper should either connect the method to this challenge or remove it from the stated motivations.

- **Performance claims in the abstract are slightly too uniform**: The abstract states that DGA "achieve[s] competitive performance with full-access fine-tuning methods" without qualification. The results show this is true for text-image and text-video retrieval but substantially less true for sketch-domain tasks (Table 7: DGA far behind all white-box methods; Table 6 ImageNet-Sketch: 8.98-point gap to LoRA). The paper acknowledges these gaps in the body text but the abstract and contribution list do not reflect the nuanced picture.

### Trivial

None.

## Nice-to-Haves

- An analysis of *when* gray-box works vs. when it doesn't along a domain-similarity axis would strengthen the paper beyond the current "distant domains are harder" observation.
- A comparison of computational cost (FLOPs per training step, parameter count, training time) between DGA and LoRA/Full FT would ground the practical efficiency claims.
- An ablation on the number of visual adapter convolutional layers and whether identity initialization matters would add depth.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Practical feasibility is not discussed (Structural)"** — The harsh critic asks "who runs the training loop" and "how are gradients communicated." This is a research paper formalizing a new setting, not a production deployment specification. Many fine-tuning papers (including LoRA, Prefix-Tuning) do not detail the deployment architecture. Removed because this standard is not applied uniformly across papers and the setting is described clearly enough for the research contribution.

2. **"Methodological novelty is modest"** — While the critic's observation that DGA combines existing techniques is technically true, the paper's contribution is the formalization of the gray-box setting and the empirical characterization under strong access restrictions. Novelty of the adaptive mechanism is not the claim; the setting itself is the novelty. Removed as a generic criticism that does not harm the paper's core contribution.

3. **"LGA layer dimensionality exposure contradicts hidden layers claim"** — The paper explicitly states what information is revealed at entry points (dimensionality, gradients). The paper does not claim these are hidden; it describes exactly what is exposed. Removed as factually inaccurate — the paper is transparent about what LGA reveals.

4. **Strength Finder strengths about "addressing an important problem" and "targeting an interesting question"** — Removed as generic/superficial. Only concrete, evidence-grounded strengths were retained.

## Novel Insights

The most interesting observation emerging from combining the reviews and the paper is the non-monotonic relationship between model access and performance: DGA (no weight access) actually outperforms LoRA and Full FT (full weight access) on Stanford-Cars, a domain-specific retrieval task with few samples. This suggests that for data-scarce, domain-specific settings, restricting adaptation to the input space may act as a beneficial regularizer, preventing overfitting that weight-space methods are prone to. This phenomenon — where *less* access yields *better* results — is a counterintuitive finding that merits deeper investigation beyond the speculative explanation the paper currently provides. The review process surfaces this as the paper's most provocative result, one that could motivate future work on the relationship between model-access level and generalization under low-data regimes.

## Suggestions

1. Add a Limitations paragraph discussing gradient-based data leakage (cite Zhu et al., Geiping et al.) and clarify that the paper's privacy claims are about *model* privacy (hiding architecture/weights), not training data privacy.
2. Remove the "upper bound" language for LoRA and Full FT; replace with "strong white-box baselines."
3. Add confidence intervals or standard deviations to all tables.
4. Report training hyperparameters (optimizer, learning rate, batch size, epochs, scheduler) for reproducibility.
5. Add a sentence in the abstract acknowledging that gray-box methods underperform on distant-domain tasks.
6. Either connect the edge-device optimization challenge to the method or remove it from the list of addressed challenges.

## Score and Decision

**Score: 6.5**

**Decision: Accept**

The paper makes a genuine contribution by formalizing and systematically evaluating a useful new setting (gray-box fine-tuning with only gradient access). The empirical results are broad, the ablation study is clear, and several findings (competitive performance on in-distribution tasks, superior performance on low-data domain-specific tasks, predictable degradation on distant domains) are informative and well-supported. The main weaknesses — the unaddressed gradient data-leakage literature, the absence of error bars, missing hyperparameters, and slightly overstated claims in the abstract — are fixable in revision and do not undermine the core empirical contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>