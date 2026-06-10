## Summary

This paper proposes DGQ, a post-training quantization method for text-to-image diffusion models that addresses two distributional phenomena identified by the authors: activation outliers (which they show causally affect image quality) and the bimodal distribution of cross-attention scores caused by the `<start>` token (which affects text-image alignment). The method combines outlier-preserving group quantization (with automated dimension selection and K-means grouping) and attention-aware quantization (logarithmic quantizer with prompt-dynamic scaling, separating the `<start>` token). On MS-COCO and PartiPrompts, DGQ outperforms Q-Diffusion and TFMQ-DM across several bit-width settings, with particularly large margins at sub-8-bit widths.

## Strengths

1. **Causal analysis of activation outliers for text-to-image diffusion models.** Section 3.2 (Figure 4(a), Table 1) provides a controlled ablation: dropping a single outlier activation per layer drastically changes image quality, while dropping a random non-outlier activation has minimal effect. This goes beyond merely observing outliers to demonstrating their causal importance, which is a meaningful distinction from prior LLM/ViT outlier studies that focused on weight outliers.

2. **Discovery of the `<start>` token's distinct role in cross-attention.** Section 3.2 (Figure 5) identifies that cross-attention scores have a bimodal distribution — a peak near 1.0 from the `<start>` token (corresponding to background pixels) and a separate distribution for remaining tokens — which differs fundamentally from the log-normal distribution of self-attention assumed by prior ViT quantization work. This analysis is novel and directly motivates the method's design.

3. **Well-constructed ablation study.** Table 3(a)-(c) systematically isolates each component (outlier-preserving group quantization, log quantizer, `<start>` token separation, dynamic scale, dimension selection), and the results confirm that each contributes positively. The ablation for attention-aware quantization (Table 3(c)) is particularly informative, showing that the dynamic log quantizer dramatically outperforms static alternatives at 6-bit.

4. **Strong quantitative results at sub-8-bit settings.** At W4A6 and W4A4, prior methods produce FID >200 (essentially failed generation), while DGQ achieves 43.66 and 43.86 respectively (Table 2, Section 4.2). Whether or not the comparison is perfectly isolated (see Weaknesses), the gap is large enough to indicate a real improvement in handling very low-bit attention quantization.

5. **Automated dimension selection mechanism.** The metric $D_d$ (Equation 1) provides a principled way to determine whether to group by channel or pixel dimension per layer, rather than using a fixed scheme. Ablation Table 3(b) confirms that this dimension selection consistently improves both FID and CLIP score over grouping by channel or pixel alone.

## Weaknesses

### Fatal
None.

### Major

1. **Baseline comparison conflates attention and activation contributions, and the paper's framing misrepresents this.** The paper states (Section 4.1, lines 193–194) that Q-Diffusion and TFMQ-DM "set the attention score's quantizer bits of Stable Diffusion to 16 bits to avoid text-image alignment degradation. However, in our implementation, to ensure a fair comparison, we set all attention score's quantizer bits to match the activation bits." This means the baselines are evaluated at a setting their own designers explicitly avoided because it degrades alignment. DGQ's contribution includes a specialized attention quantization scheme that handles low-bit attention well. The resulting comparison therefore tests "DGQ's full method (including its attention scheme)" vs. "baselines forced to use their generic attention quantizer at destructive bit-widths." The dramatic baseline collapse at sub-8-bit (FID >200) is unsurprising under this setup. The paper should have additionally reported results with the baselines at their recommended 16-bit attention (to isolate the activation quantization contribution) and clearly attributed which part of the performance gap comes from better attention quantization versus better activation quantization. The current framing — "baselines essentially failed to generate viable images" (Section 4.2) without acknowledging the design choice caveat — is misleading.

2. **Quantized model surpassing full-precision FID is reported without any analysis.** The paper highlights (lines 49–50, 207) that DGQ at W8A8 achieves FID 13.15 relative to the full-precision model's 14.44 — a quantized model outperforming the unquantized original. This is an unusual and interesting result, but the paper offers zero analysis. Possible explanations include: quantization acting as a regularizer, the metric favoring certain quantization artifacts, evaluation pipeline mismatch (different seeds, samples), or calibration data distribution overlap. Without any investigation or even acknowledgement that this requires explanation, the result erodes rather than strengthens confidence in the evaluation methodology.

### Minor

1. **No measures of variance or statistical significance.** Every FID, IS, and CLIP score in Tables 2 and 3 is a point estimate with no standard deviations, confidence intervals, or mention of multiple seeds/runs. For the headline claim of a 1.29 FID improvement over full precision, it is impossible to assess whether this difference is within evaluation noise. While single-run evaluation is common in generative model benchmarks, the presence of an anomalous result (quantized beating full precision) makes the absence of variance measures particularly problematic.

