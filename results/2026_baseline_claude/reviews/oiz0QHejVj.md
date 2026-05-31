## Summary

CLIP-Map proposes a mapping-based compression framework for CLIP-like vision-language models. Rather than the conventional select-based approach (pruning unimportant weights and discarding them), it introduces learnable transformation matrices factorized via Kronecker products to continuously map large pretrained weights into a smaller compressed space. A Diagonal Inheritance Initialization scheme addresses optimization instability arising from the Kronecker factorization, and a two-stage mapping-then-retraining pipeline with knowledge distillation is used to recover any remaining performance gap.

## Strengths

- **Conceptually novel reframing**: The mapping-based approach to compression (vs. selection-based) is a meaningful departure from standard pruning. Applying it to CLIP compression is timely and well-motivated, and the connections to model-growth literature (LiGO, LeTs) are clearly articulated.
- **Technically sound Kronecker factorization**: Reducing the mapping parameter count from O(D₁²D₂²) to O(D₁D₂) via the Kronecker product identity is elegant and practically important. The derivation in Sec. 3.2.2 is clean and correct.
- **Well-motivated initialization**: The theoretical analysis of variance amplification under naïve initialization (Eqs. 5–8) directly motivates the Diagonal Inheritance Initialization. Table 5 strongly validates this choice — random/Kaiming/Xavier all produce near-zero performance while diagonal init reaches 28.9% IN-1K, demonstrating the initialization is load-bearing rather than incidental.
- **Strong results at extreme compression**: At 1% and 10% compression ratios, CLIP-Map_small/tiny consistently outperform TinyCLIP across both retrieval (MSCOCO, Flickr30K) and classification benchmarks, with meaningful absolute gaps (e.g., MSCOCO TR@1: 15.8 vs 12.5, Flickr TR@1: 30.3 vs 24.5 at 1%).
- **Efficiency advantage**: Table 3 shows CLIP-Map_small achieves 42.7% IN-1K zero-shot with only 0.45B seen samples vs. TinyCLIP's 0.75B at similar model size, demonstrating faster convergence.

## Weaknesses

### Fatal
None.

### Major

- **Inconsistent results at 50% compression (Table 1)**: At the 50% compression ratio, CLIP-Map_base *underperforms* TinyCLIP on several key retrieval metrics (Flickr TR@1: 81.9 vs 84.6, Flickr TR@5: 96.2 vs 96.7, MSCOCO TR@10: 86.5 vs 87.2, MSCOCO IR@1: 37.9 vs 38.9). The paper's claim of "outperforms select-based frameworks across various compression ratios" is thus partially unsupported. The improvement is primarily concentrated in the high compression regime.

- **Severe degradation on specific zero-shot classification tasks at 50% compression (Table 2)**: At ViT-39M/16 (50% compression), CLIP-Map_base is dramatically worse than TinyCLIP on VOC2007 (22.2 vs 76.0), Oxford Pets (48.5 vs 80.8), STL10 (13.0 vs 93.2!), and DTD (77.0 vs 87.3). These are not marginal gaps — a 80-point drop on STL10 and a 54-point drop on VOC indicate the compression may fundamentally distort certain feature representations. This inconsistency is unexplained and may undermine confidence in the approach's general applicability.

- **Depth compression under-analyzed**: The depth-compression operator L_depth (Eq. 2) linearly combines weight matrices from *different* layers. Combining weights across semantically different layers (e.g., early attention layers and final layers) via linear interpolation may not produce meaningful representations. There is no ablation separating width and depth compression contributions, and no analysis of what structure L_depth learns.

### Minor

- **Narrow baseline comparison**: The primary comparison is almost exclusively against TinyCLIP. While Table 3 adds MoPE-CLIP, MobileCLIP, and ViT-T/16, these use different training data, making direct comparison difficult. No comparison against UPoP, Lottery-ticket-based CLIP pruning, or other recent compression methods under controlled settings.

- **Mapping learning analysis is thin**: The paper states the mapping evolves "from diagonal toward a more uniform structure," but no analysis is provided of what structure actually emerges or why this leads to better initialization. Visualizing or analyzing the learned F_in/F_out would strengthen understanding.

- **ResNet encoder evaluation is incomplete**: The paper evaluates CLIP with ResNet encoder only through the mapping stage (no retraining), making this result of limited value for direct comparison.

### Trivial

- Eq. 9 is stated as the initialization, but the footnote about "small random values" for off-diagonal elements is unclear — the ablation in Table 5 only compares diagonal (presumably zeros off-diagonal) vs. other methods, leaving the small-random-value variant uncharacterized.

## Nice-to-Haves

- Ablation separating the contribution of width compression vs. depth compression to understand which provides most of the gain.
- Analysis of the learned mapping matrices F_in and F_out to understand what structure the optimizer discovers beyond the diagonal initialization.
- Explanation or diagnosis of the severe STL10 and VOC2007 degradation at 50% compression — is it an artifact of the distillation setup or a structural limitation of the mapping?
- Comparison at equivalent total training compute (rather than just total seen samples) to more fairly assess efficiency.

## Novel Insights

The most genuinely novel insight is the observation that mapping-based model growth techniques (designed to expand small → large) can be inverted for compression (large → small) by applying Kronecker-factorized linear maps along both input and output dimensions simultaneously. The Diagonal Inheritance Initialization as a solution to Kronecker variance explosion is a clean, theoretically grounded, and empirically validated contribution. The finding that just 5 epochs of mapping optimization provides a strong initialization — substantially better than any standard random scheme — suggests the optimization landscape of the compressed model is highly amenable to mapping-based initialization, which may have broader implications for other architecture compression problems.

## Suggestions

- Provide a separate ablation for depth vs. width compression to quantify each component's contribution.
- Investigate and explain the severe performance degradation on STL10 and VOC2007 at 50% compression in Table 2 — this anomaly requires explanation to prevent misinterpretation of the method's general effectiveness.
- Report results with additional baselines under controlled training settings (same data, same epochs) to provide a cleaner comparison.
- Analyze the structure of converged mapping matrices F_in and F_out to provide interpretability for what the approach learns.

## Score and Decision

The paper makes a genuine and well-motivated contribution to CLIP compression with a novel mapping-based paradigm, a technically sound Kronecker factorization, and a clearly validated initialization scheme. The performance at extreme compression ratios is convincingly demonstrated. However, the major concern is the inconsistency at 50% compression — especially the catastrophic failures on specific tasks in Table 2 — which undermines the claim of consistent superiority. The narrow comparison baseline and thin analysis of the depth compression component further limit the paper's completeness. On balance, this is a borderline paper with real merit and real gaps.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>