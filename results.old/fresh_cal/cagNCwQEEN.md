Now I have all the information I need to produce the final consolidated review. Let me write it.

## Summary

This paper proposes a multimodal LLM (SYSNAME) that replaces the standard transformer backbone with Jamba—a hybrid architecture interleaving Mamba (state-space) layers with transformer layers—to efficiently handle long visual token sequences from high-resolution images and high-frame-rate videos. A "train-on-short-infer-on-long" recipe trains the model on low-resolution images / few frames and then tests at much higher resolutions / more frames. The model is evaluated on 18 image and video benchmarks with efficiency gains of up to 4× over LLaVA-NeXT-13B.

## Strengths

1. **Hybrid Mamba–Transformer architecture yields large efficiency gains for long multimodal sequences.** Figure 2 shows that at 4368² resolution, SYSNAME achieves ~4× throughput improvement over LLaVA‑NeXT‑13B with first-inference latency increasing far more slowly. This is a concrete, quantitative advantage directly supporting the paper's central motivation.

2. **Train-on-short-infer-on-long recipe prevents the catastrophic collapse that standard transformers suffer at out-of-distribution resolutions.** Table 4 (the resolution analysis) demonstrates that when inference resolution increases from 672² to 1344², LLaVA‑NeXT‑13B's MME drops from 1575 to 1353 and MM‑Vet drops from 48.4 to 35.6, whereas SYSNAME maintains MME ≈1655 and improves MM‑Vet from 51.6 to 53.1. This directly validates that the hybrid backbone avoids the information-loss pitfalls of positional-encoding-bound transformers when processing longer visual sequences.

3. **Competitive performance against open-source models of similar activated parameter count.** In Table 1, SYSNAME (12.4B active) achieves strong scores on MME (1655), MMB‑EN (80.9), and MM‑Vet (51.6), outperforming several MoE baselines (CuMo, LongLLaVA). In Table 3 (video), it sets competitive results on EgoSchema (58.7), Perception Test (55.8), and MVBench (61.0).

4. **The model benefits from longer context in some video benchmarks.** Table 5 shows increasing frames from 8 to 16–64 improves results on Perception Test (55.8→56.2), VideoMME (50.1→51.8), and MSVD (73.7→75.0), providing direct evidence that the model can productively use additional visual tokens.

## Weaknesses

### Fatal
None.

### Major

1. **Missing analysis of positional encoding extrapolation for the transformer layers in the hybrid backbone.** The paper attributes the train-short-infer-long capability entirely to "the recurrent nature of Mamba layer" (Section 3.3), but the backbone (Jamba) interleaves Mamba layers with **transformer layers** that use positional encodings. The paper provides no discussion—not a single sentence—about how the transformer component handles extrapolation from a training max of 4096 tokens to inference at up to ~40k tokens. There is no mention of position interpolation, RoPE base frequency scaling, or any mechanism. If the transformer layers degrade at long contexts (as they do in LLaVA-NeXT), the reported efficiency gains and stable performance at high resolutions could be undermined by a quality bottleneck. The paper must either confirm that Jamba's positional encodings support extrapolation, provide an ablation, or measure performance on a long-context task. **This is a methodological gap at the core of the paper's claim.**

2. **The resolution analysis comparison against LLaVA-NeXT is not a controlled comparison despite claims otherwise.** Section 6 (Training Recipe) states that baselines "all [follow] the same train-short-inference-long strategy," which is misleading. LLaVA-NeXT checkpoints were trained at resolutions up to 672×672 with positional encodings that do not extrapolate; they were **not** designed or trained with a short-context recipe. When fed 1344² or 2688² images, their performance collapses predictably due to positional encoding mismatch, not because of any architectural inferiority *per se*. A fairer comparison would retrain LLaVA-NeXT with the same short-context training recipe, or at minimum control for the number of visual tokens. The comparison still demonstrates the proposed model's advantage, but the framing overstates the conclusiveness. This weakens the evidential support for the claim that the proposed model is uniquely capable of handling resolution extrapolation.

### Minor

3. **Performance drops on several video benchmarks with more frames are not adequately explained.** Table 5 shows that EgoSchema drops from 58.7 (8 frames) to 52.5 (64 frames) and MVBench drops from 61.0 to 58.8. The paper attributes this to "the inherent nature and characteristics of different benchmarks" without any analysis. This is important because the paper's core motivation is that more frames should improve performance; a systematic drop on 3 out of 6 benchmarks warrants closer investigation (e.g., perhaps redundant frames introduce noise, or the model's context window is saturated without an effective mechanism to prioritize relevant information).