2. **The "first to achieve low-bit quantization (≤8-bit) without fine-tuning" claim is imprecisely scoped.** The paper repeats this claim three times (abstract line 10, intro lines 52–54, conclusion line 235). Q-Diffusion and TFMQ-DM are also post-training quantization methods that operate without fine-tuning. The paper's own weight quantization relies on BRECQ and Adaround — the same methods used by prior work. The genuine novelty appears to be achieving functional results at very low bit-widths (sub-8-bit attention), but the blanket phrasing "first to achieve low-bit quantization" needs sharper qualification to avoid overclaiming.

3. **The method for determining K (number of groups) is underspecified for reproducibility.** The ablation explores K=2, 8, 16 (Table 3(b)), but the paper never states how K is selected at test time. The K-means clustering step for grouping vectors by activation range (Section 3.3, line 156) — described as "divide the activation values into K groups" — is not specified as static-per-layer or per-timestep, not does the paper clarify whether the clustering is applied during calibration or at inference. These are non-trivial design choices that affect both the method's behavior and its computational cost.

4. **Hardware-efficiency claims are asserted but not validated.** The paper criticizes mixed-precision methods as "challenging for hardware implementation" (line 27, line 73) and claims its own approach is hardware-friendly (line 84), but provides no latency measurements, throughput benchmarks, or hardware implementation analysis. DGQ uses per-timestep group quantization scales and dynamic inference-time scale computation; whether this is actually more hardware-friendly than mixed-precision alternatives is not demonstrated.

### Trivial

None.

## Nice-to-Haves

- Report the PartiPrompts evaluation with FID and IS metrics, not just CLIP score, to more fully support the generalization claim.
- Include an additional experiment where baselines use their default 16-bit attention, to isolate the contribution of the outlier-preserving group quantization component separately from the attention quantization component.
- Provide a brief analysis or discussion of why a quantized model improves over full-precision FID, even if speculative.

## Removed Points

These points were raised in the inputs but are removed after verification against the paper:

- **"Garbled/incomplete sentence at line 23"**: This is a PDF parser artifact, not an author error. Removed per formatting-artifact rule.
- **"Missing comparison against MixDQ/QuEST"**: The paper's related work section (line 73) explains that MixDQ and PCR rely on mixed precision (challenging for hardware) and QuEST focuses on weight quantization (complementary to this work's activation focus). The paper provides a rationale for exclusion. Removed per rule requiring verification of criticisms against paper content.
- **"FID improvement over full precision should be dropped as a strength"**: This is a genuine numerical result from the paper. The weakness (lack of explanation) and the strength (the numerical result itself) can coexist — they do not directly conflict. The weakness addresses the interpretation, not the existence, of the result.
- **"The paper should add <missing related work X>"**: Per instructions, not to mention missing related works as I cannot verify their existence.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any observation about the paper that its authors had not already identified.

## Suggestions

1. Add an experiment comparing DGQ against baselines at their recommended 16-bit attention setting, alongside the current equal-bit-width comparison. This would cleanly separate whether DGQ's advantage comes from better activation quantization, better attention quantization, or both.
2. Provide variance estimates (multi-seed or confidence intervals) for all main results, and specifically investigate whether the FID improvement over full precision is reproducible and robust.
3. Clarify the K selection procedure for the grouping mechanism — is K fixed per layer, selected via a criterion during calibration, or something else? Specify whether the K-means clustering is a one-time calibration step or required per timestep.
4. Sharpen the novelty claims to precisely state what was not possible before (e.g., "first PTQ method achieving FID <50 at W4A6 for text-to-image diffusion models") rather than the broader "first to achieve low-bit quantization."

## Score and Decision

The paper makes genuine analytical contributions — the causal demonstration of activation outliers in text-to-image diffusion models and the discovery of the `<start>` token's bimodal cross-attention distribution are valuable insights that extend beyond the quantization context. The method is well-motivated and the ablation is thorough.

However, two major weaknesses prevent acceptance at the ICLR bar. First, the baseline comparison design conflates two separate contributions, and the paper's framing implies a broader failure of baselines than the experimental setup justifies. Second, the unexplained result that a quantized model outperforms full precision undermines the credibility of the evaluation. These issues together mean the headline quantitative claims are not presented in a sufficiently rigorous form for a top venue.

The paper would benefit from restructuring the experiments to cleanly isolate the activation quantization contribution, providing variance estimates, and addressing the anomalous FID result.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>