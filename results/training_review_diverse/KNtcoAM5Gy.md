Now I have all the information I need. Let me write the consolidated review.

## Summary

BaFTA proposes a backpropagation-free test-time adaptation method for vision-language models (CLIP). Instead of gradient-based prompt tuning (as in TPT), it directly estimates class centroids via online clustering in a projected embedding space, and combines text-based and clustering-based predictions using Rényi entropy weighting. Experiments across 15 benchmarks show consistent improvements over CLIP baselines and competitive/stronger results than TPT and other test-time adaptation methods, with approximately 5× speedup.

## Strengths

- **Backpropagation-free design eliminates learning-rate tuning and collapse risk.** BaFTA updates class centroids via simple online averaging (Eq. 2–5) rather than gradient descent on prompts, avoiding the instability TPT guards against by restarting per example. This design also achieves a genuine ~5× wall-clock speedup over TPT (158.7 ms vs 873 ms per image on ViT‑B/16, Section 4.2 ablation).

- **Rényi entropy aggregation demonstrably improves over alternatives.** The ablation in Table 5 shows BaFTA (TE & OC with Rényi entropy) achieves 68.11% average accuracy across 15 datasets, outperforming BaFTA‑Avg (simple average) by 1.87%. Table 6 further shows Rényi entropy of order 0.5 (71.00%) surpasses simple averaging (69.43%), max‑probability weighting (70.60%), and TPT’s top‑10% rule (70.34%) on ImageNet.

- **Consistent gains across a broad benchmark suite and two backbones.** On ImageNet with ViT‑B/16, BaFTA reaches 72.15% vs TPT’s 68.98% and CLIP multi’s 68.34% (Table 1). On five OOD variants, BaFTA averages 65.46% vs TPT’s 60.81%. On ten fine-grained datasets, BaFTA averages 68.77% vs TPT’s 65.10% (Table 2). The pattern holds with RN50, though margins are smaller.

- **Component-level ablation study is informative.** Table 5 cleanly decomposes contributions from multi-template prompts, text-embedding predictions, online-clustering predictions, and Rényi entropy aggregation, allowing readers to see the marginal benefit of each piece.

- **Multi-template prompt usage without additional cost.** Unlike prompt-tuning methods constrained to a single template for computational reasons, BaFTA leverages all CLIP-provided templates, yielding a +1.37% gain over the single-template version (68.11% vs 66.70%, Table 5).

## Weaknesses

### Fatal
None.

### Major

- **Hyperparameter β is unspecified.** The balancing factor β in Eq. (7) controls the relative weight between text-embedding predictions and online-clustering predictions. The paper never states what value of β is used, whether it is fixed across all datasets, or how it was chosen. Given that the optimal balance plausibly varies across datasets (some have well-clustered visual embeddings, others have many classes with few examples), this is a significant reproducibility gap. If β was tuned per dataset on a validation split, that would need to be disclosed; if it is fixed, its value and justification must be reported. *Note: α for the Rényi entropy is specified as 0.50 in Table 6.*

- **The main comparison to TPT conflates the cumulative protocol with the method itself.** This is the most substantive concern. TPT adapts per-example and discards the prompt for the next example (restart strategy). BaFTA accumulates information across all test examples via online centroids that are never reset. The paper acknowledges this distinction qualitatively (Section 3, lines 92–98), and the ablation provides a partially controlled comparison (BaFTA_single vs TPT-Agg, 65.95 vs 64.34). However, the main results (Tables 1–2) compare BaFTA in its cumulative setting directly against TPT in its per-example setting without quantifying how much of the gap comes from the protocol versus the algorithm itself. The 3.17% ImageNet gain conflates both factors. The paper should clearly separate the two settings and evaluate BaFTA in the same per-example protocol (resetting centroids per image) to isolate the method-level contribution.

### Minor

- **No error bars or statistical significance reported anywhere.** BaFTA involves randomness from augmentations and test-set ordering (online clustering is order-dependent). Yet no standard deviations, confidence intervals, or multi-seed experiments are reported for any table. This is a significant omission, especially given that several ablations show small differences (e.g., 70.85 vs 71.00 in Table 6) where significance is unclear.

- **The large gain on ImageNet‑A is unexplained.** BaFTA achieves a remarkable +13.47 absolute improvement over CLIP multi on ImageNet‑A (49.89 → 63.36, ViT‑B/16) — nearly triple the average OOD gain. ImageNet‑A is adversarially selected to be hard for standard classifiers. The paper provides no analysis of why online clustering helps so disproportionately on this subset. A diagnostic experiment (e.g., does the gain concentrate in certain classes? Is it an ordering artifact?) would substantially strengthen credibility.

- **Underperformance on some datasets is not discussed.** With RN50, BaFTA underperforms TPT on Cars (57.52 vs 58.46) and SwapPrompt on SUN397 (63.30 vs 63.93). The paper does not discuss these failures, leaving readers to wonder about the method's failure modes.