4. **The "first to be trained on low-resolution and infer on high-resolution" claim is overstated.** Several prior models using ALiBi, RoPE with base frequency scaling, or pure Mamba backbones (e.g., LongLLaVA) can also support inference at resolutions beyond their training resolution. The unique contribution is the *combination* of the hybrid architecture with this recipe, not the recipe itself being unprecedented. The authors should soften this claim.

5. **Active vs. total parameter disparity is not discussed.** Jamba-52B has 52B total but only 12.4B active parameters due to MoE. This provides a larger total knowledge capacity than dense models of similar active count. While MoE comparisons are standard, a brief discussion of this trade-off (e.g., memory footprint, knowledge storage capacity) would improve transparency, especially since some baselines are dense 13B models trained end-to-end with fewer total parameters.

6. **Resolution distribution (Table 3) shows that for several benchmarks (GQA, VQAv2, POPE, SQA), all images are at ≤672² resolution.** The paper correctly notes that performance "remains consistent" at higher resolutions for these benchmarks, but this is a trivial consequence of the data rather than a meaningful property of the model. The paper should be more explicit about this rather than presenting it as uniform evidence of robustness.

### Trivial

- The visual adapter for video uses a 2D convolution layer, but kernel size, stride, and number of output tokens are not specified.
- Efficiency measurement protocol (Figure 2) lacks details on GPU type, batch size, and whether visual encoding time is included.

## Nice-to-Haves

- **Compare efficiency against another Mamba-based MLLM (e.g., LongLLaVA)** to isolate the benefit of the hybrid architecture over pure Mamba, rather than only against the transformer-based LLaVA-NeXT.
- **Ablate the Mamba-to-transformer layer ratio** in the hybrid backbone to justify the design choice and understand its impact on long-context extrapolation.
- **Add error bars or standard deviations** for key results on at least a subset of benchmarks.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Data contamination (training on VQAv2/GQA and evaluating on them):** The reviewer claimed this "invalidates" results. This is standard practice in the MLLM field—all baselines in the comparison tables (LLaVA-NeXT, InstructBLIP, CuMo, etc.) also train on these datasets' training splits and evaluate on held-out splits. This is well-established methodology, not contamination. The criticism misunderstands standard evaluation protocol. **Removed.**

- **Criticism that LLaVA-NeXT baselines "deteriorate significantly" is unfair because of resolution mismatch:** This is reframed in the Major weaknesses section above. The core observation is retained but the severity is reduced—the comparison demonstrates architectural advantage even if not perfectly controlled.

- **Missing appendix, missing proofs in appendix, or absent references:** These are artifacts of the PDF extraction process; the original submission contains them. **Removed per instructions.**

- **Formatting, typo, or style nitpicks:** Removed per instructions as parser artifacts.

- **Criticism that "increasing resolution cannot improve performance" on benchmarks with already-low-res images:** This is partially valid but is kept in Minor (point 6) with proper framing. The original criticism that the paper "claims" improvement where none is possible is inaccurate—the paper says "performance remains consistent," which is factually correct.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the positional encoding gap (the hybrid backbone's transformer layers may bottleneck the claimed extrapolation capability) and the need for better-controlled baselines in the resolution analysis, but these are critical gaps rather than novel insights.

## Suggestions

1. **Address positional encoding extrapolation.** State explicitly how Jamba's transformer layers handle sequences 10× longer than training. If Jamba uses RoPE with base frequency scaling or some other mechanism, say so. If not, provide an ablation or a long-context quality measurement.

2. **Tone down or remove the "first" claim** for the train-short-infer-long recipe, as the novelty is in the architectural combination, not the recipe itself.

3. **Clarify the resolution comparison.** Remove the claim that baselines "all follow the same train-short-inference-long strategy" and instead present the comparison as: "Transformers collapse when pushed far beyond their training resolution; our hybrid architecture does not, demonstrating the advantage of Mamba layers for length extrapolation."

4. **Investigate and discuss** why performance drops on EgoSchema, MVBench, and ActivityNet with more frames—this is directly relevant to the paper's motivation.

5. **Report the training resolution distribution** of the actual images in the training mixture, not just the max allowed resolution, to clarify what the model has actually seen.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>