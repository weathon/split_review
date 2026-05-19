Now I have my calibration. Let me compose the final review.

## Summary

This paper introduces Toto, a causal transformer pre-trained autoregressively (next-token prediction) on over 1 trillion visual tokens from a mixture of ImageNet, Kinetics-600, Ego4D, and HowTo100M. The model uses modern architectural components (RoPE, SwiGLU, RMSNorm) and dVAE tokenization. The paper presents a large-scale empirical study evaluating models up to 1B parameters across image classification, action recognition, action forecasting, video tracking, object permanence, robotic manipulation, and scaling laws. The central claim is that, despite minimal inductive biases, this autoregressive video pre-training approach achieves competitive performance across all benchmarks.

## Strengths

1. **Large-scale empirical study of autoregressive video pre-training**: The paper pre-trains models at up to 1B parameters on over 1 trillion visual tokens drawn from a diverse mixture spanning 100,000+ hours of video (Table 2, Figure 2). This is one of the first extensive studies of scaling autoregressive visual pre-training to video.

2. **Extensive architectural ablations on a controlled setting**: The paper systematically ablates tokenizers (dVAE, VQGAN, patches — Table 3), probing methods (attention vs. average pooling, Table 5), resolution strategies (Table 4), and architectures (GPT2, Mamba vs. Toto, Table 6). These ablations are conducted on a controlled ImageNet-only pre-training setup (400 epochs), providing useful design guidance.

3. **Diverse evaluation across many task types**: The paper evaluates on 7+ distinct task categories — ImageNet classification, Kinetics-400 action recognition, Ego4D action anticipation, DAVIS tracking, CATER object permanence, simulated and real-world robot manipulation, and scaling laws. This breadth demonstrates the generality of the learned representations.

4. **Scaling law analysis**: Section 4.8 derives a power law \(L(C) = 7.42 \cdot C^{-0.0386}\) for visual autoregressive models, showing clear scaling behavior and comparing the exponent to GPT-3's. This provides a useful reference for the community even if the absolute comparison is indirect.

5. **Strong results on tracking and object permanence**: On DAVIS tracking (Table 10), Toto-large at 512 resolution achieves J&F 68.3%, outperforming DINO (66.9%) and MAE (63.7%) in zero-shot label propagation. On CATER (Table 12), Toto achieves 89.4% snitch localization at 32 frames, surpassing specialized prior methods.

## Weaknesses

### Fatal
None.

### Major

1. **Abstract claims "competitive performance across all benchmarks" but Kinetics-400 results contradict this directly.** The paper states that discriminatively trained models outperform generative models and that Toto is "comparable among generative models," but the abstract and conclusion make the unqualified claim of "competitive performance across all benchmarks/tasks." On Kinetics-400, Toto-1B trails masked autoencoding approaches (VideoMAE, ST-MAE) by a large margin. The paper acknowledges this gap implicitly ("discriminately trained models perform better") but does not discuss its magnitude or meaning. The abstract-level claim is not supported by the evidence on the most demanding video action recognition benchmark.

2. **ImageNet comparisons are uncontrolled for pre-training data.** Toto is pre-trained on a massive mixture including 60% HowTo100M, 10% Ego4D, 10% Kinetics, and 20% ImageNet — totaling over 100,000 hours of video. Baselines such as SimCLR, DINO, and MAE are typically pre-trained on ImageNet alone. Table 7 compares them without controlling for data. The paper positions Toto "among generative/autoregressive models," which narrows the scope, but the headline comparison still misleadingly benefits from significantly more pre-training data. The paper does not provide an ImageNet-only pre-training baseline for the main model configuration, making it impossible to attribute the performance to the autoregressive objective vs. the additional data.