- **No limitations section.** The paper lacks any discussion of when BaFTA might struggle — small test sets, highly imbalanced class distributions, rapid distribution shifts, or few-class tasks where the projection (removing the first principal component from a small matrix) may be ill-conditioned. Adding a limitations paragraph would improve scientific honesty.

- **No analysis of test-set ordering effects.** Online clustering is inherently order-dependent; erroneous early assignments can propagate. The paper does not analyze how sensitive results are to test-set shuffling or whether multiple orderings produce stable results.

- **Space projection may be ill-conditioned for few-class tasks.** The projection P^* removes the first principal component of the text embedding matrix, which is reasonable only when the number of classes J is sufficiently large for a meaningful PCA. For tasks with very few classes (e.g., 2–5), this operation may be unstable or degenerate. This limitation should be noted.

### Trivial

- **The temporal order of prediction vs centroid update could be stated more explicitly.** The natural reading (predictions use centroids as they were before the current example; update happens afterward) is clear from context, but stating this in a numbered algorithm list would remove any ambiguity.

- **The aggregation equation (7) notation is unnecessarily dense.** The R₁, R₂ notation with nested normalization could be simplified to a direct weighted-average expression for readability.

## Nice-to-Haves

- A per-image ablation where centroids are reset for each test example, exactly matching TPT's protocol, to isolate the method's intrinsic contribution.
- A sensitivity sweep for β on 1–2 representative datasets to show how performance varies with this parameter.
- An analysis of how BaFTA's performance changes as a function of test-set size (does it continue improving with more examples, or plateau?).

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **"Circular dependency in online clustering is underspecified"** (Harsh Critic #3): The paper's description implies the standard temporal order — predictions are made using current centroids, then centroids are updated. The critic acknowledges this ("The natural reading is that centroids are used as they were after processing all prior examples"). The concern is overblown; the ordering is clear from context and is standard online clustering. Downgraded to Trivial.
- **"Inference-time superiority claim needs more detailed profiling"** (Harsh Critic #4): The paper explains the timing difference (two forward + one backward pass for TPT vs one forward pass for BaFTA, text encoder run offline for BaFTA). The 5× claim is plausible and adequately supported. The critic's demand for a per-operation breakdown is excessive for a conference paper and does not threaten the core claim. Downgraded to Trivial.
- **"Rényi entropy justification relies on speech recognition paper"**: The paper also provides empirical evidence (Table 6) showing Rényi entropy outperforms alternatives. This is sufficient empirical validation.
- **"BaFTA_single vs TPT-Agg comparison is confounded"**: The ablation naturally compares a full pipeline variant against another full pipeline variant. The individual component contributions are separately shown in the same table (BaFTA-TE, BaFTA-OC). This is not a weakness; it is standard ablation practice.
- **"Rényi entropy improvements are marginal"**: The gap between Rényi entropy (71.00) and the next-best method (max-probability weighting, 70.60) is 0.4%, which is meaningful in the ImageNet setting. This criticism is unsupported without error bars — which is itself a separate weakness listed above.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the review synthesis is that the combination of text-embedding predictions (which work well for most examples) and online-clustering predictions (which excel on hard, adversarially selected examples like ImageNet‑A) is complementary in a way that neither reviewer fully unpacked. The 13.47-point gain on ImageNet‑A strongly suggests that clustering centroids (which aggregate visual evidence from many examples) are more robust to distribution shift than static text embeddings — a claim that deserves deeper analysis than the paper currently provides. Conversely, the text-embedding predictions serve as a stabilizing prior for classes with few seen examples, where cluster centroids are unreliable. This complementary dynamic is the paper's most interesting finding and deserves explicit treatment.

## Suggestions

1. **Report β** — state its value, whether it is fixed, and if tuned, how.
2. **Add a per-image (reset centroids) ablation** to disentangle the method advantage from the cumulative-protocol advantage.
3. **Report standard deviations** for all main results, repeating with different test-set orderings and random seeds.
4. **Analyze the ImageNet‑A result** — e.g., per-class breakdown, comparison of centroid quality vs text-embedding quality on hard examples.
5. **Add a limitations paragraph** covering small test sets, class imbalance, few-class tasks, and ordering sensitivity.
6. **Discuss the few datasets where BaFTA underperforms baselines** (Cars, SUN397 with RN50).

## Score and Decision

This paper presents a genuinely novel approach to VLM test-time adaptation that avoids backpropagation altogether — a clever and practically motivated idea. The empirical evaluation is broad (15 datasets, two backbones) and the ablation study is well-structured. The primary concerns are (a) the unspecified β hyperparameter, which hurts reproducibility, and (b) the conflation of protocol-level and method-level advantages in the main comparisons. Neither issue invalidates the core contribution, but both weaken the claims as currently stated. With the suggested fixes (especially reporting β and adding a per-image ablation), the paper would be a solid contribution. As-is, it is borderline but acceptable with major revisions.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>