3. **No ablation isolating the contribution of video data to downstream performance.** The paper studies design choices (tokenizers, architectures, probing) on ImageNet-only pre-training (400 epochs), but the *main* results use the full video mixture. There is no experiment that holds architecture and tokenizer constant and compares (A) pre-training on ImageNet only vs. (B) pre-training on the full video mixture. Given the paper's title and framing center on "learning from videos," this omission is structural — the reader cannot determine whether adding video data improves image or video task performance over the image-only baseline. The closest proxy (resolution fine-tuning in Table 4) does not isolate the data dimension.

### Minor

4. **Scaling study uses a different tokenizer (VQGAN) than the main models (dVAE).** Section 4.8 explicitly states that the scaling law experiments use VQGAN tokens while the main pre-trained models use dVAE with vocabulary size 8k. The paper acknowledges this but does not justify it or discuss how tokenizer choice affects the scaling exponents. This limits the direct applicability of the derived power law to the main models being evaluated downstream.

5. **No error bars or uncertainty estimates on key results.** None of the main benchmark results (ImageNet, Kinetics, Ego4D, DAVIS, CATER) report standard deviations or confidence intervals. For numbers that are close (e.g., DAVIS tracking J&F scores), this makes it impossible to assess whether differences are meaningful. The robot manipulation experiments report no variance over random seeds, and the real-world experiment (16 trials) reports only a point success rate.

### Trivial
None.

## Nice-to-Haves

- A controlled study comparing the same model pre-trained on ImageNet only vs. the full video mixture would directly answer "does video data help?" and would strengthen the core contribution.
- Including error bars on major benchmarks would improve statistical rigor.
- A discussion of the gap on Kinetics-400 between autoregressive and masked autoencoding approaches would improve the paper's credibility and honesty.

## Removed Points

These points were flagged by reviewers but are removed or downgraded in this consolidated review with justification:

- **"Missing ablation of mixing ratio"**: The reviewer asks for ablations removing Ego4D or HowTo100M. This is a nice-to-have but not a core weakness — the paper's scope is a broad empirical study, not a systematic data composition analysis.
- **"dVAE trained on image-text pairs may introduce biases"**: This is purely speculative and not specific enough to constitute a weakness.
- **"Table 8 omits strong generative baselines from comparison rows"**: The paper's text confirms these baselines (MAE, ST-MAE, VideoMAE) ARE in Table 8. The reviewer's phrasing is contradictory.
- **"Missing compute budget (GPU-hours)"**: The paper reports "over 1 trillion tokens" which is a meaningful scale metric. GPU-hours is a nice-to-have but not a standard requirement.
- **"Data overlap analysis for robot manipulation"**: Speculative concern without evidence of actual contamination.
- **"No comparison to VideoMAE at same data scale"**: The paper's contribution is autoregressive pre-training, not necessarily outperforming masked modeling. Requesting this shifts the goalposts.
- Strength Finder strengths about "competitive performance across diverse benchmarks" conflict with verified weaknesses and are removed or demoted accordingly.
- **"Statistical significance not reported"**: Already captured in Weakness 5.

## Novel Insights

The harsh critic frames the paper as an overclaimed empirical study with structural evaluation flaws, while the strength finder emphasizes the breadth and scale. The most interesting tension is that the paper's genuine contribution — being one of the first systematic demonstrations that autoregressive next-token prediction scales to video and transfers to diverse tasks — is undermined by the very breadth it prides itself on: the comparisons across different benchmarks use different baselines with different training setups, making it hard to assess where the method truly stands. The scaling law analysis (Section 4.8) is the cleanest contribution, as it abstracts away the messy data-mixture issues by focusing on loss vs. compute. However, even this is weakened by the tokenizer inconsistency. A sharper paper would either narrow its claims to match the evidence or provide the controlled experiments needed to support the broader claims.

## Suggestions

1. **Moderate the abstract/conclusion claims.** Replace "competitive performance across all benchmarks" with language that acknowledges where the method lags (e.g., Kinetics) and where it excels (e.g., tracking, CATER). The paper's value does not require claiming universal competitiveness.

2. **Add a controlled comparison isolating the effect of video data.** Pre-train the large model on ImageNet only and compare to the full-mixture model on both ImageNet and Kinetics. This single experiment would directly substantiate the "learning from videos" framing and provide a fairer baseline for comparisons.

3. **Provide a more honest discussion of the Kinetics results relative to masked autoencoding approaches.** Discussing why autoregressive pre-training might lag behind masked modeling on action recognition (e.g., objective mismatch, decoder-only vs. encoder-decoder) would strengthen the paper rather than weaken it.

4. **Justify or address the tokenizer discrepancy in the scaling analysis.** Either provide evidence that the scaling law holds for dVAE tokens as well, or explicitly discuss the limitations of generalizing from VQGAN-based scaling to dVAE-based models.

5. **Report error bars** on all major evaluation results, especially those where comparisons are close.

## Score and Decision

### Round 1 — Bracketing
- **Low anchor** (high\_score ≤ 3): Papers on autoregressive video modeling scored ~1.5–3.0 (e.g., "Uncertainty Preservation in Generative Visual Autoregression" at 1.5, "Autoregressive Video Autoencoder" at 3.0). These have fundamental methodological flaws or incomplete evaluations.
- **Mid anchor** (4 ≤ score ≤ 7): Papers on video representation learning and generative pre-training scored 4.5–6.0. Examples: "Video models are zero-shot learners and reasoners" (4.5, Reject), "Video-GPT via Next Clip Diffusion" (6.0, Accept Poster), "Dynamic Reflections" (5.5, Accept Poster).
- **High anchor** (score ≥ 8): Papers scored 8.0 but are topically unrelated to this work (RL, 3D, navigation).

**Initial bracket**: 4.5–6.0

### Round 2 — Narrowing
- **Anchors in [4.5, 6.0]**: "D-AR: Diffusion via Autoregressive Models" (5.0, Accept Poster), "NextStep-1" (4.5, Accept Oral), "reAR" (5.5, Accept Poster), "Video-GPT" (6.0, Accept Poster).
- **Anchors in [5.0, 6.5]**: "Video-GPT" (6.0), "VideoReasonBench" (5.5), "VideoPhy-2" (5.0), "Improving Autoregressive Video Modeling" (5.5).

### Final calibration against specific anchors

| Anchor | Score | Round | Comparison to Toto |
|--------|-------|-------|-------------------|
| Autoregressive Video Autoencoder | 3.00 | R1 | Weaker — has fundamental flaws in method. Toto is clearly stronger. |
| Uncertainty Preservation in Gen. Visual AR | 1.50 | R1 | Much weaker — scores near zero indicate non-functional paper. |
| Video models are zero-shot learners | 4.50 | R1 | Similar level of overclaiming vs. evidence gap. This paper was rejected; Toto has more concrete contributions but similar framing issues. |
| D-AR | 5.00 | R2 | Comparable. D-AR has cleaner method but ImageNet-only scope; Toto is broader but has more evaluation issues. |
| NextStep-1 | 4.50 | R2 | Comparable. Both have genuine contributions undermined by presentation/evaluation issues. NextStep-1 had strong practical results but some low reviewer scores. |
| reAR | 5.50 | R2 | Toto is slightly weaker. reAR has a focused, cleanly-evaluated contribution; Toto is broader but has uncontrolled comparisons. |
| Video-GPT | 6.00 | R2 | Toto is weaker. Video-GPT has a clear novel paradigm and SOTA on a specific benchmark; Toto's contributions are more diffuse. |
| Dynamic Reflections | 5.50 | R2 | Slightly above Toto; cleanly scoped study with rigorous evaluation. |

Toto's evaluation issues (uncontrolled data comparisons, missing ablation, overclaimed framing) place it below the cleaner papers like reAR (5.5) and Video-GPT (6.0). It is most comparable to D-AR (5.0) and NextStep-1 (4.5) in terms of the gap between ambition and execution. I place it at **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>